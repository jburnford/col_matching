<!-- {"case_id": "case_birch_w-c_e1914", "bio_ids": ["birch_w-c_e1914", "birch_w-c_e1914-2"], "stint_ids": ["Birch, W. C___Kenya___1917"]} -->
# Dossier case_birch_w-c_e1914

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 28 official(s) with this surname in the graph's staff lists; 14 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Birch, W. C___Kenya___1917'] have more than one claimant biography in this case.
- Phase 1 found `birch_w-c_e1914` ↔ `Birch, W. C___Kenya___1917` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- Phase 1 found `birch_w-c_e1914-2` ↔ `Birch, W. C___Kenya___1917` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).

## Biography `birch_w-c_e1914`

- Printed name: **BIRCH, W. C**
- Birth year: not printed
- Appears in editions: [1918, 1919, 1920, 1921, 1922, 1923]

### Verbatim printed entry text (OCR)

**Version `col1918-L48668.v` — printed in editions [1918, 1919, 1920, 1921, 1922, 1923]:**

> BIRCH, W. C.—Asst. analyst, E.A.P., July, 1914.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914 | Asst. analyst | East Africa Protectorate | [1918, 1919, 1920, 1921, 1922, 1923] |

## Biography `birch_w-c_e1914-2`

- Printed name: **BIRCH, W. C**
- Birth year: not printed
- Appears in editions: [1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940]

### Verbatim printed entry text (OCR)

**Version `col1924-L52368.v` — printed in editions [1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940]:**

> BIRCH, W. C.—Astt. analyst, E.A.P., July, 1914; senr. chemical offr., Apr., 1923.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914 | Astt. analyst | East Africa Protectorate | [1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940] |
| 1 | 1923 | senr. chemical offr | East Africa Protectorate *(inherited from previous clause)* | [1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1940] |

## Candidate stint `Birch, W. C___Kenya___1917`

- Staff-list name: **Birch, W. C** | colony: **Kenya** | listed 1917–1925 | editions [1917, 1919, 1920, 1922, 1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1917 | W. C. Birch | Assistant Analyst | Laboratories | — | — |
| 1919 | W. C. Birch | Assistant Analysts | Laboratories | — | — |
| 1920 | W. C. Birch | Assistant Analysts | Laboratories | — | — |
| 1922 | W. C. Birch | Senior Chemical Officer | Chemical Research Department | — | — |
| 1923 | W. C. Birch | Senior Chemical Officer | Chemical Research Department | — | — |
| 1924 | W. C. Birch | Senior Chemical Officer | Chemical Research Department | — | — |
| 1925 | W. C. Birch | Government Analyst | Medical Department | — | — |

### Deterministic checks: `birch_w-c_e1914` vs `Birch, W. C___Kenya___1917`

- [PASS] surname_gate: bio 'BIRCH' vs stint 'Birch, W. C' (exact)
- [PASS] initials: bio ['W', 'C'] ~ stint ['W', 'C']
- [PASS] age_gate: stint starts 1917; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1917-1925
- [PASS] position_sim: best 83 vs bar 60: 'Asst. analyst' ~ 'Assistant Analyst'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 2 agreeing edition-year(s) [1919, 1920] pos~80 (bar: >=2)
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `birch_w-c_e1914-2` vs `Birch, W. C___Kenya___1917`

- [PASS] surname_gate: bio 'BIRCH' vs stint 'Birch, W. C' (exact)
- [PASS] initials: bio ['W', 'C'] ~ stint ['W', 'C']
- [PASS] age_gate: stint starts 1917; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1917-1925
- [PASS] position_sim: best 88 vs bar 60: 'senr. chemical offr' ~ 'Senior Chemical Officer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): 1 agreeing edition-year(s) [1924] pos~88 (bar: >=2)
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

