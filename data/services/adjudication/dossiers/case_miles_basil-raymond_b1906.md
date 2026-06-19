<!-- {"case_id": "case_miles_basil-raymond_b1906", "bio_ids": ["miles_basil-raymond_b1906"], "stint_ids": ["Miles, B. R___Gambia___1954"]} -->
# Dossier case_miles_basil-raymond_b1906

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 29 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `miles_basil-raymond_b1906`

- Printed name: **MILES, Basil Raymond**
- Birth year: 1906 (attested in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1951, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1958-L25278.v` — printed in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> MILES, B. R.—b. 1906; ed. Harrow and Oxford Univ.; called to bar; mil. serv., 1940-45; res. mag., Tang., 1946; judge, sup. ct., (redesign. chief justice) Gam., 1953; puisne judge, Ken., 1957. (Ken. Govt. service.)

**Version `col1954-L21586.v` — printed in editions [1954, 1955, 1956, 1957]:**

> MILES, B. R.—b. 1906; ed. Harrow and Oxford Univ.; called to bar; mil. serv., 1940-45; res. mag., Tang., 1946; judge, sup. ct., Gam., 1953.

**Version `col1951-L40846.v` — printed in editions [1951]:**

> MILES, Basil Raymond.—b. 1906; ed. Elstree Prep. Sch., Harrow Sch. and Magdalen Coll., Oxford, B.A. (hons.); barrister-at-law, Inner Temple; on mil. serv., 1940-45; res. mag., T.T., 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | res. mag. | Tanganyika | [1951, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1953 | judge, sup. ct., (redesign. chief justice) Gam | Tanganyika *(inherited from previous clause)* | [1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1957 | puisne judge | Kenya | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Miles, B. R___Gambia___1954`

- Staff-list name: **Miles, B. R** | colony: **Gambia** | listed 1954–1957 | editions [1954, 1955, 1956, 1957]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1954 | B. R. Miles | Judge, Supreme Court | Civil Establishment | — | — |
| 1955 | B. R. Miles | Judge, Supreme Court | Civil Establishment | — | — |
| 1956 | B. R. Miles | Judge, Supreme Court | Civil Establishment | — | — |
| 1957 | B. R. Miles | Judge, Supreme Court | Civil Establishment | — | — |

### Deterministic checks: `miles_basil-raymond_b1906` vs `Miles, B. R___Gambia___1954`

- [PASS] surname_gate: bio 'MILES' vs stint 'Miles, B. R' (exact)
- [PASS] initials: bio ['B', 'R'] ~ stint ['B', 'R']
- [PASS] age_gate: stint starts 1954, birth 1906 (age 48)
- [FAIL] colony: no placed event resolves to 'Gambia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1954-1957
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

