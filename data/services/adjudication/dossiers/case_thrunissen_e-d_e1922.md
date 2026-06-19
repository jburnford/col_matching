<!-- {"case_id": "case_thrunissen_e-d_e1922", "bio_ids": ["thrunissen_e-d_e1922"], "stint_ids": ["Thennissen, E. D___Kenya___1914", "Theunissen, E. D___Kenya___1917"]} -->
# Dossier case_thrunissen_e-d_e1922

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Theunissen, E. D___Kenya___1917` is also gate-compatible with biography(ies) outside this case: ['theunissen_e-d_e1922'] (already linked elsewhere or filtered).

## Biography `thrunissen_e-d_e1922`

- Printed name: **THRUNISSEN, E. D**
- Birth year: not printed
- Appears in editions: [1931, 1936]

### Verbatim printed entry text (OCR)

**Version `col1931-L68618.v` — printed in editions [1931, 1936]:**

> THRUNISSEN, E. D.—Asst. supt. pol., Kenya, Nov., 1922.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1922 | Asst. supt. pol. | Kenya | [1931, 1936] |

## Candidate stint `Thennissen, E. D___Kenya___1914`

- Staff-list name: **Thennissen, E. D** | colony: **Kenya** | listed 1914–1915 | editions [1914, 1915]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1914 | E. D. Thennissen | Assistant Inspector | Police | — | — |
| 1915 | E. D. Thennissen | Assistant Inspector | Police | — | — |

### Deterministic checks: `thrunissen_e-d_e1922` vs `Thennissen, E. D___Kenya___1914`

- [PASS] surname_gate: bio 'THRUNISSEN' vs stint 'Thennissen, E. D' (fuzzy:2)
- [PASS] initials: bio ['E', 'D'] ~ stint ['E', 'D']
- [PASS] age_gate: stint starts 1914; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1914-1915
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Theunissen, E. D___Kenya___1917`

- Staff-list name: **Theunissen, E. D** | colony: **Kenya** | listed 1917–1934 | editions [1917, 1918, 1920, 1922, 1923, 1924, 1925, 1928, 1930, 1932, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1917 | E. D. Theunissen | Inspectors | Police | — | — |
| 1918 | E. D. Theunissen | Inspectors | Police | — | — |
| 1920 | E. D. Theunissen | Inspector | Police | — | — |
| 1922 | E. D. Theunissen | Inspector | Police | — | — |
| 1923 | E. D. Theunissen | Inspector | Police | — | — |
| 1924 | E. D. Theunissen | Assistant Superintendent | Police | — | — |
| 1925 | E. D. Theunissen | Assistant Superintendent | Police Department | — | — |
| 1928 | E. D. Theunissen | Assistant Superintendent | Police Department | — | — |
| 1930 | E. D. Theunissen | Superintendent | Police Department | — | — |
| 1932 | E. D. Theunissen | Superintendent | Police Department | — | — |
| 1934 | E. D. Theunissen | Superintendent | Police Department | — | — |

### Deterministic checks: `thrunissen_e-d_e1922` vs `Theunissen, E. D___Kenya___1917`

- [PASS] surname_gate: bio 'THRUNISSEN' vs stint 'Theunissen, E. D' (fuzzy:1)
- [PASS] initials: bio ['E', 'D'] ~ stint ['E', 'D']
- [PASS] age_gate: stint starts 1917; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1917-1934
- [FAIL] position_sim: best 49 vs bar 60: 'Asst. supt. pol.' ~ 'Assistant Superintendent'
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

