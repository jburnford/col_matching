<!-- {"case_id": "case_mccoll_james-hiers_b1844", "bio_ids": ["mccoll_james-hiers_b1844"], "stint_ids": ["McColl, J. H___Commonwealth Of Australia___1905", "McColl, Jeffry___Canada___1888"]} -->
# Dossier case_mccoll_james-hiers_b1844

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mccoll_james-hiers_b1844`

- Printed name: **McCOLL, James Hiers**
- Birth year: 1844 (attested in editions [1918, 1920])
- Appears in editions: [1918, 1920]

### Verbatim printed entry text (OCR)

**Version `col1918-L52382.v` — printed in editions [1918, 1920]:**

> McCOLL, Hon. James Hiers.—B. 1844; min. of mines, Victoria, 1893-4; min. of lands, Victoria, 1899-1900; mem. of Senate, C. of A., 1906; vice-pres. of exec. coun., C. of A., June, 1913-Sept., 1914.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1893–1894 | min. of mines | Victoria | [1918, 1920] |
| 1 | 1899–1900 | min. of lands | Victoria | [1918, 1920] |
| 2 | 1906 | mem. of Senate, C. of A | Victoria *(inherited from previous clause)* | [1918, 1920] |
| 3 | 1913–1914 | vice-pres. of exec. coun., C. of A | Victoria *(inherited from previous clause)* | [1918, 1920] |

## Candidate stint `McColl, J. H___Commonwealth Of Australia___1905`

- Staff-list name: **McColl, J. H** | colony: **Commonwealth Of Australia** | listed 1905–1907 | editions [1905, 1907]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | J. H. McColl | Member of Legislative Assembly | Parliament | — | — |
| 1907 | J. H. McColl | Echuca | — | — | — |

### Deterministic checks: `mccoll_james-hiers_b1844` vs `McColl, J. H___Commonwealth Of Australia___1905`

- [PASS] surname_gate: bio 'McCOLL' vs stint 'McColl, J. H' (exact)
- [PASS] initials: bio ['J', 'H'] ~ stint ['J', 'H']
- [PASS] age_gate: stint starts 1905, birth 1844 (age 61)
- [FAIL] colony: no placed event resolves to 'Commonwealth Of Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1907
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `McColl, Jeffry___Canada___1888`

- Staff-list name: **McColl, Jeffry** | colony: **Canada** | listed 1888–1890 | editions [1888, 1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | Jeffry McColl | Member | Constituencies | — | — |
| 1889 | Jeffry McColl | Picton County | Members | — | — |
| 1890 | Jeffry McColl | — | — | — | — |

### Deterministic checks: `mccoll_james-hiers_b1844` vs `McColl, Jeffry___Canada___1888`

- [PASS] surname_gate: bio 'McCOLL' vs stint 'McColl, Jeffry' (exact)
- [PASS] initials: bio ['J', 'H'] ~ stint ['J']
- [PASS] age_gate: stint starts 1888, birth 1844 (age 44)
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1888-1890
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

