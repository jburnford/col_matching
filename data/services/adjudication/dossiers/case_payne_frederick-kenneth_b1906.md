<!-- {"case_id": "case_payne_frederick-kenneth_b1906", "bio_ids": ["payne_frederick-kenneth_b1906"], "stint_ids": ["Payne, F. K___Leeward Islands___1949"]} -->
# Dossier case_payne_frederick-kenneth_b1906

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 29 official(s) with this surname in the graph's staff lists; 14 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `payne_frederick-kenneth_b1906`

- Printed name: **PAYNE, Frederick Kenneth**
- Birth year: 1906 (attested in editions [1948, 1950, 1951])
- Appears in editions: [1948, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L35158.v` — printed in editions [1948, 1950, 1951]:**

> PAYNE, Frederick Kenneth.—b. 1906; ed. Alleyns, Dulwich, Margate Coll.; man., Kingston employment bureau, J'ca., 1940; lab. offr., gr. III, 1943; dist. comsnr., Caicos Is., 1943; asst. fed. lab. offr., Lee-ward Is., 1944; fed. lab. offr., 1945; spec. duties in connection with construction of American bases., 1941-42.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1940 | man., Kingston employment bureau | Jamaica | [1948, 1950, 1951] |
| 1 | 1941–1942 | spec. duties in connection with construction of American bases | Jamaica *(inherited from previous clause)* | [1948, 1950, 1951] |
| 2 | 1943 | lab. offr., gr. III | Jamaica *(inherited from previous clause)* | [1948, 1950, 1951] |
| 3 | 1944 | asst. fed. lab. offr., Lee-ward Is | Jamaica *(inherited from previous clause)* | [1948, 1950, 1951] |
| 4 | 1945 | fed. lab. offr | Jamaica *(inherited from previous clause)* | [1948, 1950, 1951] |

## Candidate stint `Payne, F. K___Leeward Islands___1949`

- Staff-list name: **Payne, F. K** | colony: **Leeward Islands** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | F. K. Payne | Federal Labour Officer | LABOUR | — | — |
| 1950 | F. K. Payne | Federal Labour Officer | LABOUR | — | — |

### Deterministic checks: `payne_frederick-kenneth_b1906` vs `Payne, F. K___Leeward Islands___1949`

- [PASS] surname_gate: bio 'PAYNE' vs stint 'Payne, F. K' (exact)
- [PASS] initials: bio ['F', 'K'] ~ stint ['F', 'K']
- [PASS] age_gate: stint starts 1949, birth 1906 (age 43)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1950
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

