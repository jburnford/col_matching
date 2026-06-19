<!-- {"case_id": "case_burch_j_b1917", "bio_ids": ["burch_j_b1917"], "stint_ids": ["Birch, J. P___Uganda___1933"]} -->
# Dossier case_burch_j_b1917

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 28 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['burch_j_b1917'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Birch, J. P___Uganda___1933` is also gate-compatible with biography(ies) outside this case: ['birch_john-pryor_b1908'] (already linked elsewhere or filtered).

## Biography `burch_j_b1917`

- Printed name: **BURCH, J**
- Birth year: 1917 (attested in editions [1957, 1958, 1959, 1960, 1961, 1963, 1964])
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1957-L21563.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1963, 1964]:**

> BURCH, J.—b. 1917; ed. Bishops Stortford Gram. Sch. and City of London Sch.; acctnt., acctnt.-gen's. dept., Nig., 1948; senr., 1951; prin. acctnt., treasy., N. Nig., 1954; dep. acctnt.-gen., 1958; acctnt.-gen., 1960-63. (Nig. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1948 | acctnt., acctnt.-gen's. dept. | Nigeria | [1957, 1958, 1959, 1960, 1961, 1963, 1964] |
| 1 | 1951 | senr | Nigeria *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1963, 1964] |
| 2 | 1954 | prin. acctnt., treasy. | Northern Nigeria | [1957, 1958, 1959, 1960, 1961, 1963, 1964] |
| 3 | 1958 | dep. acctnt.-gen | Northern Nigeria *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1963, 1964] |
| 4 | 1960–1963 | acctnt.-gen | Northern Nigeria *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1963, 1964] |

## Candidate stint `Birch, J. P___Uganda___1933`

- Staff-list name: **Birch, J. P** | colony: **Uganda** | listed 1933–1954 | editions [1933, 1936, 1937, 1939, 1940, 1949, 1951, 1952, 1953, 1954]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | J. P. Birch | Cadets | Provincial Administration | — | — |
| 1936 | J. P. Birch | Administrative Officer | Civil Establishment | — | — |
| 1937 | J. P. Birch | District Officers and Assistant District Officers | Provincial Administration | — | — |
| 1939 | J. P. Birch | District Officer | Provincial Administration | — | — |
| 1940 | J. P. Birch | District Officers and Assistant District Officers | Provincial Administration | — | — |
| 1949 | J. P. Birch | District Officers and Assistant District Officers | Provincial Administration | — | — |
| 1951 | J. P. Birch | District Officers and Assistant District Officers | Provincial Administration | — | — |
| 1952 | J. P. Birch | Resident | Civil Establishment | — | — |
| 1953 | J. P. Birch | Resident, Buganda | Civil Establishment | — | — |
| 1954 | J. P. Birch | Resident, Buganda | Civil Establishment | — | — |

### Deterministic checks: `burch_j_b1917` vs `Birch, J. P___Uganda___1933`

- [PASS] surname_gate: bio 'BURCH' vs stint 'Birch, J. P' (fuzzy:1)
- [PASS] initials: bio ['J'] ~ stint ['J', 'P']
- [PASS] age_gate: stint starts 1933, birth 1917 (age 16)
- [FAIL] colony: no placed event resolves to 'Uganda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1933-1954
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

