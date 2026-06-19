<!-- {"case_id": "case_miles_francis-norman_b1897", "bio_ids": ["miles_francis-norman_b1897"], "stint_ids": ["Miles, F. N___Jamaica___1922", "Miles, F. N___Jamaica___1949"]} -->
# Dossier case_miles_francis-norman_b1897

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 29 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `miles_francis-norman_b1897`

- Printed name: **MILES, Francis Norman**
- Birth year: 1897 (attested in editions [1949, 1950, 1951])
- Appears in editions: [1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1949-L34307.v` — printed in editions [1949, 1950, 1951]:**

> MILES, Francis Norman.—b. 1897; ed. Blundell's Sch. and H.M.S. "Worcester"; Nautical Training Coll.; on naval serv. 1915-19, sub-lt., R.N.V.R., R.N.P.; sub-inspr. of pol., J'ca., 1921; 3rd cl. inspr., 1924; 2nd cl., 1932; 1st cl., 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915–1919 | sub-lt. | — | [1949, 1950, 1951] |
| 1 | 1921 | sub-inspr. of pol. | Jamaica | [1949, 1950, 1951] |
| 2 | 1924 | 3rd cl. inspr. | — | [1949, 1950, 1951] |
| 3 | 1932 | 2nd cl. | — | [1949, 1950, 1951] |
| 4 | 1938 | 1st cl. | — | [1949, 1950, 1951] |

## Candidate stint `Miles, F. N___Jamaica___1922`

- Staff-list name: **Miles, F. N** | colony: **Jamaica** | listed 1922–1940 | editions [1922, 1923, 1925, 1927, 1928, 1930, 1933, 1934, 1937, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | F. N. Miles | Sub-Inspector | Jamaica Constabulary | — | — |
| 1923 | F. N. Miles | Sub-Inspector | Jamaica Constabulary | — | — |
| 1925 | F. N. Miles | 3rd Class Inspector | Jamaica Constabulary | — | — |
| 1927 | F. N. Miles | 3rd Class Inspector | Jamaica Constabulary | — | — |
| 1928 | F. N. Miles | 3rd Class Inspector | Jamaica Constabulary | — | — |
| 1930 | F. N. Miles | 3rd Class Inspector | Jamaica Constabulary | — | — |
| 1933 | F. N. Miles | 2nd Class Inspector | Jamaica Constabulary | — | — |
| 1934 | F. N. Miles | 2nd Class Inspector | Jamaica Constabulary | — | — |
| 1937 | F. N. Miles | 2nd Class Inspector | Jamaica Constabulary | — | — |
| 1940 | F. N. Miles | 1st Class Inspector | Jamaica Constabulary | — | — |

### Deterministic checks: `miles_francis-norman_b1897` vs `Miles, F. N___Jamaica___1922`

- [PASS] surname_gate: bio 'MILES' vs stint 'Miles, F. N' (exact)
- [PASS] initials: bio ['F', 'N'] ~ stint ['F', 'N']
- [PASS] age_gate: stint starts 1922, birth 1897 (age 25)
- [PASS] colony: 1 placed event(s) resolve to 'Jamaica'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1922-1940
- [FAIL] position_sim: best 59 vs bar 60: 'sub-inspr. of pol.' ~ 'Sub-Inspector'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Miles, F. N___Jamaica___1949`

- Staff-list name: **Miles, F. N** | colony: **Jamaica** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | F. N. Miles | Superintendents of Police | POLICE | — | — |
| 1950 | F. N. Miles | Superintendent of Police | Police | — | — |
| 1951 | F. N. Miles | Superintendent of Police | POLICE | — | — |

### Deterministic checks: `miles_francis-norman_b1897` vs `Miles, F. N___Jamaica___1949`

- [PASS] surname_gate: bio 'MILES' vs stint 'Miles, F. N' (exact)
- [PASS] initials: bio ['F', 'N'] ~ stint ['F', 'N']
- [PASS] age_gate: stint starts 1949, birth 1897 (age 52)
- [PASS] colony: 1 placed event(s) resolve to 'Jamaica'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
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

