<!-- {"case_id": "case_lawrence_nathan-cooj_b1900", "bio_ids": ["lawrence_nathan-cooj_b1900"], "stint_ids": ["Lawrence, N. C___Gold Coast___1949", "Lawrence, N___Hong Kong___1956"]} -->
# Dossier case_lawrence_nathan-cooj_b1900

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 58 official(s) with this surname in the graph's staff lists; 24 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Lawrence, N. C___Gold Coast___1949` is also gate-compatible with biography(ies) outside this case: ['lawrence_n_b1918', 'lawrence_nathan-codjoe_b1900', 'lawrence_nathan-cojo_b1900'] (already linked elsewhere or filtered).
- NOTE: stint `Lawrence, N___Hong Kong___1956` is also gate-compatible with biography(ies) outside this case: ['lawrence_c-n_b1917', 'lawrence_n_b1918', 'lawrence_nathan-codjoe_b1900', 'lawrence_nathan-cojo_b1900'] (already linked elsewhere or filtered).

## Biography `lawrence_nathan-cooj_b1900`

- Printed name: **LAWRENCE, NATHAN COOJ**
- Birth year: 1900 (attested in editions [1939, 1940])
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L68541.v` — printed in editions [1939, 1940]:**

> LAWRENCE, NATHAN COOJ, B.A. (London), Teachers' Dipl., Educn. (Lond.), Mem., Inner Temple.—B. 1900; ed. Kppong Methodist Schol., King's Coll., London and Univ. of London; clk., gov.'s office, Gold Coast, July, 1924; resigned, 1930; 2nd divn. teacher, 1937; inspr. schls., 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1924 | clk., gov.'s office | Gold Coast | [1939, 1940] |
| 1 | 1930 | resigned | Gold Coast *(inherited from previous clause)* | [1939, 1940] |
| 2 | 1937 | 2nd divn. teacher | Gold Coast *(inherited from previous clause)* | [1939, 1940] |
| 3 | 1938 | inspr. schls | Gold Coast *(inherited from previous clause)* | [1939, 1940] |

## Candidate stint `Lawrence, N. C___Gold Coast___1949`

- Staff-list name: **Lawrence, N. C** | colony: **Gold Coast** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | N. C. Lawrence | Education Officer | Education | — | — |
| 1950 | N. C. Lawrence | Education Officers | Education | — | — |

### Deterministic checks: `lawrence_nathan-cooj_b1900` vs `Lawrence, N. C___Gold Coast___1949`

- [PASS] surname_gate: bio 'LAWRENCE' vs stint 'Lawrence, N. C' (exact)
- [PASS] initials: bio ['N', 'C'] ~ stint ['N', 'C']
- [PASS] age_gate: stint starts 1949, birth 1900 (age 49)
- [PASS] colony: 4 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1950
- [FAIL] position_sim: best 34 vs bar 60: 'inspr. schls' ~ 'Education Officers'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Lawrence, N___Hong Kong___1956`

- Staff-list name: **Lawrence, N** | colony: **Hong Kong** | listed 1956–1963 | editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1956 | N. Lawrence | Deputy Director of Royal Observatory | Civil Establishment | — | — |
| 1957 | N. Lawrence | Deputy Director of Royal Observatory | Civil Establishment | — | — |
| 1958 | N. Lawrence | Deputy Director of Royal Observatory | Civil Establishment | — | — |
| 1959 | N. Lawrence | Deputy Director of Royal Observatory | Civil Establishment | — | — |
| 1960 | N. Lawrence | Deputy Director of Royal Observatory | Civil Establishment | — | — |
| 1961 | N. Lawrence | Deputy Director of Royal Observatory | Civil Establishment | — | — |
| 1962 | N. Lawrence | Deputy Director of Royal Observatory | Civil Establishment | — | — |
| 1963 | N. Lawrence | Deputy Director of Royal Observatory | Civil Establishment | — | — |

### Deterministic checks: `lawrence_nathan-cooj_b1900` vs `Lawrence, N___Hong Kong___1956`

- [PASS] surname_gate: bio 'LAWRENCE' vs stint 'Lawrence, N' (exact)
- [PASS] initials: bio ['N', 'C'] ~ stint ['N']
- [PASS] age_gate: stint starts 1956, birth 1900 (age 56)
- [FAIL] colony: no placed event resolves to 'Hong Kong'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1956-1963
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

