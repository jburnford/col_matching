<!-- {"case_id": "case_balfe_r-s_b1892", "bio_ids": ["balfe_r-s_b1892"], "stint_ids": ["Balfe, Reginald Seymour___Basutoland___1920"]} -->
# Dossier case_balfe_r-s_b1892

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `balfe_r-s_b1892`

- Printed name: **BALFE, R. S**
- Birth year: 1892 (attested in editions [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940])
- Appears in editions: [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1927-L56951.v` — printed in editions [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940]:**

> BALFE, R. S.—B. 1892; cler.-asst., Basutoland, 1912; sub-inspr., Basutoland mounted pol., 1915; war serv., 1916-19; inspr., 1927; dep. asst. comsrr., 1930; dist. comsrr., 1936.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1912 | cler.-asst. | Basutoland | [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 1 | 1915 | sub-inspr., Basutoland mounted pol | Basutoland | [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 2 | 1927 | inspr | Basutoland *(inherited from previous clause)* | [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 3 | 1930 | dep. asst. comsrr | Basutoland *(inherited from previous clause)* | [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 4 | 1936 | dist. comsrr | Basutoland *(inherited from previous clause)* | [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |

## Candidate stint `Balfe, Reginald Seymour___Basutoland___1920`

- Staff-list name: **Balfe, Reginald Seymour** | colony: **Basutoland** | listed 1920–1922 | editions [1920, 1921, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1920 | Reginald Seymour Balfe | Sub-Inspector of Police | Civil Establishment | — | — |
| 1921 | Reginald Seymour Balfe | Sub-Inspector of Police | Establishment | — | — |
| 1922 | Reginald Seymour Balfe | Sub-Inspector of Police | Establishment | — | — |

### Deterministic checks: `balfe_r-s_b1892` vs `Balfe, Reginald Seymour___Basutoland___1920`

- [PASS] surname_gate: bio 'BALFE' vs stint 'Balfe, Reginald Seymour' (exact)
- [PASS] initials: bio ['R', 'S'] ~ stint ['R', 'S']
- [PASS] age_gate: stint starts 1920, birth 1892 (age 28)
- [PASS] colony: 5 placed event(s) resolve to 'Basutoland'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1920-1922
- [FAIL] position_sim: best 53 vs bar 60: 'sub-inspr., Basutoland mounted pol' ~ 'Sub-Inspector of Police'
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

