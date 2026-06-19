<!-- {"case_id": "case_rainford_r-f_e1914", "bio_ids": ["rainford_r-f_e1914"], "stint_ids": ["Rainford, R. F___Kenya___1917", "Rainford, R. F___Kenya___1930"]} -->
# Dossier case_rainford_r-f_e1914

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `rainford_r-f_e1914`

- Printed name: **RAINFORD, R. F**
- Birth year: not printed
- Appears in editions: [1921]

### Verbatim printed entry text (OCR)

**Version `col1921-L59366.v` — printed in editions [1921]:**

> RAINFORD, R. F.—Ast. supt. of police, E.A.P., Apr., 1914.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914 | Ast. supt. of police | East Africa Protectorate | [1921] |

## Candidate stint `Rainford, R. F___Kenya___1917`

- Staff-list name: **Rainford, R. F** | colony: **Kenya** | listed 1917–1918 | editions [1917, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1917 | R. F. Rainford | Assistant Superintendents | Police | — | — |
| 1918 | R. F. Rainford | Assistant Superintendents | Police | — | — |

### Deterministic checks: `rainford_r-f_e1914` vs `Rainford, R. F___Kenya___1917`

- [PASS] surname_gate: bio 'RAINFORD' vs stint 'Rainford, R. F' (exact)
- [PASS] initials: bio ['R', 'F'] ~ stint ['R', 'F']
- [PASS] age_gate: stint starts 1917; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1917-1918
- [FAIL] position_sim: best 37 vs bar 60: 'Ast. supt. of police' ~ 'Assistant Superintendents'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Rainford, R. F___Kenya___1930`

- Staff-list name: **Rainford, R. F** | colony: **Kenya** | listed 1930–1932 | editions [1930, 1932]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1930 | R. F. Rainford | Superintendent | Police Department | — | Captain |
| 1932 | R. F. Rainford | Superintendent | Police Department | — | Captain |

### Deterministic checks: `rainford_r-f_e1914` vs `Rainford, R. F___Kenya___1930`

- [PASS] surname_gate: bio 'RAINFORD' vs stint 'Rainford, R. F' (exact)
- [PASS] initials: bio ['R', 'F'] ~ stint ['R', 'F']
- [PASS] age_gate: stint starts 1930; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1930-1932
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

