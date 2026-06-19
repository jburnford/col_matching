<!-- {"case_id": "case_baldwin_joseph-mason_b1878", "bio_ids": ["baldwin_joseph-mason_b1878"], "stint_ids": ["Baldwin, J. M___Australia___1918"]} -->
# Dossier case_baldwin_joseph-mason_b1878

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 16 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `baldwin_joseph-mason_b1878`

- Printed name: **BALDWIN, JOSEPH MASON**
- Birth year: 1878 (attested in editions [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937])
- Honours: M.A
- Appears in editions: [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937]

### Verbatim printed entry text (OCR)

**Version `col1927-L56945.v` — printed in editions [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937]:**

> BALDWIN, JOSEPH MASON, M.A., D.Sc.—B. 1878; ag. govt. astronomer, Victoria, 1915; govt. astronomer, 1st July, 1919.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915 | ag. govt. astronomer | Victoria | [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937] |
| 1 | 1919 | govt. astronomer | Victoria *(inherited from previous clause)* | [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937] |

## Candidate stint `Baldwin, J. M___Australia___1918`

- Staff-list name: **Baldwin, J. M** | colony: **Australia** | listed 1918–1927 | editions [1918, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1918 | J. M. Baldwin | Government Astronomer (acting) | Observatory | — | — |
| 1927 | J. M. Baldwin | Government Astronomer | Observatory | — | — |

### Deterministic checks: `baldwin_joseph-mason_b1878` vs `Baldwin, J. M___Australia___1918`

- [PASS] surname_gate: bio 'BALDWIN' vs stint 'Baldwin, J. M' (exact)
- [PASS] initials: bio ['J', 'M'] ~ stint ['J', 'M']
- [PASS] age_gate: stint starts 1918, birth 1878 (age 40)
- [FAIL] colony: no placed event resolves to 'Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1918-1927
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

