<!-- {"case_id": "case_pitcher_w-e-c_b1918", "bio_ids": ["pitcher_w-e-c_b1918"], "stint_ids": ["Pitcher, W. E. C___High Commission Territories___1952", "Pitcher, W. E. C___Swaziland___1954"]} -->
# Dossier case_pitcher_w-e-c_b1918

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `pitcher_w-e-c_b1918`

- Printed name: **PITCHER, W. E. C**
- Birth year: 1918 (attested in editions [1953, 1954, 1955, 1956, 1957, 1958, 1961, 1962, 1963])
- Honours: O.B.E (1958)
- Appears in editions: [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1953-L18734.v` — printed in editions [1953, 1954, 1955, 1956, 1957, 1958, 1961, 1962, 1963]:**

> PITCHER, W. E. C., O.B.E. (1958).—b. 1918; ed. Estcourt High Sch., Natal Univ. Coll. and Pretoria Univ.; mil. serv., 1939-46, lieut.; Natal educ. dept., 1939-45; inspr. of schs., Swaz., 1946; educ. offir., 1949; prin. educ. offir., 1951; dir., educ., 1954.

**Version `col1959-L26894.v` — printed in editions [1959, 1960]:**

> PITCHER, W. E. C., O.B.E. (1958).—b. 1918; ed. Estcourt High Sch., Natal Univ. Coll. and Pretoria Univ.; mil. serv., 1940-45, lieut.; Natal educ. dept., 1939-45; inspr. of schs., Swaz., 1946; educ. offr., 1949; dir., educ., 1951.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1939–1945 | Natal educ. dept | Natal | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 1 | 1946 | inspr. of schs., Swaz | Natal *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 2 | 1951 | prin. educ. offir | Natal *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 3 | 1954 | dir., educ | Natal *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1961, 1962, 1963] |

## Candidate stint `Pitcher, W. E. C___High Commission Territories___1952`

- Staff-list name: **Pitcher, W. E. C** | colony: **High Commission Territories** | listed 1952–1963 | editions [1952, 1959, 1960, 1963]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1952 | W. E. C. Pitcher | Principal Education Officer | SWAZILAND | — | — |
| 1959 | W. E. C. Pitcher | Director of Education | SWAZILAND | O.B.E. | — |
| 1960 | W. E. C. Pitcher | Director of Education | SWAZILAND | O.B.E. | — |
| 1963 | W. E. C. Pitcher | Director of Education | SECRETARIAT | O.B.E. | — |

### Deterministic checks: `pitcher_w-e-c_b1918` vs `Pitcher, W. E. C___High Commission Territories___1952`

- [PASS] surname_gate: bio 'PITCHER' vs stint 'Pitcher, W. E. C' (exact)
- [PASS] initials: bio ['W', 'E', 'C'] ~ stint ['W', 'E', 'C']
- [PASS] age_gate: stint starts 1952, birth 1918 (age 34)
- [FAIL] colony: no placed event resolves to 'High Commission Territories'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1952-1963
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: O.B.E
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Pitcher, W. E. C___Swaziland___1954`

- Staff-list name: **Pitcher, W. E. C** | colony: **Swaziland** | listed 1954–1962 | editions [1954, 1962]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1954 | W. E. C. Pitcher | Principal Education Officer | — | — | — |
| 1962 | W. E. C. Pitcher | Director of Education | Secretariat | — | — |

### Deterministic checks: `pitcher_w-e-c_b1918` vs `Pitcher, W. E. C___Swaziland___1954`

- [PASS] surname_gate: bio 'PITCHER' vs stint 'Pitcher, W. E. C' (exact)
- [PASS] initials: bio ['W', 'E', 'C'] ~ stint ['W', 'E', 'C']
- [PASS] age_gate: stint starts 1954, birth 1918 (age 36)
- [FAIL] colony: no placed event resolves to 'Swaziland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1954-1962
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

