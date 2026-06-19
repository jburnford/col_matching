<!-- {"case_id": "case_quick_john_b1852", "bio_ids": ["quick_john_b1852"], "stint_ids": ["Quick, J. E___British Guiana___1914", "Quick, John___Commonwealth Of Australia___1905"]} -->
# Dossier case_quick_john_b1852

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 13 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['quick_john_b1852'] carry a single initial only — the namesake trap applies.

## Biography `quick_john_b1852`

- Printed name: **QUICK, John**
- Birth year: 1852 (attested in editions [1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1931, 1932])
- Honours: K.T.
- Appears in editions: [1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1931, 1932]

### Verbatim printed entry text (OCR)

**Version `col1910-L48230.v` — printed in editions [1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1931, 1932]:**

> QUICK, Hon. Sir John, K.T., B.A. (1901); LL.D.—B. 1852; elec. to first H. of R., Commonwealth of Australia, 1901; re-elec. in 1903 and 1906; postmr.-gen., C. of A., June, 1909; retired from politics, 1913; now dep. judge, federal arbitration, etc.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1901–1901 | elec. to first H. of R. | Commonwealth of Australia | [1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1931, 1932] |
| 1 | 1903–1906 | re-elec. | — | [1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1931, 1932] |
| 2 | 1909–1909 | postmr.-gen. | Commonwealth of Australia | [1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1931, 1932] |
| 3 | 1913–1913 | retired from politics | — | [1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1931, 1932] |

## Candidate stint `Quick, J. E___British Guiana___1914`

- Staff-list name: **Quick, J. E** | colony: **British Guiana** | listed 1914–1915 | editions [1914, 1915]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1914 | J. E. Quick | Rector of St. Patrick's | Ecclesiastical Establishments (Church of England) | — | — |
| 1915 | J. E. Quick | Rector of St. Patrick's | Ecclesiastical Establishments (Church of England) | — | — |

### Deterministic checks: `quick_john_b1852` vs `Quick, J. E___British Guiana___1914`

- [PASS] surname_gate: bio 'QUICK' vs stint 'Quick, J. E' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J', 'E']
- [PASS] age_gate: stint starts 1914, birth 1852 (age 62)
- [FAIL] colony: no placed event resolves to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1914-1915
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Quick, John___Commonwealth Of Australia___1905`

- Staff-list name: **Quick, John** | colony: **Commonwealth Of Australia** | listed 1905–1907 | editions [1905, 1907]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | John Quick | Member of Legislative Assembly | Parliament | — | — |
| 1907 | John Quick | Hendigo | — | — | — |

### Deterministic checks: `quick_john_b1852` vs `Quick, John___Commonwealth Of Australia___1905`

- [PASS] surname_gate: bio 'QUICK' vs stint 'Quick, John' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1905, birth 1852 (age 53)
- [PASS] colony: 2 placed event(s) resolve to 'Commonwealth Of Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1907
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

