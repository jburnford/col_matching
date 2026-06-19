<!-- {"case_id": "case_thomsett_henry-g_e1840", "bio_ids": ["thomsett_henry-g_e1840"], "stint_ids": ["Thomsett, Henry G___Hong Kong___1877"]} -->
# Dossier case_thomsett_henry-g_e1840

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `thomsett_henry-g_e1840`

- Printed name: **THOMSETT, HENRY G.**
- Birth year: not printed
- Honours: C.M.G. (1888)
- Terminal: retired 1870 — “and was placed on the retired list of the royal navy in 1870”
- Appears in editions: [1883, 1886, 1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1883-L29734.v` — printed in editions [1883, 1886, 1888, 1889]:**

> THOMSETT, HENRY G.—Entered the royal navy, 1840, and served actively for twenty-one years; was engaged in a combined attack of British and French naval and land force under Commodore Fanshawe on a horda of pirates at Basia, Jeba River, West Africa, 12th December, 1849; during two periods of service on the African station, assisted in the capture of twenty-seven slave vessels in the bight of Benin and coast of Loando; commanded H.M.'s ship 'Princess Charlotte' at Hong Kong, from February, 1858, to Sept., 1861; acting harbour master, 17th March to 26th Nov., 1860, and again 1st March to the 31st Aug., 1861, when he was appointed harbour master, marine magistrate, and emigration and customs officer, at Hong Kong, July, 1861, and was placed on the retired list of the royal navy in 1870.

**Version `col1890-L37024.v` — printed in editions [1890]:**

> THOMSETT, Henry G., C.M.G. (1888).—Entered the R.N. 1840; engaged in a combined attack of British and French force on pirates at Basis, Jeba River, West Africa, 1849; during service on the African station, assisted in the capture of twenty-seven slave vessels in the bight of Benin and coast of Loando; commanded H.M.'s ship 'Princess Charlotte' at Hong Kong, Feb., 1858, harbour master, 1861; member of council; retired, 1889.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1840–1861 | Entered the royal navy | — | [1883, 1886, 1888, 1889] |
| 1 | 1840 | — | — | [1890] |
| 2 | 1849–1849 | — | West Africa | [1883, 1886, 1888, 1889, 1890] |
| 3 | 1858–1861 | commanded H.M.'s ship 'Princess Charlotte' | Hong Kong | [1883, 1886, 1888, 1889, 1890] |
| 4 | 1860–1860 | acting harbour master | — | [1883, 1886, 1888, 1889] |
| 5 | 1861–1861 | — | — | [1883, 1886, 1888, 1889] |
| 6 | 1861 | harbour master, marine magistrate, and emigration and customs officer | Hong Kong | [1883, 1886, 1888, 1889, 1890] |

## Candidate stint `Thomsett, Henry G___Hong Kong___1877`

- Staff-list name: **Thomsett, Henry G** | colony: **Hong Kong** | listed 1877–1888 | editions [1877, 1878, 1880, 1883, 1886, 1888]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | Henry G. Thomsett | Harbour-Master, Marine Magistrate, Emigration and Customs Officer | Harbour-Master's Department | — | — |
| 1878 | Henry G. Thomsett | Harbour-Master, Marine Magistrate, Emigration and Customs Officer | Harbour-Master's Department | — | — |
| 1880 | Henry G. Thomsett | Harbour-Master, Marine Magistrate, Emigration and Customs Officer | Harbour-Master's Department | — | — |
| 1883 | Henry G. Thomsett | Harbour-Master, Marine Magistrate, Emigration and Customs Officer | Harbour-Master's Department | — | — |
| 1886 | Henry G. Thomsett | Harbour-Master, Boarding Magistrate, Emigration and Customs Officer | Harbour-Master's Department | — | — |
| 1888 | Henry G. Thomsett | Harbour-Master, Marine Magistrate, Emigration and Customs Officer | Harbour-Master's Department | — | — |

### Deterministic checks: `thomsett_henry-g_e1840` vs `Thomsett, Henry G___Hong Kong___1877`

- [PASS] surname_gate: bio 'THOMSETT' vs stint 'Thomsett, Henry G' (exact)
- [PASS] initials: bio ['H', 'G'] ~ stint ['H', 'G']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Hong Kong'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1888
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

