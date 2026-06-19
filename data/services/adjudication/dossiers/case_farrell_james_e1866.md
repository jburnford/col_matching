<!-- {"case_id": "case_farrell_james_e1866", "bio_ids": ["farrell_james_e1866"], "stint_ids": ["Farrell, J. V___Leeward Islands___1897", "Farrell, J___Cape of Good Hope___1877", "Farrell, W. J___Palestine___1924"]} -->
# Dossier case_farrell_james_e1866

## Case context

- 1 biography(ies) and 3 candidate stint(s) are entangled in this case.
- Corpus context: 13 official(s) with this surname in the graph's staff lists; 10 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['farrell_james_e1866'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Farrell, W. J___Palestine___1924` is also gate-compatible with biography(ies) outside this case: ['farrell_wilfrid-jerome_b1882'] (already linked elsewhere or filtered).

## Biography `farrell_james_e1866`

- Printed name: **FARRELL, JAMES**
- Birth year: not printed
- Appears in editions: [1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1888-L33354.v` — printed in editions [1888, 1889, 1890]:**

> FARRELL, JAMES.—Member legislative assembly, Victoria, 1866-78; librarian to parliament, Jan., 1879.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1866–1878 | Member legislative assembly | Victoria | [1888, 1889, 1890] |
| 1 | 1879 | librarian to parliament | Victoria *(inherited from previous clause)* | [1888, 1889, 1890] |

## Candidate stint `Farrell, J. V___Leeward Islands___1897`

- Staff-list name: **Farrell, J. V** | colony: **Leeward Islands** | listed 1897–1899 | editions [1897, 1899]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1897 | J. V. Farrell | A.D.C. Secretary and A.D.C. | Civil Establishment | — | — |
| 1897 | J. Farrell | Keeper of H.M. Prison | Police and Prison | — | — |
| 1899 | J. Farrell | Keeper of H.M. Prison | Police and Prison | — | — |

### Deterministic checks: `farrell_james_e1866` vs `Farrell, J. V___Leeward Islands___1897`

- [PASS] surname_gate: bio 'FARRELL' vs stint 'Farrell, J. V' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J', 'V']
- [PASS] age_gate: stint starts 1897; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1897-1899
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Farrell, J___Cape of Good Hope___1877`

- Staff-list name: **Farrell, J** | colony: **Cape of Good Hope** | listed 1877–1880 | editions [1877, 1878, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | J. Farrell | Tide Waiter | Port of Cape Town | — | — |
| 1878 | J. Farrell | Tide Waiter | Port of Cape Town | — | — |
| 1880 | J. Farrell | Tide Waiter | Port of Cape Town | — | — |

### Deterministic checks: `farrell_james_e1866` vs `Farrell, J___Cape of Good Hope___1877`

- [PASS] surname_gate: bio 'FARRELL' vs stint 'Farrell, J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1880
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Farrell, W. J___Palestine___1924`

- Staff-list name: **Farrell, W. J** | colony: **Palestine** | listed 1924–1940 | editions [1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1924 | W. J. Farrell | Education Officers | Education | — | — |
| 1925 | W. J. Farrell | Senior Inspector | Department of Education | — | — |
| 1927 | W. J. Farrell | Senior Inspector | Department of Education | — | — |
| 1928 | W. J. Farrell | Assistant Director | Department of Education | — | — |
| 1929 | W. J. Farrell | Assistant Director | Department of Education | — | — |
| 1930 | W. J. Farrell | Deputy Director | Department of Education | — | — |
| 1931 | W. J. Farrell | Deputy Director | Department of Education | — | — |
| 1932 | W. J. Farrell | Deputy Director | Department of Education | — | — |
| 1940 | W. J. Farrell | Director | Department of Education | — | — |

### Deterministic checks: `farrell_james_e1866` vs `Farrell, W. J___Palestine___1924`

- [PASS] surname_gate: bio 'FARRELL' vs stint 'Farrell, W. J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['W', 'J']
- [PASS] age_gate: stint starts 1924; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Palestine'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1924-1940
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

