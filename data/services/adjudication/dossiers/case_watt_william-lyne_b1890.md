<!-- {"case_id": "case_watt_william-lyne_b1890", "bio_ids": ["watt_william-lyne_b1890"], "stint_ids": ["Watt, W. L___Kenya___1931"]} -->
# Dossier case_watt_william-lyne_b1890

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 39 official(s) with this surname in the graph's staff lists; 20 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `watt_william-lyne_b1890`

- Printed name: **WATT, William Lyne**
- Birth year: 1890 (attested in editions [1948, 1949, 1950])
- Honours: M.B.E
- Appears in editions: [1948, 1949, 1950]

### Verbatim printed entry text (OCR)

**Version `col1948-L36718.v` — printed in editions [1948, 1949, 1950]:**

> WATT, William Lyne, M.B.E.—b. 1890; ed. Robert Gordon's, Aberdeen, Marishall Coll., Aberdeen Univ. and Eberswalde Forest Coll., Germany; on war serv., 1914-18, flt.-lieut.; agric. supervisor, Ken., 1923; senr. agric. offr., 1937; agrarian dev. offr., 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1923 | agric. supervisor | Kenya | [1948, 1949, 1950] |
| 1 | 1937 | senr. agric. offr | Kenya *(inherited from previous clause)* | [1948, 1949, 1950] |
| 2 | 1947 | agrarian dev. offr | Kenya *(inherited from previous clause)* | [1948, 1949, 1950] |

## Candidate stint `Watt, W. L___Kenya___1931`

- Staff-list name: **Watt, W. L** | colony: **Kenya** | listed 1931–1940 | editions [1931, 1932, 1934, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | W. L. Watt | Agricultural Officer | Division of Native Agriculture | — | — |
| 1932 | W. L. Watt | Agricultural Officer | Sub-Division of Native Agriculture | — | — |
| 1934 | W. L. Watt | Agricultural Officers | Sub-Division of Native Agriculture | — | — |
| 1937 | W. L. Watt | Agricultural Officers | Sub-Division of Native Agriculture | — | — |
| 1939 | W. L. Watt | Senior Agricultural Officer | Agricultural Department | — | — |
| 1940 | W. L. Watt | Senior Agricultural Officer | Agricultural Department | — | — |

### Deterministic checks: `watt_william-lyne_b1890` vs `Watt, W. L___Kenya___1931`

- [PASS] surname_gate: bio 'WATT' vs stint 'Watt, W. L' (exact)
- [PASS] initials: bio ['W', 'L'] ~ stint ['W', 'L']
- [PASS] age_gate: stint starts 1931, birth 1890 (age 41)
- [PASS] colony: 3 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1931-1940
- [PASS] position_sim: best 71 vs bar 60: 'senr. agric. offr' ~ 'Senior Agricultural Officer'
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

