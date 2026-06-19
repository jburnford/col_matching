<!-- {"case_id": "case_wall_francis-joseph_b1900", "bio_ids": ["wall_francis-joseph_b1900"], "stint_ids": ["Wall, F. J___Trinidad and Tobago___1934"]} -->
# Dossier case_wall_francis-joseph_b1900

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 22 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `wall_francis-joseph_b1900`

- Printed name: **WALL, FRANCIS JOSEPH**
- Birth year: 1900 (attested in editions [1934, 1935, 1936, 1939, 1940])
- Appears in editions: [1934, 1935, 1936, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1934-L63819.v` — printed in editions [1934, 1935, 1936, 1939, 1940]:**

> WALL, FRANCIS JOSEPH.—B. 1900; supt., prisons, Trinidad, Nov., 1932.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1932 | supt., prisons | Trinidad | [1934, 1935, 1936, 1939, 1940] |

## Candidate stint `Wall, F. J___Trinidad and Tobago___1934`

- Staff-list name: **Wall, F. J** | colony: **Trinidad and Tobago** | listed 1934–1937 | editions [1934, 1937]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | F. J. Wall | Superintendent of Prisons, and Keeper of Royal Gaol | Constabulary and Gaols | — | — |
| 1937 | F. J. Wall | Superintendent of Prisons | Prisons | — | — |

### Deterministic checks: `wall_francis-joseph_b1900` vs `Wall, F. J___Trinidad and Tobago___1934`

- [PASS] surname_gate: bio 'WALL' vs stint 'Wall, F. J' (exact)
- [PASS] initials: bio ['F', 'J'] ~ stint ['F', 'J']
- [PASS] age_gate: stint starts 1934, birth 1900 (age 34)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1934-1937
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

