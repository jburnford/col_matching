<!-- {"case_id": "case_bostock_wilfred-cramer_b1879", "bio_ids": ["bostock_wilfred-cramer_b1879"], "stint_ids": ["Bostock, W. C___Nigeria___1922", "Bostock, W. C___Sierra Leone___1920"]} -->
# Dossier case_bostock_wilfred-cramer_b1879

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bostock_wilfred-cramer_b1879`

- Printed name: **BOSTOCK, WILFRED CRAMER**
- Birth year: 1879 (attested in editions [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934])
- Appears in editions: [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934]

### Verbatim printed entry text (OCR)

**Version `col1927-L57322.v` — printed in editions [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934]:**

> BOSTOCK, WILFRED CRAMER.—B. 1879; ed. St. Lawrence Coll., Ramsgate; served S. African War, Imp. Yeomanry; asst. engrnr., P.W.D., N. Nigeria, Sept., 1908; transf'd., Baro-Kano rly., Jan., 1909; res. engrnr., constrn., Sierra Leone, Oct., 1914 to Dec., 1915; asst. ch. engrnr., Nigerian rly., Jan., 1918; gen. man., Sierra Leone rly., Nov., 1919; ch. engrnr., Nigerian rly., Jan., 1922; dep. gen. man., Feb., 1924.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1908 | asst. engrnr., P.W.D., N. Nigeria | — | [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934] |
| 1 | 1909 | transf'd., Baro-Kano rly | — | [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934] |
| 2 | 1914–1915 | res. engrnr., constrn. | Sierra Leone | [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934] |
| 3 | 1918 | asst. ch. engrnr., Nigerian rly | Sierra Leone *(inherited from previous clause)* | [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934] |
| 4 | 1919 | gen. man., Sierra Leone rly | Sierra Leone | [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934] |
| 5 | 1922 | ch. engrnr., Nigerian rly | Sierra Leone *(inherited from previous clause)* | [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934] |
| 6 | 1924 | dep. gen. man | Sierra Leone *(inherited from previous clause)* | [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934] |

## Candidate stint `Bostock, W. C___Nigeria___1922`

- Staff-list name: **Bostock, W. C** | colony: **Nigeria** | listed 1922–1923 | editions [1922, 1923]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | W. C. Bostock | Chief Engineer | Ways and Works | — | — |
| 1923 | W. C. Bostock | Chief Engineer | Ways and Works | — | — |

### Deterministic checks: `bostock_wilfred-cramer_b1879` vs `Bostock, W. C___Nigeria___1922`

- [PASS] surname_gate: bio 'BOSTOCK' vs stint 'Bostock, W. C' (exact)
- [PASS] initials: bio ['W', 'C'] ~ stint ['W', 'C']
- [PASS] age_gate: stint starts 1922, birth 1879 (age 43)
- [FAIL] colony: no placed event resolves to 'Nigeria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1922-1923
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Bostock, W. C___Sierra Leone___1920`

- Staff-list name: **Bostock, W. C** | colony: **Sierra Leone** | listed 1920–1921 | editions [1920, 1921]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1920 | W. C. Bostock | General Manager | Railway Department | — | — |
| 1921 | W. C. Bostock | General Manager | Railway Department | — | — |

### Deterministic checks: `bostock_wilfred-cramer_b1879` vs `Bostock, W. C___Sierra Leone___1920`

- [PASS] surname_gate: bio 'BOSTOCK' vs stint 'Bostock, W. C' (exact)
- [PASS] initials: bio ['W', 'C'] ~ stint ['W', 'C']
- [PASS] age_gate: stint starts 1920, birth 1879 (age 41)
- [PASS] colony: 5 placed event(s) resolve to 'Sierra Leone'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1920-1921
- [FAIL] position_sim: best 51 vs bar 60: 'gen. man., Sierra Leone rly' ~ 'General Manager'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

