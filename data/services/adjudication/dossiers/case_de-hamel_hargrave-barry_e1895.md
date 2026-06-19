<!-- {"case_id": "case_de-hamel_hargrave-barry_e1895", "bio_ids": ["de-hamel_hargrave-barry_e1895"], "stint_ids": ["de Hamel, H. B___Gold Coast___1896", "de Hamel, H. B___Straits Settlements___1911"]} -->
# Dossier case_de-hamel_hargrave-barry_e1895

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `de-hamel_hargrave-barry_e1895`

- Printed name: **DE HAMEL, HARGRAVE BARRY**
- Birth year: not printed
- Appears in editions: [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920]

### Verbatim printed entry text (OCR)

**Version `col1910-L45327.v` — printed in editions [1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920]:**

> DE HAMEL, HARGRAVE BARRY.—Major, Londonderry Artillery; seconded to G. Coast Haussa; July, 1895; Ashanti expedit., Dec., 1895 (star); asst. supt. of pol., Straits Stltmts., June, 1896; seconded as ag. asst. comsnnr. of pol., Kinta, Perak, Dec., 1905; supt. of pol., Penang, May, 1907.

**Version `col1908-L44071.v` — printed in editions [1908, 1909]:**

> DE HAMEL, HARGRAVE BARRY.—Major, Londonderry Artillery; asst. supt. of pol., Straits Settlements, June, 1897; seconded as ag. asst. commr. of pol., Kinta, Perak, Dec., 1905; supt. of pol., Penang, May, 1907.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1895 | — | — | [1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920] |
| 1 | 1895 | Ashanti expedit | Ashanti | [1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920] |
| 2 | 1896 | asst. supt. of pol., Straits Stltmts | Ashanti *(inherited from previous clause)* | [1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920] |
| 3 | 1897 | asst. supt. of pol. | Straits Settlements | [1908, 1909] |
| 4 | 1905 | seconded as ag. asst. comsnnr. of pol., Kinta, Perak | Ashanti *(inherited from previous clause)* | [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920] |
| 5 | 1907 | supt. of pol., Penang | Ashanti *(inherited from previous clause)* | [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920] |

## Candidate stint `de Hamel, H. B___Gold Coast___1896`

- Staff-list name: **de Hamel, H. B** | colony: **Gold Coast** | listed 1896–1897 | editions [1896, 1897]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1896 | H. B. de Hamel | Assistant Inspector | Constabulary—Hausa | — | — |
| 1897 | H. B. de Hamel | Assistant Inspector | Constabulary | — | — |

### Deterministic checks: `de-hamel_hargrave-barry_e1895` vs `de Hamel, H. B___Gold Coast___1896`

- [PASS] surname_gate: bio 'DE HAMEL' vs stint 'de Hamel, H. B' (exact)
- [PASS] initials: bio ['H', 'B'] ~ stint ['H', 'B']
- [PASS] age_gate: stint starts 1896; no printed birth year — UNCHECKED
- [PASS] colony: 4 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1896-1897
- [FAIL] position_sim: best 53 vs bar 60: 'Ashanti expedit' ~ 'Assistant Inspector'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `de Hamel, H. B___Straits Settlements___1911`

- Staff-list name: **de Hamel, H. B** | colony: **Straits Settlements** | listed 1911–1913 | editions [1911, 1913]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1911 | H. B. de Hamel | Superintendent of Police | Penang | — | Major |
| 1913 | H. B. de Hamel | Superintendent of Police | Penang | — | Major |

### Deterministic checks: `de-hamel_hargrave-barry_e1895` vs `de Hamel, H. B___Straits Settlements___1911`

- [PASS] surname_gate: bio 'DE HAMEL' vs stint 'de Hamel, H. B' (exact)
- [PASS] initials: bio ['H', 'B'] ~ stint ['H', 'B']
- [PASS] age_gate: stint starts 1911; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1911-1913
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

