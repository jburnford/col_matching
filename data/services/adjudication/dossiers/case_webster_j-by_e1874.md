<!-- {"case_id": "case_webster_j-by_e1874", "bio_ids": ["webster_j-by_e1874"], "stint_ids": ["Webster, B___Canada___1918", "Webster, John___Canada___1905"]} -->
# Dossier case_webster_j-by_e1874

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 44 official(s) with this surname in the graph's staff lists; 21 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Webster, John___Canada___1905` is also gate-compatible with biography(ies) outside this case: ['webster_john-sutton_b1884'] (already linked elsewhere or filtered).

## Biography `webster_j-by_e1874`

- Printed name: **WEBSTER, J. BY**
- Birth year: not printed
- Honours: F.R.C.S.E
- Appears in editions: [1897]

### Verbatim printed entry text (OCR)

**Version `col1897-L35022.v` — printed in editions [1897]:**

> WEBSTER, J. BY, EDWARD E., F.R.C.S.E.—Ed. Diocesan to England, Cape; King's Coll., Lond., and land, 1874; 1st class honours in medicine, medal in Botany, 1st class honours midwifery and diseases of women, asst. demonstrator anatomy, Edin., L.R.C.P.E., L.R.C.S.E., fellow of Obstetrical Soc., Edin.; colonial surgeon, St. Helena, 1889.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1874 | King's Coll., Lond., and land | — | [1897] |
| 1 | 1889 | colonial surgeon | St. Helena | [1897] |

## Candidate stint `Webster, B___Canada___1918`

- Staff-list name: **Webster, B** | colony: **Canada** | listed 1918–1922 | editions [1918, 1919, 1920, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1918 | B. Webster | County Court Judge | County Court Judges | — | — |
| 1919 | B. Webster | County Court Judge | County Court Judges | — | — |
| 1920 | B. Webster | County Court Judge | County Court Judges | — | — |
| 1922 | B. Webster | County Court Judges | County Court Judges | — | — |

### Deterministic checks: `webster_j-by_e1874` vs `Webster, B___Canada___1918`

- [PASS] surname_gate: bio 'WEBSTER' vs stint 'Webster, B' (exact)
- [PASS] initials: bio ['J', 'B'] ~ stint ['B']
- [PASS] age_gate: stint starts 1918; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1918-1922
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Webster, John___Canada___1905`

- Staff-list name: **Webster, John** | colony: **Canada** | listed 1905–1907 | editions [1905, 1906, 1907]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | J. S. Webster | Chief Clerk | Department of Fisheries | — | — |
| 1906 | J. S. Webster | Chief Clerk | Department of Fisheries | — | — |
| 1907 | J. S. Webster | Chief Clerk | Department of Fisheries | — | — |

### Deterministic checks: `webster_j-by_e1874` vs `Webster, John___Canada___1905`

- [PASS] surname_gate: bio 'WEBSTER' vs stint 'Webster, John' (exact)
- [PASS] initials: bio ['J', 'B'] ~ stint ['J']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1907
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

