<!-- {"case_id": "case_bassett_william-eric_b1901", "bio_ids": ["bassett_william-eric_b1901"], "stint_ids": ["Bassett, William E___Leeward Islands___1933"]} -->
# Dossier case_bassett_william-eric_b1901

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bassett_william-eric_b1901`

- Printed name: **BASSETT, William Eric**
- Birth year: 1901 (attested in editions [1948, 1949, 1950, 1951, 1953, 1954])
- Honours: M.B.E. (1949)
- Appears in editions: [1948, 1949, 1950, 1951, 1953, 1954]

### Verbatim printed entry text (OCR)

**Version `col1948-L31023.v` — printed in editions [1948, 1949, 1950, 1951, 1953, 1954]:**

> BASSETT, William Eric, M.B.E. (1949).—b. 1901; trained at Royal Botanic Gdns., Kew; asst. supt., Victoria bot. gdns., Br. Cams., 1927; asst. agric. offr., Dominica, Leeward Is., 1932; curator, agric. dept., Montserrat, 1838; supt., 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | asst. supt., Victoria bot. gdns. | British Cameroons | [1948, 1949, 1950, 1951, 1953, 1954] |
| 1 | 1932 | asst. agric. offr. | Dominica, Leeward Islands | [1948, 1949, 1950, 1951, 1953, 1954] |
| 2 | 1938 | curator, agric. dept. | Montserrat | [1948, 1949, 1950, 1951, 1953, 1954] |
| 3 | 1946 | supt. | — | [1948, 1949, 1950, 1951, 1953, 1954] |

## Candidate stint `Bassett, William E___Leeward Islands___1933`

- Staff-list name: **Bassett, William E** | colony: **Leeward Islands** | listed 1933–1954 | editions [1933, 1936, 1939, 1940, 1948, 1949, 1950, 1951, 1952, 1953, 1954]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | W. E. Bassett | Assistant Agricultural Officer | Agriculture | — | — |
| 1936 | W. E. Bassett | Assistant Agricultural Officers | Agriculture | — | — |
| 1939 | W. E. Bassett | Curator | Agricultural Department | — | — |
| 1940 | W. E. Bassett | Curator | Agricultural Department | — | — |
| 1948 | W. E. Bassett | Agricultural Officer | Executive Council | — | — |
| 1949 | W. E. Bassett | Agricultural Officer | AGRICULTURE | — | — |
| 1949 | W. E. Bassett | Agricultural Superintendent | Executive Council | — | — |
| 1950 | W. E. Bassett | Agricultural Superintendent | Executive Council | — | — |
| 1950 | W. E. Bassett | Agricultural Officer | AGRICULTURE | — | — |
| 1951 | William E. Bassett | Agricultural Officer | Agriculture | — | — |
| 1951 | W. E. Bassett | Agricultural Superintendent | Executive Council | — | — |
| 1952 | W. E. Bassett | Agricultural Officer | Civil Establishment | — | — |
| 1952 | W. E. Bassett | Agricultural Officer | Executive Council | — | — |
| 1953 | W. E. Bassett | Agricultural Superintendent | Civil Establishment | — | — |
| 1954 | W. E. Bassett | Agricultural Superintendent | Civil Establishment | — | — |

### Deterministic checks: `bassett_william-eric_b1901` vs `Bassett, William E___Leeward Islands___1933`

- [PASS] surname_gate: bio 'BASSETT' vs stint 'Bassett, William E' (exact)
- [PASS] initials: bio ['W', 'E'] ~ stint ['W', 'E']
- [PASS] age_gate: stint starts 1933, birth 1901 (age 32)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
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

