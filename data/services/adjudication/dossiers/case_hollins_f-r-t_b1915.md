<!-- {"case_id": "case_hollins_f-r-t_b1915", "bio_ids": ["hollins_f-r-t_b1915"], "stint_ids": ["Hollins, F. R. T___Fiji___1950", "Hollins, F. R. T___Western Pacific___1954"]} -->
# Dossier case_hollins_f-r-t_b1915

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hollins_f-r-t_b1915`

- Printed name: **HOLLINS, F. R. T**
- Birth year: 1915 (attested in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963])
- Appears in editions: [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1956-L21937.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963]:**

> HOLLINS, F. R. T.—b. 1915; ed. Wesley Coll., Dublin, and Dublin Univ.; mil. serv., 1940-46; M.O.H., Fiji, 1946; S.M.O., B.S.I.P., 1953; Tang., 1956-62. (Tang. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | M.O.H. | Fiji | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 1 | 1953 | S.M.O., B.S.I.P | Fiji *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 2 | 1956–1962 | S.M.O., B.S.I.P | Tanganyika | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |

## Candidate stint `Hollins, F. R. T___Fiji___1950`

- Staff-list name: **Hollins, F. R. T** | colony: **Fiji** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | F. R. T. Hollins | Medical Officer | Medical | — | — |
| 1951 | F. R. T. Hollins | Medical Officer | MEDICAL | — | — |

### Deterministic checks: `hollins_f-r-t_b1915` vs `Hollins, F. R. T___Fiji___1950`

- [PASS] surname_gate: bio 'HOLLINS' vs stint 'Hollins, F. R. T' (exact)
- [PASS] initials: bio ['F', 'R', 'T'] ~ stint ['F', 'R', 'T']
- [PASS] age_gate: stint starts 1950, birth 1915 (age 35)
- [PASS] colony: 2 placed event(s) resolve to 'Fiji'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1950-1951
- [FAIL] position_sim: best 22 vs bar 60: 'M.O.H.' ~ 'Medical Officer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Hollins, F. R. T___Western Pacific___1954`

- Staff-list name: **Hollins, F. R. T** | colony: **Western Pacific** | listed 1954–1956 | editions [1954, 1955, 1956]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1954 | F. R. T. Hollins | Senior Medical Officer | Civil Establishment | — | — |
| 1955 | F. R. T. Hollins | Senior Medical Officer | Civil Establishment | — | — |
| 1956 | F. R. T. Hollins | Senior Medical Officer | Civil Establishment | — | — |

### Deterministic checks: `hollins_f-r-t_b1915` vs `Hollins, F. R. T___Western Pacific___1954`

- [PASS] surname_gate: bio 'HOLLINS' vs stint 'Hollins, F. R. T' (exact)
- [PASS] initials: bio ['F', 'R', 'T'] ~ stint ['F', 'R', 'T']
- [PASS] age_gate: stint starts 1954, birth 1915 (age 39)
- [FAIL] colony: no placed event resolves to 'Western Pacific'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1954-1956
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

