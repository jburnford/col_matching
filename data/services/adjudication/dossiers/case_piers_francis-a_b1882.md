<!-- {"case_id": "case_piers_francis-a_b1882", "bio_ids": ["piers_francis-a_b1882"], "stint_ids": ["Piers, Francis Arthur___Basutoland___1911", "Piers, Francis Arthur___South Africa___1914"]} -->
# Dossier case_piers_francis-a_b1882

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 13 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `piers_francis-a_b1882`

- Printed name: **PIERS, Francis A**
- Birth year: 1882 (attested in editions [1940])
- Appears in editions: [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L67591.v` — printed in editions [1940]:**

> PIERS, Major Francis A.—B. 1882; sub-inspr., Basutoland mounted pol., 1910; inspr., 1923; supt., pol., 1936; commr., pol. and prisons, 1939.

**Version `col1927-L62021.v` — printed in editions [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939]:**

> PIERS, FRANCIS A.—B. 1882; sub-inspr., Basutoland mounted pol., 1910; inspr., 1923; supr., pol., 1936.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1910 | sub-inspr., Basutoland mounted pol | Basutoland | [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 1 | 1923 | inspr | Basutoland *(inherited from previous clause)* | [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 2 | 1936 | supt., pol | Basutoland *(inherited from previous clause)* | [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 3 | 1939 | commr., pol. and prisons | Basutoland *(inherited from previous clause)* | [1940] |

## Candidate stint `Piers, Francis Arthur___Basutoland___1911`

- Staff-list name: **Piers, Francis Arthur** | colony: **Basutoland** | listed 1911–1925 | editions [1911, 1917, 1921, 1922, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1911 | Francis Arthur Piers | Sub-Inspector of Police | Establishment | — | — |
| 1917 | Francis Arthur Piers | Sub-Inspector of Police | Establishment | — | — |
| 1921 | Francis Arthur Piers | Sub-Inspector of Police | Establishment | — | — |
| 1922 | Francis Arthur Piers | Sub-Inspector of Police | Establishment | — | — |
| 1924 | Francis Arthur Piers | Inspector | Police | — | Captain |
| 1925 | Francis Arthur Piers | Inspector | Police | — | Captain |

### Deterministic checks: `piers_francis-a_b1882` vs `Piers, Francis Arthur___Basutoland___1911`

- [PASS] surname_gate: bio 'PIERS' vs stint 'Piers, Francis Arthur' (exact)
- [PASS] initials: bio ['F', 'A'] ~ stint ['F', 'A']
- [PASS] age_gate: stint starts 1911, birth 1882 (age 29)
- [PASS] colony: 4 placed event(s) resolve to 'Basutoland'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1911-1925
- [PASS] position_sim: best 71 vs bar 60: 'inspr' ~ 'Inspector'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Piers, Francis Arthur___South Africa___1914`

- Staff-list name: **Piers, Francis Arthur** | colony: **South Africa** | listed 1914–1918 | editions [1914, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1914 | Francis Arthur Piers | Sub-Inspector of Police | Civil Establishment | — | — |
| 1918 | Francis Arthur Piers | Sub-Inspector of Police | Establishment | — | — |

### Deterministic checks: `piers_francis-a_b1882` vs `Piers, Francis Arthur___South Africa___1914`

- [PASS] surname_gate: bio 'PIERS' vs stint 'Piers, Francis Arthur' (exact)
- [PASS] initials: bio ['F', 'A'] ~ stint ['F', 'A']
- [PASS] age_gate: stint starts 1914, birth 1882 (age 32)
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1914-1918
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

