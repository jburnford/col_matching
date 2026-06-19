<!-- {"case_id": "case_ibbott_john-thomas_e1860", "bio_ids": ["ibbott_john-thomas_e1860"], "stint_ids": ["Ibbott, J. T___British Guiana___1877"]} -->
# Dossier case_ibbott_john-thomas_e1860

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `ibbott_john-thomas_e1860`

- Printed name: **IBBOTT, JOHN THOMAS**
- Birth year: not printed
- Appears in editions: [1883, 1886, 1889]

### Verbatim printed entry text (OCR)

**Version `col1883-L28106.v` — printed in editions [1883, 1886]:**

> IBBOTT, JOHN THOMAS.—Sub-controller of customs and sub-bookkeeper, Berbice, 16th March, 1875; acting tide waiter, Georgetown, Demerara, from the 9th July, 1869, to the 1st of Feb., 1860; clerk in charge of the colonial bonded warehouse, Georgetown, 1st Feb., 1860; acting sub-controller of customs and sub-bookkeeper, Berbice, from the 9th Sept., 1869, to the 23rd December, 1870; acting assistant government secretary, and acting receiver-general, Berbice, from the 24th Dec., 1870, to the 23rd March, 1872; 1st clerk to the customs, 16th Feb., 1870, Georgetown, Demerara; assumed the duties on the 23rd March, 1872; acted as comptroller of customs from 26th July, 1874, to 3rd February, 1876.

**Version `col1889-L33869.v` — printed in editions [1889]:**

> IBBOTT, John Thomas.—Sub-controller of customs and sub-bookkeeper, Berbice Mar., 1875; acting tide waiter, Georgetown, July, 1869, to Feb., 1860; clerk in charge, bonded warehouse, George town, Feb., 1860; acting sub-controller of customs and sub bookkeeper, Berbice, Sept., 1869, to Dec., 1870; acting assistant government secretary, and acting receiver-general, Berbice, Dec., 1870, to Mar., 1872; 1st clerk, customs, Feb., 1870; acted as comptroller of customs, July, 1874, to Feb., 1876.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1860–1860 | clerk in charge of the colonial bonded warehouse | Demerara | [1883, 1886, 1889] |
| 1 | 1869–1860 | acting tide waiter | Demerara | [1883, 1886, 1889] |
| 2 | 1869–1870 | acting sub-controller of customs and sub-bookkeeper | Berbice | [1883, 1886, 1889] |
| 3 | 1870–1872 | acting assistant government secretary, and acting receiver-general | Berbice | [1883, 1886, 1889] |
| 4 | 1870–1870 | 1st clerk to the customs | Demerara | [1883, 1886, 1889] |
| 5 | 1872–1872 | — | — | [1883, 1886] |
| 6 | 1874–1876 | comptroller of customs | — | [1883, 1886, 1889] |
| 7 | 1875–1875 | Sub-controller of customs and sub-bookkeeper | Berbice | [1883, 1886, 1889] |

## Candidate stint `Ibbott, J. T___British Guiana___1877`

- Staff-list name: **Ibbott, J. T** | colony: **British Guiana** | listed 1877–1896 | editions [1877, 1878, 1879, 1880, 1883, 1886, 1889, 1890, 1894, 1896]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | J. T. Ibbott | Sub-Comptroller at Berbice | Customs | — | — |
| 1878 | J. T. Ibbott | Sub-Comptroller at Berbice | Customs | — | — |
| 1879 | J. T. Ibbott | Sub-Comptroller at Berbice | Customs | — | — |
| 1880 | J. T. Ibbott | Sub-Comptroller | Customs | — | — |
| 1883 | J. T. Ibbott | Sub-Comproller at Berbice | Customs | — | — |
| 1886 | J. T. Ibbott | Sub-Comptroller at Berbice | Customs | — | — |
| 1889 | J. T. Ibbott | Assistant Receiver-General | Treasury | — | — |
| 1890 | J. T. Ibbott | Assistant Receiver-General | Treasury | — | — |
| 1894 | J. T. Ibbott | Assistant Receiver-General | Treasury and Savings Bank | — | — |
| 1896 | J. T. Ibbott | Assistant Receiver-General | Treasury and Savings Bank | — | — |

### Deterministic checks: `ibbott_john-thomas_e1860` vs `Ibbott, J. T___British Guiana___1877`

- [PASS] surname_gate: bio 'IBBOTT' vs stint 'Ibbott, J. T' (exact)
- [PASS] initials: bio ['J', 'T'] ~ stint ['J', 'T']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1896
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

