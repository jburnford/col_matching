<!-- {"case_id": "case_grieve_r_e1873", "bio_ids": ["grieve_r_e1873"], "stint_ids": ["Grieve, Dr. Robert___British Guiana___1877", "Grieve, R___British Guiana___1886"]} -->
# Dossier case_grieve_r_e1873

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['grieve_r_e1873'] carry a single initial only — the namesake trap applies.

## Biography `grieve_r_e1873`

- Printed name: **GRIEVE, R**
- Birth year: not printed
- Honours: C.M.G (1894), M.D
- Appears in editions: [1888, 1890, 1894, 1896, 1897, 1898, 1899, 1905, 1906]

### Verbatim printed entry text (OCR)

**Version `col1898-L33686.v` — printed in editions [1898, 1899, 1905, 1906]:**

> GRIEVE, R., M.D., C.M.G. (1894).—Med. supt., lun. asyl., Berbice, Br. Guiana, Sept., 1873; ag. med. offr., imigrn. dept., Aug., 1886; surg. gen. of col., Oct., 1886; ret. 1894.

**Version `col1888-L33764.v` — printed in editions [1888, 1890, 1894, 1896, 1897]:**

> GRIEVE, R., M.D., C.M.G. (1894)—Medical superintendent, Lunatic Asylum, Berbice, 24th Sept., 1875; acting medical officer, immigration department, Aug., 1885; surgeon-general of colony, Oct., 1885.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1873 | Med. supt., lun. asyl., Berbice | British Guiana | [1898, 1899, 1905, 1906] |
| 1 | 1875 | Medical superintendent, Lunatic Asylum, Berbice | — | [1888, 1890, 1894, 1896, 1897] |
| 2 | 1885 | acting medical officer, immigration department | — | [1888, 1890, 1894, 1896, 1897] |
| 3 | 1885 | surgeon-general of colony | — | [1888, 1890, 1894, 1896, 1897] |
| 4 | 1886 | ag. med. offr., imigrn. dept | British Guiana *(inherited from previous clause)* | [1898, 1899, 1905, 1906] |
| 5 | 1894 | ret | British Guiana *(inherited from previous clause)* | [1898, 1899, 1905, 1906] |

## Candidate stint `Grieve, Dr. Robert___British Guiana___1877`

- Staff-list name: **Grieve, Dr. Robert** | colony: **British Guiana** | listed 1877–1883 | editions [1877, 1878, 1879, 1880, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | Dr. Grieve | Superintendent | Colonial Lunatic Asylum | — | — |
| 1878 | Dr. R. Grieve | Superintendent | Colonial Lunatic Asylum, Berbice | — | — |
| 1878 | Dr. Robert Grieve | Medical Attendant | Leper Asylum, Mahaica | — | — |
| 1879 | Dr. R. Grieve | Superintendent | Colonial Lunatic Asylum, Berbice | — | — |
| 1880 | Dr. R. Grieve | Superintendent | Colonial Lunatic Asylum, Berbice | — | — |
| 1883 | Dr. R. Grieve | Superintendent | Colonial Lunatic Asylum, Berbice | — | — |

### Deterministic checks: `grieve_r_e1873` vs `Grieve, Dr. Robert___British Guiana___1877`

- [PASS] surname_gate: bio 'GRIEVE' vs stint 'Grieve, Dr. Robert' (exact)
- [PASS] initials: bio ['R'] ~ stint ['D', 'R']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1883
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Grieve, R___British Guiana___1886`

- Staff-list name: **Grieve, R** | colony: **British Guiana** | listed 1886–1894 | editions [1886, 1888, 1889, 1890, 1894]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1886 | R. Grieve | Surgeon-General | Colonial Hospital, Demerara | — | — |
| 1888 | R. Grieve | Surgeon-General | Medical Department | — | — |
| 1889 | R. Grieve | Surgeon-General | Medical Department | — | — |
| 1890 | R. Grieve | Surgeon-General | Medical Department | — | — |
| 1894 | R. Grieve | Surgeon-General | Medical Department | — | — |

### Deterministic checks: `grieve_r_e1873` vs `Grieve, R___British Guiana___1886`

- [PASS] surname_gate: bio 'GRIEVE' vs stint 'Grieve, R' (exact)
- [PASS] initials: bio ['R'] ~ stint ['R']
- [PASS] age_gate: stint starts 1886; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'British Guiana'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1886-1894
- [FAIL] position_sim: best 32 vs bar 60: 'ag. med. offr., imigrn. dept' ~ 'Surgeon-General'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

