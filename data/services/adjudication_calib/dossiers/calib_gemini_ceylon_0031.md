<!-- {"case_id": "calib_gemini_ceylon_0031", "bio_ids": ["vanderstraaten_j-l_e1863"], "stint_ids": ["Vanderstraaten, J. L___Ceylon___1878", "Vanderstraaten, J. L___Ceylon___1898"]} -->
# Dossier calib_gemini_ceylon_0031

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `vanderstraaten_j-l_e1863`

- Printed name: **VANDERSTRAATEN, J. L.**
- Birth year: not printed
- Appears in editions: [1886, 1888, 1890, 1898, 1899, 1900]

### Verbatim printed entry text (OCR)

**Version `col1886-L36090.v` — printed in editions [1886]:**

> VANDERSTRAATEN, J. L., M.D.—Medical assistant, Ceylon, 1863; assistant colonial surgeon, second class, 1867; first class, 1868; senior medical officer, Batticaloa, July, 1883; colonial surgeon, 1885.

**Version `col1888-L36489.v` — printed in editions [1888, 1890, 1898, 1899, 1900]:**

> VANDERSTRAATEN, J. L., M.D., St. And., M.R.C.P., Lond., L.R.C.P., Edin., L.S.A., Lond., Fellow Chemical, Medical, and Obstetrical Societies, London.—Medical assistant, Ceylon, 1863; assistant colonial surgeon, second class, 1867; first class, 1868; colonial surgeon, 1885, and principal, Ceylon medical college, and supt. of vaccination, W. and N.W. P.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1863 | Medical assistant | Ceylon | [1886, 1888, 1890, 1898, 1899, 1900] |
| 1 | 1867 | assistant colonial surgeon, second class | Ceylon *(inherited from previous clause)* | [1886, 1888, 1890, 1898, 1899, 1900] |
| 2 | 1868 | first class | Ceylon *(inherited from previous clause)* | [1886, 1888, 1890, 1898, 1899, 1900] |
| 3 | 1883 | senior medical officer, Batticaloa | Ceylon *(inherited from previous clause)* | [1886] |
| 4 | 1885 | colonial surgeon | Ceylon | [1886, 1888, 1890, 1898, 1899, 1900] |

## Candidate stint `Vanderstraaten, J. L___Ceylon___1878`

- Staff-list name: **Vanderstraaten, J. L** | colony: **Ceylon** | listed 1878–1894 | editions [1878, 1879, 1880, 1883, 1886, 1888, 1889, 1890, 1894]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1878 | J. L. Vanderstraaten | Assistant Colonial Surgeons | Medical Department | — | — |
| 1879 | J. L. Vanderstraaten | Assistant Colonial Surgeons | Medical Department | — | — |
| 1880 | J. L. Vanderstraaten | Assistant Colonial Surgeons | Medical Department | — | — |
| 1883 | J. L. Vanderstraaten | Assistant Colonial Surgeon | Medical Department | — | — |
| 1886 | J. L. Vanderstraaten | Colonial Surgeon | Medical Department | — | — |
| 1888 | J. L. Vanderstraaten | Colonial Surgeon | Medical Department | — | — |
| 1889 | J. L. Vanderstraaten | Colonial Surgeon | Medical Department | — | — |
| 1890 | J. L. Vanderstraaten | Colonial Surgeon | Medical Department | — | — |
| 1894 | J. L. Vanderstraaten | Colonial Surgeon | Medical Department | — | — |

### Deterministic checks: `vanderstraaten_j-l_e1863` vs `Vanderstraaten, J. L___Ceylon___1878`

- [PASS] surname_gate: bio 'VANDERSTRAATEN' vs stint 'Vanderstraaten, J. L' (exact)
- [PASS] initials: bio ['J', 'L'] ~ stint ['J', 'L']
- [PASS] age_gate: stint starts 1878; no printed birth year — UNCHECKED
- [PASS] colony: 5 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1878-1894
- [PASS] position_sim: best 100 vs bar 60: 'colonial surgeon' ~ 'Colonial Surgeon'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 3 agreeing edition-year(s) [1886, 1888, 1890] pos~100 (bar: >=2)
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Vanderstraaten, J. L___Ceylon___1898`

- Staff-list name: **Vanderstraaten, J. L** | colony: **Ceylon** | listed 1898–1899 | editions [1898, 1899]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1898 | J. L. Vanderstraaten | Colonial Surgeon | Medical Department | — | — |
| 1899 | J. L. Vanderstraaten | Colonial Surgeon | Medical Department | — | — |

### Deterministic checks: `vanderstraaten_j-l_e1863` vs `Vanderstraaten, J. L___Ceylon___1898`

- [PASS] surname_gate: bio 'VANDERSTRAATEN' vs stint 'Vanderstraaten, J. L' (exact)
- [PASS] initials: bio ['J', 'L'] ~ stint ['J', 'L']
- [PASS] age_gate: stint starts 1898; no printed birth year — UNCHECKED
- [PASS] colony: 5 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1898-1899
- [PASS] position_sim: best 100 vs bar 60: 'colonial surgeon' ~ 'Colonial Surgeon'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 2 agreeing edition-year(s) [1898, 1899] pos~100 (bar: >=2)
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

