<!-- {"case_id": "case_hardy_richard-kenneth_b1898", "bio_ids": ["hardy_richard-kenneth_b1898"], "stint_ids": ["Hardy, R. K___Nigeria___1933", "Hardy, R___Mauritius___1914", "Hardy, R___Mauritius___1927"]} -->
# Dossier case_hardy_richard-kenneth_b1898

## Case context

- 1 biography(ies) and 3 candidate stint(s) are entangled in this case.
- Corpus context: 18 official(s) with this surname in the graph's staff lists; 14 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hardy_richard-kenneth_b1898`

- Printed name: **HARDY, Richard Kenneth**
- Birth year: 1898 (attested in editions [1948, 1949])
- Appears in editions: [1948, 1949]

### Verbatim printed entry text (OCR)

**Version `col1948-L33160.v` — printed in editions [1948, 1949]:**

> HARDY, Richard Kenneth.—b. 1898; ed. Bradford and Queen's Coll., Oxford (exhib. and schol.), B.A. (hons., chem.), Oxford; on mil. serv. 1917-19; govt. laboratory, London, 1924; asst. govt. chmst., Nig., 1927; govt. chmst., 1945.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1924 | govt. laboratory, London | — | [1948, 1949] |
| 1 | 1927 | asst. govt. chmst. | Nigeria | [1948, 1949] |
| 2 | 1945 | govt. chmst | Nigeria *(inherited from previous clause)* | [1948, 1949] |

## Candidate stint `Hardy, R. K___Nigeria___1933`

- Staff-list name: **Hardy, R. K** | colony: **Nigeria** | listed 1933–1939 | editions [1933, 1934, 1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | R. K. Hardy | Assistant Government Analyst | Analyst | — | — |
| 1934 | R. K. Hardy | Assistant Government Analyst | Analyst | — | — |
| 1936 | R. K. Hardy | Assistant Government Analyst | Analyst | — | — |
| 1939 | R. K. Hardy | Assistant Government Analysts | Analyst | — | — |

### Deterministic checks: `hardy_richard-kenneth_b1898` vs `Hardy, R. K___Nigeria___1933`

- [PASS] surname_gate: bio 'HARDY' vs stint 'Hardy, R. K' (exact)
- [PASS] initials: bio ['R', 'K'] ~ stint ['R', 'K']
- [PASS] age_gate: stint starts 1933, birth 1898 (age 35)
- [PASS] colony: 2 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1933-1939
- [FAIL] position_sim: best 51 vs bar 60: 'asst. govt. chmst.' ~ 'Assistant Government Analyst'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Hardy, R___Mauritius___1914`

- Staff-list name: **Hardy, R** | colony: **Mauritius** | listed 1914–1918 | editions [1914, 1915, 1917, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1914 | R. Hardy | Clerk | Master and Registrar's Office and Curator Accountant's Office | — | — |
| 1915 | R. Hardy | Clerk | Master and Registrar's Office and Curator Accountant's Office | — | — |
| 1917 | R. Hardy | Clerk | Master and Registrar's Office and Curator Accountant's Office | — | — |
| 1918 | R. Hardy | Clerk | Master and Registrar's Office and Curator Accountant's Office | — | — |

### Deterministic checks: `hardy_richard-kenneth_b1898` vs `Hardy, R___Mauritius___1914`

- [PASS] surname_gate: bio 'HARDY' vs stint 'Hardy, R' (exact)
- [PASS] initials: bio ['R', 'K'] ~ stint ['R']
- [PASS] age_gate: stint starts 1914, birth 1898 (age 16)
- [FAIL] colony: no placed event resolves to 'Mauritius'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1914-1918
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Hardy, R___Mauritius___1927`

- Staff-list name: **Hardy, R** | colony: **Mauritius** | listed 1927–1931 | editions [1927, 1928, 1929, 1931]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | R. Hardy | 3rd Class Clerk | Supreme Court | — | — |
| 1928 | R. Hardy | Clerk to Judges, 3rd Class | Supreme Court | — | — |
| 1929 | R. Hardy | 3rd Class Clerk | Supreme Court | — | — |
| 1931 | R. Hardy | 3rd Class Clerk | Supreme Court | — | — |

### Deterministic checks: `hardy_richard-kenneth_b1898` vs `Hardy, R___Mauritius___1927`

- [PASS] surname_gate: bio 'HARDY' vs stint 'Hardy, R' (exact)
- [PASS] initials: bio ['R', 'K'] ~ stint ['R']
- [PASS] age_gate: stint starts 1927, birth 1898 (age 29)
- [FAIL] colony: no placed event resolves to 'Mauritius'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1927-1931
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

