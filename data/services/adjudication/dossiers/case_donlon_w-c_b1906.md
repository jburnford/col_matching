<!-- {"case_id": "case_donlon_w-c_b1906", "bio_ids": ["donlon_w-c_b1906"], "stint_ids": ["Donlon, W. C___Nyasaland___1950"]} -->
# Dossier case_donlon_w-c_b1906

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `donlon_w-c_b1906`

- Printed name: **DONLON, W. C**
- Birth year: 1906 (attested in editions [1959, 1960, 1961, 1962])
- Appears in editions: [1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1959-L22483.v` — printed in editions [1959, 1960, 1961, 1962]:**

> DONLON, W. C.—b. 1906; mil. serv., 1941-43; senr. educ. offr., Pal., 1946-48; educ. offr., Nyasa., 1949-61.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946–1948 | senr. educ. offr. | Palestine | [1959, 1960, 1961, 1962] |

## Candidate stint `Donlon, W. C___Nyasaland___1950`

- Staff-list name: **Donlon, W. C** | colony: **Nyasaland** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | W. C. Donlon | Education Officer (Male) | EDUCATION | — | — |
| 1951 | W. C. Donlon | Education Officer | Education | — | — |

### Deterministic checks: `donlon_w-c_b1906` vs `Donlon, W. C___Nyasaland___1950`

- [PASS] surname_gate: bio 'DONLON' vs stint 'Donlon, W. C' (exact)
- [PASS] initials: bio ['W', 'C'] ~ stint ['W', 'C']
- [PASS] age_gate: stint starts 1950, birth 1906 (age 44)
- [FAIL] colony: no placed event resolves to 'Nyasaland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1950-1951
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

