<!-- {"case_id": "case_buttress_eric-frank_b1905", "bio_ids": ["buttress_eric-frank_b1905"], "stint_ids": ["Buttriss, E. F___Hong Kong___1937"]} -->
# Dossier case_buttress_eric-frank_b1905

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `buttress_eric-frank_b1905`

- Printed name: **BUTTRESS, ERIC FRANK**
- Birth year: 1905 (attested in editions [1940])
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L62871.v` — printed in editions [1940]:**

> BUTTRESS, ERIC FRANK, B.Sc. (Eng.), Lond., Dip. Eng., King's Coll., A.M.Inat.C.E., Chartd. Civ. Engrn.—B. 1905; ed. County Schl., Windsor and King's Coll., Lond. Univ.; engrnr., P.W.D., Hong Kong, 1929.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | engrnr., P.W.D. | Hong Kong | [1940] |

## Candidate stint `Buttriss, E. F___Hong Kong___1937`

- Staff-list name: **Buttriss, E. F** | colony: **Hong Kong** | listed 1937–1940 | editions [1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1937 | E. F. Buttriss | Engineer | Public Works Department | — | — |
| 1939 | E. F. Buttriss | Engineer | Public Works Department | — | — |
| 1940 | E. F. Buttriss | Engineers | Public Works Department | — | — |

### Deterministic checks: `buttress_eric-frank_b1905` vs `Buttriss, E. F___Hong Kong___1937`

- [PASS] surname_gate: bio 'BUTTRESS' vs stint 'Buttriss, E. F' (fuzzy:1)
- [PASS] initials: bio ['E', 'F'] ~ stint ['E', 'F']
- [PASS] age_gate: stint starts 1937, birth 1905 (age 32)
- [PASS] colony: 1 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1937-1940
- [FAIL] position_sim: best 56 vs bar 60: 'engrnr., P.W.D.' ~ 'Engineer'
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

