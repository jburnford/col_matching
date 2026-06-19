<!-- {"case_id": "case_ayers_henry_e1863", "bio_ids": ["ayers_henry_e1863"], "stint_ids": ["Ayers, Henry___South Australia___1877", "Ayers, Henry___South Australia___1888"]} -->
# Dossier case_ayers_henry_e1863

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['ayers_henry_e1863'] carry a single initial only — the namesake trap applies.

## Biography `ayers_henry_e1863`

- Printed name: **AYERS, Henry**
- Birth year: not printed
- Honours: G.C.M.G. (1894), K.C.M.G. (1872)
- Appears in editions: [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897]

### Verbatim printed entry text (OCR)

**Version `col1883-L26274.v` — printed in editions [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897]:**

> AYERS, The Hon. Sir Henry, G.C.M.G. (1894), K.C.M.G. (1872).—Was member of the Cabinet of South Australia without office, in Mr. Dutton's ministry, July, 1863; chief secretary, July, 1863, to October, 1865, and from May, 1867, to Sept., 1868, and again from Oct. 18, 1868, to Nov. 2, 1868; also from Jan., 1872, to July, 1873, and again in 1876 and 1887; president of the legislative council from 1881 to 1893.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1863–1863 | member of the Cabinet without office | South Australia | [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897] |
| 1 | 1863–1865 | chief secretary | — | [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897] |
| 2 | 1867–1868 | chief secretary | — | [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897] |
| 3 | 1868–1868 | chief secretary | — | [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897] |
| 4 | 1872–1873 | chief secretary | — | [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897] |
| 5 | 1876–1887 | chief secretary | — | [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897] |
| 6 | 1881–1893 | president of the legislative council | — | [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897] |

## Candidate stint `Ayers, Henry___South Australia___1877`

- Staff-list name: **Ayers, Henry** | colony: **South Australia** | listed 1877–1879 | editions [1877, 1878, 1879]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | Sir Henry Ayers | Chief Secretary | Chief Secretary's Department | K.C.M.G. | — |
| 1878 | Henry Ayers | Treasurer | University of Adelaide - Council | K.C.M.G. | — |
| 1878 | Sir Henry Ayers | Member | Legislative Council | K.C.M.G. | — |
| 1879 | Henry Ayers | Member | Legislative Council | K.C.M.G. | — |

### Deterministic checks: `ayers_henry_e1863` vs `Ayers, Henry___South Australia___1877`

- [PASS] surname_gate: bio 'AYERS' vs stint 'Ayers, Henry' (exact)
- [PASS] initials: bio ['H'] ~ stint ['H']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'South Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1879
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: K.C.M.G.
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Ayers, Henry___South Australia___1888`

- Staff-list name: **Ayers, Henry** | colony: **South Australia** | listed 1888–1890 | editions [1888, 1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | Hon. Sir Henry Ayers, K.C.M.G. | President | Legislative Council | K.C.M.G. | — |
| 1889 | Sir Henry Ayers | President | Legislative Council | K.C.M.G. | — |
| 1890 | Henry Ayers | President (Legislative Council) | Legislative Council | K.C.M.G. | — |

### Deterministic checks: `ayers_henry_e1863` vs `Ayers, Henry___South Australia___1888`

- [PASS] surname_gate: bio 'AYERS' vs stint 'Ayers, Henry' (exact)
- [PASS] initials: bio ['H'] ~ stint ['H']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'South Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1888-1890
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: K.C.M.G.
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

