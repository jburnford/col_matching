<!-- {"case_id": "case_cosser_s-c-a_b1880", "bio_ids": ["cosser_s-c-a_b1880"], "stint_ids": ["Cosser, S. C. A___South Africa___1912"]} -->
# Dossier case_cosser_s-c-a_b1880

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `cosser_s-c-a_b1880`

- Printed name: **COSSER, S. C. A**
- Birth year: 1880 (attested in editions [1914, 1915, 1919, 1922, 1924, 1925, 1927, 1928, 1931, 1932, 1933, 1934, 1935])
- Appears in editions: [1913, 1914, 1915, 1917, 1919, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1930, 1931, 1932, 1933, 1934, 1935]

### Verbatim printed entry text (OCR)

**Version `col1914-L45543.v` — printed in editions [1914, 1915, 1919, 1922, 1924, 1925, 1927, 1928, 1931, 1932, 1933, 1934, 1935]:**

> COSSER, S. C. A.—B. 1880; ed. Trowbridge; clk., treasy., Transvaal, 8th May, 1901; asst. acctnt., treasy., 1st Dec., 1905; asst. acctnt., treasy., Union of S. Africa, 31st May, 1910; provincial acctnt., Transvaal Prov., 21st Nov., 1910; served in European War, 1915-19 (Gen. Serv. Victory and Milly. Meds.).

**Version `col1917-L48743.v` — printed in editions [1917, 1921, 1923, 1930]:**

> COSSEY, S. C. A.—B. 1880; ed. Tonbridge; clk., treasy., Transvaal, 8th May, 1901; asst. acctnt., treasy., 1st Dec., 1905; asst. acctnt., treasy., Union of S. Africa, 31st May, 1910; provincial acctnt., Transvaal Prov., 21st Nov., 1910; served in European War, 1915-19 (Gen. Serv., Victory and Mily. Meds.)

**Version `col1913-L44956.v` — printed in editions [1913]:**

> COSSEER, S. C. A.—B. 1880; clk., treasy., Transvaal, 8th May, 1911; asst. acctnt., treasy., 1st Dec., 1905; asst. acctnt., treasy., Union of S. Africa, 31st May, 1910; provincial acctnt., Transvaal Prov., 21st Nov., 1910.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1901 | clk., treasy. | Transvaal | [1914, 1915, 1917, 1919, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1930, 1931, 1932, 1933, 1934, 1935] |
| 1 | 1905 | asst. acctnt., treasy | Transvaal *(inherited from previous clause)* | [1913, 1914, 1915, 1917, 1919, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1930, 1931, 1932, 1933, 1934, 1935] |
| 2 | 1910 | asst. acctnt., treasy., Union of S. Africa | Transvaal | [1913, 1914, 1915, 1917, 1919, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1930, 1931, 1932, 1933, 1934, 1935] |
| 3 | 1911 | clk., treasy. | Transvaal | [1913] |
| 4 | 1915–1919 | served in European War | Transvaal *(inherited from previous clause)* | [1914, 1915, 1917, 1919, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1930, 1931, 1932, 1933, 1934, 1935] |

## Candidate stint `Cosser, S. C. A___South Africa___1912`

- Staff-list name: **Cosser, S. C. A** | colony: **South Africa** | listed 1912–1918 | editions [1912, 1914, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | S. C. A. Cosser | Provincial Accountant | Provincial Administration | — | — |
| 1914 | S. C. A. Cosser | Provincial Accountant | Provincial Administration | — | — |
| 1918 | S. C. A. Cosser | Provincial Accountant | Provincial Administration | — | — |

### Deterministic checks: `cosser_s-c-a_b1880` vs `Cosser, S. C. A___South Africa___1912`

- [PASS] surname_gate: bio 'COSSER' vs stint 'Cosser, S. C. A' (exact)
- [PASS] initials: bio ['S', 'C', 'A'] ~ stint ['S', 'C', 'A']
- [PASS] age_gate: stint starts 1912, birth 1880 (age 32)
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

