<!-- {"case_id": "case_henry_k-c-st-l_b1926", "bio_ids": ["henry_k-c-st-l_b1926"], "stint_ids": ["Henry, S. L___Leeward Islands___1949"]} -->
# Dossier case_henry_k-c-st-l_b1926

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 42 official(s) with this surname in the graph's staff lists; 21 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `henry_k-c-st-l_b1926`

- Printed name: **HENRY, K. C. St. L**
- Birth year: 1926 (attested in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964])
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1957-L24017.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]:**

> HENRY, K. C. St. L.—b. 1926; ed. J'ca Coll.; barrister-at-law; asst. clk., gr. II, resdt. mag's court, J'ca, 1944; asst. clk., gr. I, 1946; dep. clk., courts, 1951; legal clk., sup. court, 1954; dep. registr., sup. court, 1955; asst. legal dtsmn., 1958. (J'ca Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1944 | asst. clk., gr. II, resdt. mag's court | Jamaica | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1946 | asst. clk., gr. I | Jamaica *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 2 | 1951 | dep. clk., courts | Jamaica *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 3 | 1954 | legal clk., sup. court | Jamaica *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 4 | 1955 | dep. registr., sup. court | Jamaica *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 5 | 1958 | asst. legal dtsmn | Jamaica *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Henry, S. L___Leeward Islands___1949`

- Staff-list name: **Henry, S. L** | colony: **Leeward Islands** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | S. L. Henry | Marketing Officer | Agricultural | — | — |
| 1950 | S. L. Henry | Marketing Officer | Agricultural | — | — |
| 1951 | S. L. Henry | Marketing Officer | Agricultural | — | — |

### Deterministic checks: `henry_k-c-st-l_b1926` vs `Henry, S. L___Leeward Islands___1949`

- [PASS] surname_gate: bio 'HENRY' vs stint 'Henry, S. L' (exact)
- [PASS] initials: bio ['K', 'C', 'S', 'L'] ~ stint ['S', 'L']
- [PASS] age_gate: stint starts 1949, birth 1926 (age 23)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
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

