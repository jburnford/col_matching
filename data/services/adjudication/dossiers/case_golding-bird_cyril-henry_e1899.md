<!-- {"case_id": "case_golding-bird_cyril-henry_e1899", "bio_ids": ["golding-bird_cyril-henry_e1899"], "stint_ids": ["Golding-Bird, C. H___Mauritius___1920"]} -->
# Dossier case_golding-bird_cyril-henry_e1899

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `golding-bird_cyril-henry_e1899`

- Printed name: **GOLDING-BIRD, CYRIL HENRY**
- Birth year: not printed
- Appears in editions: [1929, 1930, 1931]

### Verbatim printed entry text (OCR)

**Version `col1929-L60563.v` — printed in editions [1929, 1930, 1931]:**

> GOLDING-BIRD, CYRIL HENRY.—Ed. Merchant Taylor Schl. and Lincoln Coll. Oxford (Davenport Exhibnr.), M.A., D.D., hon. D.D. W. Univ. of Canada, hon. D.D., Trinity Coll., Dublin; curate, All Saints, Margaret St., 1899-1902; chaplain lst. Cavalry Brig., S. African F.F., 1900; vicar, St. Barnabas, Dover, 1902-07; dean and vicar-gen., Newcastle, N.S.W., 1908-14; S.C.F., A.I.F., 1914-15; S.C.F., C.M.F., 1915-19; bishop of Kalgoorlie, W.A., 1914-18; bishop of Mauritius, 1919.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1899–1902 | curate, All Saints, Margaret St | — | [1929, 1930, 1931] |
| 1 | 1900 | chaplain lst. Cavalry Brig., S. African F.F | — | [1929, 1930, 1931] |
| 2 | 1902–1907 | vicar, St. Barnabas, Dover | — | [1929, 1930, 1931] |
| 3 | 1908–1914 | dean and vicar-gen., Newcastle | New South Wales | [1929, 1930, 1931] |
| 4 | 1914–1915 | S.C.F., A.I.F | New South Wales *(inherited from previous clause)* | [1929, 1930, 1931] |
| 5 | 1915–1919 | S.C.F., C.M.F | New South Wales *(inherited from previous clause)* | [1929, 1930, 1931] |
| 6 | 1919 | bishop of Mauritius | New South Wales *(inherited from previous clause)* | [1929, 1930, 1931] |

## Candidate stint `Golding-Bird, C. H___Mauritius___1920`

- Staff-list name: **Golding-Bird, C. H** | colony: **Mauritius** | listed 1920–1931 | editions [1920, 1921, 1922, 1923, 1925, 1927, 1928, 1929, 1931]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1920 | C. H. Golding-Bird | Bishop of Mauritius | Church of England | — | — |
| 1921 | C. H. Golding-Bird | Bishop of Mauritius | Church of England | — | — |
| 1922 | C. H. Golding-Bird | Bishop of Mauritius | Church of England | — | — |
| 1923 | C. H. Golding-Bird | Bishop of Mauritius | Church of England | — | — |
| 1925 | C. H. Golding-Bird | Bishop of Mauritius, Right Rev. | Church of England | — | — |
| 1927 | Right Rev. C. H. Golding-Bird | Bishop of Mauritius | Church of England | — | — |
| 1928 | C. H. Golding-Bird | Bishop of Mauritius | Church of England | — | — |
| 1929 | C. H. Golding-Bird | Bishop of Mauritius | Church of England | — | — |
| 1931 | C. H. Golding-Bird | Bishop of Mauritius | Church of England | — | — |

### Deterministic checks: `golding-bird_cyril-henry_e1899` vs `Golding-Bird, C. H___Mauritius___1920`

- [PASS] surname_gate: bio 'GOLDING-BIRD' vs stint 'Golding-Bird, C. H' (exact)
- [PASS] initials: bio ['C', 'H'] ~ stint ['C', 'H']
- [PASS] age_gate: stint starts 1920; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Mauritius'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1920-1931
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

