<!-- {"case_id": "case_doran_pierce-trollip_e1894", "bio_ids": ["doran_pierce-trollip_e1894"], "stint_ids": ["Doran, P. T___Cape of Good Hope___1908", "Doran, P. T___South Africa___1912"]} -->
# Dossier case_doran_pierce-trollip_e1894

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `doran_pierce-trollip_e1894`

- Printed name: **DORAN, PIERCE TROLLIP**
- Birth year: not printed
- Appears in editions: [1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925]

### Verbatim printed entry text (OCR)

**Version `col1915-L46537.v` — printed in editions [1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925]:**

> DORAN, PIERCE TROLLIP.—Field asst. to conservator of forests, Transkeian conservancy, Cape, 1894; elk. and acctnt. to conservator, 1896; dist. forest offr., Umtata, 1898; ditto, Butterworth, 1903; 3rd grade conservator of forests, Transkeian conservancy, 1st July, 1910.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1894 | Field asst. to conservator of forests, Transkeian conservancy | Cape of Good Hope | [1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925] |
| 1 | 1896 | elk. and acctnt. to conservator | Cape of Good Hope *(inherited from previous clause)* | [1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925] |
| 2 | 1898 | dist. forest offr., Umtata | Cape of Good Hope *(inherited from previous clause)* | [1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925] |
| 3 | 1903 | ditto, Butterworth | Cape of Good Hope *(inherited from previous clause)* | [1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925] |
| 4 | 1910 | 3rd grade conservator of forests, Transkeian conservancy | Cape of Good Hope *(inherited from previous clause)* | [1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925] |

## Candidate stint `Doran, P. T___Cape of Good Hope___1908`

- Staff-list name: **Doran, P. T** | colony: **Cape of Good Hope** | listed 1908–1909 | editions [1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1908 | P. T. Doran | District Forest Officers | Office of Chief Conservator of Forests | — | — |
| 1909 | P. T. Doran | District Forest Officer | Office of Chief Conservator of Forests | — | — |

### Deterministic checks: `doran_pierce-trollip_e1894` vs `Doran, P. T___Cape of Good Hope___1908`

- [PASS] surname_gate: bio 'DORAN' vs stint 'Doran, P. T' (exact)
- [PASS] initials: bio ['P', 'T'] ~ stint ['P', 'T']
- [PASS] age_gate: stint starts 1908; no printed birth year — UNCHECKED
- [PASS] colony: 5 placed event(s) resolve to 'Cape of Good Hope'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1908-1909
- [FAIL] position_sim: best 43 vs bar 60: '3rd grade conservator of forests, Transkeian conservancy' ~ 'District Forest Officers'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Doran, P. T___South Africa___1912`

- Staff-list name: **Doran, P. T** | colony: **South Africa** | listed 1912–1918 | editions [1912, 1914, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | P. Doran | Assistant Conservator | Department of Forests | — | — |
| 1914 | P. Doran | Assistant Conservator | Department of Forests | — | — |
| 1918 | P. T. Doran | Conservator, Transkeian Conservancy | Department of Forests | — | — |

### Deterministic checks: `doran_pierce-trollip_e1894` vs `Doran, P. T___South Africa___1912`

- [PASS] surname_gate: bio 'DORAN' vs stint 'Doran, P. T' (exact)
- [PASS] initials: bio ['P', 'T'] ~ stint ['P', 'T']
- [PASS] age_gate: stint starts 1912; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1918
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

