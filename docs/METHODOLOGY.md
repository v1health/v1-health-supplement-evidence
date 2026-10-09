# Methodology and scope

**Scope:** A selected, manually curated research index focused on 17 ingredients relevant to supplement formulation. Inclusion is editorial, not a comprehensive, PRISMA-compliant systematic literature search. The dataset includes randomized human trials, reviews, meta-analyses, protocol publications and selected nutritional evidence.

## What each entry represents

A row describes *the specific outcome measured in the specified population, intervention and dose*. `finding_direction` is not an ingredient-wide verdict. `positive` may mean a small biomarker or surrogate-endpoint result; `neutral` means no statistically confirmed benefit on the relevant reported outcome; `mixed` reflects inconsistent endpoints; `insufficient` describes a review/protocol or lack of direct efficacy evidence.

## Screening source and limitations

The initial 18 rows are labelled `abstract_screened`. Of the 20 additions, the source audit labels 8 `full_text_checked` and 12 `abstract_screened`. **These labels are supplied by the research source; independent re-appraisal, funding verification, complete adverse-event assessment and systematic retraction checks are pending.** Do not treat `full_text_checked` as equivalent to a low-risk-of-bias or formal GRADE rating.

Publication links, DOI/PMID values and short summaries are provided for reproducibility. Empty bibliographic identifiers are intentional where the source audit had not verified them. `last_checked` is source-record review date, not evidence that the entire literature was searched up to that day.

## Independence and duplicate counting

Separate publications are not necessarily separate trial cohorts. See `data/overlapping_evidence.csv` for known non-independent pairs. In particular, a VITAL fracture analysis and a VITAL primary-outcome article share a parent trial; prenatal-choline follow-up uses its parent cohort; two quercetin meta-analyses overlap; pooled creatine studies must not be counted twice when also cited as individual trials.

## Evidence interpretation

1. Separate direct human clinical outcomes from preclinical or mechanistic effects.
2. Keep deficiency treatment distinct from enhancement in people with adequate nutrient status.
3. Keep surrogate outcomes (NAD metabolites, homocysteine, methylation clocks, imaging, arterial stiffness) distinct from morbidity, mortality and life extension.
4. Account for studied **dose, formulation, duration and population**; do not imply commercial products use matching doses.
5. Attribute combination-intervention evidence (e.g. GlyNAC) to the combination, not isolated glycine.
6. Report magnesium's *elemental dose* separately from magnesium-salt mass.
7. Read a negative primary endpoint before emphasizing exploratory subgroup findings.
8. Record sponsor/funding, conflicts, registered outcomes, corrections and retractions when independently checked.

## Regulatory scope

Commercial labelling and advertising in the EU depend on the **actual permitted ingredient, official authorized claim and conditions of use**, not whether an outcome appears in a paper. The supplemental EU table is preliminary and is **not legal approval**. See the [EU Register](https://ec.europa.eu/food/food-feed-portal/screen/health-claims/eu-register) and [Regulation (EC) 1924/2006](https://eur-lex.europa.eu/eli/reg/2006/1924/oj). Consult qualified regulatory advice for any product-specific communication.

## Revisions

Propose corrections with full DOI/PMID, population, trial design, outcome, dose, journal correction/retraction status, evidence of full-text review, and a plain-language explanation. The source-batch attribution lives in `data/study_provenance.csv`. This release has **not** received a full independent systematic peer review.
