<!-- {"case_id": "case_george_mcc-d-b_b1915", "bio_ids": ["george_mcc-d-b_b1915"], "stint_ids": ["George, McC. B___West Indies Federation___1961", "George, McC. D. B___Leeward Islands___1955"]} -->
# Dossier case_george_mcc-d-b_b1915

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 61 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `george_mcc-d-b_b1915`

- Printed name: **GEORGE, McC. D. B**
- Birth year: 1915 (attested in editions [1956, 1957, 1958, 1959, 1960, 1961])
- Appears in editions: [1956, 1957, 1958, 1959, 1960, 1961]

### Verbatim printed entry text (OCR)

**Version `col1956-L21340.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961]:**

> GEORGE, McC. D. B.—b. 1915; ed. Holy Trinity Sch., Barbuda, Antigua Gram. Sch., Univ. Coll., London and Gray's Inn; o'seer, Barbuda, 1933; P.O. clk., 1936; cashier, treasy., Antigua, 1942; acctnt., marketing offr., 1945; peasant devel. offr., 1954-60.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1933 | o'seer | Barbuda | [1956, 1957, 1958, 1959, 1960, 1961] |
| 1 | 1936 | P.O. clk | Barbuda *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961] |
| 2 | 1942 | cashier, treasy. | Antigua | [1956, 1957, 1958, 1959, 1960, 1961] |
| 3 | 1945 | acctnt., marketing offr | Antigua *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961] |
| 4 | 1954–1960 | peasant devel. offr | Antigua *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961] |

## Candidate stint `George, McC. B___West Indies Federation___1961`

- Staff-list name: **George, McC. B** | colony: **West Indies Federation** | listed 1961–1962 | editions [1961, 1962]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1961 | McC. B. George | Member without portfolio | Executive Council | — | — |
| 1962 | McC. B. George | Member without portfolio | Executive Council | — | — |

### Deterministic checks: `george_mcc-d-b_b1915` vs `George, McC. B___West Indies Federation___1961`

- [PASS] surname_gate: bio 'GEORGE' vs stint 'George, McC. B' (exact)
- [PASS] initials: bio ['M', 'D', 'B'] ~ stint ['M', 'B']
- [PASS] age_gate: stint starts 1961, birth 1915 (age 46)
- [FAIL] colony: no placed event resolves to 'West Indies Federation'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1961-1962
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `George, McC. D. B___Leeward Islands___1955`

- Staff-list name: **George, McC. D. B** | colony: **Leeward Islands** | listed 1955–1957 | editions [1955, 1956, 1957]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1955 | McC. George | Peasant Development Officer | Civil Establishment | — | — |
| 1956 | McC. D. B. George | Peasant Development Officer | Civil Establishment | — | — |
| 1957 | McC. D. B. George | Peasant Development Officer | Civil Establishment | — | — |

### Deterministic checks: `george_mcc-d-b_b1915` vs `George, McC. D. B___Leeward Islands___1955`

- [PASS] surname_gate: bio 'GEORGE' vs stint 'George, McC. D. B' (exact)
- [PASS] initials: bio ['M', 'D', 'B'] ~ stint ['M', 'D', 'B']
- [PASS] age_gate: stint starts 1955, birth 1915 (age 40)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1955-1957
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

