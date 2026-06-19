<!-- {"case_id": "case_harley_octavius_e1862", "bio_ids": ["harley_octavius_e1862"], "stint_ids": ["Harley, O___Trinidad___1877"]} -->
# Dossier case_harley_octavius_e1862

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['harley_octavius_e1862'] carry a single initial only — the namesake trap applies.

## Biography `harley_octavius_e1862`

- Printed name: **HARLEY, OCTAVIUS**
- Birth year: not printed
- Appears in editions: [1883, 1888, 1889, 1894, 1896, 1897, 1898, 1899, 1900]

### Verbatim printed entry text (OCR)

**Version `col1888-L33885.v` — printed in editions [1888, 1889, 1894, 1896, 1897, 1898, 1899, 1900]:**

> HARLEY, OCTAVIUS.—Clerk in treasury, Trinidad, April, 1862; cashier in that department about three years; acted as warden and coroner for the Diego Martin Ward Union, July, 1870, to April, 1871; suptd. of prisons, Oct., 1873, and inspector of industrial schools also, Oct., 1885; stipendiary J.P. for E dist. city of St. George, and inspr. of prisons and reformatories Apr., 1889; acted as stip. J.P., W. dist. St. George and town of Port of Spain, June, 1892 to Feb., 1893; chairman of committee on prison accommodation, Mar., 1893.

**Version `col1883-L27864.v` — printed in editions [1883]:**

> HARLEY, OCTAVIUS.—Clerk in the treasury, Trinidad, 17th April, 1862; was cashier in that department about three years; acted as warden and coroner for the Diego Martin Ward Union from July, 1870, to April, 1871; superintendent of prisons, 25th October, 1873.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1862 | Clerk in treasury | Trinidad | [1883, 1888, 1889, 1894, 1896, 1897, 1898, 1899, 1900] |
| 1 | 1870–1871 | acted as warden and coroner | Diego Martin Ward Union | [1883, 1888, 1889, 1894, 1896, 1897, 1898, 1899, 1900] |
| 2 | 1873 | suptd. of prisons | — | [1883, 1888, 1889, 1894, 1896, 1897, 1898, 1899, 1900] |
| 3 | 1885 | inspector of industrial schools | — | [1888, 1889, 1894, 1896, 1897, 1898, 1899, 1900] |
| 4 | 1889 | stipendiary J.P. and inspr. of prisons and reformatories | St. George | [1888, 1889, 1894, 1896, 1897, 1898, 1899, 1900] |
| 5 | 1892–1893 | acted as stip. J.P. | Port of Spain | [1888, 1889, 1894, 1896, 1897, 1898, 1899, 1900] |
| 6 | 1893 | chairman of committee on prison accommodation | — | [1888, 1889, 1894, 1896, 1897, 1898, 1899, 1900] |
| 7 | ? | cashier in that department | — | [1888, 1889, 1894, 1896, 1897, 1898, 1899, 1900] |

## Candidate stint `Harley, O___Trinidad___1877`

- Staff-list name: **Harley, O** | colony: **Trinidad** | listed 1877–1890 | editions [1877, 1878, 1879, 1880, 1883, 1886, 1888, 1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | O. Harley | Superintendent of Prisons, and Keeper of Royal Gaol | Police and Gaols | — | — |
| 1878 | O. Harley | Superintendent of Inspector of Prisons, and Keeper of Royal Gaol | Police and Gaols | — | — |
| 1879 | O. Harley | Superintendent of Prisons, and Keeper of Royal Gaol | Police and Gaols | — | — |
| 1880 | O. Harley | Superintendent of Prisons, and Keeper of Royal Gaol | Police and Gaols | — | — |
| 1883 | O. Harley | Superintendent of Prisons, and Keeper of Royal Gaol | Police and Gaols | — | — |
| 1886 | O. Harley | Superintendent of Prisons, and Keeper of Royal Gaol | Police and Gaols | — | — |
| 1888 | O. Harley | Inspector of Industrial Schools | Police and Gaols | — | — |
| 1889 | O. Harley | Inspector of Industrial Schools | Police and Gaols | — | — |
| 1890 | O. Harley | Official | Eastern District, County St. George | — | — |
| 1890 | O. Harley | Inspector of Prisons | Police and Gaols | — | — |

### Deterministic checks: `harley_octavius_e1862` vs `Harley, O___Trinidad___1877`

- [PASS] surname_gate: bio 'HARLEY' vs stint 'Harley, O' (exact)
- [PASS] initials: bio ['O'] ~ stint ['O']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Trinidad'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1890
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

