<!-- {"case_id": "case_vidal_roland-espeut_b1907", "bio_ids": ["vidal_roland-espeut_b1907"], "stint_ids": ["Vidal, R. E___Gold Coast___1950"]} -->
# Dossier case_vidal_roland-espeut_b1907

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `vidal_roland-espeut_b1907`

- Printed name: **VIDAL, Roland Espeut**
- Birth year: 1907 (attested in editions [1959, 1960, 1961])
- Honours: T.D.
- Appears in editions: [1951, 1959, 1960, 1961]

### Verbatim printed entry text (OCR)

**Version `col1959-L28884.v` — printed in editions [1959, 1960, 1961]:**

> VIDAL, R. E., T.D.—b. 1907; ed. St. Paul's Sch.; mil. serv., 1939-46, lt.-col.; admin. offr., Gold Coast, 1946; asst. sec., commerce and indus., 1948; dir., supplies, cont., imports and exports, cont. of prices, 1948, 1949-51; asst. dir., commerce, Nig., 1953; dep. dir., commerce and indus., Fed. of Nig., 1955; dep. sec. (industry), 1959-60.

**Version `col1951-L43427.v` — printed in editions [1951]:**

> VIDAL, Roland Espeut.—b. 1907; ed. St. Paul's Sch.; on mil. serv., 1939–46, lt.-col.; cadet, G.C., 1946; asst. sec. for comm. and indus., contrlr., imp. and exp., contrlr., prices, 1948.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1939–1946 | mil. serv., lt.-col. | — | [1959, 1960, 1961] |
| 1 | 1946–1946 | admin. offr. | Gold Coast | [1951, 1959, 1960, 1961] |
| 2 | 1948–1948 | asst. sec., commerce and indus. | Gold Coast *(inherited from previous clause)* | [1951, 1959, 1960, 1961] |
| 3 | 1948–1951 | dir., supplies, cont., imports and exports, cont. of prices | — | [1959, 1960, 1961] |
| 4 | 1953–1953 | asst. dir., commerce | Nigeria | [1959, 1960, 1961] |
| 5 | 1955–1955 | dep. dir., commerce and indus. | Federation of Nigeria | [1959, 1960, 1961] |
| 6 | 1959–1960 | dep. sec. (industry) | — | [1959, 1960, 1961] |

## Candidate stint `Vidal, R. E___Gold Coast___1950`

- Staff-list name: **Vidal, R. E** | colony: **Gold Coast** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | R. E. Vidal | Assistant Secretary for Commerce and Industry (Commercial) | Commerce and Industry | — | — |
| 1951 | R. E. Vidal | Assistant Director of Commerce and Industry (Commercial) | Commerce and Industry | — | — |

### Deterministic checks: `vidal_roland-espeut_b1907` vs `Vidal, R. E___Gold Coast___1950`

- [PASS] surname_gate: bio 'VIDAL' vs stint 'Vidal, R. E' (exact)
- [PASS] initials: bio ['R', 'E'] ~ stint ['R', 'E']
- [PASS] age_gate: stint starts 1950, birth 1907 (age 43)
- [PASS] colony: 2 placed event(s) resolve to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1950-1951
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

