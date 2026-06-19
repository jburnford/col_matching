<!-- {"case_id": "case_pullinger_j-s_b1919", "bio_ids": ["pullinger_j-s_b1919"], "stint_ids": ["Pullinger, J. S___Gambia___1958"]} -->
# Dossier case_pullinger_j-s_b1919

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `pullinger_j-s_b1919`

- Printed name: **PULLINGER, J. S**
- Birth year: 1919 (attested in editions [1960, 1961, 1962, 1963, 1964])
- Honours: O.B.E (1962)
- Appears in editions: [1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1960-L27122.v` — printed in editions [1960, 1961, 1962, 1963, 1964]:**

> PULLINGER, J. S., O.B.E. (1962), G.M.—b. 1919; ed. Lewes Gram. Sch., and Birmingham Univ.; mil. serv., 1939-46; exec. engnr., Tang., 1951; D.P.W., Gam., 1957.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1951 | exec. engnr. | Tanganyika | [1960, 1961, 1962, 1963, 1964] |
| 1 | 1957 | D.P.W., Gam | Tanganyika *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Pullinger, J. S___Gambia___1958`

- Staff-list name: **Pullinger, J. S** | colony: **Gambia** | listed 1958–1964 | editions [1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1958 | J. S. Pullinger | Director of Public Works | Civil Establishment | — | — |
| 1959 | J. S. Pullinger | Director of Public Works | Civil Establishment | — | — |
| 1960 | J. S. Pullinger | Director of Public Works | Civil Establishment | — | — |
| 1961 | J. S. Pullinger | Director of Public Works | Civil Establishment | — | — |
| 1962 | J. S. Pullinger | Director of Public Works | Civil Establishment | — | — |
| 1963 | J. S. Pullinger | Secretary to Ministry and Director of Public Works | Ministry of Works and Services | — | — |
| 1964 | J. S. Pullinger | Director of Public Works and Controller of Civil Aviation | Ministry of Works and Communications | — | — |

### Deterministic checks: `pullinger_j-s_b1919` vs `Pullinger, J. S___Gambia___1958`

- [PASS] surname_gate: bio 'PULLINGER' vs stint 'Pullinger, J. S' (exact)
- [PASS] initials: bio ['J', 'S'] ~ stint ['J', 'S']
- [PASS] age_gate: stint starts 1958, birth 1919 (age 39)
- [FAIL] colony: no placed event resolves to 'Gambia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1958-1964
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

