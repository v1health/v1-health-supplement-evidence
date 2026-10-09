# V1 Health — Supplement Evidence Dataset

**An open, machine-readable evidence index for supplement research.**

Curated by [V1 Health](https://v1health.ro/) | [Science & quality](https://v1health.ro/pages/stiinta)

**17 ingredient records · 38 research records · updated 9 October 2026**

This public resource organizes **positive, neutral, mixed, insufficient and negative findings** alongside the actual intervention, dose, population, study design, duration and limitations. The 38 entries include primary trials, reviews, meta-analyses and a protocol: they are **not 38 independent clinical trials**.

> **Read this first:** This is a selected educational evidence index, **not a systematic review, independent peer review, clinical guideline, legal health-claim register or proof that V1 products work**. Screening flags are attributed to the underlying research audit; the entire dataset has not been independently validated by a separate reviewer. A listed ingredient, study dose, or favorable endpoint does not authorize a commercial product claim.

## Browse the data

| File | Contents |
| --- | --- |
| [data/ingredients.csv](data/ingredients.csv) | 17 ingredients, aliases, categories and editorial snapshots |
| [data/studies.csv](data/studies.csv) | 38 source-linked records; primary, neutral and negative evidence retained |
| [data/ingredients.json](data/ingredients.json) | Structured export of ingredient records |
| [data/studies.json](data/studies.json) | Structured export of all research records |
| [data/study_provenance.csv](data/study_provenance.csv) | Original versus newly added source batches, screening attribution |
| [data/overlapping_evidence.csv](data/overlapping_evidence.csv) | Shared cohorts, overlapping meta-analyses and non-independence warnings |
| [data/assessments/efficacy_matrix.csv](data/assessments/efficacy_matrix.csv) | Outcome-specific, pragmatic confidence assessment |
| [data/assessments/safety_limits.csv](data/assessments/safety_limits.csv) | Important ingredient-specific cautions and interpretation limits |
| [data/assessments/eu_claims_audit.csv](data/assessments/eu_claims_audit.csv) | **Preliminary** EU communications review; legal verification required |
| [docs/METHODOLOGY.md](docs/METHODOLOGY.md) | Selection, screening, uncertainty, overlap and curation scope |
| [docs/DATA_DICTIONARY.md](docs/DATA_DICTIONARY.md) | Column definitions and conventions |
| [docs/RESEARCH_NOTES.md](docs/RESEARCH_NOTES.md) | Context and outstanding research questions |
| [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md) | Submit reproducible, citable corrections |

## Evidence in context

- **Creatine:** Strong exercise-performance evidence, but cognition effects are inconsistent across populations and endpoints.
- **Nicotinamide riboside (NR):** Changes to NAD-related metabolites are not demonstration of better healthspan or longer human lifespan.
- **Spermidine:** The SmartAge trial did not achieve its primary memory endpoint.
- **Calcium AKG:** Animal/mechanistic observations and a study protocol are not clinical proof of anti-aging efficacy.
- **Glycine:** Small sleep-related studies do not demonstrate a human longevity effect.

These examples describe **individual research outcomes**, not consumer-facing product claims.

## Method and limitations

The original batch contained 18 records. An additional 20 unique publications were added on 9 October 2026, resulting in 38 unique `study_id` values. Some reports reuse the **same parent-trial participants**; meta-analyses can overlap. Counting lines in the CSV does not estimate the number of independent trials or quantify certainty. Read [methodology](docs/METHODOLOGY.md) and [overlap notes](data/overlapping_evidence.csv).

Screening statuses: `abstract_screened` (abstract/metadata reviewed in the source audit) or `full_text_checked` (accessible full text inspected according to the source audit). These are **screening provenance, not a quality grade or guarantee**. Original data and newly added records are retained with their study IDs.

## Use and validate

```python
import csv
with open("data/studies.csv", newline="", encoding="utf-8") as handle:
    records = list(csv.DictReader(handle))
print([s for s in records if s["ingredient_id"] == "spermidine"])
```

```bash
python scripts/validate.py
```

## Research ethics, commercial disclosures and licensing

V1 Health markets supplements and maintains this educational index. **Brand affiliation is disclosed**; entries include unfavorable results to reduce selective presentation. Do not generalize trial findings to commercial products, other formulations, lower product doses, different populations or other endpoints. The EU health-claims table is an **editorial screening aid only**: verify authorized claims, ingredient legality and current use conditions in official registers before commercial use.

Original curation, tables, and editorial summaries: [CC BY 4.0](LICENSE-DATA.md); code: [MIT](LICENSE-CODE). Third-party articles are **linked, not redistributed**. We welcome source-backed corrections via [GitHub Issues](../../issues) or pull requests.

**Release:** v0.2.0 research-preview · 2026-10-09. No study in this selected dataset demonstrates extension of human lifespan through supplementation.
