<!-- {"case_id": "case_loch_henry-brougham_e1844", "bio_ids": ["loch_henry-brougham_e1844"], "stint_ids": ["Loch, H. B___South Africa___1890"]} -->
# Dossier case_loch_henry-brougham_e1844

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `loch_henry-brougham_e1844`

- Printed name: **LOCH, HENRY BROUGHAM**
- Birth year: not printed
- Honours: C.B. (1860), K.C.B. (1880)
- Appears in editions: [1886, 1888, 1889, 1890, 1894]

### Verbatim printed entry text (OCR)

**Version `col1886-L34525.v` — printed in editions [1886, 1888, 1889, 1890, 1894]:**

> LOCH, SIR HENRY BROUGHAM, K.C.B. (1880), C.B. (1860).—Son of James Loch, Esq., M.P., of Drylaw, County Midlothian; entered 3rd Bengal Cavalry, 1844; served Sutledge campaign, 1846-46; aide-de-camp to the commander-in-chief, Lord Gough; adjutant and 2nd in command, Skinner's Horse, till 1858; sent on special military service to Turkey to assist in organizing Turkish troops, with local rank of major, 1854; crossed with army from Varna to Crimea, 1854; accompanied Earl of Elgin's special embassy to China, 1857-58; attached to head-quarters of commander-in-chief during operations in the field; bearer to England of Treaty of Yeddo, 1858; secretary to Earl of Elgin's second embassy to China, 1860; attached to head-quarters of the army during military operations; was treacherously made prisoner and cruelly treated by the Chinese, while engaged in negotiations under flag of truce; brought home ratified treaty of Tsin-Tsin, and Convention of Pekin; private secretary to Right Hon. Sir George Grey, secretary of state for home department, 1861-62-63; lieutenant-governor, Isle of Man, 1863 to 1882; colonel commandant, 4th battalion, Cheshire Regiment; Her Majesty's commissioner of woods, forests, and land revenue from 1882 to 1884; Governor of Victoria, 1884. Married, 1862, Elizabeth, daughter of the late Hon. Edward Villiers.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1844–1844 | entered 3rd Bengal Cavalry | — | [1886, 1888, 1889, 1890, 1894] |
| 1 | 1846–1846 | — | — | [1886, 1888, 1889, 1890, 1894] |
| 2 | 1854–1854 | special military service | Turkey | [1886, 1888, 1889, 1890, 1894] |
| 3 | 1854–1854 | — | Crimea | [1886, 1888, 1889, 1890, 1894] |
| 4 | 1857–1858 | — | China | [1886, 1888, 1889, 1890, 1894] |
| 5 | 1858–1858 | bearer to England of Treaty of Yeddo | England | [1886, 1888, 1889, 1890, 1894] |
| 6 | 1860–1860 | secretary to Earl of Elgin's second embassy | China | [1886, 1888, 1889, 1890, 1894] |
| 7 | 1861–1863 | private secretary to Right Hon. Sir George Grey, secretary of state for home department | — | [1886, 1888, 1889, 1890, 1894] |
| 8 | 1863–1882 | lieutenant-governor | Isle of Man | [1886, 1888, 1889, 1890, 1894] |
| 9 | 1882–1884 | commissioner of woods, forests, and land revenue | — | [1886, 1888, 1889, 1890, 1894] |
| 10 | 1884 | Governor | Victoria | [1886, 1888, 1889, 1890, 1894] |
| 11 | ? | aide-de-camp to the commander-in-chief | — | [1886, 1888, 1889, 1890, 1894] |
| 12 | ?–1858 | adjutant and 2nd in command, Skinner's Horse | — | [1886, 1888, 1889, 1890, 1894] |
| 13 | ? | — | — | [1886, 1888, 1889, 1890, 1894] |
| 14 | ? | — | — | [1886, 1888, 1889, 1890, 1894] |
| 15 | ? | colonel commandant, 4th battalion, Cheshire Regiment | — | [1886, 1888, 1889, 1890, 1894] |

## Candidate stint `Loch, H. B___South Africa___1890`

- Staff-list name: **Loch, H. B** | colony: **South Africa** | listed 1890–1894 | editions [1890, 1894]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1890 | Sir H. B. Loch | High Commissioner | High Commission | G.C.M.G., K.C.B. | — |
| 1894 | Sir H. B. Loch | High Commissioner | High Commission | G.C.M.G., K.C.B. | — |

### Deterministic checks: `loch_henry-brougham_e1844` vs `Loch, H. B___South Africa___1890`

- [PASS] surname_gate: bio 'LOCH' vs stint 'Loch, H. B' (exact)
- [PASS] initials: bio ['H', 'B'] ~ stint ['H', 'B']
- [PASS] age_gate: stint starts 1890; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1890-1894
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: K.C.B.
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

