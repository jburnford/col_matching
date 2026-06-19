<!-- {"case_id": "case_watt_cecil-james_b1899", "bio_ids": ["watt_cecil-james_b1899", "watt_cecil-james_b1899-2"], "stint_ids": ["Watt, C. J___Gold Coast___1917"]} -->
# Dossier case_watt_cecil-james_b1899

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 39 official(s) with this surname in the graph's staff lists; 20 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Watt, C. J___Gold Coast___1917'] have more than one claimant biography in this case.
- NOTE: stint `Watt, C. J___Gold Coast___1917` is also gate-compatible with biography(ies) outside this case: ['watt_j_e1866', 'watt_james_e1889'] (already linked elsewhere or filtered).
- NOTE: stint `Watt, C. J___Gold Coast___1917` is also gate-compatible with biography(ies) outside this case: ['watt_j_e1866', 'watt_james_e1889'] (already linked elsewhere or filtered).

## Biography `watt_cecil-james_b1899`

- Printed name: **WATT, CECIL JAMES**
- Birth year: 1899 (attested in editions [1939])
- Appears in editions: [1939]

### Verbatim printed entry text (OCR)

**Version `col1939-L71640.v` — printed in editions [1939]:**

> WATT, CECIL JAMES.—B. 1899; under secy., dept. of pub. health, N.S.W., 1930.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1930 | under secy., dept. of pub. health | New South Wales | [1939] |

## Biography `watt_cecil-james_b1899-2`

- Printed name: **WATT, Cecil James**
- Birth year: 1899 (attested in editions [1940])
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L69424.v` — printed in editions [1940]:**

> WATT, Cecil James.—B. 1899; under secy., dept. of pub. health, N.S.W., Nov., 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1938 | under secy., dept. of pub. health | New South Wales | [1940] |

## Candidate stint `Watt, C. J___Gold Coast___1917`

- Staff-list name: **Watt, C. J** | colony: **Gold Coast** | listed 1917–1919 | editions [1917, 1918, 1919]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1917 | C. J. Watt | Assistant Transport Officer | Transport Department | — | — |
| 1918 | C. J. Watt | Assistant Transport Officer | Transport Department | — | — |
| 1919 | C. J. Watt | Assistant Transport Officer | Transport Department | — | — |

### Deterministic checks: `watt_cecil-james_b1899` vs `Watt, C. J___Gold Coast___1917`

- [PASS] surname_gate: bio 'WATT' vs stint 'Watt, C. J' (exact)
- [PASS] initials: bio ['C', 'J'] ~ stint ['C', 'J']
- [PASS] age_gate: stint starts 1917, birth 1899 (age 18)
- [FAIL] colony: no placed event resolves to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1917-1919
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `watt_cecil-james_b1899-2` vs `Watt, C. J___Gold Coast___1917`

- [PASS] surname_gate: bio 'WATT' vs stint 'Watt, C. J' (exact)
- [PASS] initials: bio ['C', 'J'] ~ stint ['C', 'J']
- [PASS] age_gate: stint starts 1917, birth 1899 (age 18)
- [FAIL] colony: no placed event resolves to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1917-1919
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

