<!-- {"case_id": "case_fell_w-m_b1916", "bio_ids": ["fell_w-m_b1916"], "stint_ids": ["Fell, W. M___Singapore___1960", "Fell, W. M___Trinidad and Tobago___1953"]} -->
# Dossier case_fell_w-m_b1916

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 10 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `fell_w-m_b1916`

- Printed name: **FELL, W. M**
- Birth year: 1916 (attested in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Honours: C.B.E (1965)
- Appears in editions: [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1956-L21095.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> FELL, W. M., C.B.E. (1965).—b. 1916; ed. Newport High Sch.; mil. serv., 1940-46, capt.; asst. audr., Nig., 1946; audr., G. & E.Is. Col., 1950; senr. audr., Trin., 1954; redesign, dep. dir., audit, 1958; dep. dir., audit, S'pore, 1959-62; ret., re-apptd. dir. audit, S'pore, 1963.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | asst. audr. | Nigeria | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1950 | audr., G. & E.Is. Col | Nigeria *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1954 | senr. audr. | Trinidad | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1958 | redesign, dep. dir., audit | Trinidad *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 4 | 1959–1962 | dep. dir., audit, S'pore | Trinidad *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 5 | 1963 | ret., re-apptd. dir. audit, S'pore | Trinidad *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Fell, W. M___Singapore___1960`

- Staff-list name: **Fell, W. M** | colony: **Singapore** | listed 1960–1963 | editions [1960, 1962, 1963]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1960 | W. M. Fell | Deputy Director of Audit | Civil Establishment | — | — |
| 1962 | W. M. Fell | Deputy Director of Audit | Civil Establishment | — | — |
| 1963 | W. M. Fell | Director of Audit | Civil Establishment | — | — |

### Deterministic checks: `fell_w-m_b1916` vs `Fell, W. M___Singapore___1960`

- [PASS] surname_gate: bio 'FELL' vs stint 'Fell, W. M' (exact)
- [PASS] initials: bio ['W', 'M'] ~ stint ['W', 'M']
- [PASS] age_gate: stint starts 1960, birth 1916 (age 44)
- [FAIL] colony: no placed event resolves to 'Singapore'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1960-1963
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Fell, W. M___Trinidad and Tobago___1953`

- Staff-list name: **Fell, W. M** | colony: **Trinidad and Tobago** | listed 1953–1954 | editions [1953, 1954]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1953 | W. M. Fell | Senior Auditor | Civil Establishment | — | — |
| 1954 | W. M. Fell | Senior Auditor | Civil Establishment | — | — |

### Deterministic checks: `fell_w-m_b1916` vs `Fell, W. M___Trinidad and Tobago___1953`

- [PASS] surname_gate: bio 'FELL' vs stint 'Fell, W. M' (exact)
- [PASS] initials: bio ['W', 'M'] ~ stint ['W', 'M']
- [PASS] age_gate: stint starts 1953, birth 1916 (age 37)
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

