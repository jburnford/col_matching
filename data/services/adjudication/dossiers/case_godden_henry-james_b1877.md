<!-- {"case_id": "case_godden_henry-james_b1877", "bio_ids": ["godden_henry-james_b1877"], "stint_ids": ["Godden, J___Newfoundland___1894"]} -->
# Dossier case_godden_henry-james_b1877

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `godden_henry-james_b1877`

- Printed name: **GODDEN, HENRY JAMES**
- Birth year: 1877 (attested in editions [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939])
- Honours: M.B.E (1929)
- Appears in editions: [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939]

### Verbatim printed entry text (OCR)

**Version `col1927-L59226.v` — printed in editions [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939]:**

> GODDEN, HENRY JAMES, M.B.E. (1929)—B. 1877; telegraphist, Basutoland, 1902; postmr., 1907; clk. to astt. comnrs., 1917; ag. astt. comnrs., 1922; passed 1st grade Sesuto, 1922; ch. clk., mast. of st. and regnr., 1924.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1902 | telegraphist | Basutoland | [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939] |
| 1 | 1907 | postmr | Basutoland *(inherited from previous clause)* | [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939] |
| 2 | 1917 | clk. to astt. comnrs | Basutoland *(inherited from previous clause)* | [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939] |
| 3 | 1922 | ag. astt. comnrs | Basutoland *(inherited from previous clause)* | [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939] |
| 4 | 1924 | ch. clk., mast. of st. and regnr | Basutoland *(inherited from previous clause)* | [1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939] |

## Candidate stint `Godden, J___Newfoundland___1894`

- Staff-list name: **Godden, J** | colony: **Newfoundland** | listed 1894–1899 | editions [1894, 1896, 1897, 1898, 1899]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | J. Godden | Sub-Collector | Civil Establishment | — | — |
| 1896 | J. Godden | Sub-Collector | Civil Establishment | — | — |
| 1897 | J. Godden | Sub-Collector | Civil Establishment | — | — |
| 1898 | J. Godden | Sub-Collector | Civil Establishment | — | — |
| 1899 | J. Godden | Sub-Collector | — | — | — |

### Deterministic checks: `godden_henry-james_b1877` vs `Godden, J___Newfoundland___1894`

- [PASS] surname_gate: bio 'GODDEN' vs stint 'Godden, J' (exact)
- [PASS] initials: bio ['H', 'J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1894, birth 1877 (age 17)
- [FAIL] colony: no placed event resolves to 'Newfoundland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1894-1899
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

