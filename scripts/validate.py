#!/usr/bin/env python3
"""Dependency-free validation for V1 Health research dataset."""
import csv
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read_csv(rel):
    with (ROOT / rel).open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

def main():
    ing = read_csv("data/ingredients.csv")
    studies = read_csv("data/studies.csv")
    prov = read_csv("data/study_provenance.csv")
    overlaps = read_csv("data/overlapping_evidence.csv")
    assert len(ing) == 17, f"Expected 17 ingredients, got {len(ing)}"
    assert len(studies) == 38, f"Expected 38 research records, got {len(studies)}"
    ingredient_ids = [r["ingredient_id"] for r in ing]
    ids = [r["study_id"] for r in studies]
    assert len(set(ingredient_ids)) == len(ing), "Duplicate ingredients"
    assert len(set(ids)) == len(studies), "Duplicate study IDs"
    assert set(r["ingredient_id"] for r in studies) <= set(ingredient_ids), "Unknown ingredient ID"
    assert all(r["source_url"].startswith("https://") for r in studies), "Insecure source URL"
    assert all(r["screening_status"] in {"abstract_screened", "full_text_checked"} for r in studies), "Invalid screening status"
    assert all(r["finding_direction"] in {"positive","neutral","mixed","insufficient"} for r in studies), "Invalid finding direction"
    for col in ("pmid", "doi"):
        values = [r[col].lower() for r in studies if r[col]]
        assert len(values) == len(set(values)), f"Duplicate {col}"
    assert set(r["study_id"] for r in prov) == set(ids), "Provenance doesn't cover all studies"
    assert Counter(r["batch"] for r in prov) == {"original_18":18, "addition_20":20}, "Batch totals wrong"
    for r in overlaps:
        assert r["study_id_a"] in ids and r["study_id_b"] in ids, "Unknown overlap ID"
    for name, expected in (("data/assessments/efficacy_matrix.csv",17),
                           ("data/assessments/safety_limits.csv",17),
                           ("data/assessments/eu_claims_audit.csv",17)):
        assert len(read_csv(name)) == expected, f"{name}: incorrect number of rows"
    for rel, expected_csv in (("data/ingredients.json",ing), ("data/studies.json",studies)):
        with (ROOT / rel).open(encoding="utf-8") as f:
            assert json.load(f) == expected_csv, f"{rel}: CSV/JSON mismatch"
    print(f"PASS: {len(ing)} ingredients, {len(studies)} unique research records, "
          f"{len(prov)} provenance rows, {len(overlaps)} overlap warnings and 3 assessment matrices.")

if __name__ == "__main__":
    main()
