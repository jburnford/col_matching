<!-- {"case_id": "case_dawes_guy-prescott_b1906", "bio_ids": ["dawes_guy-prescott_b1906"], "stint_ids": ["Dawes, G. P___Leeward Islands___1936"]} -->
# Dossier case_dawes_guy-prescott_b1906

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `dawes_guy-prescott_b1906`

- Printed name: **DAWES, Guy Prescott**
- Birth year: 1906 (attested in editions [1949, 1950, 1951])
- Appears in editions: [1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1949-L31548.v` — printed in editions [1949, 1950, 1951]:**

> DAWES, Guy Prescott.—b. 1906; ed. Wellington and Sandhurst (prize cadet); a.d.c. and p.s. gov., Leeward Is., 1932; asst. supt., police, 1935; supt. and o/c local forces, Seychelles, 1938; 3rd cl. inspr., J’ca., 1941; 2nd cl., 1943; conducted police and prisons end., Turks and Caicos Is., 1942.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1932 | a.d.c. and p.s. gov., Leeward Is | — | [1949, 1950, 1951] |
| 1 | 1935 | asst. supt., police | — | [1949, 1950, 1951] |
| 2 | 1938 | supt. and o/c local forces | Seychelles | [1949, 1950, 1951] |
| 3 | 1941 | 3rd cl. inspr. | Jamaica | [1949, 1950, 1951] |
| 4 | 1942 | conducted police and prisons end., Turks and Caicos Is | Jamaica *(inherited from previous clause)* | [1949, 1950, 1951] |
| 5 | 1943 | 2nd cl | Jamaica *(inherited from previous clause)* | [1949, 1950, 1951] |

## Candidate stint `Dawes, G. P___Leeward Islands___1936`

- Staff-list name: **Dawes, G. P** | colony: **Leeward Islands** | listed 1936–1939 | editions [1936, 1937, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | G. P. Dawes | Sub-Inspector | Police | — | — |
| 1937 | G. P. Dawes | Sub-Inspector | Police | — | — |
| 1939 | G. P. Dawes | Sub-Inspector | Police | — | — |

### Deterministic checks: `dawes_guy-prescott_b1906` vs `Dawes, G. P___Leeward Islands___1936`

- [PASS] surname_gate: bio 'DAWES' vs stint 'Dawes, G. P' (exact)
- [PASS] initials: bio ['G', 'P'] ~ stint ['G', 'P']
- [PASS] age_gate: stint starts 1936, birth 1906 (age 30)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1936-1939
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

