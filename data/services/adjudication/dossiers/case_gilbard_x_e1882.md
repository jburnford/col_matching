<!-- {"case_id": "case_gilbard_x_e1882", "bio_ids": ["gilbard_x_e1882", "gillard_richard_e1852"], "stint_ids": ["Gillard, C. R___Jamaica___1879", "Gillard, R___Jamaica___1877"]} -->
# Dossier case_gilbard_x_e1882

## Case context

- 2 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['gilbard_x_e1882', 'gillard_richard_e1852'] carry a single initial only — the namesake trap applies.
- CONTESTED: stint(s) ['Gillard, C. R___Jamaica___1879', 'Gillard, R___Jamaica___1877'] have more than one claimant biography in this case.

## Biography `gilbard_x_e1882`

- Printed name: **GILBARD, (no given names printed)**
- Birth year: not printed
- Appears in editions: [1883, 1886]

### Verbatim printed entry text (OCR)

**Version `col1883-L27641.v` — printed in editions [1883, 1886]:**

> GILBARD, MAJOR, J. G.—Police magistrate, Gibraltar, 1882.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1882 | Police magistrate | Gibraltar | [1883, 1886] |

## Biography `gillard_richard_e1852`

- Printed name: **GILLARD, RICHARD**
- Birth year: not printed
- Appears in editions: [1883, 1886, 1888, 1889, 1890, 1894]

### Verbatim printed entry text (OCR)

**Version `col1883-L27649.v` — printed in editions [1883, 1886, 1888, 1889, 1890, 1894]:**

> GILLARD, RICHARD.—Clerk in the customs, Bridgwater, England, Jan., 1852; third class clerk in secretary's office, London, July, 1855; second class, Dec., 1858; promoted to first class, Jan., 1866; surveyor-general of customs and inspector or invoices, Kingston, Jamaica, Nov., 1868; collector of customs, Kingston, 1st March, 1869; collector general, 1st May, 1883.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1852 | Clerk in the customs, Bridgwater, England | — | [1883, 1886, 1888, 1889, 1890, 1894] |
| 1 | 1855 | third class clerk in secretary's office, London | — | [1883, 1886, 1888, 1889, 1890, 1894] |
| 2 | 1858 | second class | — | [1883, 1886, 1888, 1889, 1890, 1894] |
| 3 | 1866 | promoted to first class | — | [1883, 1886, 1888, 1889, 1890, 1894] |
| 4 | 1868 | surveyor-general of customs and inspector or invoices, Kingston | Jamaica | [1883, 1886, 1888, 1889, 1890, 1894] |
| 5 | 1869 | collector of customs, Kingston | Jamaica *(inherited from previous clause)* | [1883, 1886, 1888, 1889, 1890, 1894] |
| 6 | 1883 | collector general | Jamaica *(inherited from previous clause)* | [1883, 1886, 1888, 1889, 1890, 1894] |

## Candidate stint `Gillard, C. R___Jamaica___1879`

- Staff-list name: **Gillard, C. R** | colony: **Jamaica** | listed 1879–1888 | editions [1879, 1880, 1883, 1888]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1879 | C. Gillard | Government Medical Officer | Government Medical Officers | — | — |
| 1880 | C. Gillard | Medical Officer | Government Medical Officers | — | — |
| 1883 | C. Gillard | Government Medical Officer | Government Medical Officers | — | — |
| 1888 | C. R. Gillard | District Medical Officer | Medical Department | — | — |

### Deterministic checks: `gilbard_x_e1882` vs `Gillard, C. R___Jamaica___1879`

- [PASS] surname_gate: bio 'GILBARD' vs stint 'Gillard, C. R' (fuzzy:1)
- [PASS] initials: bio ['?'] ~ stint ['C', 'R']
- [PASS] age_gate: stint starts 1879; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Jamaica'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1879-1888
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `gillard_richard_e1852` vs `Gillard, C. R___Jamaica___1879`

- [PASS] surname_gate: bio 'GILLARD' vs stint 'Gillard, C. R' (exact)
- [PASS] initials: bio ['R'] ~ stint ['C', 'R']
- [PASS] age_gate: stint starts 1879; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'Jamaica'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1879-1888
- [FAIL] position_sim: best 37 vs bar 60: 'collector general' ~ 'Government Medical Officer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Gillard, R___Jamaica___1877`

- Staff-list name: **Gillard, R** | colony: **Jamaica** | listed 1877–1880 | editions [1877, 1878, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | R. Gillard, jun. | 1st Class Clerk | Revenue Department | — | — |
| 1878 | R. Gillard, jun. | 1st Class Clerks | Revenue Department | — | — |
| 1879 | R. Gillard | 1st Class Clerks | Revenue Department | — | — |
| 1880 | R. Gillard | 1st Class Clerks | Revenue Department | — | — |

### Deterministic checks: `gilbard_x_e1882` vs `Gillard, R___Jamaica___1877`

- [PASS] surname_gate: bio 'GILBARD' vs stint 'Gillard, R' (fuzzy:1)
- [PASS] initials: bio ['?'] ~ stint ['R']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Jamaica'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1880
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `gillard_richard_e1852` vs `Gillard, R___Jamaica___1877`

- [PASS] surname_gate: bio 'GILLARD' vs stint 'Gillard, R' (exact)
- [PASS] initials: bio ['R'] ~ stint ['R']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'Jamaica'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1880
- [FAIL] position_sim: best 36 vs bar 60: 'collector of customs, Kingston' ~ '1st Class Clerks'
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

