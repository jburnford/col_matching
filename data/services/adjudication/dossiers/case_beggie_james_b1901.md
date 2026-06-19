<!-- {"case_id": "case_beggie_james_b1901", "bio_ids": ["beggie_james_b1901"], "stint_ids": ["Boggie, W. J___Rhodesia___1921", "Boggie, W. J___Southern Rhodesia___1925"]} -->
# Dossier case_beggie_james_b1901

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['beggie_james_b1901'] carry a single initial only — the namesake trap applies.

## Biography `beggie_james_b1901`

- Printed name: **BEGGIE, James**
- Birth year: 1901 (attested in editions [1950, 1951])
- Appears in editions: [1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1950-L33570.v` — printed in editions [1950, 1951]:**

> BEGGIE, James.—b. 1901; ed. Dundee Tech. Sch., 1st cl. B. of T. eng. cert., steam; on mil. serv., 1939-45, lt.-commdr. (E); engrnr., marine dept., Nig., 1928; prin. engrnr., 1948.

**Version `col1949-L30359.v` — printed in editions [1949]:**

> BEGBIE, James.—b. 1901; ed. Dundee Tech. Sch.; 1st cl. B. of T. eng. cert., steam; on mil. serv., 1939-45, lt.-commdr. (E); eng., marine dept., Nig., 1928.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | engrnr., marine dept. | Nigeria | [1949, 1950, 1951] |
| 1 | 1948 | prin. engrnr | Nigeria *(inherited from previous clause)* | [1950, 1951] |

## Candidate stint `Boggie, W. J___Rhodesia___1921`

- Staff-list name: **Boggie, W. J** | colony: **Rhodesia** | listed 1921–1923 | editions [1921, 1923]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | W. J. Boggie | — | — | — | Major |
| 1923 | W. J. Boggie | — | Legislative Council | — | Major |

### Deterministic checks: `beggie_james_b1901` vs `Boggie, W. J___Rhodesia___1921`

- [PASS] surname_gate: bio 'BEGGIE' vs stint 'Boggie, W. J' (fuzzy:1)
- [PASS] initials: bio ['J'] ~ stint ['W', 'J']
- [PASS] age_gate: stint starts 1921, birth 1901 (age 20)
- [FAIL] colony: no placed event resolves to 'Rhodesia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1921-1923
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Boggie, W. J___Southern Rhodesia___1925`

- Staff-list name: **Boggie, W. J** | colony: **Southern Rhodesia** | listed 1925–1927 | editions [1925, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | W. J. Boggie | Member (Midlands) | Legislative Assembly | — | Major |
| 1927 | W. J. Boggie | Member of Legislative Assembly (Midlands) | Members of the Legislative Assembly | — | Major |

### Deterministic checks: `beggie_james_b1901` vs `Boggie, W. J___Southern Rhodesia___1925`

- [PASS] surname_gate: bio 'BEGGIE' vs stint 'Boggie, W. J' (fuzzy:1)
- [PASS] initials: bio ['J'] ~ stint ['W', 'J']
- [PASS] age_gate: stint starts 1925, birth 1901 (age 24)
- [FAIL] colony: no placed event resolves to 'Southern Rhodesia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1925-1927
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

