<!-- {"case_id": "case_amoroso-centeno_a-e-b_b1910", "bio_ids": ["amoroso-centeno_a-e-b_b1910"], "stint_ids": ["Amoroso-Centeno, A. E. B___Trinidad and Tobago___1953"]} -->
# Dossier case_amoroso-centeno_a-e-b_b1910

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `amoroso-centeno_a-e-b_b1910`

- Printed name: **AMOROSO-CENTENO, A. E. B**
- Birth year: 1910 (attested in editions [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964])
- Honours: M.B.E
- Appears in editions: [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1953-L16346.v` — printed in editions [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]:**

> AMOROSO-CENTENO, A. E. B., M.B.E.—b. 1910; ed. St. Mary's Coll., Port-of-Spain; called to bar, Gray's Inn; clk., postal, treas. and acctnt.-gen.'s depts., T'dad, 1928-42; assessor, inl. rev. dept., 1943; sec., 1950; dep. comsrr., 1952; comsrr., 1957. (T'dad Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928–1942 | clk., postal, treas. and acctnt.-gen.'s depts. | Trinidad | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1943 | assessor, inl. rev. dept | Trinidad *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 2 | 1950 | sec | Trinidad *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 3 | 1952 | dep. comsrr | Trinidad *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 4 | 1957 | comsrr | Trinidad *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Amoroso-Centeno, A. E. B___Trinidad and Tobago___1953`

- Staff-list name: **Amoroso-Centeno, A. E. B** | colony: **Trinidad and Tobago** | listed 1953–1962 | editions [1953, 1954, 1962]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1953 | A. E. B. Amoroso-Centeno | Deputy Commissioner | Civil Establishment | — | — |
| 1954 | A. E. B. Amoroso-Centeno | Deputy Commissioner | Civil Establishment | M.B.E. | — |
| 1962 | A. E. B. Amoroso-Centeno | Commissioner of Inland Revenue | Civil Establishment | — | — |

### Deterministic checks: `amoroso-centeno_a-e-b_b1910` vs `Amoroso-Centeno, A. E. B___Trinidad and Tobago___1953`

- [PASS] surname_gate: bio 'AMOROSO-CENTENO' vs stint 'Amoroso-Centeno, A. E. B' (exact)
- [PASS] initials: bio ['A', 'E', 'B'] ~ stint ['A', 'E', 'B']
- [PASS] age_gate: stint starts 1953, birth 1910 (age 43)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1953-1962
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: M.B.E
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

