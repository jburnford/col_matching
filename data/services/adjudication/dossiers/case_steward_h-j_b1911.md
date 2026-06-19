<!-- {"case_id": "case_steward_h-j_b1911", "bio_ids": ["steward_h-j_b1911"], "stint_ids": ["Steward, H. J___High Commission Territories___1959", "Steward, H. J___Swaziland___1962"]} -->
# Dossier case_steward_h-j_b1911

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 10 official(s) with this surname in the graph's staff lists; 13 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `steward_h-j_b1911`

- Printed name: **STEWARD, H. J**
- Birth year: 1911 (attested in editions [1957, 1958, 1959, 1960, 1961, 1963, 1964, 1965, 1966])
- Honours: O.B.E (1956)
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1957-L27506.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1963, 1964, 1965, 1966]:**

> STEWARD, H. J., O.B.E. (1956).—b. 1911; ed. Potchefstroom Boys' High Sch. and Witwatersrand Univ.; clk., Swaz., 1930; asst. D.O., 1937; D.O., 1948; 1st asst. sec., 1955; asst. govt. sec., 1961-65.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1930 | clk., Swaz | — | [1957, 1958, 1959, 1960, 1961, 1963, 1964, 1965, 1966] |
| 1 | 1937 | asst. D.O | — | [1957, 1958, 1959, 1960, 1961, 1963, 1964, 1965, 1966] |
| 2 | 1948 | asst. D.O | Dominions Office | [1957, 1958, 1959, 1960, 1961, 1963, 1964, 1965, 1966] |
| 3 | 1955 | 1st asst. sec | Dominions Office *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1963, 1964, 1965, 1966] |
| 4 | 1961–1965 | asst. govt. sec | Dominions Office *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1963, 1964, 1965, 1966] |

## Candidate stint `Steward, H. J___High Commission Territories___1959`

- Staff-list name: **Steward, H. J** | colony: **High Commission Territories** | listed 1959–1964 | editions [1959, 1960, 1963, 1964]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1959 | H. J. Steward | First Assistant Secretary | SWAZILAND | O.B.E. | — |
| 1960 | H. J. Steward | First Assistant Secretary | SWAZILAND | O.B.E. | — |
| 1963 | H. J. Steward | Assistant Government Secretary | SECRETARIAT | O.B.E. | — |
| 1964 | H. J. Steward | Assistant Chief Secretary | Civil Establishment | — | — |

### Deterministic checks: `steward_h-j_b1911` vs `Steward, H. J___High Commission Territories___1959`

- [PASS] surname_gate: bio 'STEWARD' vs stint 'Steward, H. J' (exact)
- [PASS] initials: bio ['H', 'J'] ~ stint ['H', 'J']
- [PASS] age_gate: stint starts 1959, birth 1911 (age 48)
- [FAIL] colony: no placed event resolves to 'High Commission Territories'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1959-1964
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: O.B.E
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Steward, H. J___Swaziland___1962`

- Staff-list name: **Steward, H. J** | colony: **Swaziland** | listed 1962–1965 | editions [1962, 1965]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1962 | H. J. Steward | Assistant Secretary | Secretariat | — | — |
| 1965 | H. J. Steward | Assistant Chief Secretary | Secretariat | — | — |

### Deterministic checks: `steward_h-j_b1911` vs `Steward, H. J___Swaziland___1962`

- [PASS] surname_gate: bio 'STEWARD' vs stint 'Steward, H. J' (exact)
- [PASS] initials: bio ['H', 'J'] ~ stint ['H', 'J']
- [PASS] age_gate: stint starts 1962, birth 1911 (age 51)
- [FAIL] colony: no placed event resolves to 'Swaziland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1962-1965
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

