<!-- {"case_id": "case_curtis_oswald_e1858", "bio_ids": ["curtis_oswald_e1858"], "stint_ids": ["Curtis, O___New Zealand___1883", "Curtis, W. O___Australia___1912", "Curtis, W. O___Tasmania___1908"]} -->
# Dossier case_curtis_oswald_e1858

## Case context

- 1 biography(ies) and 3 candidate stint(s) are entangled in this case.
- Corpus context: 27 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['curtis_oswald_e1858'] carry a single initial only — the namesake trap applies.

## Biography `curtis_oswald_e1858`

- Printed name: **CURTIS, OSWALD**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L27051.v` — printed in editions [1883]:**

> CURTIS, OSWALD.—Member of the provincial council of the province of Nelson, New Zealand, from 1858 to 1867; elected superintendent of the province of Nelson in 1867; re-elected in 1869, and again in 1873; member of the House of Representatives for the city of Nelson from 1865 to the present time (1878); postmaster-general, telegraph commissioner, commissioner of customs, commissioner of stamp duties, 1872; fellow and member of the senate of the University of New Zealand, and one of the council of governors of Nelson College.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1858–1867 | Member of the provincial council | New Zealand | [1883] |
| 1 | 1865–1878 | member of the House of Representatives | — | [1883] |
| 2 | 1867–1867 | superintendent | — | [1883] |
| 3 | 1869–1873 | — | — | [1883] |
| 4 | 1872–1872 | postmaster-general, telegraph commissioner, commissioner of customs, commissioner of stamp duties | — | [1883] |

## Candidate stint `Curtis, O___New Zealand___1883`

- Staff-list name: **Curtis, O** | colony: **New Zealand** | listed 1883–1888 | editions [1883, 1886, 1888]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1883 | O. Curtis | Resident Magistrate | Judicial | — | — |
| 1886 | O. Curtis | Resident Magistrate | Judicial | — | — |
| 1888 | O. Curtis | Resident Magistrate | Resident Magistrates | — | — |

### Deterministic checks: `curtis_oswald_e1858` vs `Curtis, O___New Zealand___1883`

- [PASS] surname_gate: bio 'CURTIS' vs stint 'Curtis, O' (exact)
- [PASS] initials: bio ['O'] ~ stint ['O']
- [PASS] age_gate: stint starts 1883; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'New Zealand'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1883-1888
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Curtis, W. O___Australia___1912`

- Staff-list name: **Curtis, W. O** | colony: **Australia** | listed 1912–1918 | editions [1912, 1913, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | W. O. Curtis | Draftsman | Tasmanian Government Railways | — | — |
| 1913 | W. O. Curtis | Draftsman | Tasmanian Government Railways | — | — |
| 1918 | W. O. Curtis | Chief Clerk | Tasmanian Government Railways | — | — |

### Deterministic checks: `curtis_oswald_e1858` vs `Curtis, W. O___Australia___1912`

- [PASS] surname_gate: bio 'CURTIS' vs stint 'Curtis, W. O' (exact)
- [PASS] initials: bio ['O'] ~ stint ['W', 'O']
- [PASS] age_gate: stint starts 1912; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1918
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Curtis, W. O___Tasmania___1908`

- Staff-list name: **Curtis, W. O** | colony: **Tasmania** | listed 1908–1917 | editions [1908, 1909, 1917]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1908 | W. O. Curtis | Draftsman | Tasmanian Government Railways. | — | — |
| 1909 | W. O. Curtis | Draftsman | Tasmanian Government Railways | — | — |
| 1917 | W. O. Curtis | Chief Clerks | Tasmanian Government Railways | — | — |

### Deterministic checks: `curtis_oswald_e1858` vs `Curtis, W. O___Tasmania___1908`

- [PASS] surname_gate: bio 'CURTIS' vs stint 'Curtis, W. O' (exact)
- [PASS] initials: bio ['O'] ~ stint ['W', 'O']
- [PASS] age_gate: stint starts 1908; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Tasmania'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1908-1917
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

