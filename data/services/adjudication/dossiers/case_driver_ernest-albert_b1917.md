<!-- {"case_id": "case_driver_ernest-albert_b1917", "bio_ids": ["driver_ernest-albert_b1917"], "stint_ids": ["Driver, E. A___West Indies Federation___1961"]} -->
# Dossier case_driver_ernest-albert_b1917

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `driver_ernest-albert_b1917`

- Printed name: **DRIVER, Ernest Albert**
- Birth year: 1917 (attested in editions [1958, 1959])
- Appears in editions: [1951, 1958, 1959]

### Verbatim printed entry text (OCR)

**Version `col1958-L22144.v` — printed in editions [1958, 1959]:**

> DRIVER, E. A.—b. 1917; ed. City of Norwich Sch.; mil. serv., 1939-45, lt.-col.; Br. P.O., 1936; asst. contrlr., E.A. posts and tels., 1949; P.M.G., Trin., 1955-58.

**Version `col1951-L37702.v` — printed in editions [1951]:**

> DRIVER, Ernest Albert.—b. 1917; ed. Norwich Elem. Sch., and City of Norwich Sch.; on mil. serv., 1939-45, lieut.-col.; Br. P.O., 1935; asst. contrlr., posts and tels., E.A., 1949.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1935 | Br. P.O | — | [1951] |
| 1 | 1936 | Br. P.O | — | [1958, 1959] |
| 2 | 1949 | asst. contrlr., E.A. posts and tels | — | [1951, 1958, 1959] |
| 3 | 1955–1958 | P.M.G. | Trinidad | [1958, 1959] |

## Candidate stint `Driver, E. A___West Indies Federation___1961`

- Staff-list name: **Driver, E. A** | colony: **West Indies Federation** | listed 1961–1962 | editions [1961, 1962]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1961 | E. A. Driver | Postal Services Adviser | Law Officers | — | — |
| 1962 | E. A. Driver | Postal Services Adviser | Law Officers | — | — |

### Deterministic checks: `driver_ernest-albert_b1917` vs `Driver, E. A___West Indies Federation___1961`

- [PASS] surname_gate: bio 'DRIVER' vs stint 'Driver, E. A' (exact)
- [PASS] initials: bio ['E', 'A'] ~ stint ['E', 'A']
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

