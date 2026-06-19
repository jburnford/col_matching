<!-- {"case_id": "case_horsham_j-f_b1917", "bio_ids": ["horsham_j-f_b1917"], "stint_ids": ["Horsham, J. F___West Indies Federation___1961"]} -->
# Dossier case_horsham_j-f_b1917

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `horsham_j-f_b1917`

- Printed name: **HORSHAM, J. F**
- Birth year: 1917 (attested in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965])
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]

### Verbatim printed entry text (OCR)

**Version `col1957-L24209.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]:**

> HORSHAM, J. F.—b. 1917; ed. Arima High Sch. and Coll. of Tech., Manchester; mil. serv., 1942-46, flt. sgt.; 2nd cl. clk., Trin., 1939; 1st cl., 1947; labr. offr., 1952; asst. sec., 1954; senr. asst. sec., W. Indies, 1958.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1939 | 2nd cl. clk. | Trinidad | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 1 | 1947 | 1st cl | Trinidad *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 2 | 1952 | labr. offr | Trinidad *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 3 | 1954 | asst. sec | Trinidad *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 4 | 1958 | senr. asst. sec., W. Indies | Trinidad *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |

## Candidate stint `Horsham, J. F___West Indies Federation___1961`

- Staff-list name: **Horsham, J. F** | colony: **West Indies Federation** | listed 1961–1962 | editions [1961, 1962]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1961 | J. F. Horsham | Ministry of Communications and Works | Civil Establishment | — | — |
| 1962 | J. F. Horsham | Ministry of Communications and Works | Civil Establishment | — | — |

### Deterministic checks: `horsham_j-f_b1917` vs `Horsham, J. F___West Indies Federation___1961`

- [PASS] surname_gate: bio 'HORSHAM' vs stint 'Horsham, J. F' (exact)
- [PASS] initials: bio ['J', 'F'] ~ stint ['J', 'F']
- [PASS] age_gate: stint starts 1961, birth 1917 (age 44)
- [FAIL] colony: no placed event resolves to 'West Indies Federation'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1961-1962
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

