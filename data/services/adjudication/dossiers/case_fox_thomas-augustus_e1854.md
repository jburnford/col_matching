<!-- {"case_id": "case_fox_thomas-augustus_e1854", "bio_ids": ["fox_thomas-augustus_e1854"], "stint_ids": ["Fox, Alexander___Fiji___1907", "Fox, T. A___Straits Settlements___1877"]} -->
# Dossier case_fox_thomas-augustus_e1854

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 43 official(s) with this surname in the graph's staff lists; 18 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `fox_thomas-augustus_e1854`

- Printed name: **FOX, THOMAS AUGUSTUS**
- Birth year: not printed
- Appears in editions: [1883, 1886]

### Verbatim printed entry text (OCR)

**Version `col1883-L27524.v` — printed in editions [1883, 1886]:**

> FOX, THOMAS AUGUSTUS.—Entered the naval service in 1854, and served on board the 'Hilton,' 'Dudbrook,' 'Berhampooter,' 'Fire Queen,' 'Aracan;' commander of the Straits Settlements steamer 'Tonze,' 1862; of the 'Pluto,' 1864 to 1867; and of the 'Peiho,' Aug. 1867; served as a volunteer in the Bengal yeomanry cavalry, 1858, 1859, during the Indian mutiny; has a medal for that service, and also for service in China in 1860; and received a Lieutenant's commission for services rendered during that war; lieut. Royal naval reserve, 1868; acting harbour-master and marine magistrate, Penang, May, 1871; deputy master Attendant of Singapore, January, 1873, was confirmed in the appointment of harbour-master and postmaster, at Penang in April, 1874; elected a member of the Royal Geographical Society, 1870.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1854–1854 | naval service | — | [1883, 1886] |
| 1 | 1858–1859 | volunteer | Bengal | [1883, 1886] |
| 2 | 1860–1860 | — | China | [1883, 1886] |
| 3 | 1862–1862 | commander | Straits Settlements | [1883, 1886] |
| 4 | 1864–1867 | commander | — | [1883, 1886] |
| 5 | 1867–1867 | commander | — | [1883, 1886] |
| 6 | 1868–1868 | lieut. | — | [1883, 1886] |
| 7 | 1870–1870 | member | — | [1883, 1886] |
| 8 | 1871–1871 | acting harbour-master and marine magistrate | Penang | [1883, 1886] |
| 9 | 1873–1873 | deputy master Attendant | Singapore | [1883, 1886] |
| 10 | 1874–1874 | harbour-master and postmaster | Penang | [1883, 1886] |

## Candidate stint `Fox, Alexander___Fiji___1907`

- Staff-list name: **Fox, Alexander** | colony: **Fiji** | listed 1907–1910 | editions [1907, 1908, 1909, 1910]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1907 | A. Fox | Steward | Medical Department | — | — |
| 1908 | A. Fox | Steward | Medical Department | — | — |
| 1909 | Alexander Fox | Chief Warden | Medical Department | — | — |
| 1910 | Alexander Fox | Chief Warder | Leper Asylum | — | — |

### Deterministic checks: `fox_thomas-augustus_e1854` vs `Fox, Alexander___Fiji___1907`

- [PASS] surname_gate: bio 'FOX' vs stint 'Fox, Alexander' (exact)
- [PASS] initials: bio ['T', 'A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1907; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Fiji'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1907-1910
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Fox, T. A___Straits Settlements___1877`

- Staff-list name: **Fox, T. A** | colony: **Straits Settlements** | listed 1877–1880 | editions [1877, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | T. A. Fox | Postmaster | Post Office | — | — |
| 1877 | T. A. Fox | Harbour Master | Marine Depot | — | — |
| 1879 | T. A. Fox | Harbour Master | Marine Dépôt | — | — |
| 1880 | T. A. Fox | Harbour Master | Marine Depot | — | — |

### Deterministic checks: `fox_thomas-augustus_e1854` vs `Fox, T. A___Straits Settlements___1877`

- [PASS] surname_gate: bio 'FOX' vs stint 'Fox, T. A' (exact)
- [PASS] initials: bio ['T', 'A'] ~ stint ['T', 'A']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Straits Settlements'
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

