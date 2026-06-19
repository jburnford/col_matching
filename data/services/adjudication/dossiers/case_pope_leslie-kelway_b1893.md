<!-- {"case_id": "case_pope_leslie-kelway_b1893", "bio_ids": ["pope_leslie-kelway_b1893"], "stint_ids": ["Pope, L. K___Palestine___1927"]} -->
# Dossier case_pope_leslie-kelway_b1893

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 35 official(s) with this surname in the graph's staff lists; 12 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `pope_leslie-kelway_b1893`

- Printed name: **POPE, Leslie Kelway**
- Birth year: 1893 (attested in editions [1948, 1949, 1950])
- Appears in editions: [1948, 1949, 1950]

### Verbatim printed entry text (OCR)

**Version `col1948-L35281.v` — printed in editions [1948, 1949, 1950]:**

> POPE, Leslie Kelway, M.B.E. (Civ.).—b. 1893; on mil. serv. 1914-18, capt. (desps. twice); constable, gendarmerie, Pal., 1922; off. survr., gr. v. (senr. surv.), dept. of customs, excise and trade, 1926; port offr., Jaffa, and asst. collct., 1929; port man., 1934.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1922 | constable, gendarmerie | Palestine | [1948, 1949, 1950] |
| 1 | 1926 | off. survr., gr. v. (senr. surv.), dept. of customs, excise and trade | Palestine *(inherited from previous clause)* | [1948, 1949, 1950] |
| 2 | 1929 | port offr., Jaffa, and asst. collct | Palestine *(inherited from previous clause)* | [1948, 1949, 1950] |
| 3 | 1934 | port man | Palestine *(inherited from previous clause)* | [1948, 1949, 1950] |

## Candidate stint `Pope, L. K___Palestine___1927`

- Staff-list name: **Pope, L. K** | colony: **Palestine** | listed 1927–1940 | editions [1927, 1928, 1929, 1930, 1931, 1932, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | L. K. Pope | Office Surveyor | Customs, Excise and Trade | — | — |
| 1928 | L. K. Pope | Office Surveyor | Department of Customs, Excise and Trade. | — | — |
| 1929 | L. K. Pope | Office Surveyor | Department of Customs, Excise and Trade | — | — |
| 1930 | L. K. Pope | Port Officers | Department of Customs, Excise and Trade. | — | — |
| 1931 | L. K. Pope | Port Officers | Department of Customs, Excise and Trade | — | — |
| 1932 | L. K. Pope | Port Officers | Department of Customs, Excise and Trade. | — | — |
| 1940 | L. K. Pope | Port Manager | Department of Customs, Excise and Trade. | — | — |

### Deterministic checks: `pope_leslie-kelway_b1893` vs `Pope, L. K___Palestine___1927`

- [PASS] surname_gate: bio 'POPE' vs stint 'Pope, L. K' (exact)
- [PASS] initials: bio ['L', 'K'] ~ stint ['L', 'K']
- [PASS] age_gate: stint starts 1927, birth 1893 (age 34)
- [PASS] colony: 4 placed event(s) resolve to 'Palestine'
- [PASS] tenure_overlap: 4 event tenure(s) overlap stint years 1927-1940
- [PASS] position_sim: best 80 vs bar 60: 'port man' ~ 'Port Manager'
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

