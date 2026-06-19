<!-- {"case_id": "case_firre_tom-freeman_e1903", "bio_ids": ["firre_tom-freeman_e1903"], "stint_ids": ["Firr, T. F___British Central Africa___1905", "Firr, T. F___Uganda___1921", "Firr, T.F___Nyasaland___1911"]} -->
# Dossier case_firre_tom-freeman_e1903

## Case context

- 1 biography(ies) and 3 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `firre_tom-freeman_e1903`

- Printed name: **FIRRE, TOM FREEMAN**
- Birth year: not printed
- Honours: A.M.I.C.E
- Appears in editions: [1933]

### Verbatim printed entry text (OCR)

**Version `col1933-L59803.v` — printed in editions [1933]:**

> FIRRE, TOM FREEMAN, A.M.I.C.E.—Ed. Crystal Palace Engng. Sch.; 1st asst. survr., Nyasaland Prot., June, 1903; asst. dir. of pub. wks., 1909.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1903 | 1st asst. survr. | Nyasaland | [1933] |
| 1 | 1909 | asst. dir. of pub. wks | Nyasaland *(inherited from previous clause)* | [1933] |

## Candidate stint `Firr, T. F___British Central Africa___1905`

- Staff-list name: **Firr, T. F** | colony: **British Central Africa** | listed 1905–1907 | editions [1905, 1906, 1907]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | T. F. Firr | Assistant Surveyor | Survey, Lands, and Mining Department | — | — |
| 1906 | T. F. Firr | 1st Surveyor | Public Works Department | — | — |
| 1907 | T. F. Firr | 1st Surveyor | Public Works Department | — | — |

### Deterministic checks: `firre_tom-freeman_e1903` vs `Firr, T. F___British Central Africa___1905`

- [PASS] surname_gate: bio 'FIRRE' vs stint 'Firr, T. F' (fuzzy:1)
- [PASS] initials: bio ['T', 'F'] ~ stint ['T', 'F']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'British Central Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1907
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Firr, T. F___Uganda___1921`

- Staff-list name: **Firr, T. F** | colony: **Uganda** | listed 1921–1923 | editions [1921, 1923]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | T. F. Firr | Deputy Director | Public Works | — | — |
| 1923 | T. F. Firr | Deputy Director | Public Works | — | — |

### Deterministic checks: `firre_tom-freeman_e1903` vs `Firr, T. F___Uganda___1921`

- [PASS] surname_gate: bio 'FIRRE' vs stint 'Firr, T. F' (fuzzy:1)
- [PASS] initials: bio ['T', 'F'] ~ stint ['T', 'F']
- [PASS] age_gate: stint starts 1921; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Uganda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1921-1923
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Firr, T.F___Nyasaland___1911`

- Staff-list name: **Firr, T.F** | colony: **Nyasaland** | listed 1911–1920 | editions [1911, 1912, 1913, 1914, 1917, 1918, 1919, 1920]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1911 | T. F. Firr | Assistant Director | Public Works Department | — | — |
| 1912 | T. F. Firr | Assistant Director | Public Works Department | — | — |
| 1913 | T. F. Firr | Assistant Director | Public Works Department | — | — |
| 1914 | T. F. Firr | Assistant Director | Public Works Department | — | — |
| 1917 | T.F. Firr | Assistant Director | Public Works Department | — | — |
| 1918 | T. F. Firr | Assistant Director | Public Works Department | — | — |
| 1919 | T. F. Firr | Assistant Director | Public Works Department | — | — |
| 1920 | T. F. Firr | Assistant Director | Public Works Department | — | — |

### Deterministic checks: `firre_tom-freeman_e1903` vs `Firr, T.F___Nyasaland___1911`

- [PASS] surname_gate: bio 'FIRRE' vs stint 'Firr, T.F' (fuzzy:1)
- [PASS] initials: bio ['T', 'F'] ~ stint ['T', 'F']
- [PASS] age_gate: stint starts 1911; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Nyasaland'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1911-1920
- [FAIL] position_sim: best 49 vs bar 60: 'asst. dir. of pub. wks' ~ 'Assistant Director'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

