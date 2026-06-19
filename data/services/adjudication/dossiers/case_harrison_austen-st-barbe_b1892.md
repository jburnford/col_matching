<!-- {"case_id": "case_harrison_austen-st-barbe_b1892", "bio_ids": ["harrison_austen-st-barbe_b1892"], "stint_ids": ["Harrison, A. S___Ceylon___1915", "Harrison, A. St. B___Palestine___1923"]} -->
# Dossier case_harrison_austen-st-barbe_b1892

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 85 official(s) with this surname in the graph's staff lists; 30 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Harrison, A. S___Ceylon___1915` is also gate-compatible with biography(ies) outside this case: ['harrison_albert-seddon_b1887'] (already linked elsewhere or filtered).
- NOTE: stint `Harrison, A. St. B___Palestine___1923` is also gate-compatible with biography(ies) outside this case: ['harrison_albert-seddon_b1887'] (already linked elsewhere or filtered).

## Biography `harrison_austen-st-barbe_b1892`

- Printed name: **HARRISON, AUSTEN ST. BARBE**
- Birth year: 1892 (attested in editions [1936, 1937, 1940])
- Appears in editions: [1936, 1937, 1940]

### Verbatim printed entry text (OCR)

**Version `col1936-L61393.v` — printed in editions [1936, 1937, 1940]:**

> HARRISON, AUSTEN ST. BARBE, R.I.B.A. (chtd. archt.), mem. of Town Planning Inst.—B. 1892; ed. Monkton Combe Schol. and McGill Univ., Montreal; archt. and town planner, miny. of communications, Greece, 1920-22; archt., P.W.D., Palestine, 1922.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920–1922 | archt. and town planner, miny. of communications, Greece | — | [1936, 1937, 1940] |
| 1 | 1922 | archt., P.W.D. | Palestine | [1936, 1937, 1940] |

## Candidate stint `Harrison, A. S___Ceylon___1915`

- Staff-list name: **Harrison, A. S** | colony: **Ceylon** | listed 1915–1931 | editions [1915, 1917, 1918, 1920, 1921, 1922, 1923, 1925, 1927, 1928, 1929, 1931]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1915 | A. S. Harrison | Inspector of Schools | Education Department | — | — |
| 1917 | A. S. Harrison | Inspector of Schools | Education Department | — | — |
| 1918 | A. S. Harrison | Inspector of Schools | Education Department | — | — |
| 1920 | A. S. Harrison | Inspector of Schools | Education Department | — | — |
| 1921 | A. S. Harrison | Assistant Director | Education Department | — | — |
| 1922 | A. S. Harrison | Principal, Training College | University College | — | — |
| 1923 | A. S. Harrison | Principal | Training College | — | — |
| 1925 | A. S. Harrison | Principal | Training College | — | — |
| 1927 | A. S. Harrison | Principal | Training College | — | — |
| 1928 | A. S. Harrison | Principal | Training College | — | — |
| 1929 | A. S. Harrison | Principal | Training College | — | — |
| 1931 | A. S. Harrison | Principal | Training College | — | — |

### Deterministic checks: `harrison_austen-st-barbe_b1892` vs `Harrison, A. S___Ceylon___1915`

- [PASS] surname_gate: bio 'HARRISON' vs stint 'Harrison, A. S' (exact)
- [PASS] initials: bio ['A', 'S', 'B'] ~ stint ['A', 'S']
- [PASS] age_gate: stint starts 1915, birth 1892 (age 23)
- [FAIL] colony: no placed event resolves to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1915-1931
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Harrison, A. St. B___Palestine___1923`

- Staff-list name: **Harrison, A. St. B** | colony: **Palestine** | listed 1923–1932 | editions [1923, 1925, 1927, 1928, 1929, 1930, 1931, 1932]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1923 | A. St. B. Harrison | Architect | PUBLIC WORKS | — | — |
| 1925 | A. St. B. Harrison | Architect | Public Works | — | — |
| 1927 | A. St. B. Harrison | Architect | Department of Public Works | — | — |
| 1928 | A. St. B. Harrison | Architect | Public Works | — | — |
| 1929 | A. St. B. Harrison | Architect | Department of Public Works | — | — |
| 1930 | A. St. B. Harrison | Architect | Public Works | — | — |
| 1931 | A. St. B. Harrison | Architect | Public Works | — | — |
| 1932 | A. St. B. Harrison | Architect | Public Works | — | — |

### Deterministic checks: `harrison_austen-st-barbe_b1892` vs `Harrison, A. St. B___Palestine___1923`

- [PASS] surname_gate: bio 'HARRISON' vs stint 'Harrison, A. St. B' (exact)
- [PASS] initials: bio ['A', 'S', 'B'] ~ stint ['A', 'S', 'B']
- [PASS] age_gate: stint starts 1923, birth 1892 (age 31)
- [PASS] colony: 1 placed event(s) resolve to 'Palestine'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1923-1932
- [FAIL] position_sim: best 56 vs bar 60: 'archt., P.W.D.' ~ 'Architect'
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

