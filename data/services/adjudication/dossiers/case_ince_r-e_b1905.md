<!-- {"case_id": "case_ince_r-e_b1905", "bio_ids": ["ince_r-e_b1905"], "stint_ids": ["Ince, E___Barbados___1923", "Ince, R. E___Singapore___1956"]} -->
# Dossier case_ince_r-e_b1905

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 14 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `ince_r-e_b1905`

- Printed name: **INCE, R. E**
- Birth year: 1905 (attested in editions [1953, 1954, 1955, 1956, 1957])
- Appears in editions: [1953, 1954, 1955, 1956, 1957]

### Verbatim printed entry text (OCR)

**Version `col1953-L17879.v` — printed in editions [1953, 1954, 1955, 1956, 1957]:**

> INCE, R. E.—b. 1905; ed. Brentwood Sch. and Camb. Univ.; p.o.w., 1942-45; mstr., King Edward VII Sch., Taiping, 1927; asst. inspr. of schs., Penang, 1936; headmstr., govt. sch., 1937; senr. inspr., schs., Mal., 1946; S'pore, 1951; dep. dir., educ., 1952; dep. sec., min. of educ., 1955.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | mstr., King Edward VII Sch., Taiping | — | [1953, 1954, 1955, 1956, 1957] |
| 1 | 1936 | asst. inspr. of schs., Penang | — | [1953, 1954, 1955, 1956, 1957] |
| 2 | 1937 | headmstr., govt. sch | — | [1953, 1954, 1955, 1956, 1957] |
| 3 | 1942–1945 | p.o.w | — | [1953, 1954, 1955, 1956, 1957] |
| 4 | 1946 | senr. inspr., schs. | Malaya | [1953, 1954, 1955, 1956, 1957] |
| 5 | 1951 | S'pore | Malaya *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957] |
| 6 | 1952 | dep. dir., educ | Malaya *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957] |
| 7 | 1955 | dep. sec., min. of educ | Malaya *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957] |

## Candidate stint `Ince, E___Barbados___1923`

- Staff-list name: **Ince, E** | colony: **Barbados** | listed 1923–1927 | editions [1923, 1924, 1925, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1923 | E. Ince | Librarian | Public Library | — | — |
| 1924 | E. Ince | Librarian | Public Library | — | — |
| 1925 | E. Ince | Librarian | Public Library | — | — |
| 1927 | E. Ince | Librarian | Public Library | — | — |

### Deterministic checks: `ince_r-e_b1905` vs `Ince, E___Barbados___1923`

- [PASS] surname_gate: bio 'INCE' vs stint 'Ince, E' (exact)
- [PASS] initials: bio ['R', 'E'] ~ stint ['E']
- [PASS] age_gate: stint starts 1923, birth 1905 (age 18)
- [FAIL] colony: no placed event resolves to 'Barbados'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1923-1927
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Ince, R. E___Singapore___1956`

- Staff-list name: **Ince, R. E** | colony: **Singapore** | listed 1956–1957 | editions [1956, 1957]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1956 | R. E. Ince | Deputy Secretary “B”, Ministry of Education | Civil Establishment | — | — |
| 1957 | R. E. Ince | Deputy Secretary “A”, Ministry of Education | Civil Establishment | — | — |

### Deterministic checks: `ince_r-e_b1905` vs `Ince, R. E___Singapore___1956`

- [PASS] surname_gate: bio 'INCE' vs stint 'Ince, R. E' (exact)
- [PASS] initials: bio ['R', 'E'] ~ stint ['R', 'E']
- [PASS] age_gate: stint starts 1956, birth 1905 (age 51)
- [FAIL] colony: no placed event resolves to 'Singapore'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1956-1957
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

