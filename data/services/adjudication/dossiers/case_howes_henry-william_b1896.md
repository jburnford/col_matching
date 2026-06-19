<!-- {"case_id": "case_howes_henry-william_b1896", "bio_ids": ["howes_henry-william_b1896"], "stint_ids": ["Howes, H. W___British Honduras___1958", "Howes, H. W___Gibraltar___1948"]} -->
# Dossier case_howes_henry-william_b1896

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 13 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `howes_henry-william_b1896`

- Printed name: **HOWES, Henry William**
- Birth year: 1896 (attested in editions [1948])
- Honours: M.A, O.B.E
- Appears in editions: [1948, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L33476.v` — printed in editions [1948]:**

> HOWES, Henry William, M.A., M.Sc., Ph.D. (Lond.).—b. 1896; ed. Norwich, King Edward VI (Gram. Sch.), Univ. of London, Univ. of Wales, exhibtn. educ., travelling schol. in geog. with anthro., bd. of educ. teachers cert.; on mil. serv. 1915-17; ag. prin., N.W. Poly., London; prin., Norwich City Coll. and Sch. of Art; dir. of educ., Gib., 1944; pub. relations offr. since 1945 in addtn.; city coun., Gib., since 1945; mem. of comtees. and couns. on educ.; author of Spanish Folk Lore, Economic Geography of Spanish Galicia, Ocean Highways, Bruges Artistic Centre of Flanders, Anglo-Belgian Historical Relations, Anglo-Belgian Musical Relations, The Story of Gibraltar.

**Version `col1950-L36557.v` — printed in editions [1950, 1951]:**

> HOWES, Henry William, O.B.E., M.A., M.Sc., Ph.D. (Lond.), chev. of order of crown of Belgium, offr. d'academie (France), B. of E. teach. cert.—b. 1896; ed. Norwich King Edward VI Gram. Sch., Univs. of Lond. and Wales, exhibr., educ., trav. schol., geog. with anthrop.; on mil. serv., 1915–17; dir., educ., Gib., 1944; pub. rel. offr. in addn., 1945; author of Spanish Folk-lore (papers published by Folk-lore Society); Economic Geography of Spanish Galicia; Ocean Highways; Bruges, Artistic Centre of Flanders; Anglo-Belgian Historical Relations; Anglo-Belgian Musical Relations; The Story of Gibraltar.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915–1917 | on mil. serv. | — | [1948] |
| 1 | 1944 | dir. of educ. | Gibraltar | [1948, 1950, 1951] |
| 2 | 1945 | pub. relations offr. | — | [1948] |
| 3 | 1945 | city coun. | Gibraltar | [1948, 1950, 1951] |

## Candidate stint `Howes, H. W___British Honduras___1958`

- Staff-list name: **Howes, H. W** | colony: **British Honduras** | listed 1958–1960 | editions [1958, 1959, 1960]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1958 | H. W. Howes | Director of Education | Civil Establishment | — | — |
| 1959 | H. W. Howes | Director of Education | Civil Establishment | — | — |
| 1960 | H. W. Howes | Director of Education | Civil Establishment | — | — |

### Deterministic checks: `howes_henry-william_b1896` vs `Howes, H. W___British Honduras___1958`

- [PASS] surname_gate: bio 'HOWES' vs stint 'Howes, H. W' (exact)
- [PASS] initials: bio ['H', 'W'] ~ stint ['H', 'W']
- [PASS] age_gate: stint starts 1958, birth 1896 (age 62)
- [FAIL] colony: no placed event resolves to 'British Honduras'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1958-1960
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Howes, H. W___Gibraltar___1948`

- Staff-list name: **Howes, H. W** | colony: **Gibraltar** | listed 1948–1950 | editions [1948, 1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1948 | H. W. Howes | Director of Education | Colonial Government Representatives | — | — |
| 1949 | H. W. Howes | Director of Education | Education | — | — |
| 1950 | H. W. Howes | Director of Education | Education | — | — |

### Deterministic checks: `howes_henry-william_b1896` vs `Howes, H. W___Gibraltar___1948`

- [PASS] surname_gate: bio 'HOWES' vs stint 'Howes, H. W' (exact)
- [PASS] initials: bio ['H', 'W'] ~ stint ['H', 'W']
- [PASS] age_gate: stint starts 1948, birth 1896 (age 52)
- [PASS] colony: 2 placed event(s) resolve to 'Gibraltar'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1948-1950
- [FAIL] position_sim: best 40 vs bar 60: 'city coun.' ~ 'Director of Education'
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

