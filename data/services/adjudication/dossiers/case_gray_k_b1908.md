<!-- {"case_id": "case_gray_k_b1908", "bio_ids": ["gray_k_b1908"], "stint_ids": ["Gray, K. W___Falkland Islands___1964"]} -->
# Dossier case_gray_k_b1908

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 93 official(s) with this surname in the graph's staff lists; 50 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['gray_k_b1908'] carry a single initial only — the namesake trap applies.

## Biography `gray_k_b1908`

- Printed name: **GRAY, K**
- Birth year: 1908 (attested in editions [1959, 1960, 1961, 1962, 1963])
- Appears in editions: [1959, 1960, 1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1959-L23551.v` — printed in editions [1959, 1960, 1961, 1962, 1963]:**

> GRAY, Miss K.—b. 1908; ed. Bacup and Rawtenstall Gram. Sch., and Univ. Coll. of Wales, Aberystwyth; prov. educ. offr., Nyasa., 1946; Uga., 1950; senr. educ. offr., 1955–62. (Uga. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | prov. educ. offr. | Nyasaland | [1959, 1960, 1961, 1962, 1963] |
| 1 | 1950 | prov. educ. offr. | Uganda | [1959, 1960, 1961, 1962, 1963] |
| 2 | 1955–1962 | senr. educ. offr | Uganda *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963] |

## Candidate stint `Gray, K. W___Falkland Islands___1964`

- Staff-list name: **Gray, K. W** | colony: **Falkland Islands** | listed 1964–1966 | editions [1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1964 | K. W. Gray | Chief Constable | Civil Establishment | M.C. | — |
| 1965 | K. W. Gray | Supt. of Police | Civil Establishment | — | — |
| 1966 | K. W. Gray | Supt. of Police | Civil Establishment | — | — |

### Deterministic checks: `gray_k_b1908` vs `Gray, K. W___Falkland Islands___1964`

- [PASS] surname_gate: bio 'GRAY' vs stint 'Gray, K. W' (exact)
- [PASS] initials: bio ['K'] ~ stint ['K', 'W']
- [PASS] age_gate: stint starts 1964, birth 1908 (age 56)
- [FAIL] colony: no placed event resolves to 'Falkland Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1964-1966
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

