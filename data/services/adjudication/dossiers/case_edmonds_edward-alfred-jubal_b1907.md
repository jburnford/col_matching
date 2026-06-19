<!-- {"case_id": "case_edmonds_edward-alfred-jubal_b1907", "bio_ids": ["edmonds_edward-alfred-jubal_b1907"], "stint_ids": ["Edmonds, E. A___Gold Coast___1950"]} -->
# Dossier case_edmonds_edward-alfred-jubal_b1907

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `edmonds_edward-alfred-jubal_b1907`

- Printed name: **EDMONDS, Edward Alfred Jubal**
- Birth year: 1907 (attested in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964])
- Appears in editions: [1951, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1957-L22753.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]:**

> EDMONDS, E. A. J.—b. 1907; ed. Hilton Coll. and Natal Univ.; advoc, supreme ct., S.A.; resdt. mag., Tang., 1946; puisne judge, Ken., 1955–63. (Ken. Govt. service.)

**Version `col1951-L37817.v` — printed in editions [1951]:**

> EDMONDS, Edward Alfred Jubal.—b. 1907; ed. Hilton Coll., Natal, and Natal Univ. Coll., advc. (S.A.); on mil. serv., 1939-46; res. mag., T.T., 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | resdt. mag. | Tanganyika | [1951, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1955–1963 | puisne judge | Kenya | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Edmonds, E. A___Gold Coast___1950`

- Staff-list name: **Edmonds, E. A** | colony: **Gold Coast** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | E. A. Edmonds | Geologists | Geological Survey | — | — |
| 1951 | E. A. Edmonds | Geologists | GEOLOGICAL SURVEY | — | — |

### Deterministic checks: `edmonds_edward-alfred-jubal_b1907` vs `Edmonds, E. A___Gold Coast___1950`

- [PASS] surname_gate: bio 'EDMONDS' vs stint 'Edmonds, E. A' (exact)
- [PASS] initials: bio ['E', 'A', 'J'] ~ stint ['E', 'A']
- [PASS] age_gate: stint starts 1950, birth 1907 (age 43)
- [FAIL] colony: no placed event resolves to 'Gold Coast'
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

