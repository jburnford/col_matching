<!-- {"case_id": "case_stanhope_reginald-alfred-browne_b1891", "bio_ids": ["stanhope_reginald-alfred-browne_b1891"], "stint_ids": ["Stanhope, A. B___Australia___1918"]} -->
# Dossier case_stanhope_reginald-alfred-browne_b1891

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `stanhope_reginald-alfred-browne_b1891`

- Printed name: **STANHOPE, REGINALD ALFRED BROWNE**
- Birth year: 1891 (attested in editions [1937])
- Honours: M.R.C.V.S
- Appears in editions: [1937]

### Verbatim printed entry text (OCR)

**Version `col1937-L65020.v` — printed in editions [1937]:**

> STANHOPE, REGINALD ALFRED BROWNE, B.V. Sc. (Melb.), M.R.C.V.S., Melb., Univ. of Royal Vet. Coll., Lond.—B. 1891; vet. offr., F.M.S., May, 1920; do., Pahang, June, 1924; Aug., 1935; N. Sembilan, Feb., 1921; N. Selangor and Malacca, June, 1932; Selangor, Sep., 1934.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920 | vet. offr. | Federated Malay States | [1937] |
| 1 | 1921 | N. Sembilan | Federated Malay States *(inherited from previous clause)* | [1937] |
| 2 | 1924 | do., Pahang | Federated Malay States *(inherited from previous clause)* | [1937] |
| 3 | 1932 | N. Selangor and Malacca | Federated Malay States *(inherited from previous clause)* | [1937] |
| 4 | 1934 | Selangor | Federated Malay States *(inherited from previous clause)* | [1937] |
| 5 | 1935 | do., Pahang | Federated Malay States *(inherited from previous clause)* | [1937] |

## Candidate stint `Stanhope, A. B___Australia___1918`

- Staff-list name: **Stanhope, A. B** | colony: **Australia** | listed 1918–1927 | editions [1918, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1918 | A. B. Stanhope | Inspector of Officers in Charge of Stores | Inspection of Stores | — | — |
| 1927 | A. B. Stanhope | Inspector of Officers in Charge of Stores | Inspection of Stores | — | — |

### Deterministic checks: `stanhope_reginald-alfred-browne_b1891` vs `Stanhope, A. B___Australia___1918`

- [PASS] surname_gate: bio 'STANHOPE' vs stint 'Stanhope, A. B' (exact)
- [PASS] initials: bio ['R', 'A', 'B'] ~ stint ['A', 'B']
- [PASS] age_gate: stint starts 1918, birth 1891 (age 27)
- [FAIL] colony: no placed event resolves to 'Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1918-1927
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Adjudication constraints (binding)

- The prime directive is NO FALSE MERGES. A missed link is recoverable; a
  wrong one silently corrupts the historical record. When in doubt, leave
  the stint unassigned.
- Surname identity is NOT evidence: every candidate here already shares the
  surname (it is the blocking key). Only position, place, dates, honours,
  initials/forenames, and edition co-occurrence count.
- Single-initial biographies (e.g. "J. Lewis") must never be merged on
  shared-stint or tenure-overlap evidence alone; they need a strong
  independent dimension (specific position match, shared honour, or
  multi-edition co-occurrence).
- A stint belongs to AT MOST one biography. If two biographies in this case
  could plausibly hold the same stint, assign it to neither.
- Respect hard chronology: nobody serves before age ~15 or after death.
- Generic junior titles (clerk, cadet, assistant) recur constantly; a title
  match alone on a common office is weak evidence.

