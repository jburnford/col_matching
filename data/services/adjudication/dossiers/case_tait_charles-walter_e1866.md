<!-- {"case_id": "case_tait_charles-walter_e1866", "bio_ids": ["tait_charles-walter_e1866"], "stint_ids": ["Tait, C. W___Jamaica___1877", "Tait, W___Hong Kong___1908"]} -->
# Dossier case_tait_charles-walter_e1866

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 14 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `tait_charles-walter_e1866`

- Printed name: **TAIT, CHARLES WALTER**
- Birth year: not printed
- Appears in editions: [1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1888-L36298.v` — printed in editions [1888, 1889, 1890]:**

> TAIT, CHARLES WALTER.—Clerk to inspector of Volunteers, Trinidad, 1866; second clerk, director of roads and surveyor general's department, 1867; senior clerk, 1868; secretary Rio Cobre canal, slaughter house, and Spanish town water commissions.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1866 | Clerk to inspector of Volunteers | Trinidad | [1888, 1889, 1890] |
| 1 | 1867 | second clerk, director of roads and surveyor general's department | Trinidad *(inherited from previous clause)* | [1888, 1889, 1890] |
| 2 | 1868 | senior clerk | Trinidad *(inherited from previous clause)* | [1888, 1889, 1890] |

## Candidate stint `Tait, C. W___Jamaica___1877`

- Staff-list name: **Tait, C. W** | colony: **Jamaica** | listed 1877–1898 | editions [1877, 1878, 1880, 1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | C. W. Tait | Chief Clerk | Department of the Director of Roads and Surveyor-General | — | — |
| 1878 | C. W. Tait | Chief Clerk | Department of the Director of Roads and Surveyor-General | — | — |
| 1880 | C. W. Tait | Chief Clerk | Department of the Director of Roads and Surveyor-General | — | — |
| 1886 | C. W. Tait | 1st Class Clerks | Public Works | — | — |
| 1888 | C. W. Tait | 1st Class Clerks | Department of Public Works | — | — |
| 1889 | C. W. Tait | 1st Class Clerks | Department of Public Works | — | — |
| 1890 | C. W. Tait | Senior Clerk | Department of Public Works | — | — |
| 1894 | C. W. Tait | Chief Clerk | Department of Public Works | — | — |
| 1896 | C. W. Tait | Chief Clerk | Department of Public Works | — | — |
| 1897 | C. W. Tait | Chief Clerk | Public Works | — | — |
| 1898 | C. W. Tait | Chief Clerk | Department of Public Works | — | — |

### Deterministic checks: `tait_charles-walter_e1866` vs `Tait, C. W___Jamaica___1877`

- [PASS] surname_gate: bio 'TAIT' vs stint 'Tait, C. W' (exact)
- [PASS] initials: bio ['C', 'W'] ~ stint ['C', 'W']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Jamaica'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1898
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Tait, W___Hong Kong___1908`

- Staff-list name: **Tait, W** | colony: **Hong Kong** | listed 1908–1911 | editions [1908, 1909, 1910, 1911]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1908 | W. Tait | Deputy Medical Inspector-General | Naval Establishment | — | — |
| 1909 | W. Tait | Deputy Medical Inspector-General | Naval Establishment | — | — |
| 1910 | W. Tait | Deputy Medical Inspector-General | Naval Establishment | — | — |
| 1911 | W. Tait | Deputy Medical Inspector-General | Naval Establishment | — | — |

### Deterministic checks: `tait_charles-walter_e1866` vs `Tait, W___Hong Kong___1908`

- [PASS] surname_gate: bio 'TAIT' vs stint 'Tait, W' (exact)
- [PASS] initials: bio ['C', 'W'] ~ stint ['W']
- [PASS] age_gate: stint starts 1908; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Hong Kong'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1908-1911
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

