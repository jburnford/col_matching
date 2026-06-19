<!-- {"case_id": "case_turpin_r-a_b1913", "bio_ids": ["turpin_r-a_b1913"], "stint_ids": ["Turpin, R___Western Pacific___1955"]} -->
# Dossier case_turpin_r-a_b1913

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 13 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Turpin, R___Western Pacific___1955` is also gate-compatible with biography(ies) outside this case: ['turpin_r_b1921'] (already linked elsewhere or filtered).

## Biography `turpin_r-a_b1913`

- Printed name: **TURPIN, R. A**
- Birth year: 1913 (attested in editions [1963, 1964])
- Appears in editions: [1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1963-L25803.v` — printed in editions [1963, 1964]:**

> TURPIN, R. A.—b. 1913; ed. Wolmers Sch., Kingston, J'ca.; asst., J'ca., 1934; clk., 1940; examnr. acct., 1948; senr. acctnt., 1952; acctnt., 1955; ch. acctnt., 1956; prin. asst. sec., 1961. (J'ca Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1934 | asst. | Jamaica | [1963, 1964] |
| 1 | 1940 | clk | Jamaica *(inherited from previous clause)* | [1963, 1964] |
| 2 | 1948 | examnr. acct | Jamaica *(inherited from previous clause)* | [1963, 1964] |
| 3 | 1952 | senr. acctnt | Jamaica *(inherited from previous clause)* | [1963, 1964] |
| 4 | 1955 | acctnt | Jamaica *(inherited from previous clause)* | [1963, 1964] |
| 5 | 1956 | ch. acctnt | Jamaica *(inherited from previous clause)* | [1963, 1964] |
| 6 | 1961 | prin. asst. sec | Jamaica *(inherited from previous clause)* | [1963, 1964] |

## Candidate stint `Turpin, R___Western Pacific___1955`

- Staff-list name: **Turpin, R** | colony: **Western Pacific** | listed 1955–1966 | editions [1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1955 | R. Turpin | Administrative Officer | Civil Establishment | — | — |
| 1956 | R. Turpin | Administrative Officer | Civil Establishment | — | — |
| 1957 | R. Turpin | Administrative Officer | Civil Establishment | — | — |
| 1958 | R. Turpin | Administrative Officers | Civil Establishment | — | — |
| 1959 | R. Turpin | Administrative Officer – Class B | Civil Establishment | — | — |
| 1960 | R. Turpin | Administrative Officer | Civil Establishment | — | — |
| 1961 | R. Turpin | Administrative Officer – Class B | Civil Establishment | — | — |
| 1962 | R. Turpin | Administrative Officer (Class B) | Civil Establishment | — | — |
| 1964 | R. Turpin | Senior Assistant Secretary | Civil Establishment | — | — |
| 1965 | R. Turpin | Administrative Officers | Civil Establishment | — | — |
| 1966 | R. Turpin | Administrative Officer, Class A | Civil Establishment | — | — |

### Deterministic checks: `turpin_r-a_b1913` vs `Turpin, R___Western Pacific___1955`

- [PASS] surname_gate: bio 'TURPIN' vs stint 'Turpin, R' (exact)
- [PASS] initials: bio ['R', 'A'] ~ stint ['R']
- [PASS] age_gate: stint starts 1955, birth 1913 (age 42)
- [FAIL] colony: no placed event resolves to 'Western Pacific'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1955-1966
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

