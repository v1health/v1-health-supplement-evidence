# Data dictionary

| Field | Meaning |
| --- | --- |
| `study_id` | Stable publication/evidence record ID; original IDs preserved |
| `ingredient_id` | Foreign key to `data/ingredients.csv` |
| `year` | Publication year |
| `study_design` | Author/source-reported method (may include reviews or protocol) |
| `intervention` | Actual intervention tested or reviewed |
| `studied_dose` | Studied dose, **not** a recommendation or V1 Health product serving |
| `population` | Participant description, often including sample size |
| `duration` | Observation/treatment period |
| `outcome_domain` | Evaluated outcome, not necessarily clinical |
| `finding_direction` | `positive`, `neutral`, `mixed`, or `insufficient` for described outcome |
| `finding_summary` | Short original editorial paraphrase of relevant results |
| `limitations` | Key validity / generalizability cautions |
| `pmid` | PubMed record ID where verified by source audit, blank if unavailable |
| `doi` | DOI string where verified by source audit, blank if unavailable |
| `source_url` | Link to paper or publication record |
| `intervention_context` | Single-ingredient, combination, trial follow-up, review, protocol, etc. |
| `screening_status` | `abstract_screened` / `full_text_checked` based on source audit |
| `last_checked` | Source-record review date, not systematic search date |

Ingredient columns: `ingredient_id`, `name`, `aliases`, `category`, `evidence_snapshot`, `curation_status`, `last_checked`. Ingredient `pending` means a benefit or specific evidence appraisal is not yet curated; it does not assert an absence of all publications.

The provenance CSV retains the batch (`original_18` or `addition_20`) and identifies the screening attribution. All CSVs use RFC 4180-compatible quoting and UTF-8. Do not treat an empty DOI or PMID as a zero identifier.
