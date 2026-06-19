<!-- {"case_id": "calib_gemini_ceylon_0028", "bio_ids": ["kynsey_w-r_b1840"], "stint_ids": ["Kynsey, William R___Ceylon___1878"]} -->
# Dossier calib_gemini_ceylon_0028

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `kynsey_w-r_b1840`

- Printed name: **KYNSEY, W. R**
- Birth year: 1840 (attested in editions [1883, 1886, 1896, 1898, 1900, 1907])
- Honours: F.K.Q.C.P
- Appears in editions: [1883, 1886, 1896, 1898, 1899, 1900, 1905, 1906, 1907, 1908]

### Verbatim printed entry text (OCR)

**Version `col1883-L28265.v` — printed in editions [1883, 1886, 1896, 1898, 1900, 1907]:**

> KYNSEY, Sir W. R., F.K.Q.C.P., Knt. BACH, C.M.G. 1888.—B. 1840; prin. civ. med. offr., and inspr.-gen. of hospitals, Ceylon, Feb., 1875; ret., 1897.

**Version `col1899-L35884.v` — printed in editions [1899, 1905, 1906, 1908]:**

> KYNSLEY, SIR W. R., F.K.Q.C.P., KNT. BACH., C.M.G. 1888.—B. 1840; prin. civ. med. offr., and inspr.-gen. of hospitals, Ceylon, Feb., 1875; ret. 1897.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1875 | prin. civ. med. offr., and inspr.-gen. of hospitals | Ceylon | [1883, 1886, 1896, 1898, 1899, 1900, 1905, 1906, 1907, 1908] |
| 1 | 1897 | ret | Ceylon *(inherited from previous clause)* | [1883, 1886, 1896, 1898, 1899, 1900, 1905, 1906, 1907, 1908] |

## Candidate stint `Kynsey, William R___Ceylon___1878`

- Staff-list name: **Kynsey, William R** | colony: **Ceylon** | listed 1878–1896 | editions [1878, 1879, 1883, 1886, 1888, 1889, 1890, 1894, 1896]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1878 | W. R. Kynsey | Principal Civil Medical Officer and Inspector-General of Hospitals | Medical Department | — | — |
| 1879 | W. R. Kynsey | Principal Civil Medical Officer and Inspector-General of Hospitals | Medical Department | — | — |
| 1883 | W. R. Kynsey | Principal Civil Medical Officer and Inspector-General of Hospitals | Medical Department | — | — |
| 1886 | W. R. Kynsey | Principal Civil Medical Officer and Inspector-General of Hospitals | Medical Department | — | — |
| 1888 | W. R. Kynsey | Principal Civil Medical Officer and Inspector-General of Hospitals | Medical Department | — | — |
| 1889 | W. R. Kynsey | Principal Civil Medical Officer and Inspector-General of Hospitals | Medical Department | — | — |
| 1890 | W. R. Kynsey | Principal Civil Medical Officer and Inspector-General of Hospitals | Medical Department | — | — |
| 1894 | William R. Kynsey | Principal Civil Medical Officer and Inspector-General of Hospitals | Medical Department | C.M.G. | — |
| 1896 | William R. Kynsey | Principal Civil Medical Officer and Inspector-General of Hospitals | Medical Department | C.M.G. | — |

### Deterministic checks: `kynsey_w-r_b1840` vs `Kynsey, William R___Ceylon___1878`

- [PASS] surname_gate: bio 'KYNSEY' vs stint 'Kynsey, William R' (exact)
- [PASS] initials: bio ['W', 'R'] ~ stint ['W', 'R']
- [PASS] age_gate: stint starts 1878, birth 1840 (age 38)
- [PASS] colony: 2 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1878-1896
- [PASS] position_sim: best 98 vs bar 60: 'prin. civ. med. offr., and inspr.-gen. of hospitals' ~ 'Principal Civil Medical Officer and Inspector-General of Hospitals'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 2 agreeing edition-year(s) [1883, 1886] pos~98 (bar: >=2)
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

