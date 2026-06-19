<!-- {"case_id": "case_jolly_j-m_b1927", "bio_ids": ["jolly_j-m_b1927"], "stint_ids": ["Jolly, J___Hong Kong___1949"]} -->
# Dossier case_jolly_j-m_b1927

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Jolly, J___Hong Kong___1949` is also gate-compatible with biography(ies) outside this case: ['jolly_james_b1902', 'jolly_john-william_b1899'] (already linked elsewhere or filtered).

## Biography `jolly_j-m_b1927`

- Printed name: **JOLLY, J. M**
- Birth year: 1927 (attested in editions [1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1960-L24691.v` — printed in editions [1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> JOLLY, J. M.—b. 1927; ed. Barker Coll., Sydney; asst. comsnr., customs, N. Borneo, 1949–65.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1949–1965 | asst. comsnr., customs | North Borneo | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Jolly, J___Hong Kong___1949`

- Staff-list name: **Jolly, J** | colony: **Hong Kong** | listed 1949–1957 | editions [1949, 1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | J. Jolly | Harbour Master | HARBOUR | — | — |
| 1950 | J. Jolly | Director of Marine | Marine | — | — |
| 1951 | J. Jolly | Director of Marine | Marine | — | — |
| 1952 | J. Jolly | Director of Marine | Civil Establishment | — | — |
| 1953 | J. Jolly | Director of Marine | Civil Establishment | C.B.E. | — |
| 1954 | J. Jolly | Director of Marine | Civil Establishment | — | — |
| 1955 | J. Jolly | Director of Marine | Civil Establishment | C.B.E., R.D. | — |
| 1956 | J. Jolly | Director of Marine | Civil Establishment | C.M.G. | — |
| 1957 | J. Jolly | Director of Marine | Civil Establishment | C.M.G. | — |

### Deterministic checks: `jolly_j-m_b1927` vs `Jolly, J___Hong Kong___1949`

- [PASS] surname_gate: bio 'JOLLY' vs stint 'Jolly, J' (exact)
- [PASS] initials: bio ['J', 'M'] ~ stint ['J']
- [PASS] age_gate: stint starts 1949, birth 1927 (age 22)
- [FAIL] colony: no placed event resolves to 'Hong Kong'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1957
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

