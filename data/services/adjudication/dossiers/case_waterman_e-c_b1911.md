<!-- {"case_id": "case_waterman_e-c_b1911", "bio_ids": ["waterman_e-c_b1911"], "stint_ids": ["Waterman, E. C___West Indies Federation___1961"]} -->
# Dossier case_waterman_e-c_b1911

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `waterman_e-c_b1911`

- Printed name: **WATERMAN, E. C**
- Birth year: 1911 (attested in editions [1951, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964])
- Appears in editions: [1951, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1951-L43573.v` — printed in editions [1951, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]:**

> WATERMAN, E. C.—b. 1911; ed. St. Mary's Coll., Trin.; apptd. treasy., Trin., 1931; asst. acctnt., acctnt.-gen's dept., 1947; dep. acctnt.-gen., 1948; acctnt.-gen., 1953; dep. fin. sec., 1955; fin. advr., 1958; dep. fed'l fin. sec., T.W.I., 1960.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1931 | apptd. treasy. | Trinidad | [1951, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1947 | asst. acctnt., acctnt.-gen's dept | Trinidad *(inherited from previous clause)* | [1951, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 2 | 1948 | dep. acctnt.-gen | Trinidad *(inherited from previous clause)* | [1951, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 3 | 1953 | acctnt.-gen | Trinidad *(inherited from previous clause)* | [1951, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 4 | 1955 | dep. fin. sec | Trinidad *(inherited from previous clause)* | [1951, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 5 | 1958 | fin. advr | Trinidad *(inherited from previous clause)* | [1951, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 6 | 1960 | dep. fed'l fin. sec., T.W.I | Trinidad *(inherited from previous clause)* | [1951, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Waterman, E. C___West Indies Federation___1961`

- Staff-list name: **Waterman, E. C** | colony: **West Indies Federation** | listed 1961–1962 | editions [1961, 1962]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1961 | E. C. Waterman | Deputy Federal Financial Secretary | Civil Establishment | — | — |
| 1962 | E. C. Waterman | Deputy Federal Financial Secretary | Civil Establishment | — | — |

### Deterministic checks: `waterman_e-c_b1911` vs `Waterman, E. C___West Indies Federation___1961`

- [PASS] surname_gate: bio 'WATERMAN' vs stint 'Waterman, E. C' (exact)
- [PASS] initials: bio ['E', 'C'] ~ stint ['E', 'C']
- [PASS] age_gate: stint starts 1961, birth 1911 (age 50)
- [FAIL] colony: no placed event resolves to 'West Indies Federation'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1961-1962
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

