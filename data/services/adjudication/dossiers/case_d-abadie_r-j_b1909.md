<!-- {"case_id": "case_d-abadie_r-j_b1909", "bio_ids": ["d-abadie_r-j_b1909"], "stint_ids": ["D\u2019Abadie, R. J___Trinidad and Tobago___1953", "d'Abadie, R. J___Trinidad and Tobago___1937"]} -->
# Dossier case_d-abadie_r-j_b1909

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `d-abadie_r-j_b1909`

- Printed name: **D'ABADIE, R. J**
- Birth year: 1909 (attested in editions [1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964])
- Appears in editions: [1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1951-L37364.v` — printed in editions [1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]:**

> D'ABADIE, R. J.—b. 1909; ed. St. Mary's Coll., Trin.; clk., secretariat, Trin., 1928; asst. warden, district admin., 1940; warden, 1947; senr. warden, 1958. (T'dad Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | clk., secretariat | Trinidad | [1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1940 | asst. warden, district admin | Trinidad *(inherited from previous clause)* | [1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 2 | 1947 | warden | Trinidad *(inherited from previous clause)* | [1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 3 | 1958 | senr. warden | Trinidad *(inherited from previous clause)* | [1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `D’Abadie, R. J___Trinidad and Tobago___1953`

- Staff-list name: **D’Abadie, R. J** | colony: **Trinidad and Tobago** | listed 1953–1962 | editions [1953, 1962]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1953 | R. J. D’Abadie | Wardens | Civil Establishment | — | — |
| 1962 | R. J. D’Abadie | Senior Warden, District Administration | Civil Establishment | — | — |

### Deterministic checks: `d-abadie_r-j_b1909` vs `D’Abadie, R. J___Trinidad and Tobago___1953`

- [PASS] surname_gate: bio 'D'ABADIE' vs stint 'D’Abadie, R. J' (exact)
- [PASS] initials: bio ['R', 'J'] ~ stint ['R', 'J']
- [PASS] age_gate: stint starts 1953, birth 1909 (age 44)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1953-1962
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `d'Abadie, R. J___Trinidad and Tobago___1937`

- Staff-list name: **d'Abadie, R. J** | colony: **Trinidad and Tobago** | listed 1937–1940 | editions [1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1937 | R. J. d'Abadie | 2nd Class Clerk | Colonial Secretary's Department | — | — |
| 1939 | R. J. d'Abadie | 1st Class Clerks | Colonial Secretary's Department | — | — |
| 1940 | R. J. d'Abadie | Senior Clerks | Colonial Secretary's Department | — | — |

### Deterministic checks: `d-abadie_r-j_b1909` vs `d'Abadie, R. J___Trinidad and Tobago___1937`

- [PASS] surname_gate: bio 'D'ABADIE' vs stint 'd'Abadie, R. J' (exact)
- [PASS] initials: bio ['R', 'J'] ~ stint ['R', 'J']
- [PASS] age_gate: stint starts 1937, birth 1909 (age 28)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1937-1940
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

