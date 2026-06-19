<!-- {"case_id": "case_keay_david-doig_e1901", "bio_ids": ["keay_david-doig_e1901"], "stint_ids": ["Keay, D. D___South Africa___1914"]} -->
# Dossier case_keay_david-doig_e1901

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `keay_david-doig_e1901`

- Printed name: **KEAY, DAVID DOIG**
- Birth year: not printed
- Appears in editions: [1913, 1914, 1915, 1917, 1918, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929]

### Verbatim printed entry text (OCR)

**Version `col1913-L47187.v` — printed in editions [1913, 1914, 1915, 1917, 1918, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929]:**

> KEAY, DAVID DOIG.—Clk., Natal govt. rly., 1901-2; clk., law dept., Transvaal, Mar., 1902; ag. ch. clk., admstr. branch, atty.-gen.'s off., Nov., 1903; ch. clk., July, 1904; ag. under-sec. for just., U. of S. Africa, May, 1911; chief clk., dept. of just., 1st Apr., 1912.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1901–1902 | Clk., Natal govt. rly | Natal | [1913, 1914, 1915, 1917, 1918, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929] |
| 1 | 1902 | clk., law dept. | Transvaal | [1913, 1914, 1915, 1917, 1918, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929] |
| 2 | 1903 | ag. ch. clk., admstr. branch, atty.-gen.'s off | Transvaal *(inherited from previous clause)* | [1913, 1914, 1915, 1917, 1918, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929] |
| 3 | 1904 | ch. clk | Transvaal *(inherited from previous clause)* | [1913, 1914, 1915, 1917, 1918, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929] |
| 4 | 1911 | ag. under-sec. for just., U. of S. Africa | Transvaal *(inherited from previous clause)* | [1913, 1914, 1915, 1917, 1918, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929] |
| 5 | 1912 | chief clk., dept. of just | Transvaal *(inherited from previous clause)* | [1913, 1914, 1915, 1917, 1918, 1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929] |

## Candidate stint `Keay, D. D___South Africa___1914`

- Staff-list name: **Keay, D. D** | colony: **South Africa** | listed 1914–1918 | editions [1914, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1914 | D. D. Keay | Chief Clerks | Department of Justice | — | — |
| 1918 | D. D. Keay | Chief Clerks | Department of Justice | — | — |

### Deterministic checks: `keay_david-doig_e1901` vs `Keay, D. D___South Africa___1914`

- [PASS] surname_gate: bio 'KEAY' vs stint 'Keay, D. D' (exact)
- [PASS] initials: bio ['D', 'D'] ~ stint ['D', 'D']
- [PASS] age_gate: stint starts 1914; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1914-1918
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

