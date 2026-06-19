<!-- {"case_id": "case_gibson_lennie-bertram_b1896", "bio_ids": ["gibson_lennie-bertram_b1896"], "stint_ids": ["Gibson, Leslie B___Hong Kong___1949"]} -->
# Dossier case_gibson_lennie-bertram_b1896

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 49 official(s) with this surname in the graph's staff lists; 36 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Gibson, Leslie B___Hong Kong___1949` is also gate-compatible with biography(ies) outside this case: ['gibson_leslie-bertram_b1896'] (already linked elsewhere or filtered).

## Biography `gibson_lennie-bertram_b1896`

- Printed name: **GIBSON, LENNIE BERTRAM**
- Birth year: 1896 (attested in editions [1927, 1928])
- Appears in editions: [1927, 1928]

### Verbatim printed entry text (OCR)

**Version `col1927-L59176.v` — printed in editions [1927, 1928]:**

> GIBSON, LENNIE BERTRAM.—B. 1896; ed. King Henry VIII. Schl., Coventry; hon. LL.B. (War), London; flight sub-lieut., R.N.A.S., attnd. Grand Fleet; lieut., R.A.F.; cadet, S. Stiltns., Mar., 1920; attnd. to atty.-gen.'s office, Singapore, Apr., 1920; attnd. to food control office, Penang, May, 1920; dep. dir. of food prodn., Penang, Apr., 1921; ag. collr., income tax, Malacca, Dec., 1921; passed cadet, Mar., 1922; dep. registr. and asst. offr. assignee, Penang, June, 1922; asst. sec., rec., Selangor, July, 1925.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920 | cadet, S. Stiltns | — | [1927, 1928] |
| 1 | 1920 | attnd. to atty.-gen.'s office | Singapore | [1927, 1928] |
| 2 | 1921 | dep. dir. of food prodn., Penang | Singapore *(inherited from previous clause)* | [1927, 1928] |
| 3 | 1922 | passed cadet | Singapore *(inherited from previous clause)* | [1927, 1928] |
| 4 | 1925 | asst. sec., rec., Selangor | Singapore *(inherited from previous clause)* | [1927, 1928] |

## Candidate stint `Gibson, Leslie B___Hong Kong___1949`

- Staff-list name: **Gibson, Leslie B** | colony: **Hong Kong** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | Sir Leslie B. Gibson | Chief Justice | Supreme Court | — | — |
| 1950 | Sir Leslie Gibson | Chief Justice | Supreme Court | — | — |
| 1951 | Sir Leslie Gibson | Chief Justice | Supreme Court | — | — |

### Deterministic checks: `gibson_lennie-bertram_b1896` vs `Gibson, Leslie B___Hong Kong___1949`

- [PASS] surname_gate: bio 'GIBSON' vs stint 'Gibson, Leslie B' (exact)
- [PASS] initials: bio ['L', 'B'] ~ stint ['L', 'B']
- [PASS] age_gate: stint starts 1949, birth 1896 (age 53)
- [FAIL] colony: no placed event resolves to 'Hong Kong'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
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

