<!-- {"case_id": "case_parkes_henry_e1839", "bio_ids": ["parkes_henry_e1839"], "stint_ids": ["Parkes, H___Palestine___1932", "Parkes, Henry___New South Wales___1879"]} -->
# Dossier case_parkes_henry_e1839

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 10 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['parkes_henry_e1839'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Parkes, H___Palestine___1932` is also gate-compatible with biography(ies) outside this case: ['parkes_henry_e1875'] (already linked elsewhere or filtered).
- NOTE: stint `Parkes, Henry___New South Wales___1879` is also gate-compatible with biography(ies) outside this case: ['parkes_henry_e1875'] (already linked elsewhere or filtered).

## Biography `parkes_henry_e1839`

- Printed name: **PARKES, HENRY**
- Birth year: not printed
- Honours: G.C.M.G. (1888), K.C.M.G. (1877)
- Appears in editions: [1886, 1888, 1889, 1890, 1894, 1896]

### Verbatim printed entry text (OCR)

**Version `col1886-L35172.v` — printed in editions [1886, 1888, 1889, 1890, 1894, 1896]:**

> PARKES, THE HON. SIR HENRY, G.C.M.G. (1888), K.C.M.G. (1877).—Emigrated to New South Wales, 1839; was colonial secretary from Jan., 1866, to Sept., 1868, having been previously a member of the legislature from 1854; came to England as commissioner for emigration, 1861-62; president of the council of education in New South Wales, 1867-70; colonial secretary and first minister, 1872, 1875, 1877, and from 1878 to 1882, and again 1887 and 1889 to 1891; was president of the federation convention at Sydney in 1891; author of "Fifty Years in the making of Australian History."

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1839 | — | New South Wales | [1886, 1888, 1889, 1890, 1894, 1896] |
| 1 | 1854 | member of the legislature | — | [1886, 1888, 1889, 1890, 1894, 1896] |
| 2 | 1861–1862 | commissioner for emigration | England | [1886, 1888, 1889, 1890, 1894, 1896] |
| 3 | 1866–1868 | colonial secretary | — | [1886, 1888, 1889, 1890, 1894, 1896] |
| 4 | 1867–1870 | president of the council of education | New South Wales | [1886, 1888, 1889, 1890, 1894, 1896] |
| 5 | 1872–1891 | colonial secretary and first minister | — | [1886, 1888, 1889, 1890, 1894, 1896] |
| 6 | 1891–1891 | president of the federation convention | Sydney | [1886, 1888, 1889, 1890, 1894, 1896] |

## Candidate stint `Parkes, H___Palestine___1932`

- Staff-list name: **Parkes, H** | colony: **Palestine** | listed 1932–1940 | editions [1932, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1932 | H. Parkes | Assistant Engineer in Charge, Sinai Telegraph Route | Posts, Telegraphs and Telephones | — | — |
| 1940 | H. Parkes | Assistant Engineer | Posts and Telegraphs | — | — |

### Deterministic checks: `parkes_henry_e1839` vs `Parkes, H___Palestine___1932`

- [PASS] surname_gate: bio 'PARKES' vs stint 'Parkes, H' (exact)
- [PASS] initials: bio ['H'] ~ stint ['H']
- [PASS] age_gate: stint starts 1932; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Palestine'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1932-1940
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Parkes, Henry___New South Wales___1879`

- Staff-list name: **Parkes, Henry** | colony: **New South Wales** | listed 1879–1889 | editions [1879, 1880, 1888, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1879 | Sir H. Parkes | Colonial Secretary | Colonial Secretary's Department | K.C.M.G. | — |
| 1880 | Sir Henry Parkes | Colonial Secretary | Colonial Secretary's Department | K.C.M.G. | — |
| 1888 | Hon. Sir H. Parkes | Colonial Secretary | Colonial Secretary's Department | G.C.M.G. | — |
| 1889 | Sir H. Parkes | Colonial Secretary | Colonial Secretary's and Subordinate Departments | G.C.M.G. | — |

### Deterministic checks: `parkes_henry_e1839` vs `Parkes, Henry___New South Wales___1879`

- [PASS] surname_gate: bio 'PARKES' vs stint 'Parkes, Henry' (exact)
- [PASS] initials: bio ['H'] ~ stint ['H']
- [PASS] age_gate: stint starts 1879; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'New South Wales'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1879-1889
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: G.C.M.G., K.C.M.G.
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

