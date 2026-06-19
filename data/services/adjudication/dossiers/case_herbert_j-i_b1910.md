<!-- {"case_id": "case_herbert_j-i_b1910", "bio_ids": ["herbert_j-i_b1910"], "stint_ids": ["Herbert, J. I___Uganda___1949"]} -->
# Dossier case_herbert_j-i_b1910

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 26 official(s) with this surname in the graph's staff lists; 10 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `herbert_j-i_b1910`

- Printed name: **HERBERT, J. I**
- Birth year: 1910 (attested in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964])
- Appears in editions: [1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1958-L23552.v` — printed in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964]:**

> HERBERT, J. I.—b. 1910; ed. St. Michael's Prep. Sch. and Trent Coll.; price inspr., Uga., 1940; secon. to municipality, 1949-54; probation offr., community devel. dept., 1954-63. (Uga. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1940 | price inspr. | Uganda | [1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1949–1954 | secon. to municipality | Uganda *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 2 | 1954–1963 | probation offr., community devel. dept | Uganda *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Herbert, J. I___Uganda___1949`

- Staff-list name: **Herbert, J. I** | colony: **Uganda** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | J. I. Herbert | Conservancy Officers, Kampala | Township Authorities | — | — |
| 1951 | J. I. Herbert | Conservancy Officers | Township Authorities | — | — |

### Deterministic checks: `herbert_j-i_b1910` vs `Herbert, J. I___Uganda___1949`

- [PASS] surname_gate: bio 'HERBERT' vs stint 'Herbert, J. I' (exact)
- [PASS] initials: bio ['J', 'I'] ~ stint ['J', 'I']
- [PASS] age_gate: stint starts 1949, birth 1910 (age 39)
- [PASS] colony: 3 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 45 vs bar 60: 'price inspr.' ~ 'Conservancy Officers'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

