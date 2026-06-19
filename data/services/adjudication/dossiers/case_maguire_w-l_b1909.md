<!-- {"case_id": "case_maguire_w-l_b1909", "bio_ids": ["maguire_w-l_b1909"], "stint_ids": ["Maguire, W. L___Leeward Islands___1951"]} -->
# Dossier case_maguire_w-l_b1909

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `maguire_w-l_b1909`

- Printed name: **MAGUIRE, W. L**
- Birth year: 1909 (attested in editions [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1961, 1962, 1963, 1964, 1965, 1966])
- Honours: M.B.E (1963)
- Appears in editions: [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1953-L18348.v` — printed in editions [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1961, 1962, 1963, 1964, 1965, 1966]:**

> MAGUIRE, W. L., M.B.E. (1963).—b. 1909; ed. Antigua Gram. Sch.; asst. clk., Antigua, 1928; junr. clk., 1934; senr. clk., 1943; prin., 1947; city clk., 1949; postmtr., 1953; warden, Nevis, 1959.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | asst. clk. | Antigua | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1934 | junr. clk | Antigua *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1943 | senr. clk | Antigua *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1947 | prin | Antigua *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1961, 1962, 1963, 1964, 1965, 1966] |
| 4 | 1949 | city clk | Antigua *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1961, 1962, 1963, 1964, 1965, 1966] |
| 5 | 1953 | postmtr | Antigua *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1961, 1962, 1963, 1964, 1965, 1966] |
| 6 | 1959 | warden | Nevis | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Maguire, W. L___Leeward Islands___1951`

- Staff-list name: **Maguire, W. L** | colony: **Leeward Islands** | listed 1951–1957 | editions [1951, 1953, 1954, 1955, 1956, 1957]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1951 | W. L. Maguire | City Clerk | MUNICIPAL | — | — |
| 1953 | W. L. Maguire | City Clerk | Civil Establishment | — | — |
| 1954 | W. L. Maguire | Postmaster | Civil Establishment | — | — |
| 1955 | W. L. Maguire | Postmaster | Civil Establishment | — | — |
| 1956 | W. L. Maguire | Postmaster | Civil Establishment | — | — |
| 1957 | W. L. Maguire | Postmaster | Civil Establishment | — | — |

### Deterministic checks: `maguire_w-l_b1909` vs `Maguire, W. L___Leeward Islands___1951`

- [PASS] surname_gate: bio 'MAGUIRE' vs stint 'Maguire, W. L' (exact)
- [PASS] initials: bio ['W', 'L'] ~ stint ['W', 'L']
- [PASS] age_gate: stint starts 1951, birth 1909 (age 42)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1951-1957
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

