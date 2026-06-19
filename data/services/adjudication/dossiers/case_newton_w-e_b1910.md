<!-- {"case_id": "case_newton_w-e_b1910", "bio_ids": ["newton_w-e_b1910"], "stint_ids": ["Newton, W. E___High Commission Territories___1963", "Newton, W. E___Swaziland___1962"]} -->
# Dossier case_newton_w-e_b1910

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 29 official(s) with this surname in the graph's staff lists; 14 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Newton, W. E___High Commission Territories___1963` is also gate-compatible with biography(ies) outside this case: ['newton_edward_e1859'] (already linked elsewhere or filtered).
- NOTE: stint `Newton, W. E___Swaziland___1962` is also gate-compatible with biography(ies) outside this case: ['newton_edward_e1859'] (already linked elsewhere or filtered).

## Biography `newton_w-e_b1910`

- Printed name: **NEWTON, W. E**
- Birth year: 1910 (attested in editions [1961, 1962, 1963, 1964, 1965])
- Honours: M.B.E (1947)
- Appears in editions: [1961, 1962, 1963, 1964, 1965]

### Verbatim printed entry text (OCR)

**Version `col1961-L25699.v` — printed in editions [1961, 1962, 1963, 1964, 1965]:**

> NEWTON, W. E., M.B.E. (1947).—b. 1910; ed. Vartic Sch., Mon.; mil. serv., 1939-45, capt.; U.K. prisons serv., 1939; F.O. prisons mission to Greece, 1945-50; prisons serv., Som., 1950; supt., prisons, Swaz., 1958.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1939 | U.K. prisons serv | — | [1961, 1962, 1963, 1964, 1965] |
| 1 | 1945–1950 | F.O. prisons mission to Greece | — | [1961, 1962, 1963, 1964, 1965] |
| 2 | 1950 | prisons serv. | Somaliland | [1961, 1962, 1963, 1964, 1965] |
| 3 | 1958 | supt., prisons, Swaz | Somaliland *(inherited from previous clause)* | [1961, 1962, 1963, 1964, 1965] |

## Candidate stint `Newton, W. E___High Commission Territories___1963`

- Staff-list name: **Newton, W. E** | colony: **High Commission Territories** | listed 1963–1964 | editions [1963, 1964]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1963 | W. E. Newton | Superintendent of Prisons | SECRETARIAT | M.B.E. | — |
| 1964 | W. E. Newton | Superintendent of Prisons | Civil Establishment | — | — |

### Deterministic checks: `newton_w-e_b1910` vs `Newton, W. E___High Commission Territories___1963`

- [PASS] surname_gate: bio 'NEWTON' vs stint 'Newton, W. E' (exact)
- [PASS] initials: bio ['W', 'E'] ~ stint ['W', 'E']
- [PASS] age_gate: stint starts 1963, birth 1910 (age 53)
- [FAIL] colony: no placed event resolves to 'High Commission Territories'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1963-1964
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: M.B.E
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Newton, W. E___Swaziland___1962`

- Staff-list name: **Newton, W. E** | colony: **Swaziland** | listed 1962–1966 | editions [1962, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1962 | W. E. Newton | Superintendent of Prisons | Secretariat | — | — |
| 1965 | W. E. Newton | Director of Prisons | Law Officers | — | — |
| 1966 | W. E. Newton | Director of Prisons | Civil Establishment | — | — |

### Deterministic checks: `newton_w-e_b1910` vs `Newton, W. E___Swaziland___1962`

- [PASS] surname_gate: bio 'NEWTON' vs stint 'Newton, W. E' (exact)
- [PASS] initials: bio ['W', 'E'] ~ stint ['W', 'E']
- [PASS] age_gate: stint starts 1962, birth 1910 (age 52)
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

