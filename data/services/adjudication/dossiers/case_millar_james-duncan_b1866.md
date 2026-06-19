<!-- {"case_id": "case_millar_james-duncan_b1866", "bio_ids": ["millar_james-duncan_b1866"], "stint_ids": ["Millar, Jas___British Guiana___1899", "Millar, John___Canada___1894"]} -->
# Dossier case_millar_james-duncan_b1866

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 23 official(s) with this surname in the graph's staff lists; 11 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `millar_james-duncan_b1866`

- Printed name: **MILLAR, JAMES DUNCAN**
- Birth year: 1866 (attested in editions [1917, 1918, 1919, 1920, 1922, 1923])
- Appears in editions: [1917, 1918, 1919, 1920, 1922, 1923]

### Verbatim printed entry text (OCR)

**Version `col1917-L51861.v` — printed in editions [1917, 1918, 1919, 1920, 1922, 1923]:**

> MILLAR, JAMES DUNCAN.—B. 1866; gov't. vet. surg., Trinidad, 3rd Sept., 1902.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1902 | gov't. vet. surg. | Trinidad | [1917, 1918, 1919, 1920, 1922, 1923] |

## Candidate stint `Millar, Jas___British Guiana___1899`

- Staff-list name: **Millar, Jas** | colony: **British Guiana** | listed 1899–1915 | editions [1899, 1900, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1899 | Rev. Jas. Millar | Joint Minister of St. Andrew's Parish | Church of Scotland | — | — |
| 1900 | Jas. Millar | Joint Minister of St. Andrew's Parish | Church of Scotland | — | — |
| 1906 | Rev. Jas. Millar | Joint Minister of St. Andrew's Parish | Church of Scotland | — | — |
| 1907 | Jas. Millar | Joint Minister of St. Andrew’s Parish | Church of Scotland | — | — |
| 1908 | Rev. Jas. Millar | Joint Minister of St. Andrew's Parish | — | — | — |
| 1909 | Rev. Jas. Millar | Joint Minister of St. Andrew's Parish | Church of Scotland | — | — |
| 1910 | Rev. Jas. Millar | Joint Minister of St. Andrew's Parish | Church of Scotland | — | — |
| 1911 | Jas. Millar | Joint Minister of St. Andrew's Parish | Church of Scotland | — | — |
| 1912 | Jas. Millar | Joint Minister of St. Andrew's Parish | Church of Scotland | — | — |
| 1913 | Jas. Millar | Joint Minister of St. Andrew's Parish | Church of Scotland | — | — |
| 1914 | Jas. Millar | Joint Minister of St. Andrew's Parish | Church of Scotland | — | — |
| 1915 | Jas. Millar | Joint Minister of St. Andrew's Parish | Church of Scotland | — | — |

### Deterministic checks: `millar_james-duncan_b1866` vs `Millar, Jas___British Guiana___1899`

- [PASS] surname_gate: bio 'MILLAR' vs stint 'Millar, Jas' (exact)
- [PASS] initials: bio ['J', 'D'] ~ stint ['J']
- [PASS] age_gate: stint starts 1899, birth 1866 (age 33)
- [FAIL] colony: no placed event resolves to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1899-1915
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Millar, John___Canada___1894`

- Staff-list name: **Millar, John** | colony: **Canada** | listed 1894–1905 | editions [1894, 1896, 1897, 1898, 1899, 1900, 1905]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | John Millar | Deputy | DEPARTMENT OF EDUCATION | — | — |
| 1896 | John Millar | Deputy | Department of Education | — | — |
| 1897 | John Millar | Deputy | Department of Education | — | — |
| 1898 | John Millar | Deputy | Department of Education | — | — |
| 1899 | John Millar | Deputy | DEPARTMENT OF EDUCATION | — | — |
| 1900 | John Millar | Deputy | Department of Education | — | — |
| 1905 | John Millar | Deputy | Department of Education | — | — |

### Deterministic checks: `millar_james-duncan_b1866` vs `Millar, John___Canada___1894`

- [PASS] surname_gate: bio 'MILLAR' vs stint 'Millar, John' (exact)
- [PASS] initials: bio ['J', 'D'] ~ stint ['J']
- [PASS] age_gate: stint starts 1894, birth 1866 (age 28)
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1894-1905
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

