<!-- {"case_id": "case_widdell_j-w_b1922", "bio_ids": ["widdell_j-w_b1922"], "stint_ids": ["Liddell, J___Bahamas___1954"]} -->
# Dossier case_widdell_j-w_b1922

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `widdell_j-w_b1922`

- Printed name: **WIDDELL, J. W**
- Birth year: 1922 (attested in editions [1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Honours: O.B.E (1960)
- Appears in editions: [1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1960-L29363.v` — printed in editions [1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> WIDDELL, J. W., O.B.E. (1960).—b. 1922; ed. Ulme Gram. Sch. and St. John's Coll., Camb.; mil. serv., 1941-45, capt.; admin. cadet, Nig., 1949; cl. II, E. Nig., 1957; sec. to gov., E. Nig., 1957; cl. I, 1959-62; temp. prin. C.O., 1962; prin., 1963; secon. C.A.O., 1963; secon. C.R.O., 1964-65; trans. min. of public bidgs. and wks., 1966.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1949 | admin. cadet | Nigeria | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1957 | cl. II | Eastern Nigeria | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1959–1962 | cl. I | Eastern Nigeria *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1962 | temp. prin. C.O | Eastern Nigeria *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 4 | 1963 | prin | Eastern Nigeria *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 5 | 1964–1965 | secon. C.R.O | Eastern Nigeria *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 6 | 1966 | trans. min. of public bidgs. and wks | Eastern Nigeria *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Liddell, J___Bahamas___1954`

- Staff-list name: **Liddell, J** | colony: **Bahamas** | listed 1954–1962 | editions [1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1954 | J. Liddell | Registrar-General | Civil Establishment | — | — |
| 1955 | J. Liddell. | Registrar-General | Civil Establishment | — | — |
| 1956 | J. Liddell | Registrar-General | Civil Establishment | — | — |
| 1957 | J. Liddell | Registrar-General | Civil Establishment | — | — |
| 1958 | J. Liddell | Registrar-General | Civil Establishment | — | — |
| 1959 | J. Liddell | Registrar-General | Civil Establishment | — | — |
| 1960 | J. Liddell | Registrar-General | Civil Establishment | — | — |
| 1961 | J. Liddell | Registrar-General | Civil Establishment | — | — |
| 1962 | J. Liddell | Stipendiary and Circuit Magistrates | Judiciary | — | — |

### Deterministic checks: `widdell_j-w_b1922` vs `Liddell, J___Bahamas___1954`

- [PASS] surname_gate: bio 'WIDDELL' vs stint 'Liddell, J' (fuzzy:1)
- [PASS] initials: bio ['J', 'W'] ~ stint ['J']
- [PASS] age_gate: stint starts 1954, birth 1922 (age 32)
- [FAIL] colony: no placed event resolves to 'Bahamas'
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

