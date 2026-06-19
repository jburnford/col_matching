<!-- {"case_id": "case_dupree_frederick-henry_b1888", "bio_ids": ["dupree_frederick-henry_b1888"], "stint_ids": ["Dupree, F. H___Straits Settlements___1917"]} -->
# Dossier case_dupree_frederick-henry_b1888

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `dupree_frederick-henry_b1888`

- Printed name: **DUPREE, FREDERICK HENRY**
- Birth year: 1888 (attested in editions [1932, 1933])
- Honours: A.M.I.E.E
- Appears in editions: [1932, 1933]

### Verbatim printed entry text (OCR)

**Version `col1932-L59873.v` — printed in editions [1932, 1933]:**

> DUPREE, FREDERICK HENRY, A.M.I.E.E.—B. 1888; telegraphist, central S.A. govt., rly. telegraphs, 1903-05; engnr.-operator, Singapore, Oct., 1914; tech. rep. of C.O. on comtee. in London for revision of Internat. Telegraph and Radio Telegraph Conventions, Oct., 1919-Apr., 1920; F.M.S. on ap. duty, June, 1920; mem. S.S. wireless comtee., Feb., 1923; engnr.-operator, wireless statn., Singapore, Nov., 1930.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1903–1905 | telegraphist, central S.A. govt., rly. telegraphs | — | [1932, 1933] |
| 1 | 1914 | engnr.-operator | Singapore | [1932, 1933] |
| 2 | 1919–1920 | tech. rep. of C.O. on comtee. in London for revision of Internat. Telegraph and Radio Telegraph Conventions | Colonial Office | [1932, 1933] |
| 3 | 1920 | F.M.S. on ap. duty | Federated Malay States | [1932, 1933] |
| 4 | 1923 | mem. S.S. wireless comtee | Federated Malay States *(inherited from previous clause)* | [1932, 1933] |
| 5 | 1930 | engnr.-operator, wireless statn. | Singapore | [1932, 1933] |

## Candidate stint `Dupree, F. H___Straits Settlements___1917`

- Staff-list name: **Dupree, F. H** | colony: **Straits Settlements** | listed 1917–1931 | editions [1917, 1918, 1919, 1920, 1921, 1922, 1923, 1931]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1917 | F. H. Dupree | Engineer Operator, Wireless Station | Post Office | — | — |
| 1918 | F. H. Dupree | Engineer Operator, Wireless Station | Post Office | — | — |
| 1919 | F. H. Dupree | Engineer Operator, Wireless Station | Post Office | — | — |
| 1920 | F. H. Dupree | Engineer Operator, Wireless Station | Post Office | — | — |
| 1921 | F. H. Dupree | Engineer Operator, Wireless Station | Post Office | — | — |
| 1922 | F. H. Dupree | Engineer Operator, Wireless Station | Post Office | — | — |
| 1923 | F. H. Dupree | Engineer Operator, Wireless Station | Post Office | — | — |
| 1931 | F. H. Dupree | Engineer Operators, Wireless Stations | Post Office | — | — |

### Deterministic checks: `dupree_frederick-henry_b1888` vs `Dupree, F. H___Straits Settlements___1917`

- [PASS] surname_gate: bio 'DUPREE' vs stint 'Dupree, F. H' (exact)
- [PASS] initials: bio ['F', 'H'] ~ stint ['F', 'H']
- [PASS] age_gate: stint starts 1917, birth 1888 (age 29)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1917-1931
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

