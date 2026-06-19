<!-- {"case_id": "case_owen_bernard-george_b1903", "bio_ids": ["owen_bernard-george_b1903"], "stint_ids": ["Owen, B. G___Nigeria___1934"]} -->
# Dossier case_owen_bernard-george_b1903

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 58 official(s) with this surname in the graph's staff lists; 26 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `owen_bernard-george_b1903`

- Printed name: **OWEN, Bernard George**
- Birth year: 1903 (attested in editions [1948, 1949, 1950])
- Appears in editions: [1948, 1949, 1950]

### Verbatim printed entry text (OCR)

**Version `col1948-L35070.v` — printed in editions [1948, 1949, 1950]:**

> OWEN, Bernard George, M.A. (Cantab.).—b. 1903; ed. Berkhamstead Sch. and Camb. Univ. (1st cl. in finals, dip. in agric., Camb.) ; supt., agric., Nig., 1926; senr. agric. offr., 1938; asst. dir., agric. (prod. insp.), Nig., 1947; visited Ken., 1942 and U.K., 1943-44 in connection with dehydration of foods.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | supt., agric. | Nigeria | [1948, 1949, 1950] |
| 1 | 1938 | senr. agric. offr. | — | [1948, 1949, 1950] |
| 2 | 1942–1944 | — | — | [1948, 1949, 1950] |
| 3 | 1947 | asst. dir., agric. (prod. insp.) | Nigeria | [1948, 1949, 1950] |

## Candidate stint `Owen, B. G___Nigeria___1934`

- Staff-list name: **Owen, B. G** | colony: **Nigeria** | listed 1934–1939 | editions [1934, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | B. G. Owen | Superintendents | Agriculture | — | — |
| 1939 | B. G. Owen | Senior Agricultural Officers | Agriculture | — | — |

### Deterministic checks: `owen_bernard-george_b1903` vs `Owen, B. G___Nigeria___1934`

- [PASS] surname_gate: bio 'OWEN' vs stint 'Owen, B. G' (exact)
- [PASS] initials: bio ['B', 'G'] ~ stint ['B', 'G']
- [PASS] age_gate: stint starts 1934, birth 1903 (age 31)
- [PASS] colony: 2 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1934-1939
- [FAIL] position_sim: best 37 vs bar 60: 'supt., agric.' ~ 'Senior Agricultural Officers'
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

