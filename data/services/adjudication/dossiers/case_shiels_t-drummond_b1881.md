<!-- {"case_id": "case_shiels_t-drummond_b1881", "bio_ids": ["shiels_t-drummond_b1881"], "stint_ids": ["Shields, T___Australia___1918"]} -->
# Dossier case_shiels_t-drummond_b1881

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `shiels_t-drummond_b1881`

- Printed name: **SHIELS, T. DRUMMOND**
- Birth year: 1881 (attested in editions [1930, 1931, 1932, 1934, 1935, 1936, 1940, 1948, 1949, 1950, 1951])
- Honours: M.C
- Appears in editions: [1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940, 1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1930-L68179.v` — printed in editions [1930, 1931, 1932, 1934, 1935, 1936, 1940, 1948, 1949, 1950, 1951]:**

> SHIELS, DR T. DRUMMOND, M.C., M.P.—B. 1881; ed. Edinburgh Univ. (M.B., Ch.B.); served European War as offr. R. Scotz.; in command with rank as capt. one of trench mortar batteries of 9th (Scottish) Divn. (severely wounded); was a mem., Edinburgh town coun.; M.P., East Edinburgh since 1924; mem., ap. coman., Ceylon constitution, 1927; parly. under sec., India Office, June, 1924; parly. under sec. for the Cola., Dec., 1929.

**Version `col1933-L63318.v` — printed in editions [1933, 1937, 1939]:**

> SHIELDS, DR. T. DRUMMOND, M.C., M.P.—B. 1881; ed. Edinburgh Univ. (M.B., Ch. B.); served European War as offr. R. Scots.; in command, with rank as capt., one of trench mortar batteries of 9th (Scottish) Divn. (severely wounded); was a mem., Edinburgh town coun.; M.P., East Edinburgh since 1924; mem., sp. comm., Ceylon constitution, 1927; partly, under-sec., India Office, June, 1924; partly, under-sec. for cols., 1929-31.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1924 | M.P., East Edinburgh since | — | [1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940, 1948, 1949, 1950, 1951] |
| 1 | 1924 | parly. under sec., India Office | Ceylon *(inherited from previous clause)* | [1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940, 1948, 1949, 1950, 1951] |
| 2 | 1927 | mem., ap. coman., Ceylon constitution | Ceylon | [1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940, 1948, 1949, 1950, 1951] |
| 3 | 1929 | parly. under sec. for the Cola | Ceylon *(inherited from previous clause)* | [1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940, 1948, 1949, 1950, 1951] |

## Candidate stint `Shields, T___Australia___1918`

- Staff-list name: **Shields, T** | colony: **Australia** | listed 1918–1927 | editions [1918, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1918 | T. Shields | — | Legislative Council | — | — |
| 1927 | Hon. T. Shields | — | Legislative Council | — | — |

### Deterministic checks: `shiels_t-drummond_b1881` vs `Shields, T___Australia___1918`

- [PASS] surname_gate: bio 'SHIELS' vs stint 'Shields, T' (fuzzy:1)
- [PASS] initials: bio ['T', 'D'] ~ stint ['T']
- [PASS] age_gate: stint starts 1918, birth 1881 (age 37)
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

