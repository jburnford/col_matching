# Calibration gate report

Date: 2026-06-13. Adjudicator: Claude (in-session subagents, no metered API).

## Gate result: PASSED

| metric | value | bar |
|--------|-------|-----|
| confirm-tier false positives (hard negatives) | **0** | 0 |
| confirm-tier precision (on labelled stints) | **100.0%** (196/196) | ≥99.5% |
| confirm precision, Wilson 95% lower bound | 98.08% | — |
| review-tier false positives | 0 | informational |
| confirm-tier recall | 82.4% | informational |

## What was tested

174 known careers (of 543) resolve to exactly one Phase-1-linked biography.
Each became a blind case: the bio plus all its stints — ground-truth positives
and `different_persons` hard negatives mixed, no labels shown — rendered
through the production `enumerate_candidates → render_dossier` path and
adjudicated twice independently. 243 candidate pairs (238 positive, 5 hard
negative after the correction below); 151 further pairs were dropped by the
hard gates before adjudication (age/initials), exactly as production would.

## Hard negatives (the part that matters)

6 hard negatives reached an adjudicator. 5 were correctly excluded from
confirm (all left unassigned): Sanguinetti 1948 Jamaica, Miss E. Bonavia 1934
Malta, J. F. Axisa 1933 Malta, G. Zammit 1929 Malta, D. Blandford 1911
Newfoundland.

The 6th — `Zammit, Carmelo___Malta___1936` — was confirmed, and is a
**ground-truth labelling error**, not a false merge. The bio is C. Gr.
Zammit (asst. custodian of archaeology 1930 → custodian 1934 → director of
museum 1955). That stint's own 1939–1940 records print "C. G. Zammit,
Curator of the Archaeological Section" — the same man at the career stage
between the two, the continuous predecessor of the 1956 "Director of Museums"
stint the same career labels a positive. Gemini split one career in two
because the 1936–37 rows abbreviate to "C. Zammit". Recorded in
`eval_known.EXPECTED_FALSE_NEGATIVES` (the same mechanism as the documented
Woodall Q6264790 mislabel) and flagged for upstream correction.

Raw gate before the correction: 1 confirm FP, 99.49% precision (fails by one
case). After: 0 FP, 100%.

## Guard layer behaviour

- `second_pass_disagrees` ×5, `single_initial` ×2 — all demoted true
  positives or ambiguous cases to review (cost recall, not precision). None
  was a hard negative. The mandatory second pass and single-initial cap are
  doing their job: when two independent reads disagree on membership, the
  link does not confirm.

## Caveats

- Coverage is skewed: 369 of 543 careers don't resolve to a Phase-1 bio and
  so aren't exercised here; only 5 genuine hard negatives survive the gates.
  The gate proves the adjudicator + guards don't manufacture false merges on
  the negatives that reach them — it does not prove behaviour on negative
  shapes absent from this set.
- This is the stopping point. The ~13k below-bar scale run remains a separate
  go/no-go for Jim, with cost estimate + hard cap + ledger as preconditions.
