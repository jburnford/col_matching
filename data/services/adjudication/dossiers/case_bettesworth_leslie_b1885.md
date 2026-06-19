<!-- {"case_id": "case_bettesworth_leslie_b1885", "bio_ids": ["bettesworth_leslie_b1885"], "stint_ids": ["Bettesworth, L___Gold Coast___1915"]} -->
# Dossier case_bettesworth_leslie_b1885

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['bettesworth_leslie_b1885'] carry a single initial only — the namesake trap applies.

## Biography `bettesworth_leslie_b1885`

- Printed name: **BETTESWORTH, Leslie**
- Birth year: 1885 (attested in editions [1930, 1931, 1932])
- Appears in editions: [1930, 1931, 1932]

### Verbatim printed entry text (OCR)

**Version `col1930-L62570.v` — printed in editions [1930, 1931, 1932]:**

> BETTESWORTH, Leslie.—B. 1885; Imp. post office, July, 1901; dist. survr., posts and tels., Gold Coast, Oct., 1913; Togoland Field Force, 1914-15; senr. survr., July, 1917; survr., posts and tels. dept., Nigeria, Dec., 1918; senr. survr., Oct., 1920; dep. P.M.G., Apr., 1921.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1901 | Imp. post office | — | [1930, 1931, 1932] |
| 1 | 1913 | dist. survr., posts and tels. | Gold Coast | [1930, 1931, 1932] |
| 2 | 1914–1915 | Togoland Field Force | Togoland | [1930, 1931, 1932] |
| 3 | 1917 | senr. survr | Togoland *(inherited from previous clause)* | [1930, 1931, 1932] |
| 4 | 1918 | survr., posts and tels. dept. | Nigeria | [1930, 1931, 1932] |
| 5 | 1920 | senr. survr | Nigeria *(inherited from previous clause)* | [1930, 1931, 1932] |
| 6 | 1921 | dep. P.M.G | Nigeria *(inherited from previous clause)* | [1930, 1931, 1932] |

## Candidate stint `Bettesworth, L___Gold Coast___1915`

- Staff-list name: **Bettesworth, L** | colony: **Gold Coast** | listed 1915–1919 | editions [1915, 1917, 1918, 1919]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1915 | L. Bettesworth | First Grade District Surveyors | Post and Telegraph Department | — | — |
| 1917 | L. Bettesworth | First Grade District Surveyors | Post and Telegraph Department | — | — |
| 1918 | L. Bettesworth | First Grade District Surveyor | Post and Telegraph Department | — | — |
| 1919 | L. Bettesworth | First Grade District Surveyors | Post and Telegraph Department | — | — |

### Deterministic checks: `bettesworth_leslie_b1885` vs `Bettesworth, L___Gold Coast___1915`

- [PASS] surname_gate: bio 'BETTESWORTH' vs stint 'Bettesworth, L' (exact)
- [PASS] initials: bio ['L'] ~ stint ['L']
- [PASS] age_gate: stint starts 1915, birth 1885 (age 30)
- [PASS] colony: 1 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1915-1919
- [FAIL] position_sim: best 51 vs bar 60: 'dist. survr., posts and tels.' ~ 'First Grade District Surveyors'
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

