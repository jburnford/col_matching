<!-- {"case_id": "case_willis_stanley-scott_b1889", "bio_ids": ["willis_stanley-scott_b1889"], "stint_ids": ["Willis, S. S___Kenya___1920", "Willis, S. S___Tanganyika___1923"]} -->
# Dossier case_willis_stanley-scott_b1889

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 17 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `willis_stanley-scott_b1889`

- Printed name: **WILLIS, STANLEY SCOTT**
- Birth year: 1889 (attested in editions [1928, 1929, 1930, 1931])
- Appears in editions: [1928, 1929, 1930, 1931]

### Verbatim printed entry text (OCR)

**Version `col1928-L71154.v` — printed in editions [1928, 1929, 1930, 1931]:**

> WILLIS, STANLEY SCOTT.—B. 1889; ed. St. Lawrence Coll.; P.A.S.I., 1912; staff survr., Kenya, 1913; milly. survr., 1915-19; staff survr., Tanganyika Territory, 1922; on Anglo-Belgian bdy. comm., 1922-24.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1912 | P.A.S.I | — | [1928, 1929, 1930, 1931] |
| 1 | 1913 | staff survr. | Kenya | [1928, 1929, 1930, 1931] |
| 2 | 1915–1919 | milly. survr | Kenya *(inherited from previous clause)* | [1928, 1929, 1930, 1931] |
| 3 | 1922 | staff survr., Tanganyika Territory | Tanganyika | [1928, 1929, 1930, 1931] |

## Candidate stint `Willis, S. S___Kenya___1920`

- Staff-list name: **Willis, S. S** | colony: **Kenya** | listed 1920–1922 | editions [1920, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1920 | S. S. Willis | Junior Staff Surveyors | Land Survey Branch | — | — |
| 1922 | S. S. Willis | Junior Staff Surveyor | Department of Lands | — | — |

### Deterministic checks: `willis_stanley-scott_b1889` vs `Willis, S. S___Kenya___1920`

- [PASS] surname_gate: bio 'WILLIS' vs stint 'Willis, S. S' (exact)
- [PASS] initials: bio ['S', 'S'] ~ stint ['S', 'S']
- [PASS] age_gate: stint starts 1920, birth 1889 (age 31)
- [PASS] colony: 2 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1920-1922
- [FAIL] position_sim: best 44 vs bar 60: 'milly. survr' ~ 'Junior Staff Surveyor'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Willis, S. S___Tanganyika___1923`

- Staff-list name: **Willis, S. S** | colony: **Tanganyika** | listed 1923–1925 | editions [1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1923 | S. S. Willis | Junior Staff Surveyors | Land, Survey and Mines Department | — | — |
| 1924 | S. S. Willis | Junior Staff Surveyors | Land, Survey and Mines Department | — | — |
| 1925 | S. S. Willis | Junior Staff Surveyors | Land, Survey and Mines Department | — | — |

### Deterministic checks: `willis_stanley-scott_b1889` vs `Willis, S. S___Tanganyika___1923`

- [PASS] surname_gate: bio 'WILLIS' vs stint 'Willis, S. S' (exact)
- [PASS] initials: bio ['S', 'S'] ~ stint ['S', 'S']
- [PASS] age_gate: stint starts 1923, birth 1889 (age 34)
- [PASS] colony: 1 placed event(s) resolve to 'Tanganyika'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1923-1925
- [FAIL] position_sim: best 48 vs bar 60: 'staff survr., Tanganyika Territory' ~ 'Junior Staff Surveyors'
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

