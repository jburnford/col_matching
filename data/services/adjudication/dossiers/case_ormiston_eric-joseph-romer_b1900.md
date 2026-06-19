<!-- {"case_id": "case_ormiston_eric-joseph-romer_b1900", "bio_ids": ["ormiston_eric-joseph-romer_b1900"], "stint_ids": ["Ormiston, E. J___Windward Islands___1937"]} -->
# Dossier case_ormiston_eric-joseph-romer_b1900

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `ormiston_eric-joseph-romer_b1900`

- Printed name: **ORMISTON, Eric Joseph Romer**
- Birth year: 1900 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L35038.v` — printed in editions [1948, 1949, 1950, 1951]:**

> ORMISTON, Eric Joseph Romer.—b. 1900; ed. Percy Robert's Pte. Sch., Kent; on mil. serv. 1915-21 and 1939-45; maj.; const., Br. Gendarmerie, Pal., 1923; police cpl., 1936; sgt.-maj., St. V., 1936; sub-inspr., 1937; ch. of police, Gren., 1938; supt., 1940; senr. asst. supt., Nig., 1946; mem. of comsn. on federation of Windward and Leeward Is. police forces.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1923 | const., Br. Gendarmerie | Palestine | [1948, 1949, 1950, 1951] |
| 1 | 1936 | police cpl | Palestine *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 2 | 1936 | sgt.-maj. | St. Vincent | [1948, 1949, 1950, 1951] |
| 3 | 1937 | sub-inspr | St. Vincent *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 4 | 1938 | ch. of police | Grenada | [1948, 1949, 1950, 1951] |
| 5 | 1940 | supt | Grenada *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 6 | 1946 | senr. asst. supt. | Nigeria | [1948, 1949, 1950, 1951] |

## Candidate stint `Ormiston, E. J___Windward Islands___1937`

- Staff-list name: **Ormiston, E. J** | colony: **Windward Islands** | listed 1937–1939 | editions [1937, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1937 | E. J. Ormiston | Sergeant Major | Police and Prisons | — | — |
| 1939 | E. J. Ormiston | Sub-Inspector | Police and Prisons | — | — |

### Deterministic checks: `ormiston_eric-joseph-romer_b1900` vs `Ormiston, E. J___Windward Islands___1937`

- [PASS] surname_gate: bio 'ORMISTON' vs stint 'Ormiston, E. J' (exact)
- [PASS] initials: bio ['E', 'J', 'R'] ~ stint ['E', 'J']
- [PASS] age_gate: stint starts 1937, birth 1900 (age 37)
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1937-1939
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

