<!-- {"case_id": "case_bulman_joseph-waugh_b1893", "bio_ids": ["bulman_joseph-waugh_b1893"], "stint_ids": ["Bulman, J. W___Cyprus___1921"]} -->
# Dossier case_bulman_joseph-waugh_b1893

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bulman_joseph-waugh_b1893`

- Printed name: **BULMAN, JOSEPH WAUGH**
- Birth year: 1893 (attested in editions [1936, 1937, 1939, 1940])
- Honours: M.B.E
- Appears in editions: [1936, 1937, 1939, 1940, 1948]

### Verbatim printed entry text (OCR)

**Version `col1936-L59348.v` — printed in editions [1936, 1937, 1939, 1940]:**

> BULMAN, JOSEPH WAUGH, A.M.I.Loco.E.—B. 1893; ed. Petershill Pub. Schl., Glasgow; served in Navy, 1914-19; loco. foreman, Cyprus govt. rly., Nov., 1919; asst. loco. supt., Oct., 1927; aspt., rly., July, 1935.

**Version `col1948-L31497.v` — printed in editions [1948]:**

> BULMAN, Joseph Waugh, M.B.E., A.M.I.Loco.E.—b. 1893; ed. Petershill Public Sch.; on naval serv. 1914–19; engrn. apprn., Caledonian Railway Co., Glasgow, 1909; loco. foreman, Cyp., 1919; supt. of rlyws., 1935.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1909 | engrn. apprn., Caledonian Railway Co., Glasgow | — | [1948] |
| 1 | 1914–1919 | served in Navy | — | [1936, 1937, 1939, 1940] |
| 2 | 1914–1919 | on naval serv | — | [1948] |
| 3 | 1919 | loco. foreman, Cyprus govt. rly | Cyprus | [1936, 1937, 1939, 1940, 1948] |
| 4 | 1927 | asst. loco. supt | Cyprus *(inherited from previous clause)* | [1936, 1937, 1939, 1940] |
| 5 | 1935 | aspt., rly | Cyprus *(inherited from previous clause)* | [1936, 1937, 1939, 1940, 1948] |

## Candidate stint `Bulman, J. W___Cyprus___1921`

- Staff-list name: **Bulman, J. W** | colony: **Cyprus** | listed 1921–1939 | editions [1921, 1922, 1923, 1924, 1925, 1929, 1930, 1934, 1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | J. W. Bulman | Locomotive Foreman | Locomotive, Carriage and Wagon Expenses | — | — |
| 1922 | J. W. Bulman | Locomotive Foreman | Locomotive, Carriage and Wagon Expenses | — | — |
| 1923 | J. W. Bulman | Locomotive Foreman | Locomotive, Carriage and Wagon Department | — | — |
| 1924 | J. W. Bulman | Locomotive Foreman | Locomotive, Carriage and Wagon Department | — | — |
| 1925 | J. W. Bulman | Locomotive Foreman | Locomotive, Carriage and Wagon Department | — | — |
| 1929 | J. W. Bulman | Assistant Locomotive Superintendent | Locomotive, Carriage and Wagon Department | — | — |
| 1930 | J. W. Bulman | Assistant Locomotive Superintendent | Locomotive, Carriage and Wagon Department | — | — |
| 1934 | J. W. Bulman | Locomotive Superintendent | Locomotive | — | — |
| 1936 | J. W. Bulman | Superintendent | Railway Department | — | — |
| 1939 | J. W. Bulman | Superintendent | Railway Department | — | — |

### Deterministic checks: `bulman_joseph-waugh_b1893` vs `Bulman, J. W___Cyprus___1921`

- [PASS] surname_gate: bio 'BULMAN' vs stint 'Bulman, J. W' (exact)
- [PASS] initials: bio ['J', 'W'] ~ stint ['J', 'W']
- [PASS] age_gate: stint starts 1921, birth 1893 (age 28)
- [PASS] colony: 3 placed event(s) resolve to 'Cyprus'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1921-1939
- [FAIL] position_sim: best 57 vs bar 60: 'asst. loco. supt' ~ 'Assistant Locomotive Superintendent'
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

