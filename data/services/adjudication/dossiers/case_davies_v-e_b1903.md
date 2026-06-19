<!-- {"case_id": "case_davies_v-e_b1903", "bio_ids": ["davies_v-e_b1903"], "stint_ids": ["Davies, V. E___Gambia___1919", "Davies, V. E___Gambia___1957"]} -->
# Dossier case_davies_v-e_b1903

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 137 official(s) with this surname in the graph's staff lists; 84 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `davies_v-e_b1903`

- Printed name: **DAVIES, V. E**
- Birth year: 1903 (attested in editions [1954, 1955, 1956, 1959, 1960])
- Honours: O.B.E (1946)
- Appears in editions: [1954, 1955, 1956, 1957, 1958, 1959, 1960]

### Verbatim printed entry text (OCR)

**Version `col1954-L20145.v` — printed in editions [1954, 1955, 1956, 1959, 1960]:**

> DAVIES, V. E., O.B.E. (1946).—b. 1903; ed. St. John's, Leatherhead and Peterhouse, Camb.; I.C.S., 1926–49; admin. offr. (contract), Mal., 1953; dep. fin. sec. (econ.), S'pore, 1955; fin. sec., Gam., 1957–59.

**Version `col1957-L22436.v` — printed in editions [1957, 1958]:**

> DAVIES, V. E., O.B.E. (1946).—b. 1903; ed. St. John’s Leatherhead, and Peterhouse, Camb.; I.C.S., 1926–49; admin. offr. (contract), Mal., 1953; dep. fin. sec. (econ.), S’pore, 1955; fin. sec., Gam., 1957.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926–1949 | I.C.S | — | [1954, 1955, 1956, 1957, 1958, 1959, 1960] |
| 1 | 1953 | admin. offr. (contract) | Malaya | [1954, 1955, 1956, 1957, 1958, 1959, 1960] |
| 2 | 1955 | dep. fin. sec. (econ.), S'pore | Malaya *(inherited from previous clause)* | [1954, 1955, 1956, 1957, 1958, 1959, 1960] |
| 3 | 1957–1959 | fin. sec., Gam | Malaya *(inherited from previous clause)* | [1954, 1955, 1956, 1957, 1958, 1959, 1960] |

## Candidate stint `Davies, V. E___Gambia___1919`

- Staff-list name: **Davies, V. E** | colony: **Gambia** | listed 1919–1924 | editions [1919, 1921, 1922, 1923, 1924]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1919 | V. Davies | 3rd Class Compositor | Printing Branch | — | — |
| 1921 | V. E. Davies | 2nd Class Composer | Printing Branch | — | — |
| 1922 | V. E. Davies | 2nd Class Compositor | Printing Branch | — | — |
| 1923 | V. E. Davies | 2nd Class Composer | Printing Branch | — | — |
| 1924 | V. E. Davies | Five 2nd Class Compositors | Printing Branch | — | — |

### Deterministic checks: `davies_v-e_b1903` vs `Davies, V. E___Gambia___1919`

- [PASS] surname_gate: bio 'DAVIES' vs stint 'Davies, V. E' (exact)
- [PASS] initials: bio ['V', 'E'] ~ stint ['V', 'E']
- [PASS] age_gate: stint starts 1919, birth 1903 (age 16)
- [FAIL] colony: no placed event resolves to 'Gambia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1919-1924
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Davies, V. E___Gambia___1957`

- Staff-list name: **Davies, V. E** | colony: **Gambia** | listed 1957–1959 | editions [1957, 1958, 1959]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1957 | V. E. Davies | Financial Secretary | Civil Establishment | — | — |
| 1958 | V. E. Davies | Financial Secretary | Civil Establishment | — | — |
| 1959 | V. E. Davies | Financial Secretary | Civil Establishment | — | — |

### Deterministic checks: `davies_v-e_b1903` vs `Davies, V. E___Gambia___1957`

- [PASS] surname_gate: bio 'DAVIES' vs stint 'Davies, V. E' (exact)
- [PASS] initials: bio ['V', 'E'] ~ stint ['V', 'E']
- [PASS] age_gate: stint starts 1957, birth 1903 (age 54)
- [FAIL] colony: no placed event resolves to 'Gambia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1957-1959
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

