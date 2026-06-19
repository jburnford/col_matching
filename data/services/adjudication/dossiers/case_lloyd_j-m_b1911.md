<!-- {"case_id": "case_lloyd_j-m_b1911", "bio_ids": ["lloyd_j-m_b1911"], "stint_ids": ["Lloyd, J. M___Jamaica___1949", "Lloyd, J. M___Jamaica___1955"]} -->
# Dossier case_lloyd_j-m_b1911

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 58 official(s) with this surname in the graph's staff lists; 31 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `lloyd_j-m_b1911`

- Printed name: **LLOYD, J. M**
- Birth year: 1911 (attested in editions [1958, 1959, 1961, 1962, 1964])
- Honours: C.M.G (1961)
- Appears in editions: [1958, 1959, 1961, 1962, 1964]

### Verbatim printed entry text (OCR)

**Version `col1958-L24658.v` — printed in editions [1958, 1959, 1961, 1962, 1964]:**

> LLOYD, J. M., C.M.G. (1961).—b. 1911; ed. Wolmer's Boys' Sch., J'ca.; barrister-at-law, Lincoln's Inn; asstt., registr.-gen's dept., J'ca., 1931; 2nd cl. clk., 1939; 1st cl., 1943; asstt. registr.-gen., 1947; asstt. sec., sect., 1950; prin. asst. sec., 1953; perm. sec., min. of local govt. and housing, 1956; admin., Grenada, 1957.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1931 | asstt., registr.-gen's dept. | Jamaica | [1958, 1959, 1961, 1962, 1964] |
| 1 | 1939 | 2nd cl. clk | Jamaica *(inherited from previous clause)* | [1958, 1959, 1961, 1962, 1964] |
| 2 | 1943 | 1st cl | Jamaica *(inherited from previous clause)* | [1958, 1959, 1961, 1962, 1964] |
| 3 | 1947 | asstt. registr.-gen | Jamaica *(inherited from previous clause)* | [1958, 1959, 1961, 1962, 1964] |
| 4 | 1950 | asstt. sec., sect | Jamaica *(inherited from previous clause)* | [1958, 1959, 1961, 1962, 1964] |
| 5 | 1953 | prin. asst. sec | Jamaica *(inherited from previous clause)* | [1958, 1959, 1961, 1962, 1964] |
| 6 | 1956 | perm. sec., min. of local govt. and housing | Jamaica *(inherited from previous clause)* | [1958, 1959, 1961, 1962, 1964] |
| 7 | 1957 | admin. | Grenada | [1958, 1959, 1961, 1962, 1964] |

## Candidate stint `Lloyd, J. M___Jamaica___1949`

- Staff-list name: **Lloyd, J. M** | colony: **Jamaica** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | J. M. Lloyd | Assistant Registrar General | Registrar General and Island Record Office | — | — |
| 1950 | J. M. Lloyd | Assistant Registrar General | Registrar General and Island Record Office | — | — |
| 1951 | J. M. Lloyd | Assistant Registrar-General | Registrar-General and Island Record | — | — |

### Deterministic checks: `lloyd_j-m_b1911` vs `Lloyd, J. M___Jamaica___1949`

- [PASS] surname_gate: bio 'LLOYD' vs stint 'Lloyd, J. M' (exact)
- [PASS] initials: bio ['J', 'M'] ~ stint ['J', 'M']
- [PASS] age_gate: stint starts 1949, birth 1911 (age 38)
- [PASS] colony: 7 placed event(s) resolve to 'Jamaica'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [PASS] position_sim: best 76 vs bar 60: 'asstt. registr.-gen' ~ 'Assistant Registrar-General'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Lloyd, J. M___Jamaica___1955`

- Staff-list name: **Lloyd, J. M** | colony: **Jamaica** | listed 1955–1956 | editions [1955, 1956]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1955 | J. M. Lloyd | Principal Assistant Secretary | Civil Establishment | — | — |
| 1956 | J. M. Lloyd | Principal Assistant Secretary | Civil Establishment | — | — |

### Deterministic checks: `lloyd_j-m_b1911` vs `Lloyd, J. M___Jamaica___1955`

- [PASS] surname_gate: bio 'LLOYD' vs stint 'Lloyd, J. M' (exact)
- [PASS] initials: bio ['J', 'M'] ~ stint ['J', 'M']
- [PASS] age_gate: stint starts 1955, birth 1911 (age 44)
- [PASS] colony: 7 placed event(s) resolve to 'Jamaica'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1955-1956
- [PASS] position_sim: best 62 vs bar 60: 'prin. asst. sec' ~ 'Principal Assistant Secretary'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

