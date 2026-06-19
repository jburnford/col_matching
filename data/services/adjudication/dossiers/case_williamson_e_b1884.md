<!-- {"case_id": "case_williamson_e_b1884", "bio_ids": ["williamson_e_b1884"], "stint_ids": ["Williamson, G. E___Jamaica___1911"]} -->
# Dossier case_williamson_e_b1884

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 17 official(s) with this surname in the graph's staff lists; 14 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['williamson_e_b1884'] carry a single initial only — the namesake trap applies.

## Biography `williamson_e_b1884`

- Printed name: **WILLIAMSON, E**
- Birth year: 1884 (attested in editions [1924, 1927, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1937, 1939, 1940])
- Appears in editions: [1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1924-L58921.v` — printed in editions [1924, 1927, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1937, 1939, 1940]:**

> WILLIAMSON, E.—B. 1884; clk., G.P.O., Transvaal, Mar., 1903; treasy., Transvaal, July, 1904; senr. clk., Jan., 1919; prin. clk., Apr., 1921; sec., cabinet comte., on expenditure, 1922-24; ch. clk., estimates, June, 1929; under-secr. for finance, July, 1931.

**Version `col1925-L60427.v` — printed in editions [1925]:**

> WILLIAMSON, E.—B. 1884; clk., Transvaal, 1904; senr. clk., Jan., 1919; prin. clk., 1921; sec., cabinet comttee. on expenditure.

**Version `col1928-L71145.v` — printed in editions [1928]:**

> WILLIAMSON, E.—B. 1884; clk., G.P.O., Transvaal, Mar., 1903; treasy., Transvaal, July,

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1903 | clk., G.P.O. | Transvaal | [1924, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1937, 1939, 1940] |
| 1 | 1904 | treasy. | Transvaal | [1924, 1925, 1927, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1937, 1939, 1940] |
| 2 | 1919 | senr. clk | Transvaal *(inherited from previous clause)* | [1924, 1925, 1927, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1937, 1939, 1940] |
| 3 | 1921 | prin. clk | Transvaal *(inherited from previous clause)* | [1924, 1925, 1927, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1937, 1939, 1940] |
| 4 | 1922–1924 | sec., cabinet comte., on expenditure | Transvaal *(inherited from previous clause)* | [1924, 1927, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1937, 1939, 1940] |
| 5 | 1929 | ch. clk., estimates | Transvaal *(inherited from previous clause)* | [1924, 1927, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1937, 1939, 1940] |
| 6 | 1931 | under-secr. for finance | Transvaal *(inherited from previous clause)* | [1924, 1927, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1937, 1939, 1940] |

## Candidate stint `Williamson, G. E___Jamaica___1911`

- Staff-list name: **Williamson, G. E** | colony: **Jamaica** | listed 1911–1921 | editions [1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1911 | G. E. Williamson | Copyists | Titles Office | — | — |
| 1912 | G. E. Williamson | Copyists | Titles Office | — | — |
| 1913 | G. E. Williamson | Assistant | Titles Office | — | — |
| 1914 | G. E. Williamson | Assistant | Titles Office | — | — |
| 1915 | G. E. Williamson | Assistant | Titles Office | — | — |
| 1917 | G. E. Williamson | Assistant | Titles Office | — | — |
| 1918 | G. E. Williamson | Assistant | Titles Office | — | — |
| 1919 | G. E. Williamson | Assistant | Titles Office | — | — |
| 1920 | G. E. Williamson | Assistant | Titles Office | — | — |
| 1921 | G. E. Williamson | Assistant | Titles Office | — | — |

### Deterministic checks: `williamson_e_b1884` vs `Williamson, G. E___Jamaica___1911`

- [PASS] surname_gate: bio 'WILLIAMSON' vs stint 'Williamson, G. E' (exact)
- [PASS] initials: bio ['E'] ~ stint ['G', 'E']
- [PASS] age_gate: stint starts 1911, birth 1884 (age 27)
- [FAIL] colony: no placed event resolves to 'Jamaica'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1911-1921
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

