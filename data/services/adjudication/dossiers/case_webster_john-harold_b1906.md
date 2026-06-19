<!-- {"case_id": "case_webster_john-harold_b1906", "bio_ids": ["webster_john-harold_b1906"], "stint_ids": ["Webster, J. H___Tanganyika___1952", "Webster, J. L. H___Kenya___1949"]} -->
# Dossier case_webster_john-harold_b1906

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 44 official(s) with this surname in the graph's staff lists; 21 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Webster, J. H___Tanganyika___1952` is also gate-compatible with biography(ies) outside this case: ['webster_j-l-h_b1913'] (already linked elsewhere or filtered).
- NOTE: stint `Webster, J. L. H___Kenya___1949` is also gate-compatible with biography(ies) outside this case: ['webster_j-l-h_b1913'] (already linked elsewhere or filtered).

## Biography `webster_john-harold_b1906`

- Printed name: **WEBSTER, John Harold**
- Birth year: 1906 (attested in editions [1948, 1949, 1950, 1951, 1953])
- Appears in editions: [1948, 1949, 1950, 1951, 1953]

### Verbatim printed entry text (OCR)

**Version `col1948-L36740.v` — printed in editions [1948, 1949, 1950, 1951, 1953]:**

> WEBSTER, John Harold.—b. 1906 ; ed. Marlborough Coll. and Merton Coll., Oxford, B.A., solvr., sup. ct., Eng. ; asst. land offr., T.T., 1937 ; dep. cust. of enemy prop., 1942 ; conveyancer and regitr. of titles, Uga., 1947 ; admin.-gen., Tang., 1950.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1937 | asst. land offr., T.T | — | [1948, 1949, 1950, 1951, 1953] |
| 1 | 1942 | dep. cust. of enemy prop | — | [1948, 1949, 1950, 1951, 1953] |
| 2 | 1947 | conveyancer and regitr. of titles | Uganda | [1948, 1949, 1950, 1951, 1953] |
| 3 | 1950 | admin.-gen. | Tanganyika | [1948, 1949, 1950, 1951, 1953] |

## Candidate stint `Webster, J. H___Tanganyika___1952`

- Staff-list name: **Webster, J. H** | colony: **Tanganyika** | listed 1952–1953 | editions [1952, 1953]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1952 | J. H. Webster | Administrator General | Civil Establishment | — | — |
| 1953 | J. H. Webster | Administrator-General | Civil Establishment | — | — |

### Deterministic checks: `webster_john-harold_b1906` vs `Webster, J. H___Tanganyika___1952`

- [PASS] surname_gate: bio 'WEBSTER' vs stint 'Webster, J. H' (exact)
- [PASS] initials: bio ['J', 'H'] ~ stint ['J', 'H']
- [PASS] age_gate: stint starts 1952, birth 1906 (age 46)
- [PASS] colony: 1 placed event(s) resolve to 'Tanganyika'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1952-1953
- [FAIL] position_sim: best 57 vs bar 60: 'admin.-gen.' ~ 'Administrator-General'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): 1 agreeing edition-year(s) [1953] pos~57 (bar: >=2)
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Webster, J. L. H___Kenya___1949`

- Staff-list name: **Webster, J. L. H** | colony: **Kenya** | listed 1949–1954 | editions [1949, 1951, 1953, 1954]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | J. L. H. Webster | Assistant Secretary | Secretariat | — | — |
| 1951 | J. L. H. Webster | Secretary | Development and Reconstruction Authority (Headquarters) | — | — |
| 1953 | J. L. H. Webster | Secretary, Development and Reconstruction Authority | Civil Establishment | — | — |
| 1954 | J. L. H. Webster | Secretary for Legal Affairs | Civil Establishment | — | — |

### Deterministic checks: `webster_john-harold_b1906` vs `Webster, J. L. H___Kenya___1949`

- [PASS] surname_gate: bio 'WEBSTER' vs stint 'Webster, J. L. H' (exact)
- [PASS] initials: bio ['J', 'H'] ~ stint ['J', 'L', 'H']
- [PASS] age_gate: stint starts 1949, birth 1906 (age 43)
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1954
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

