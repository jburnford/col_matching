<!-- {"case_id": "case_nicol_george-croley_e1849", "bio_ids": ["nicol_george-croley_e1849"], "stint_ids": ["Nicol, George___Gambia___1879"]} -->
# Dossier case_nicol_george-croley_e1849

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 24 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `nicol_george-croley_e1849`

- Printed name: **NICOL, GEORGE CROLEY**
- Birth year: not printed
- Appears in editions: [1883, 1886, 1888]

### Verbatim printed entry text (OCR)

**Version `col1883-L28865.v` — printed in editions [1883]:**

> NICOL, Rev. George.—Ordained deacon at St. Paul's cathedral in 1849, by Dr. Bloomfield, late bishop of London; priest, the same year; mathematical tutor at the Fourah Bay Institution, Sierra Leone, under the C.M.S., 1850 to 1856; appointed to the parish of St. Charles's, Regent, in the mountain district, 1856, and St. Patrick, Risley, and Wellington, 1857; re-appointed to Regent, 1859; disconnected with nine other pastors from the C.M.S., and form the native pastorate under the superintendence of the bishop of Sierra Leone; chaplain to the bishop in 1862; preferred to the chaplaincy of the Gambia, 1869; colonial registrar, 1872; acting colonial chaplain of Sierra Leone, from July to Dec., 1874.

**Version `col1886-L35016.v` — printed in editions [1886, 1888]:**

> NICOL, REV. GEORGE CROLEY, M.A. (Hon.), Durham.—Mathematical tutor, Fourah Bay College, Sierra Leone, under the C.M.S., 1850 to 1856; appointed to the parish of St. Charles's, Regent, in the mountain district, 1856, and St. Patrick, Kissey, and Wellington, 1857; re-appointed to Regent, 1859; chaplain to the bishop in 1862; preferred to the chaplaincy of the Gambia, 1869; colonial registrar, 1872; acting colonial chaplain of Sierra Leone from July to Dec., 1874; J.P., 1877.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1849–1849 | deacon | — | [1883] |
| 1 | 1849–1849 | priest | — | [1883] |
| 2 | 1850–1856 | mathematical tutor | Sierra Leone | [1883, 1886, 1888] |
| 3 | 1856–1856 | appointed to the parish of St. Charles's | — | [1883, 1886, 1888] |
| 4 | 1857–1857 | parish of St. Patrick, Risley, and Wellington | — | [1883, 1886, 1888] |
| 5 | 1859–1859 | re-appointed to Regent | — | [1883, 1886, 1888] |
| 6 | 1862–1862 | chaplain to the bishop | — | [1883, 1886, 1888] |
| 7 | 1869–1869 | chaplaincy | Gambia | [1883, 1886, 1888] |
| 8 | 1872–1872 | colonial registrar | — | [1883, 1886, 1888] |
| 9 | 1874–1874 | acting colonial chaplain | Sierra Leone | [1883, 1886, 1888] |
| 10 | 1877–1877 | J.P. | — | [1886, 1888] |

## Candidate stint `Nicol, George___Gambia___1879`

- Staff-list name: **Nicol, George** | colony: **Gambia** | listed 1879–1883 | editions [1879, 1880, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1879 | George Nicol | Colonial Chaplain | Ecclesiastical Establishment | — | — |
| 1880 | George Nicol | Colonial Chaplain | Ecclesiastical Establishment | — | — |
| 1883 | Rev. George Nicol | Colonial Chaplain | Ecclesiastical Establishment | — | — |

### Deterministic checks: `nicol_george-croley_e1849` vs `Nicol, George___Gambia___1879`

- [PASS] surname_gate: bio 'NICOL' vs stint 'Nicol, George' (exact)
- [PASS] initials: bio ['G', 'C'] ~ stint ['G']
- [PASS] age_gate: stint starts 1879; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Gambia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1879-1883
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

