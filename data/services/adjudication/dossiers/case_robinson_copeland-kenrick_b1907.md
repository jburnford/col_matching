<!-- {"case_id": "case_robinson_copeland-kenrick_b1907", "bio_ids": ["robinson_copeland-kenrick_b1907"], "stint_ids": ["Robinson, C. K___Windward Islands___1936"]} -->
# Dossier case_robinson_copeland-kenrick_b1907

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 136 official(s) with this surname in the graph's staff lists; 56 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `robinson_copeland-kenrick_b1907`

- Printed name: **ROBINSON, Copeland Kenrick**
- Birth year: 1907 (attested in editions [1949, 1950, 1951])
- Honours: M.B.E. D.I.C.T.A
- Appears in editions: [1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1949-L35306.v` — printed in editions [1949, 1950, 1951]:**

> ROBINSON, Copeland Kenrick, M.B.E. D.I.C.T.A., M.S. (U.S.A.).—b. 1907; ed. Queen's Royal Coll. and I.C.T.A., postgrad. course in agric. econ. at Cornell Univ., U.S.A.; agric. asst., St. V., 1934; supt., agric., registr., agric. credit socs. and chmn., comtee. of management. govt. cotton ginnery, 1938; dep. chmn., land settlement and dev. bd., 1945; prov. M.E.C., St. V., 1939-45; contrlr. of supplies, 1939-42; St. V. rep. at supplies conf., Washington, 1943; advsr. Anglo-Caribbean conf., Barb., 1944; M.E.C., St. V., 1947; jt. author of *The Agricultural Soils of St. Vincent.*

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1934 | agric. asst. | St. Vincent | [1949, 1950, 1951] |
| 1 | 1938 | supt., agric., registr., agric. credit socs. and chmn., comtee. of management. govt. cotton ginnery | St. Vincent *(inherited from previous clause)* | [1949, 1950, 1951] |
| 2 | 1939–1945 | prov. M.E.C. | St. Vincent | [1949, 1950, 1951] |
| 3 | 1943 | St. V. rep. at supplies conf., Washington | St. Vincent *(inherited from previous clause)* | [1949, 1950, 1951] |
| 4 | 1944 | advsr. Anglo-Caribbean conf. | Barbados | [1949, 1950, 1951] |
| 5 | 1945 | dep. chmn., land settlement and dev. bd | St. Vincent *(inherited from previous clause)* | [1949, 1950, 1951] |
| 6 | 1947 | M.E.C. | St. Vincent | [1949, 1950, 1951] |

## Candidate stint `Robinson, C. K___Windward Islands___1936`

- Staff-list name: **Robinson, C. K** | colony: **Windward Islands** | listed 1936–1948 | editions [1936, 1937, 1939, 1948]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | C. K. Robinson | Agricultural Assistant | Agricultural Department | — | — |
| 1937 | C. K. Robinson | Agricultural Assistant | Agricultural Department | — | — |
| 1939 | C. K. Robinson | Agricultural Superintendent | Agricultural Department | — | — |
| 1948 | C. K. Robinson | Executive Council Member | Executive Council | — | — |

### Deterministic checks: `robinson_copeland-kenrick_b1907` vs `Robinson, C. K___Windward Islands___1936`

- [PASS] surname_gate: bio 'ROBINSON' vs stint 'Robinson, C. K' (exact)
- [PASS] initials: bio ['C', 'K'] ~ stint ['C', 'K']
- [PASS] age_gate: stint starts 1936, birth 1907 (age 29)
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1936-1948
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

