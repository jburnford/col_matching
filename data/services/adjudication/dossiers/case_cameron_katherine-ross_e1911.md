<!-- {"case_id": "case_cameron_katherine-ross_e1911", "bio_ids": ["cameron_katherine-ross_e1911"], "stint_ids": ["Cameron, K. R___Nyasaland___1921", "Cameron, K___Zanzibar___1929"]} -->
# Dossier case_cameron_katherine-ross_e1911

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 68 official(s) with this surname in the graph's staff lists; 33 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `cameron_katherine-ross_e1911`

- Printed name: **CAMERON, KATHERINE ROSS**
- Birth year: not printed
- Honours: M.B.E (1926)
- Appears in editions: [1929, 1930, 1931, 1932, 1933, 1935, 1936, 1937]

### Verbatim printed entry text (OCR)

**Version `col1929-L58943.v` — printed in editions [1929, 1930, 1931, 1932, 1933, 1935, 1936, 1937]:**

> CAMERON, KATHERINE ROSS, M.B.E. (1926).—Nursing sister, Basutoland, 1911; ag. matron, 1914; nursing sister, Nyassaland, 1919; matron, 1923.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1911 | Nursing sister | Basutoland | [1929, 1930, 1931, 1932, 1933, 1935, 1936, 1937] |
| 1 | 1914 | ag. matron | Basutoland *(inherited from previous clause)* | [1929, 1930, 1931, 1932, 1933, 1935, 1936, 1937] |
| 2 | 1919 | nursing sister, Nyassaland | Basutoland *(inherited from previous clause)* | [1929, 1930, 1931, 1932, 1933, 1935, 1936, 1937] |
| 3 | 1923 | matron | Basutoland *(inherited from previous clause)* | [1929, 1930, 1931, 1932, 1933, 1935, 1936, 1937] |

## Candidate stint `Cameron, K. R___Nyasaland___1921`

- Staff-list name: **Cameron, K. R** | colony: **Nyasaland** | listed 1921–1936 | editions [1921, 1922, 1923, 1924, 1925, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | K. R. Cameron | Nurse | Medical Department | — | — |
| 1922 | K. R. Cameron | Nurse | Medical Department | — | — |
| 1923 | K. R. Cameron | Nurse | Medical Department | — | — |
| 1924 | K. R. Cameron | Matron | Medical Department | — | — |
| 1925 | K. R. Cameron | Matron | Medical Department | — | — |
| 1928 | K. R. Cameron | Matron | Medical | — | — |
| 1929 | K. R. Cameron | Matron | Medical | — | — |
| 1930 | K. R. Cameron | Matron | Medical | — | — |
| 1931 | K. R. Cameron | Matron | Nurses | — | — |
| 1932 | K. R. Cameron | Matron | Medical | — | — |
| 1933 | K. R. Cameron | Matron | Medical | — | — |
| 1934 | K. R. Cameron | Matron | Medical | — | — |
| 1936 | K. R. Cameron | Nurses—Matron | Medical | — | — |

### Deterministic checks: `cameron_katherine-ross_e1911` vs `Cameron, K. R___Nyasaland___1921`

- [PASS] surname_gate: bio 'CAMERON' vs stint 'Cameron, K. R' (exact)
- [PASS] initials: bio ['K', 'R'] ~ stint ['K', 'R']
- [PASS] age_gate: stint starts 1921; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Nyasaland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1921-1936
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Cameron, K___Zanzibar___1929`

- Staff-list name: **Cameron, K** | colony: **Zanzibar** | listed 1929–1930 | editions [1929, 1930]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | K. Cameron | Nursing Sister | Medical Department | — | — |
| 1930 | K. Cameron | Nursing Sister | Medical Department | — | — |

### Deterministic checks: `cameron_katherine-ross_e1911` vs `Cameron, K___Zanzibar___1929`

- [PASS] surname_gate: bio 'CAMERON' vs stint 'Cameron, K' (exact)
- [PASS] initials: bio ['K', 'R'] ~ stint ['K']
- [PASS] age_gate: stint starts 1929; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Zanzibar'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1929-1930
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

