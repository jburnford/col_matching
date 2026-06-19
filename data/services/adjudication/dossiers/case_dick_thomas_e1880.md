<!-- {"case_id": "case_dick_thomas_e1880", "bio_ids": ["dick_thomas_e1880"], "stint_ids": ["Dick, T. T___Victoria___1877", "Dick, T. T___Victoria___1890"]} -->
# Dossier case_dick_thomas_e1880

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 22 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['dick_thomas_e1880'] carry a single initial only — the namesake trap applies.

## Biography `dick_thomas_e1880`

- Printed name: **DICK, THOMAS**
- Birth year: not printed
- Terminal: resigned 1882 — “resigned post office and telegraphs, 11th October, 1882”
- Appears in editions: [1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899]

### Verbatim printed entry text (OCR)

**Version `col1886-L33063.v` — printed in editions [1886, 1888, 1889, 1890, 1894, 1896, 1897]:**

> DICK, THOMAS.—Colonial secretary, New Zealand, and, 5th March, 1880; and still holding same office, minister of education, 15th October, 1880; minister of justice, 23rd April, 1881, and postmaster-general and commissioner of telegraphs, 21st April, 1882, resigning ministry of justice; resigned post office and telegraphs, 11th October, 1882.

**Version `col1898-L33070.v` — printed in editions [1898, 1899]:**

> DICK, THE HON. THOMAS.—Col. sec., New Zealand, 5th Mar., 1880, and still holding same office; min. of educn., Oct., 1880; min. of just., Apr., 1881, and postur.-gen. and consnr. of telegraphs, Apr., 1882, resigning ministry of justice; resig. post office and telegraphs, Oct., 1882.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1880 | Colonial secretary | New Zealand | [1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899] |
| 1 | 1880 | minister of education | — | [1886, 1888, 1889, 1890, 1894, 1896, 1897] |
| 2 | 1880 | min. of educn. | — | [1898, 1899] |
| 3 | 1881 | minister of justice | — | [1886, 1888, 1889, 1890, 1894, 1896, 1897] |
| 4 | 1881–1882 | min. of just. | — | [1898, 1899] |
| 5 | 1882 | postmaster-general and commissioner of telegraphs | — | [1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899] |

## Candidate stint `Dick, T. T___Victoria___1877`

- Staff-list name: **Dick, T. T** | colony: **Victoria** | listed 1877–1883 | editions [1877, 1879, 1880, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | T. T. Dick | Medical Superintendent | Beechworth | — | — |
| 1879 | T. T. Dick | Medical Superintendent | Hospitals for the Insane | — | — |
| 1880 | T. T. Dick | Medical Superintendent | Hospitals for the Insane | — | — |
| 1883 | T. T. Dick | Medical Superintendent | Hospitals for the Insane | — | — |

### Deterministic checks: `dick_thomas_e1880` vs `Dick, T. T___Victoria___1877`

- [PASS] surname_gate: bio 'DICK' vs stint 'Dick, T. T' (exact)
- [PASS] initials: bio ['T'] ~ stint ['T', 'T']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Victoria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1883
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Dick, T. T___Victoria___1890`

- Staff-list name: **Dick, T. T** | colony: **Victoria** | listed 1890–1894 | editions [1890, 1894]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1890 | T. T. Dick | Inspector of Asylums and Superintendent | Hospitals for the Insane | — | — |
| 1894 | T. T. Dick | Inspector of Lunatic Asylums | Hospitals for the Insane | — | — |

### Deterministic checks: `dick_thomas_e1880` vs `Dick, T. T___Victoria___1890`

- [PASS] surname_gate: bio 'DICK' vs stint 'Dick, T. T' (exact)
- [PASS] initials: bio ['T'] ~ stint ['T', 'T']
- [PASS] age_gate: stint starts 1890; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Victoria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1890-1894
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

