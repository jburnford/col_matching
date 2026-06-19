<!-- {"case_id": "case_whitworth_basil-dudley_b1911", "bio_ids": ["whitworth_basil-dudley_b1911"], "stint_ids": ["Whitworth, B. D___High Commission Territories___1959", "Whitworth, B. D___Swaziland___1962"]} -->
# Dossier case_whitworth_basil-dudley_b1911

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `whitworth_basil-dudley_b1911`

- Printed name: **WHITWORTH, Basil Dudley**
- Birth year: 1911 (attested in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Honours: M.B, O.B.E (1960)
- Appears in editions: [1940, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1958-L28116.v` — printed in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> WHITWORTH, B. D., O.B.E. (1960).—b. 1911; ed. St. Andrew's Coll., Grahamstown. S.A., Emmanuel Coll., Camb. and St. George's Hosp., London; M.O., Basuto., 1938; Swaz., 1955; D.M.S., 1957-65.

**Version `col1940-L69539.v` — printed in editions [1940]:**

> WHITWORTH, Basil Dudley, M.R.C.S. (Eng.), L.R.C.P. (Lond.), M.B., B.Chir. (Cantab.).—Ed. St. Andrew's Coll., Grahamstown and Cambridge; relieving M.O., Basutoland, 1938; M.O., leper sttlmt., 1939.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1938 | M.O. | Basutoland | [1940, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1939 | M.O., leper sttlmt | Basutoland *(inherited from previous clause)* | [1940] |
| 2 | 1955 | Swaz | Basutoland *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1957–1965 | D.M.S | Basutoland *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Whitworth, B. D___High Commission Territories___1959`

- Staff-list name: **Whitworth, B. D** | colony: **High Commission Territories** | listed 1959–1964 | editions [1959, 1960, 1963, 1964]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1959 | B. D. Whitworth | Director of Medical Services | SWAZILAND | — | — |
| 1960 | B. D. Whitworth | Director of Medical Services | SWAZILAND | O.B.E. | — |
| 1963 | B. D. Whitworth | Director of Medical Services | SECRETARIAT | O.B.E. | — |
| 1964 | B. D. Whitworth | Director of Medical Services | Civil Establishment | — | — |

### Deterministic checks: `whitworth_basil-dudley_b1911` vs `Whitworth, B. D___High Commission Territories___1959`

- [PASS] surname_gate: bio 'WHITWORTH' vs stint 'Whitworth, B. D' (exact)
- [PASS] initials: bio ['B', 'D'] ~ stint ['B', 'D']
- [PASS] age_gate: stint starts 1959, birth 1911 (age 48)
- [FAIL] colony: no placed event resolves to 'High Commission Territories'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1959-1964
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: O.B.E
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Whitworth, B. D___Swaziland___1962`

- Staff-list name: **Whitworth, B. D** | colony: **Swaziland** | listed 1962–1965 | editions [1962, 1965]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1962 | B. D. Whitworth | Director of Medical Services | Secretariat | — | — |
| 1965 | B. D. Whitworth | Director of Medical Services | Law Officers | — | — |

### Deterministic checks: `whitworth_basil-dudley_b1911` vs `Whitworth, B. D___Swaziland___1962`

- [PASS] surname_gate: bio 'WHITWORTH' vs stint 'Whitworth, B. D' (exact)
- [PASS] initials: bio ['B', 'D'] ~ stint ['B', 'D']
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

