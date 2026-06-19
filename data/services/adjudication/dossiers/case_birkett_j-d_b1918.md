<!-- {"case_id": "case_birkett_j-d_b1918", "bio_ids": ["birkett_j-d_b1918"], "stint_ids": ["Birkett, J. D___Sierra Leone___1953"]} -->
# Dossier case_birkett_j-d_b1918

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `birkett_j-d_b1918`

- Printed name: **BIRKETT, J. D**
- Birth year: 1918 (attested in editions [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965])
- Appears in editions: [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]

### Verbatim printed entry text (OCR)

**Version `col1953-L16565.v` — printed in editions [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]:**

> BIRKETT, J. D.—b. 1918; ed. Rutherford Coll., Boys' Sch. and Royal (Dick) Vet. Coll.; vet. offr., Nig., 1941; senr., 1949; D.V.S., S.L., 1952. (S.L. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1941 | vet. offr. | Nigeria | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 1 | 1949 | senr | Nigeria *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 2 | 1952 | D.V.S. | Sierra Leone | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |

## Candidate stint `Birkett, J. D___Sierra Leone___1953`

- Staff-list name: **Birkett, J. D** | colony: **Sierra Leone** | listed 1953–1960 | editions [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1953 | J. D. Birkett | Director of Veterinary Services | Civil Establishment | — | — |
| 1954 | J. D. Birkett | Director of Veterinary Services | Civil Establishment | — | — |
| 1955 | J. D. Birkett | Director of Veterinary Services | Civil Establishment | — | — |
| 1956 | J. D. Birkett | Director of Veterinary Services | Civil Establishment | — | — |
| 1957 | J. D. Birkett | Director of Veterinary Services | Civil Establishment | — | — |
| 1958 | J. D. Birkett | Director of Veterinary Services | Civil Establishment | — | — |
| 1959 | J. D. Birkett | Director of Veterinary Services | Civil Establishment | — | — |
| 1960 | J. D. Birkett | Director of Veterinary Services | Civil Establishment | — | — |

### Deterministic checks: `birkett_j-d_b1918` vs `Birkett, J. D___Sierra Leone___1953`

- [PASS] surname_gate: bio 'BIRKETT' vs stint 'Birkett, J. D' (exact)
- [PASS] initials: bio ['J', 'D'] ~ stint ['J', 'D']
- [PASS] age_gate: stint starts 1953, birth 1918 (age 35)
- [PASS] colony: 1 placed event(s) resolve to 'Sierra Leone'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1953-1960
- [FAIL] position_sim: best 18 vs bar 60: 'D.V.S.' ~ 'Director of Veterinary Services'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

