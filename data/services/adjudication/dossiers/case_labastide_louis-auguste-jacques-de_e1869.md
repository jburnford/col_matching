<!-- {"case_id": "case_labastide_louis-auguste-jacques-de_e1869", "bio_ids": ["labastide_louis-auguste-jacques-de_e1869"], "stint_ids": ["Labastide, A___Trinidad and Tobago___1899", "Labastide, A___Trinidad___1894", "Labastide, L___Trinidad___1877"]} -->
# Dossier case_labastide_louis-auguste-jacques-de_e1869

## Case context

- 1 biography(ies) and 3 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `labastide_louis-auguste-jacques-de_e1869`

- Printed name: **LABASTIDE, LOUIS AUGUSTE JACQUES DE**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L28271.v` — printed in editions [1883]:**

> LABASTIDE, LOUIS AUGUSTE JACQUES DE, C.E.—Entered the public service at Trinidad on the 1st of July, 1869, in the office of public works; was appointed chief draughtsman on 1st January, 1870; graduated at the University of Paris; is a bachelor of science; gained the prize in high mathematics at St. Louis College, Paris; was then admitted a member of "special mathematics" society in that college; was admitted into the government engineering school "Ecole Impériale Centrale des Arts et Manufactures;" was admitted a sworn land surveyor in March, 1872.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1869 | — | Trinidad | [1883] |
| 1 | 1870 | chief draughtsman | — | [1883] |
| 2 | 1872 | sworn land surveyor | — | [1883] |

## Candidate stint `Labastide, A___Trinidad and Tobago___1899`

- Staff-list name: **Labastide, A** | colony: **Trinidad and Tobago** | listed 1899–1900 | editions [1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1899 | A. Labastide | Chief Clerk and Office Assistant | Headquarter Staff | — | — |
| 1900 | A. Labastide | Chief Clerk and Office Assistant | Headquarters Staff | — | — |

### Deterministic checks: `labastide_louis-auguste-jacques-de_e1869` vs `Labastide, A___Trinidad and Tobago___1899`

- [PASS] surname_gate: bio 'LABASTIDE' vs stint 'Labastide, A' (exact)
- [PASS] initials: bio ['L', 'A', 'J', 'D'] ~ stint ['A']
- [PASS] age_gate: stint starts 1899; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1899-1900
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Labastide, A___Trinidad___1894`

- Staff-list name: **Labastide, A** | colony: **Trinidad** | listed 1894–1898 | editions [1894, 1896, 1898]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | A. Labastide | Engineer for Works and Maintenance | Railway Department | — | — |
| 1896 | A. Labastide | Engineer for Works and Maintenance | Railway Department | — | — |
| 1898 | A. Labastide | Chief Clerk and Office Assistant | Headquarter Staff | — | — |

### Deterministic checks: `labastide_louis-auguste-jacques-de_e1869` vs `Labastide, A___Trinidad___1894`

- [PASS] surname_gate: bio 'LABASTIDE' vs stint 'Labastide, A' (exact)
- [PASS] initials: bio ['L', 'A', 'J', 'D'] ~ stint ['A']
- [PASS] age_gate: stint starts 1894; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Trinidad'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1894-1898
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Labastide, L___Trinidad___1877`

- Staff-list name: **Labastide, L** | colony: **Trinidad** | listed 1877–1880 | editions [1877, 1878, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | L. Labastide | Draughtsman | Public Works Department | — | — |
| 1878 | L. Labastide | Draughtsman | Public Works Department | — | — |
| 1879 | L. Labastide | 2nd Assistant Director of Public Works | Public Works Department | — | — |
| 1880 | L. Labastide | 2nd Assistant to Director of Surveys | Survey Department | — | — |

### Deterministic checks: `labastide_louis-auguste-jacques-de_e1869` vs `Labastide, L___Trinidad___1877`

- [PASS] surname_gate: bio 'LABASTIDE' vs stint 'Labastide, L' (exact)
- [PASS] initials: bio ['L', 'A', 'J', 'D'] ~ stint ['L']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Trinidad'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1880
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

