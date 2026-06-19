<!-- {"case_id": "case_ford_w_b1912", "bio_ids": ["ford_w_b1912"], "stint_ids": ["Ford, W. E___Northern Rhodesia___1931", "Ford, W. O___Uganda___1927"]} -->
# Dossier case_ford_w_b1912

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 48 official(s) with this surname in the graph's staff lists; 21 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['ford_w_b1912'] carry a single initial only — the namesake trap applies.

## Biography `ford_w_b1912`

- Printed name: **FORD, W**
- Birth year: 1912 (attested in editions [1960, 1961, 1962, 1963, 1964, 1965])
- Honours: C.P.M (1955), O.B.E (1964), Q.P.M (1962)
- Appears in editions: [1960, 1961, 1962, 1963, 1964, 1965]

### Verbatim printed entry text (OCR)

**Version `col1960-L22985.v` — printed in editions [1960, 1961, 1962, 1963, 1964, 1965]:**

> FORD, W., O.B.E. (1964), Q.P.M. (1962), C.P.M. (1955).—b. 1912; ed. Westoe Secondary Sch., and Durham Univ.; asst. supt. police, Nig., 1944; sen. asst. supt., 1949; supt., 1952; senr. supt., 1954; asst. comsnr., 1958; dep. comsnr., 1962-64. (Nig. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1944 | asst. supt. police | Nigeria | [1960, 1961, 1962, 1963, 1964, 1965] |
| 1 | 1949 | sen. asst. supt | Nigeria *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964, 1965] |
| 2 | 1952 | supt | Nigeria *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964, 1965] |
| 3 | 1954 | senr. supt | Nigeria *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964, 1965] |
| 4 | 1958 | asst. comsnr | Nigeria *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964, 1965] |
| 5 | 1962–1964 | dep. comsnr | Nigeria *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964, 1965] |

## Candidate stint `Ford, W. E___Northern Rhodesia___1931`

- Staff-list name: **Ford, W. E** | colony: **Northern Rhodesia** | listed 1931–1933 | editions [1931, 1933]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | W. E. Ford | Research Assistants | Animal Health | — | — |
| 1933 | W. E. Ford | Research Assistant | Animal Health | — | — |

### Deterministic checks: `ford_w_b1912` vs `Ford, W. E___Northern Rhodesia___1931`

- [PASS] surname_gate: bio 'FORD' vs stint 'Ford, W. E' (exact)
- [PASS] initials: bio ['W'] ~ stint ['W', 'E']
- [PASS] age_gate: stint starts 1931, birth 1912 (age 19)
- [FAIL] colony: no placed event resolves to 'Northern Rhodesia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1933
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Ford, W. O___Uganda___1927`

- Staff-list name: **Ford, W. O** | colony: **Uganda** | listed 1927–1940 | editions [1927, 1928, 1929, 1930, 1933, 1936, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | W. O. Ford | Foreman | Public Works | — | — |
| 1928 | W. O. Ford | Foreman | Public Works | — | — |
| 1929 | W. O. Ford | Building Foreman | Public Works | — | — |
| 1930 | W. O. Ford | Building Foreman | Police and Prisons | — | — |
| 1933 | W. O. Ford | Overseer | Public Works Department | — | — |
| 1936 | W. O. Ford | Overseer | Public Works Department | — | — |
| 1939 | W. O. Ford | Overseer | Public Works Department | — | — |
| 1940 | W. O. Ford | Overseer | Public Works Department | — | — |

### Deterministic checks: `ford_w_b1912` vs `Ford, W. O___Uganda___1927`

- [PASS] surname_gate: bio 'FORD' vs stint 'Ford, W. O' (exact)
- [PASS] initials: bio ['W'] ~ stint ['W', 'O']
- [PASS] age_gate: stint starts 1927, birth 1912 (age 15)
- [FAIL] colony: no placed event resolves to 'Uganda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1927-1940
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

