<!-- {"case_id": "case_leonard_james-weston_e1881", "bio_ids": ["leonard_james-weston_e1881"], "stint_ids": ["Leonard, James Weston___Cape of Good Hope___1883"]} -->
# Dossier case_leonard_james-weston_e1881

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 12 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- Phase 1 found `leonard_james-weston_e1881` ↔ `Leonard, James Weston___Cape of Good Hope___1883` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Leonard, James Weston___Cape of Good Hope___1883` is also gate-compatible with biography(ies) outside this case: ['leonard_j-w_e1882'] (already linked elsewhere or filtered).

## Biography `leonard_james-weston_e1881`

- Printed name: **LEONARD, JAMES WESTON**
- Birth year: not printed
- Terminal: resigned 1884 — “resigned, 1884.”
- Appears in editions: [1890, 1894, 1896, 1897]

### Verbatim printed entry text (OCR)

**Version `col1890-L35274.v` — printed in editions [1890, 1894, 1896, 1897]:**

> LEONARD, THE HON. JAMES WESTON—Att'y-gen., Cape of Good Hope, 1 July, 1882; member of leg. assembly, and of exec. council, 1881; Q.C.; resigned, 1884.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1881 | member of leg. assembly, and of exec. council | Cape of Good Hope *(inherited from previous clause)* | [1890, 1894, 1896, 1897] |
| 1 | 1882 | Att'y-gen. | Cape of Good Hope | [1890, 1894, 1896, 1897] |

## Candidate stint `Leonard, James Weston___Cape of Good Hope___1883`

- Staff-list name: **Leonard, James Weston** | colony: **Cape of Good Hope** | listed 1883–1889 | editions [1883, 1888, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1883 | J. W. Leonard | Member | Constituency | — | — |
| 1883 | J. W. Leonard | Attorney-General | Attorney-General's Office | — | — |
| 1888 | James Weston Leonard | Member | Constituency Members | — | — |
| 1889 | James Weston Leonard | — | Constituency | — | — |

### Deterministic checks: `leonard_james-weston_e1881` vs `Leonard, James Weston___Cape of Good Hope___1883`

- [PASS] surname_gate: bio 'LEONARD' vs stint 'Leonard, James Weston' (exact)
- [PASS] initials: bio ['J', 'W'] ~ stint ['J', 'W']
- [PASS] age_gate: stint starts 1883; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Cape of Good Hope'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1883-1889
- [PASS] position_sim: best 100 vs bar 60: 'member of leg. assembly, and of exec. council' ~ 'Member'
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

