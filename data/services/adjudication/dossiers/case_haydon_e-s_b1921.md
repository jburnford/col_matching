<!-- {"case_id": "case_haydon_e-s_b1921", "bio_ids": ["haydon_e-s_b1921"], "stint_ids": ["Haydon, E. S___Uganda___1949", "Haydon, E. S___Uganda___1955"]} -->
# Dossier case_haydon_e-s_b1921

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 10 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `haydon_e-s_b1921`

- Printed name: **HAYDON, E. S**
- Birth year: 1921 (attested in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1957-L23938.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> HAYDON, E. S.—b. 1921; ed. Reading Sch. and Univ.; mil. serv., 1942-46, maj.; cadet, Uga., 1946; D.O., 1948; judicial advr., Buganda, 1954; mag., H.K., 1960; prin. mag., 1963.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | cadet | Uganda | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1948 | cadet | Dominions Office | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1954 | judicial advr., Buganda | Dominions Office *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1960 | mag. | Hong Kong | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 4 | 1963 | prin. mag | Hong Kong *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Haydon, E. S___Uganda___1949`

- Staff-list name: **Haydon, E. S** | colony: **Uganda** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | E. S. Haydon | District Officers and Assistant District Officers | Provincial Administration | — | — |
| 1951 | E. S. Haydon | Secretaries (Seconded from the Provincial Administration) | Secretariat | — | — |
| 1951 | E. S. Haydon | District Officers and Assistant District Officers | Provincial Administration | — | — |

### Deterministic checks: `haydon_e-s_b1921` vs `Haydon, E. S___Uganda___1949`

- [PASS] surname_gate: bio 'HAYDON' vs stint 'Haydon, E. S' (exact)
- [PASS] initials: bio ['E', 'S'] ~ stint ['E', 'S']
- [PASS] age_gate: stint starts 1949, birth 1921 (age 28)
- [PASS] colony: 1 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 17 vs bar 60: 'cadet' ~ 'Secretaries (Seconded from the Provincial Administration)'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Haydon, E. S___Uganda___1955`

- Staff-list name: **Haydon, E. S** | colony: **Uganda** | listed 1955–1959 | editions [1955, 1957, 1959]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1955 | E. S. Haydon | Judicial Adviser | Civil Establishment | — | — |
| 1957 | E. S. Haydon | Judicial Adviser, Buganda | Civil Establishment | — | — |
| 1959 | E. S. Haydon | Judicial Adviser, Buganda | Civil Establishment | — | — |

### Deterministic checks: `haydon_e-s_b1921` vs `Haydon, E. S___Uganda___1955`

- [PASS] surname_gate: bio 'HAYDON' vs stint 'Haydon, E. S' (exact)
- [PASS] initials: bio ['E', 'S'] ~ stint ['E', 'S']
- [PASS] age_gate: stint starts 1955, birth 1921 (age 34)
- [PASS] colony: 1 placed event(s) resolve to 'Uganda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1955-1959
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

