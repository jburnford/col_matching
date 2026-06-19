<!-- {"case_id": "case_belt_reginald-walter-burnley_b1897", "bio_ids": ["belt_reginald-walter-burnley_b1897"], "stint_ids": ["Belt, R. W. B___Barbados___1952"]} -->
# Dossier case_belt_reginald-walter-burnley_b1897

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `belt_reginald-walter-burnley_b1897`

- Printed name: **BELT, Reginald Walter Burnley**
- Birth year: 1897 (attested in editions [1948])
- Appears in editions: [1948]

### Verbatim printed entry text (OCR)

**Version `col1948-L31120.v` — printed in editions [1948]:**

> BELT, Reginald Walter Burnley.—b. 1897; ed. Woolwich Poly.; on mil. serv., 1916–19; imp. customs serv., 1915; asst. dir. of customs, Pal., 1935; dir. of customs, 1938; mem. of Pal. trade del. to Egypt, 1935, and Lebanon–Syria, 1939.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915 | imp. customs serv | — | [1948] |
| 1 | 1935 | asst. dir. of customs | Palestine | [1948] |
| 2 | 1938 | dir. of customs | Palestine *(inherited from previous clause)* | [1948] |
| 3 | 1939 | Lebanon–Syria | Palestine *(inherited from previous clause)* | [1948] |

## Candidate stint `Belt, R. W. B___Barbados___1952`

- Staff-list name: **Belt, R. W. B** | colony: **Barbados** | listed 1952–1954 | editions [1952, 1953, 1954]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1952 | R. W. B. Belt | Comptroller of Customs | Civil Establishment | — | — |
| 1953 | R. W. B. Belt | Comptroller of Customs | Civil Establishment | — | — |
| 1954 | R. W. B. Belt | Comptroller of Customs | Civil Establishment | — | — |

### Deterministic checks: `belt_reginald-walter-burnley_b1897` vs `Belt, R. W. B___Barbados___1952`

- [PASS] surname_gate: bio 'BELT' vs stint 'Belt, R. W. B' (exact)
- [PASS] initials: bio ['R', 'W', 'B'] ~ stint ['R', 'W', 'B']
- [PASS] age_gate: stint starts 1952, birth 1897 (age 55)
- [FAIL] colony: no placed event resolves to 'Barbados'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1952-1954
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

