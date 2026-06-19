<!-- {"case_id": "case_heath_douglas-frank_b1897", "bio_ids": ["heath_douglas-frank_b1897"], "stint_ids": ["Heath, K. D. F___British Somaliland___1949"]} -->
# Dossier case_heath_douglas-frank_b1897

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 38 official(s) with this surname in the graph's staff lists; 16 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `heath_douglas-frank_b1897`

- Printed name: **HEATH, Douglas Frank**
- Birth year: 1897 (attested in editions [1950, 1951])
- Appears in editions: [1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1950-L36264.v` — printed in editions [1950, 1951]:**

> HEATH, Douglas Frank.—b. 1897; ed. Mill Hill Sch. and Glasgow Univ.; on mil. serv., 1915-21 and 1939-43; apptd. col. admin. serv., Nig., 1924; C.O., 1946; sec., med. dept., Tang., 1947; author in collaboration of *Blindness in British African and Middle East Territories*, 1948, and contribution to *Man and Africa*.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915–1921 | mil. serv. | — | [1950, 1951] |
| 1 | 1924 | col. admin. serv. | Nigeria | [1950, 1951] |
| 2 | 1939–1943 | mil. serv. | — | [1950, 1951] |
| 3 | 1946 | C.O. | — | [1950, 1951] |
| 4 | 1947 | sec., med. dept. | Tanganyika | [1950, 1951] |

## Candidate stint `Heath, K. D. F___British Somaliland___1949`

- Staff-list name: **Heath, K. D. F** | colony: **British Somaliland** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | K. D. F. Heath | Office Assistant | Governor and Personal Staff | — | — |
| 1950 | K. D. F. Heath | Office Assistant | GOVERNOR AND PERSONAL STAFF | — | — |

### Deterministic checks: `heath_douglas-frank_b1897` vs `Heath, K. D. F___British Somaliland___1949`

- [PASS] surname_gate: bio 'HEATH' vs stint 'Heath, K. D. F' (exact)
- [PASS] initials: bio ['D', 'F'] ~ stint ['K', 'D', 'F']
- [PASS] age_gate: stint starts 1949, birth 1897 (age 52)
- [FAIL] colony: no placed event resolves to 'British Somaliland'
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

