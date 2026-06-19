<!-- {"case_id": "case_allen_w-r_b1896", "bio_ids": ["allen_w-r_b1896", "allen_william-ruskin_b1895"], "stint_ids": ["Allen, W. R___Gold Coast___1930"]} -->
# Dossier case_allen_w-r_b1896

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 103 official(s) with this surname in the graph's staff lists; 49 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Allen, W. R___Gold Coast___1930'] have more than one claimant biography in this case.
- Phase 1 found `allen_w-r_b1896` ↔ `Allen, W. R___Gold Coast___1930` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- Phase 1 found `allen_william-ruskin_b1895` ↔ `Allen, W. R___Gold Coast___1930` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).

## Biography `allen_w-r_b1896`

- Printed name: **ALLEN, W. R**
- Birth year: 1896 (attested in editions [1933, 1934, 1935, 1936])
- Appears in editions: [1933, 1934, 1935, 1936]

### Verbatim printed entry text (OCR)

**Version `col1933-L57404.v` — printed in editions [1933, 1934, 1935, 1936]:**

> ALLEN, W. R., B.A.—B. 1896; inspr., schls., Gold Coast, Jan., 1929.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | inspr., schls. | Gold Coast | [1933, 1934, 1935, 1936] |

## Biography `allen_william-ruskin_b1895`

- Printed name: **ALLEN, William Ruskin**
- Birth year: 1895 (attested in editions [1937, 1939, 1940])
- Appears in editions: [1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1937-L58438.v` — printed in editions [1937, 1939, 1940]:**

> ALLEN, William Ruskin, B.A.—B. 1895; war serv., 1914-18; ret. with rank of capt.; inspr., schls., Gold Coast, Jan., 1929.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | inspr., schls. | Gold Coast | [1937, 1939, 1940] |

## Candidate stint `Allen, W. R___Gold Coast___1930`

- Staff-list name: **Allen, W. R** | colony: **Gold Coast** | listed 1930–1936 | editions [1930, 1932, 1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1930 | W. R. Allen | Inspector of Schools | Education Department | — | — |
| 1932 | W. R. Allen | Inspectors of Schools | Education Department | — | — |
| 1934 | W. R. Allen | Provincial Inspectors and Inspectors of Schools | Education Department | — | — |
| 1936 | W. R. Allen | Provincial Inspector and Inspector of Schools | Education Department | — | — |

### Deterministic checks: `allen_w-r_b1896` vs `Allen, W. R___Gold Coast___1930`

- [PASS] surname_gate: bio 'ALLEN' vs stint 'Allen, W. R' (exact)
- [PASS] initials: bio ['W', 'R'] ~ stint ['W', 'R']
- [PASS] age_gate: stint starts 1930, birth 1896 (age 34)
- [PASS] colony: 1 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1930-1936
- [PASS] position_sim: best 71 vs bar 60: 'inspr., schls.' ~ 'Inspector of Schools'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `allen_william-ruskin_b1895` vs `Allen, W. R___Gold Coast___1930`

- [PASS] surname_gate: bio 'ALLEN' vs stint 'Allen, W. R' (exact)
- [PASS] initials: bio ['W', 'R'] ~ stint ['W', 'R']
- [PASS] age_gate: stint starts 1930, birth 1895 (age 35)
- [PASS] colony: 1 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1930-1936
- [PASS] position_sim: best 71 vs bar 60: 'inspr., schls.' ~ 'Inspector of Schools'
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

