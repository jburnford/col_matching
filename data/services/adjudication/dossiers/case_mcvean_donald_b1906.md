<!-- {"case_id": "case_mcvean_donald_b1906", "bio_ids": ["mcvean_donald_b1906"], "stint_ids": ["McVean, D___British Somaliland___1952", "McVean, D___Cyprus___1955"]} -->
# Dossier case_mcvean_donald_b1906

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['mcvean_donald_b1906'] carry a single initial only — the namesake trap applies.

## Biography `mcvean_donald_b1906`

- Printed name: **McVEAN, Donald**
- Birth year: 1906 (attested in editions [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960])
- Honours: A.M.I.C.E, M.I.H.E
- Appears in editions: [1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960]

### Verbatim printed entry text (OCR)

**Version `col1953-L18340.v` — printed in editions [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960]:**

> McVEAN, D.—b. 1906; ed. Royal Tech. Coll., Glasgow; engrn., Glasgow Corpn., 1925; exec. engrn., Nyasa., 1940; D.P.W., Som., 1951; Cyp., 1954–59.

**Version `col1951-L40567.v` — printed in editions [1951]:**

> McVEAN, Donald, A.M.I.C.E., A.M.I. Mun.E., M.I.H.E.—b. 1906; ed. Royal Tech. Coll., Glasgow; engnr., Glasgow Corp., 1925; exec. engnr., Nyasa., 1940.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1925 | engrn., Glasgow Corpn | — | [1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960] |
| 1 | 1940 | exec. engrn. | Nyasaland | [1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960] |
| 2 | 1951 | D.P.W. | Somaliland | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960] |
| 3 | 1954–1959 | D.P.W. | Cyprus | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960] |

## Candidate stint `McVean, D___British Somaliland___1952`

- Staff-list name: **McVean, D** | colony: **British Somaliland** | listed 1952–1954 | editions [1952, 1953, 1954]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1952 | D. McVean | Director of Public Works | Civil Establishment | — | — |
| 1953 | D. McVean | Director of Public Works | Civil Establishment | — | — |
| 1954 | D. McVean | Director of Public Works | Civil Establishment | — | — |

### Deterministic checks: `mcvean_donald_b1906` vs `McVean, D___British Somaliland___1952`

- [PASS] surname_gate: bio 'McVEAN' vs stint 'McVean, D' (exact)
- [PASS] initials: bio ['D'] ~ stint ['D']
- [PASS] age_gate: stint starts 1952, birth 1906 (age 46)
- [PASS] colony: 1 placed event(s) resolve to 'British Somaliland'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1952-1954
- [FAIL] position_sim: best 22 vs bar 60: 'D.P.W.' ~ 'Director of Public Works'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `McVean, D___Cyprus___1955`

- Staff-list name: **McVean, D** | colony: **Cyprus** | listed 1955–1958 | editions [1955, 1956, 1957, 1958]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1955 | D. McVean | Director of Public Works | Civil Establishment | — | — |
| 1956 | D. McVean | Director of Public Works | Civil Establishment | — | — |
| 1957 | D. McVean | Director of Public Works | Civil Establishment | — | — |
| 1958 | D. McVean | Director of Public Works | Civil Establishment | — | — |

### Deterministic checks: `mcvean_donald_b1906` vs `McVean, D___Cyprus___1955`

- [PASS] surname_gate: bio 'McVEAN' vs stint 'McVean, D' (exact)
- [PASS] initials: bio ['D'] ~ stint ['D']
- [PASS] age_gate: stint starts 1955, birth 1906 (age 49)
- [PASS] colony: 1 placed event(s) resolve to 'Cyprus'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1955-1958
- [FAIL] position_sim: best 22 vs bar 60: 'D.P.W.' ~ 'Director of Public Works'
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

