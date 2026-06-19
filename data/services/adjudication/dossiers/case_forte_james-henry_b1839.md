<!-- {"case_id": "case_forte_james-henry_b1839", "bio_ids": ["forte_james-henry_b1839"], "stint_ids": ["Forte, J. H___British Guiana___1878"]} -->
# Dossier case_forte_james-henry_b1839

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `forte_james-henry_b1839`

- Printed name: **FORTE, JAMES HENRY**
- Birth year: 1839 (attested in editions [1883, 1886, 1888, 1889, 1890])
- Appears in editions: [1883, 1886, 1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1883-L27505.v` — printed in editions [1883, 1886, 1888, 1889, 1890]:**

> FORTE, JAMES HENRY.—Born 8th Dec., 1839, at Barbados; educated chiefly at Queen's College, British Guiana; matriculated at the University of Durham, 1865; studied at Guy's Hospital, London; M.R.C.S., England, May, 1868; L.R.C.P. Ed., July, 1868; in charge of Estates Hospitals in British Guiana, from 1869 to 1871; entered government medical immigration service as medical officer to the Mahaicony district, 1st July, 1873; in charge of the Mahaica district and Leper Asylum, in addition to Mahaica district, from Feb., 1874, to Feb., 1875; acted for five months in the Buxton and Beterverwagting district; appointed medical officer, Philadelphia district, Oct., 1875; transferred to the Aurora and Tiger Island district, Jan., 1877, acting medical officer, Plaisance district, June, 1882.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1865–1865 | — | — | [1883, 1886, 1888, 1889, 1890] |
| 1 | 1868–1868 | — | England | [1883, 1886, 1888, 1889, 1890] |
| 2 | 1868–1868 | — | — | [1883, 1886, 1888, 1889, 1890] |
| 3 | 1869–1871 | in charge of Estates Hospitals | British Guiana | [1883, 1886, 1888, 1889, 1890] |
| 4 | 1873–1873 | medical officer to the Mahaicony district | — | [1883, 1886, 1888, 1889, 1890] |
| 5 | 1874–1875 | in charge of the Mahaica district and Leper Asylum | — | [1883, 1886, 1888, 1889, 1890] |
| 6 | 1875–1875 | medical officer | — | [1883, 1886, 1888, 1889, 1890] |
| 7 | 1877–1877 | — | — | [1883, 1886, 1888, 1889, 1890] |
| 8 | 1882–1882 | acting medical officer | — | [1883, 1886, 1888, 1889, 1890] |

## Candidate stint `Forte, J. H___British Guiana___1878`

- Staff-list name: **Forte, J. H** | colony: **British Guiana** | listed 1878–1886 | editions [1878, 1880, 1883, 1886]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1878 | J. H. Forte | Medical Officer | Medical Officers of Immigration Districts | — | — |
| 1880 | J. H. Forte | Aurora and Tiger Island | Immigration Department | — | — |
| 1883 | J. H. Forte | — | Immigration Department | — | — |
| 1886 | J. H. Forte | Medical Officer | Immigration Department | — | — |

### Deterministic checks: `forte_james-henry_b1839` vs `Forte, J. H___British Guiana___1878`

- [PASS] surname_gate: bio 'FORTE' vs stint 'Forte, J. H' (exact)
- [PASS] initials: bio ['J', 'H'] ~ stint ['J', 'H']
- [PASS] age_gate: stint starts 1878, birth 1839 (age 39)
- [PASS] colony: 1 placed event(s) resolve to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1878-1886
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

