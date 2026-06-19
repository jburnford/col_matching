<!-- {"case_id": "case_nicholas_s_e1864", "bio_ids": ["nicholas_s_e1864"], "stint_ids": ["Nicholas, J. S___Ceylon___1917", "Nicholas, J. S___Ceylon___1931"]} -->
# Dossier case_nicholas_s_e1864

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 15 official(s) with this surname in the graph's staff lists; 11 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['nicholas_s_e1864'] carry a single initial only — the namesake trap applies.

## Biography `nicholas_s_e1864`

- Printed name: **NICHOLAS, S**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L28859.v` — printed in editions [1883]:**

> NICHOLAS, Rev. S.—Portuguese colonial chaplain, Colombo, Ceylon, 1864.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1864 | Portuguese colonial chaplain, Colombo | Ceylon | [1883] |

## Candidate stint `Nicholas, J. S___Ceylon___1917`

- Staff-list name: **Nicholas, J. S** | colony: **Ceylon** | listed 1917–1927 | editions [1917, 1918, 1919, 1920, 1921, 1922, 1923, 1925, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1917 | J. S. Nicholas | Assistant Superintendents | Excise Department | — | — |
| 1918 | J. S. Nicholas | Assistant Superintendent | Excise Department | — | — |
| 1919 | J. S. Nicholas | Assistant Superintendent | Excise Department | — | — |
| 1920 | J. S. Nicholas | Assistant Superintendent | Excise Department | — | — |
| 1921 | J. S. Nicholas | Assistant Superintendent | Excise Department | — | — |
| 1922 | J. S. Nicholas | Assistant Superintendent | Excise Department | — | — |
| 1923 | J. S. Nicholas | Assistant Superintendent | Excise Department | — | — |
| 1925 | J. S. Nicholas | Assistant Superintendent | Excise Department | — | — |
| 1927 | J. S. Nicholas | Assistant Superintendent | Excise Department | — | — |

### Deterministic checks: `nicholas_s_e1864` vs `Nicholas, J. S___Ceylon___1917`

- [PASS] surname_gate: bio 'NICHOLAS' vs stint 'Nicholas, J. S' (exact)
- [PASS] initials: bio ['S'] ~ stint ['J', 'S']
- [PASS] age_gate: stint starts 1917; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1917-1927
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Nicholas, J. S___Ceylon___1931`

- Staff-list name: **Nicholas, J. S** | colony: **Ceylon** | listed 1931–1940 | editions [1931, 1934, 1936, 1937, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | J. S. Nicholas | Superintendent | Excise Department | — | — |
| 1934 | J. S. Nicholas | Assistant Commissioner, Northern Division | Excise Department | — | — |
| 1936 | J. S. Nicholas | Assistant Commissioner, Northern Division | Excise Department | — | — |
| 1937 | J. S. Nicholas | Assistant Commissioner, Northern Division | Excise Department | — | — |
| 1940 | J. S. Nicholas | Assistant Commissioner, Central Division | Excise Department | — | — |

### Deterministic checks: `nicholas_s_e1864` vs `Nicholas, J. S___Ceylon___1931`

- [PASS] surname_gate: bio 'NICHOLAS' vs stint 'Nicholas, J. S' (exact)
- [PASS] initials: bio ['S'] ~ stint ['J', 'S']
- [PASS] age_gate: stint starts 1931; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1940
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

