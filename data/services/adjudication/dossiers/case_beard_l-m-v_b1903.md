<!-- {"case_id": "case_beard_l-m-v_b1903", "bio_ids": ["beard_l-m-v_b1903"], "stint_ids": ["Beard, L. McD___Trinidad and Tobago___1954"]} -->
# Dossier case_beard_l-m-v_b1903

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 14 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `beard_l-m-v_b1903`

- Printed name: **BEARD, L. M. V**
- Birth year: 1903 (attested in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964])
- Appears in editions: [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1956-L19684.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]:**

> BEARD, L. M. V.—b. 1903; ed. St. Mary's Coll., Trin. and Toronto Univ.; survr., P.W.D., Trin., 1940; dep. dir., surveys, and dep. sub-intendant of crown lands, 1952; dir. and sub-intendant, 1958. (T'dad Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1940 | survr., P.W.D. | Trinidad | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1952 | dep. dir., surveys, and dep. sub-intendant of crown lands | Trinidad *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 2 | 1958 | dir. and sub-intendant | Trinidad *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Beard, L. McD___Trinidad and Tobago___1954`

- Staff-list name: **Beard, L. McD** | colony: **Trinidad and Tobago** | listed 1954–1962 | editions [1954, 1962]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1954 | L. McD. Beard | Deputy Director | Civil Establishment | — | — |
| 1962 | L. M. V. Beard | Director of Surveys and Sub-Intendant of Crown Lands | Civil Establishment | — | — |

### Deterministic checks: `beard_l-m-v_b1903` vs `Beard, L. McD___Trinidad and Tobago___1954`

- [PASS] surname_gate: bio 'BEARD' vs stint 'Beard, L. McD' (exact)
- [PASS] initials: bio ['L', 'M', 'V'] ~ stint ['L', 'M']
- [PASS] age_gate: stint starts 1954, birth 1903 (age 51)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1954-1962
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

