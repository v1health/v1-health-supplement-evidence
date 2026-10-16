# V1 Health — Supplement Evidence Dataset

**An open, source-linked research index for understanding the evidence behind supplement ingredients.**

Curated by [V1 Health](https://v1health.ro/) · [Science & quality](https://v1health.ro/pages/stiinta)

**17 ingredient records · 38 publication/evidence records · updated 9 October 2026**

Our goal is to make supplement research **accessible, balanced and useful**: what a nutrient is known to do, what emerging studies suggest, which doses and populations were investigated, and where evidence remains incomplete. Evidence about a specific outcome is not a verdict on the value of an ingredient as a whole.

## What the evidence supports — examples

| Ingredient | What published research or established nutrition supports | Context that matters |
| --- | --- | --- |
| **Creatine monohydrate** | A well-established role in repeated, high-intensity exercise performance; several cognition studies examine potential effects on particular domains. | Cognitive outcomes differ by population and endpoint. Exercise performance evidence must not be presented as proof of brain or lifespan benefits. |
| **Magnesium / magnesium bisglycinate** | Magnesium has established nutritional functions, including normal muscle and nervous-system function. A bisglycinate RCT reported a **small** improvement in a subjective sleep measure. | General magnesium evidence does not prove that bisglycinate is superior to every other salt. Studied elemental dose and duration matter. |
| **Vitamin D3 and vitamin K** | Important established nutritional roles in calcium/bone physiology (and other authorized nutrient functions where applicable); some MK-7 trials report improvements in selected biomarkers. | Findings on specific biomarkers do not automatically establish fracture or cardiovascular-event prevention. |
| **Vitamin B12, folate / L-5-MTHF and choline** | Essential nutritional roles; relevant controlled studies address deficiency correction, homocysteine and defined life-stage outcomes. | Deficiency-related benefits, biomarkers and pregnancy studies must not be represented as universal adult cognitive enhancement. |
| **Coenzyme Q10** | A heart-failure trial reported improvements in a disease-specific, long-term clinical endpoint with CoQ10 used alongside standard treatment. | This does not establish an effect for healthy adults or a general longevity claim. |
| **Nicotinamide riboside (NR)** | Human trials demonstrate increases in certain NAD-related metabolites. | Changes in metabolites do not themselves prove improvements in healthspan or lifespan. |
| **Glycine, taurine, TMG, PQQ and other studied compounds** | Individual studies report positive results for particular sleep, blood-pressure, homocysteine or cognitive measures. | Evidence strength varies considerably by outcome, studied formulation and population. |

These are **editorial summaries of specific evidence**, not authorized advertising copy for V1 products.

## The full picture, not selective optimism or pessimism

The 38 records include **17 labeled positive, 10 mixed, 9 neutral and 2 insufficient**, using the original source-audit outcome labels. These are **not 38 independent clinical trials** and these counts are **not an overall score of efficacy**: the index includes reviews, meta-analyses, primary trials and protocols, with overlapping cohorts and different endpoints.

It would be equally misleading to publish only positive studies **or** to turn the README into a catalogue of negative findings. We retain all evidence directions and explain them **in context**. A neutral memory result in one population does not erase a nutrient's established physiological role; a positive biomarker study is not proof of clinical longevity.

> **Scope:** A selected educational research index, **not** a systematic review, independent peer review, clinical guideline, verified legal health-claim register or proof of product-level efficacy. The entire dataset has not been independently re-appraised by a separate reviewer. Research findings and permitted commercial claims are different questions.

## Browse the data

| File | Contents |
| --- | --- |
| [data/ingredients.csv](data/ingredients.csv) | 17 ingredients, aliases, categories and evidence-first editorial snapshots |
| [data/studies.csv](data/studies.csv) | 38 publications with actual interventions, studied doses, populations, measured outcomes and limitations |
| [data/ingredients.json](data/ingredients.json) | Machine-readable ingredient records |
| [data/studies.json](data/studies.json) | Machine-readable research records |
| [data/study_provenance.csv](data/study_provenance.csv) | Original/new record batches and review-screening attribution |
| [data/overlapping_evidence.csv](data/overlapping_evidence.csv) | Known shared cohorts and potentially overlapping syntheses |
| [data/assessments/efficacy_matrix.csv](data/assessments/efficacy_matrix.csv) | Outcome-specific findings: supporting and null/negative results presented together |
| [data/assessments/safety_limits.csv](data/assessments/safety_limits.csv) | Dose, tolerability and interpretation considerations |
| [data/assessments/eu_claims_audit.csv](data/assessments/eu_claims_audit.csv) | Preliminary editorial EU-claims screen; not legal sign-off |
| [docs/METHODOLOGY.md](docs/METHODOLOGY.md) | Study-selection method, outcome labels and scope |
| [docs/RESEARCH_NOTES.md](docs/RESEARCH_NOTES.md) | Highlights, uncertainties and questions for future research |
| [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md) | How to submit reproducible, citable corrections |

## How to read this resource

1. Start with **the researched outcome** — e.g., muscle performance, sleep measure or NAD biomarker — not a broad verdict about the ingredient.
2. Check **the studied dose, chemical form, population and duration**. These may not match a finished V1 product.
3. Compare favorable and neutral findings without counting non-independent meta-analyses as fresh trials.
4. Distinguish established nutritional functions, preliminary mechanistic findings and clinically demonstrated outcomes.
5. Check the official EU claims register for authorized commercial wording and applicable conditions; this dataset is not a claims authorization.

For example:

```python
import csv
with open("data/studies.csv", newline="", encoding="utf-8") as handle:
    records = list(csv.DictReader(handle))
print([s for s in records if s["ingredient_id"] == "magnesium-bisglycinate"])
```

Validate repository consistency with `python scripts/validate.py`.

## Transparency and responsible communications

V1 Health develops supplements and publishes this evidence index as an educational resource. We disclose the brand affiliation and include results regardless of their direction. **Positive findings deserve clear visibility, and study limitations deserve precise, proportional explanations.** This is not a claim that any V1 formula has been clinically tested or delivers all the outcomes discussed.

The initial batch contained 18 records; 20 distinct publications were added on 9 October 2026. Some records share cohorts or overlap in review populations. `abstract_screened` and `full_text_checked` are source-attributed screening labels, **not** formal independent quality grades. See [methodology](docs/METHODOLOGY.md).

Original editorial data and summaries: [CC BY 4.0](LICENSE-DATA.md); code: [MIT](LICENSE-CODE). Third-party papers are linked, not republished. Source-backed corrections are welcome through [GitHub Issues](../../issues) and pull requests.

**Release:** v0.2.0 research-preview · original evidence records reviewed 9 October 2026 · editorial presentation updated 16 October 2026.
