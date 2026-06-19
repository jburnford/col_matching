<!-- {"case_id": "case_giles_george-edward_b1855", "bio_ids": ["giles_george-edward_b1855"], "stint_ids": ["Giles, E___Cape of Good Hope___1906", "Giles, George Edward___Cape of Good Hope___1880"]} -->
# Dossier case_giles_george-edward_b1855

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 28 official(s) with this surname in the graph's staff lists; 11 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `giles_george-edward_b1855`

- Printed name: **GILES, GEORGE EDWARD**
- Birth year: 1855 (attested in editions [1886, 1888, 1889, 1890])
- Appears in editions: [1886, 1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1886-L33687.v` — printed in editions [1886, 1888, 1889, 1890]:**

> GILES, CAPTAIN GEORGE EDWARD, R.A.—Born 1st Jan., 1855; educated at Cheltenham College; entered R.M. Academy, 1872; lieutenant, Royal Artillery, Jan., 1875; captain, Jan., 1884; served in Gaika and Galeka campaign, South Africa, 1877 and 1878 (mentioned in despatches and London Gazette); garrison adjutant and remount officer commandment Zulu War, Cape Town; commanded Artillery Troop, C.M. Riflemen, May, 1879; served throughout Morosi campaign; commanded Artillery at final attack and capture of Morosi's Mountain (mentioned in despatches), (medal with clasp, 1877, 18781879); commanded Cape Field Artillery, 1880; served in Basuto campaign, 1880, 1881; appointed 2nd in command and assistant commissioner, 1st Battalion Perak Sikhs, Perak Straits Settlements, Aug., 1884.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1872–1872 | entered R.M. Academy | — | [1886, 1888, 1889, 1890] |
| 1 | 1875–1875 | lieutenant, Royal Artillery | — | [1886, 1888, 1889, 1890] |
| 2 | 1877–1878 | served in Gaika and Galeka campaign | South Africa | [1886, 1888, 1889, 1890] |
| 3 | 1877–1879 | commanded Artillery at final attack and capture of Morosi's Mountain | — | [1886, 1888, 1889, 1890] |
| 4 | 1879–1879 | commanded Artillery Troop, C.M. Riflemen | — | [1886, 1888, 1889, 1890] |
| 5 | 1880–1880 | commanded Cape Field Artillery | Cape Colony | [1886, 1888, 1889, 1890] |
| 6 | 1880–1881 | served in Basuto campaign | — | [1886, 1888, 1889, 1890] |
| 7 | 1884–1884 | captain | — | [1886, 1888, 1889, 1890] |
| 8 | 1884–1884 | 2nd in command and assistant commissioner, 1st Battalion Perak Sikhs | Straits Settlements | [1886, 1888, 1889, 1890] |

## Candidate stint `Giles, E___Cape of Good Hope___1906`

- Staff-list name: **Giles, E** | colony: **Cape of Good Hope** | listed 1906–1908 | editions [1906, 1907, 1908]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1906 | E. Giles | Railway Storekeeper | Railways | — | — |
| 1907 | E. Giles | Railway Storekeeper | Railways | — | — |
| 1908 | E. Giles | Railway Storekeeper | Railways | — | — |

### Deterministic checks: `giles_george-edward_b1855` vs `Giles, E___Cape of Good Hope___1906`

- [PASS] surname_gate: bio 'GILES' vs stint 'Giles, E' (exact)
- [PASS] initials: bio ['G', 'E'] ~ stint ['E']
- [PASS] age_gate: stint starts 1906, birth 1855 (age 51)
- [PASS] colony: 1 placed event(s) resolve to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1906-1908
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Giles, George Edward___Cape of Good Hope___1880`

- Staff-list name: **Giles, George Edward** | colony: **Cape of Good Hope** | listed 1880–1883 | editions [1880, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1880 | G. E. Giles | Captain | Cape Mounted Riflemen | — | — |
| 1883 | George Edward Giles | Captain | Cape Field Artillery | — | Captain |

### Deterministic checks: `giles_george-edward_b1855` vs `Giles, George Edward___Cape of Good Hope___1880`

- [PASS] surname_gate: bio 'GILES' vs stint 'Giles, George Edward' (exact)
- [PASS] initials: bio ['G', 'E'] ~ stint ['G', 'E']
- [PASS] age_gate: stint starts 1880, birth 1855 (age 25)
- [PASS] colony: 1 placed event(s) resolve to 'Cape of Good Hope'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1880-1883
- [FAIL] position_sim: best 27 vs bar 60: 'commanded Cape Field Artillery' ~ 'Captain'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

