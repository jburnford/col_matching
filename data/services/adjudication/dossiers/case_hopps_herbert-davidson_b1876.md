<!-- {"case_id": "case_hopps_herbert-davidson_b1876", "bio_ids": ["hopps_herbert-davidson_b1876"], "stint_ids": ["Hopps, H. D___Tanganyika___1921"]} -->
# Dossier case_hopps_herbert-davidson_b1876

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hopps_herbert-davidson_b1876`

- Printed name: **HOPPS, HERBERT DAVIDSON**
- Birth year: 1876 (attested in editions [1929, 1930, 1931])
- Appears in editions: [1929, 1930, 1931]

### Verbatim printed entry text (OCR)

**Version `col1929-L61171.v` — printed in editions [1929, 1930, 1931]:**

> HOPPS, HERBERT DAVIDSON.—B. 1876; asst. foreman, Indian State Rly., 1903; foreman, 1919; E. African Forces, 1914-19; asst. loco. supt., Tanganyika Rlys., Oct., 1919.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1903 | asst. foreman, Indian State Rly | — | [1929, 1930, 1931] |
| 1 | 1914–1919 | E. African Forces | — | [1929, 1930, 1931] |
| 2 | 1919 | foreman | — | [1929, 1930, 1931] |
| 3 | 1919 | asst. loco. supt., Tanganyika Rlys | Tanganyika | [1929, 1930, 1931] |

## Candidate stint `Hopps, H. D___Tanganyika___1921`

- Staff-list name: **Hopps, H. D** | colony: **Tanganyika** | listed 1921–1925 | editions [1921, 1922, 1923, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | H. D. Hopps | Assistant Locomotive Superintendents | Railways | — | — |
| 1922 | H. D. Hopps | Assistant Locomotive Superintendents | Railways | — | — |
| 1923 | H. D. Hopps | Assistant Locomotive Superintendents | Railways | — | — |
| 1925 | H. D. Hopps | Assistant Locomotive Superintendents | Railways | — | — |

### Deterministic checks: `hopps_herbert-davidson_b1876` vs `Hopps, H. D___Tanganyika___1921`

- [PASS] surname_gate: bio 'HOPPS' vs stint 'Hopps, H. D' (exact)
- [PASS] initials: bio ['H', 'D'] ~ stint ['H', 'D']
- [PASS] age_gate: stint starts 1921, birth 1876 (age 45)
- [PASS] colony: 1 placed event(s) resolve to 'Tanganyika'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1921-1925
- [FAIL] position_sim: best 48 vs bar 60: 'asst. loco. supt., Tanganyika Rlys' ~ 'Assistant Locomotive Superintendents'
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

