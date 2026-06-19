<!-- {"case_id": "case_march_harry-thomas_b1881", "bio_ids": ["march_harry-thomas_b1881"], "stint_ids": ["March, H. T___Sierra Leone___1913", "March, H. T___Southern Nigeria___1909"]} -->
# Dossier case_march_harry-thomas_b1881

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 14 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `march_harry-thomas_b1881`

- Printed name: **MARCH, HARRY THOMAS**
- Birth year: 1881 (attested in editions [1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936])
- Appears in editions: [1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936]

### Verbatim printed entry text (OCR)

**Version `col1923-L56469.v` — printed in editions [1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936]:**

> MARCH, HARRY THOMAS.—B. 1881; ed. King's Coll., London; 2nd divn. clk., post office, 1900-07; acctnt., post office, Nigeria, 20th Apr., 1907 to 31st Jan., 1912; postmtr.-gen., Sierra Leone, 1st Feb., 1912.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1900–1907 | 2nd divn. clk., post office | — | [1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936] |
| 1 | 1907–1912 | acctnt., post office | Nigeria | [1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936] |
| 2 | 1912 | postmtr.-gen. | Sierra Leone | [1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936] |

## Candidate stint `March, H. T___Sierra Leone___1913`

- Staff-list name: **March, H. T** | colony: **Sierra Leone** | listed 1913–1925 | editions [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1922, 1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1913 | H. T. March | Colonial Postmaster-General and Manager Savings Bank | Post Office | — | — |
| 1914 | H. T. March | Colonial Postmaster-General and Manager Savings Bank | Post Office | — | — |
| 1915 | H. T. March | Postmaster General | Post Office | — | — |
| 1917 | H. T. March | Postmaster General | Post Office | — | — |
| 1918 | H. T. March | Postmaster General | Post Office | — | — |
| 1919 | H. T. March | Postmaster General | Post Office | — | — |
| 1920 | H. T. March | Postmaster General | Post Office | — | — |
| 1922 | H. T. March | Postmaster General | Post Office | — | — |
| 1923 | H. T. March | Postmaster General | Post Office | — | — |
| 1924 | H. T. March | Postmaster General | Post Office | — | — |
| 1925 | H. T. March | Postmaster General | Post Office | — | — |

### Deterministic checks: `march_harry-thomas_b1881` vs `March, H. T___Sierra Leone___1913`

- [PASS] surname_gate: bio 'MARCH' vs stint 'March, H. T' (exact)
- [PASS] initials: bio ['H', 'T'] ~ stint ['H', 'T']
- [PASS] age_gate: stint starts 1913, birth 1881 (age 32)
- [PASS] colony: 1 placed event(s) resolve to 'Sierra Leone'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1913-1925
- [FAIL] position_sim: best 50 vs bar 60: 'postmtr.-gen.' ~ 'Postmaster General'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `March, H. T___Southern Nigeria___1909`

- Staff-list name: **March, H. T** | colony: **Southern Nigeria** | listed 1909–1912 | editions [1909, 1910, 1911, 1912]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1909 | H. T. March | Accountant | Post Office | — | — |
| 1910 | H. T. March | Accountant | Post Office | — | — |
| 1911 | H. T. March | Accountant | Post Office | — | — |
| 1912 | H. T. March | Accountant | Post Office | — | — |

### Deterministic checks: `march_harry-thomas_b1881` vs `March, H. T___Southern Nigeria___1909`

- [PASS] surname_gate: bio 'MARCH' vs stint 'March, H. T' (exact)
- [PASS] initials: bio ['H', 'T'] ~ stint ['H', 'T']
- [PASS] age_gate: stint starts 1909, birth 1881 (age 28)
- [FAIL] colony: no placed event resolves to 'Southern Nigeria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1909-1912
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

