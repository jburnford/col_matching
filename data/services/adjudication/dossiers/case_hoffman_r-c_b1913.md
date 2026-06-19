<!-- {"case_id": "case_hoffman_r-c_b1913", "bio_ids": ["hoffman_r-c_b1913"], "stint_ids": ["Hoffman, R. C___Singapore___1956"]} -->
# Dossier case_hoffman_r-c_b1913

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hoffman_r-c_b1913`

- Printed name: **HOFFMAN, R. C**
- Birth year: 1913 (attested in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1957-L24129.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> HOFFMAN, R. C.—b. 1913; ed. Raffles Instn. and Coll., S'pore, and Christ Church, Oxford; barrister-at-law, Gray's Inn; probr., S.S., 1937; asst. dist. offr., 1939; dep. collr., land rev., 1947; dist. judge and mag., 1952; asst. sec. (service), S'pore, 1956; perm. sec. (estab.), 1957.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1937 | probr. | Straits Settlements | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1939 | asst. dist. offr | Straits Settlements *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1947 | dep. collr., land rev | Straits Settlements *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1952 | dist. judge and mag | Straits Settlements *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 4 | 1956 | asst. sec. (service), S'pore | Straits Settlements *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 5 | 1957 | perm. sec. (estab.) | Straits Settlements *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Hoffman, R. C___Singapore___1956`

- Staff-list name: **Hoffman, R. C** | colony: **Singapore** | listed 1956–1960 | editions [1956, 1958, 1959, 1960]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1956 | R. C. Hoffman | Secretary to Chief Minister | Civil Establishment | — | — |
| 1958 | R. C. Hoffman | Permanent Secretary (Establishment) | Civil Establishment | — | — |
| 1959 | R. C. Hoffman | Permanent Secretary (Establishment) | Civil Establishment | — | — |
| 1960 | R. C. Hoffman | Permanent Secretary to Ministry of Education and Director of Education | MINISTRY OF EDUCATION | — | — |

### Deterministic checks: `hoffman_r-c_b1913` vs `Hoffman, R. C___Singapore___1956`

- [PASS] surname_gate: bio 'HOFFMAN' vs stint 'Hoffman, R. C' (exact)
- [PASS] initials: bio ['R', 'C'] ~ stint ['R', 'C']
- [PASS] age_gate: stint starts 1956, birth 1913 (age 43)
- [FAIL] colony: no placed event resolves to 'Singapore'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1956-1960
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

