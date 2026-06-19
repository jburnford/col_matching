<!-- {"case_id": "case_fairlie_m-j_b1920", "bio_ids": ["fairlie_m-j_b1920"], "stint_ids": ["Fairlie, M. J___High Commission Territories___1963", "Fairlie, M. J___Swaziland___1962"]} -->
# Dossier case_fairlie_m-j_b1920

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `fairlie_m-j_b1920`

- Printed name: **FAIRLIE, M. J**
- Birth year: 1920 (attested in editions [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Honours: O.B.E (1963)
- Appears in editions: [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1959-L22836.v` — printed in editions [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> FAIRLIE, M. J., O.B.E. (1963).—b. 1920; ed. Edin. Academy and Edin. Univ.; mil. serv., 1939-45, capt.; admin. offr., Bech. Prot., 1946; p.s. to high comsnr., B.B. & S., 1951; admin. offr., Swaz., 1953; seconded to C.R.O., 1955-58; first sec., Swaz., 1961; sec. loc. govt. and soc. educ., 1962.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | admin. offr. | Bechuanaland | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1951 | p.s. to high comsnr., B.B. & S | Bechuanaland *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1953 | admin. offr., Swaz | Bechuanaland *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1955–1958 | seconded to C.R.O | Bechuanaland *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 4 | 1961 | first sec., Swaz | Bechuanaland *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 5 | 1962 | sec. loc. govt. and soc. educ | Bechuanaland *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Fairlie, M. J___High Commission Territories___1963`

- Staff-list name: **Fairlie, M. J** | colony: **High Commission Territories** | listed 1963–1964 | editions [1963, 1964]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1963 | M. J. Fairlie | Secretary for Local Government and Social Education | SECRETARIAT | — | — |
| 1964 | M. J. Fairlie | Secretary for Social and Political Affairs | Civil Establishment | — | — |

### Deterministic checks: `fairlie_m-j_b1920` vs `Fairlie, M. J___High Commission Territories___1963`

- [PASS] surname_gate: bio 'FAIRLIE' vs stint 'Fairlie, M. J' (exact)
- [PASS] initials: bio ['M', 'J'] ~ stint ['M', 'J']
- [PASS] age_gate: stint starts 1963, birth 1920 (age 43)
- [FAIL] colony: no placed event resolves to 'High Commission Territories'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1963-1964
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Fairlie, M. J___Swaziland___1962`

- Staff-list name: **Fairlie, M. J** | colony: **Swaziland** | listed 1962–1966 | editions [1962, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1962 | M. J. Fairlie | First Assistant Secretary | Secretariat | — | — |
| 1965 | M. J. Fairlie | Secretary for Social and Political Affairs | Secretariat | — | — |
| 1966 | M. J. Fairlie | Secretary for External Affairs and Labour | Civil Establishment | — | — |

### Deterministic checks: `fairlie_m-j_b1920` vs `Fairlie, M. J___Swaziland___1962`

- [PASS] surname_gate: bio 'FAIRLIE' vs stint 'Fairlie, M. J' (exact)
- [PASS] initials: bio ['M', 'J'] ~ stint ['M', 'J']
- [PASS] age_gate: stint starts 1962, birth 1920 (age 42)
- [FAIL] colony: no placed event resolves to 'Swaziland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1962-1966
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

