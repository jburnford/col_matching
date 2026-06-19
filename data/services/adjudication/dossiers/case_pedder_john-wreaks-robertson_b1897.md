<!-- {"case_id": "case_pedder_john-wreaks-robertson_b1897", "bio_ids": ["pedder_john-wreaks-robertson_b1897"], "stint_ids": ["Pedder, J. W. R___Nigeria___1934"]} -->
# Dossier case_pedder_john-wreaks-robertson_b1897

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `pedder_john-wreaks-robertson_b1897`

- Printed name: **PEDDER, John Wreaks Robertson**
- Birth year: 1897 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L35177.v` — printed in editions [1948, 1949, 1950, 1951]:**

> PEDDER, John Wreaks Robertson.—b. 1897; ed. Calday Gram. Sch., Holmes Chapel Agric. Coll. (dip.), and Reading Univ.; on mil. serv., 1915-19; supt., agric., Nig., 1924; senr. agric. offr., 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1924 | supt., agric. | Nigeria | [1948, 1949, 1950, 1951] |
| 1 | 1938 | senr. agric. offr | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Pedder, J. W. R___Nigeria___1934`

- Staff-list name: **Pedder, J. W. R** | colony: **Nigeria** | listed 1934–1939 | editions [1934, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | J. W. R. Pedder | Superintendents | Agriculture | — | — |
| 1939 | J. W. R. Pedder | Senior Agricultural Officers | Agriculture | — | — |

### Deterministic checks: `pedder_john-wreaks-robertson_b1897` vs `Pedder, J. W. R___Nigeria___1934`

- [PASS] surname_gate: bio 'PEDDER' vs stint 'Pedder, J. W. R' (exact)
- [PASS] initials: bio ['J', 'W', 'R'] ~ stint ['J', 'W', 'R']
- [PASS] age_gate: stint starts 1934, birth 1897 (age 37)
- [PASS] colony: 2 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1934-1939
- [PASS] position_sim: best 70 vs bar 60: 'senr. agric. offr' ~ 'Senior Agricultural Officers'
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

