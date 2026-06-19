<!-- {"case_id": "case_richmond_ernest-tatham_e1874", "bio_ids": ["richmond_ernest-tatham_e1874"], "stint_ids": ["Richmond, E. T___Palestine___1928"]} -->
# Dossier case_richmond_ernest-tatham_e1874

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 16 official(s) with this surname in the graph's staff lists; 11 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `richmond_ernest-tatham_e1874`

- Printed name: **RICHMOND, ERNEST TATHAM**
- Birth year: not printed
- Honours: F.R.I.B.A
- Appears in editions: [1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1936-L64053.v` — printed in editions [1936, 1937, 1939, 1940]:**

> RICHMOND, ERNEST TATHAM, F.R.I.B.A.—B.; 1874; ed. High Croft Schl., Clifton Coll., Bristol, Architectural Schl., Westminster and R. Acad. Architectural Schl.; archt. to pub. wks., miny., Egypt, 1900; subsequently dir.-gen. state bldgs. dept.; attld., dept. of fortif., and wks., W.O., Dec., 1914—Oct., 1916; in ch., grenade sec., trench warfare dept., miny. of munitions, Mar., 1917; lieut., R.N.V.R., Mar., 1917; archt. attd. to war graves serv., France, 1918-19; asst. civ. sec., Palestine, 1920; dir., antiquities, 1927.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1874 | — | — | [1936, 1937, 1939, 1940] |
| 1 | 1900 | archt. to pub. wks., miny., Egypt | — | [1936, 1937, 1939, 1940] |
| 2 | 1914–1916 | attld., dept. of fortif., and wks., W.O | — | [1936, 1937, 1939, 1940] |
| 3 | 1917 | in ch., grenade sec., trench warfare dept., miny. of munitions | — | [1936, 1937, 1939, 1940] |
| 4 | 1917 | lieut., R.N.V.R | — | [1936, 1937, 1939, 1940] |
| 5 | 1918–1919 | archt. attd. to war graves serv., France | — | [1936, 1937, 1939, 1940] |
| 6 | 1920 | asst. civ. sec. | Palestine | [1936, 1937, 1939, 1940] |
| 7 | 1927 | dir., antiquities | Palestine *(inherited from previous clause)* | [1936, 1937, 1939, 1940] |

## Candidate stint `Richmond, E. T___Palestine___1928`

- Staff-list name: **Richmond, E. T** | colony: **Palestine** | listed 1928–1932 | editions [1928, 1929, 1930, 1931, 1932]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1928 | E. T. Richmond | Director | Department of Antiquities | — | — |
| 1929 | E. T. Richmond | Director | Department of Antiquities | — | — |
| 1930 | E. T. Richmond | Director | Department of Antiquities | — | — |
| 1931 | E. T. Richmond | Director | Department of Antiquities | — | — |
| 1932 | E. T. Richmond | Director | Department of Antiquities | — | — |

### Deterministic checks: `richmond_ernest-tatham_e1874` vs `Richmond, E. T___Palestine___1928`

- [PASS] surname_gate: bio 'RICHMOND' vs stint 'Richmond, E. T' (exact)
- [PASS] initials: bio ['E', 'T'] ~ stint ['E', 'T']
- [PASS] age_gate: stint starts 1928; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Palestine'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1928-1932
- [FAIL] position_sim: best 30 vs bar 60: 'asst. civ. sec.' ~ 'Director'
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

