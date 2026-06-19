<!-- {"case_id": "case_galt_alexander-casimir_b1853", "bio_ids": ["galt_alexander-casimir_b1853"], "stint_ids": ["Galt, A. C___Canada___1913", "Galt, A___Victoria___1877"]} -->
# Dossier case_galt_alexander-casimir_b1853

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Galt, A___Victoria___1877` is also gate-compatible with biography(ies) outside this case: ['galt_alex-t_b1817'] (already linked elsewhere or filtered).

## Biography `galt_alexander-casimir_b1853`

- Printed name: **GALT, ALEXANDER CASIMIR**
- Birth year: 1853 (attested in editions [1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935])
- Appears in editions: [1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935]

### Verbatim printed entry text (OCR)

**Version `col1921-L56411.v` — printed in editions [1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935]:**

> GALT, HON. ALEXANDER CASIMIR.—B. 1853; ed. Hellmuth Coll., Toronto Univ.; practised law in Toronto, 1876-1896; Rossland, B.C., 1896-1906; Winnipeg, 1906-1912; judge of the ct. of king's bench, Manitoba, 1912; contribr. to Can. Law Journal and Can. Law Times.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1876–1896 | practised law in Toronto | — | [1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935] |
| 1 | 1896–1906 | Rossland | British Columbia | [1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935] |
| 2 | 1906–1912 | Winnipeg | British Columbia *(inherited from previous clause)* | [1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935] |
| 3 | 1912 | judge of the ct. of king's bench, Manitoba | British Columbia *(inherited from previous clause)* | [1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935] |

## Candidate stint `Galt, A. C___Canada___1913`

- Staff-list name: **Galt, A. C** | colony: **Canada** | listed 1913–1918 | editions [1913, 1914, 1915, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1913 | A. C. Galt | Puisne Judge, Court of King's Bench | Government | — | — |
| 1914 | Hon. A. C. Galt | Puisne Judge, Court of King's Bench | — | — | — |
| 1915 | A. C. Galt | Puisne Judges, Court of King's Bench | — | — | — |
| 1918 | A. C. Galt | Puisne Judge, Court of King's Bench | Judicial | — | — |

### Deterministic checks: `galt_alexander-casimir_b1853` vs `Galt, A. C___Canada___1913`

- [PASS] surname_gate: bio 'GALT' vs stint 'Galt, A. C' (exact)
- [PASS] initials: bio ['A', 'C'] ~ stint ['A', 'C']
- [PASS] age_gate: stint starts 1913, birth 1853 (age 60)
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1913-1918
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Galt, A___Victoria___1877`

- Staff-list name: **Galt, A** | colony: **Victoria** | listed 1877–1878 | editions [1877, 1878]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | A. Galt | Secretary | Department of Public Works | — | — |
| 1878 | A. Galt | Secretary | Department of Public Works | — | — |

### Deterministic checks: `galt_alexander-casimir_b1853` vs `Galt, A___Victoria___1877`

- [PASS] surname_gate: bio 'GALT' vs stint 'Galt, A' (exact)
- [PASS] initials: bio ['A', 'C'] ~ stint ['A']
- [PASS] age_gate: stint starts 1877, birth 1853 (age 24)
- [FAIL] colony: no placed event resolves to 'Victoria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1878
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

