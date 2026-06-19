<!-- {"case_id": "case_dunn_c-de-s_e1901", "bio_ids": ["dunn_c-de-s_e1901"], "stint_ids": ["Dunn, C. de S___Windward Islands___1918"]} -->
# Dossier case_dunn_c-de-s_e1901

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 33 official(s) with this surname in the graph's staff lists; 11 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `dunn_c-de-s_e1901`

- Printed name: **DUNN, C. de S**
- Birth year: not printed
- Appears in editions: [1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1914-L46014.v` — printed in editions [1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1937, 1939, 1940]:**

> DUNN, C. de S.—Served in South Africa, 1901-1902 (medal and five clasps); S.A.C., 1903-1906; camel constab., Somaliland, 1912.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1901–1902 | Served in South Africa | — | [1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1937, 1939, 1940] |
| 1 | 1903–1906 | S.A.C | — | [1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1937, 1939, 1940] |
| 2 | 1912 | camel constab. | Somaliland | [1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1937, 1939, 1940] |

## Candidate stint `Dunn, C. de S___Windward Islands___1918`

- Staff-list name: **Dunn, C. de S** | colony: **Windward Islands** | listed 1918–1920 | editions [1918, 1919, 1920]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1918 | C. de S. Dunn | Chief of Police, Superintendent of Prison, Chief Relieving Officer and Chief Sanitary Officer | Police, Excise, and Prisons | — | — |
| 1919 | C. de S. Dunn | Chief of Police, Superintendent of Prison, Chief Relieving Officer and Chief Sanitary Officer | Police, Excise, and Prisons | — | — |
| 1920 | C. de S. Dunn | Chief of Police, Superintendent of Prison, Chief Relieving Officer and Chief Sanitary Officer | Police, Excise, and Prisons | — | — |

### Deterministic checks: `dunn_c-de-s_e1901` vs `Dunn, C. de S___Windward Islands___1918`

- [PASS] surname_gate: bio 'DUNN' vs stint 'Dunn, C. de S' (exact)
- [PASS] initials: bio ['C', 'D', 'S'] ~ stint ['C', 'D', 'S']
- [PASS] age_gate: stint starts 1918; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1918-1920
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

