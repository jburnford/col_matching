<!-- {"case_id": "case_aleong_r-v-s_b1911", "bio_ids": ["aleong_r-v-s_b1911"], "stint_ids": ["Aleong, R. V. S___Trinidad and Tobago___1953"]} -->
# Dossier case_aleong_r-v-s_b1911

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `aleong_r-v-s_b1911`

- Printed name: **ALEONG, R. V. S**
- Birth year: 1911 (attested in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964])
- Appears in editions: [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1956-L19377.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]:**

> ALEONG, R. V. S.—b. 1911; ed. Queen's Royal Coll., Trin., Faraday Hse. Elec. Engrng. Coll., London; chief electrical inspector, Trin., 1950. (T'dad Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1950 | chief electrical inspector | Trinidad | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Aleong, R. V. S___Trinidad and Tobago___1953`

- Staff-list name: **Aleong, R. V. S** | colony: **Trinidad and Tobago** | listed 1953–1954 | editions [1953, 1954]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1953 | R. V. S. Aleong | Chief Electrical Inspector | Civil Establishment | — | — |
| 1954 | R. V. S. Aleong | Chief Electrical Inspector | Civil Establishment | — | — |

### Deterministic checks: `aleong_r-v-s_b1911` vs `Aleong, R. V. S___Trinidad and Tobago___1953`

- [PASS] surname_gate: bio 'ALEONG' vs stint 'Aleong, R. V. S' (exact)
- [PASS] initials: bio ['R', 'V', 'S'] ~ stint ['R', 'V', 'S']
- [PASS] age_gate: stint starts 1953, birth 1911 (age 42)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1953-1954
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

