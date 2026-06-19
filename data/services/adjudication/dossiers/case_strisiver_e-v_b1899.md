<!-- {"case_id": "case_strisiver_e-v_b1899", "bio_ids": ["strisiver_e-v_b1899"], "stint_ids": ["Strisiver, E. V___Sierra Leone___1950"]} -->
# Dossier case_strisiver_e-v_b1899

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `strisiver_e-v_b1899`

- Printed name: **STRISIVER, E. V**
- Birth year: 1899 (attested in editions [1964, 1965, 1966])
- Appears in editions: [1956, 1957, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1964-L22156.v` — printed in editions [1964, 1965, 1966]:**

> STRISIVER, E. V.—b. 1899; ed. Edin., Glasgow and Berlin; med. supt., St. Kitts-Nevis, 1939; M.O., S. Leone, 1948; surgical specialist, 1953; retd., 1956; re-empld. contract, specialist M.O., Trin., 1956. (Trin. Govt. service.)

**Version `col1956-L24405.v` — printed in editions [1956, 1957]:**

> STRISIVER, E. V.—b. 1899; ed. Edin., Glasgow and Berlin; med. supt., St. Kitts-Nevis, 1939; M.O., S. Leone, 1948; surgical specialist, 1953.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1939 | med. supt., St. Kitts-Nevis | — | [1956, 1957, 1964, 1965, 1966] |
| 1 | 1948 | M.O., S. Leone | — | [1956, 1957, 1964, 1965, 1966] |
| 2 | 1953 | surgical specialist | — | [1956, 1957, 1964, 1965, 1966] |
| 3 | 1956 | retd | — | [1964, 1965, 1966] |
| 4 | 1956 | re-empld. contract, specialist M.O. | Trinidad | [1964, 1965, 1966] |

## Candidate stint `Strisiver, E. V___Sierra Leone___1950`

- Staff-list name: **Strisiver, E. V** | colony: **Sierra Leone** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | E. V. Strisiver | Medical Officer | Medical | — | — |
| 1951 | E. V. Strisiver | Medical Officer | Medical | — | — |

### Deterministic checks: `strisiver_e-v_b1899` vs `Strisiver, E. V___Sierra Leone___1950`

- [PASS] surname_gate: bio 'STRISIVER' vs stint 'Strisiver, E. V' (exact)
- [PASS] initials: bio ['E', 'V'] ~ stint ['E', 'V']
- [PASS] age_gate: stint starts 1950, birth 1899 (age 51)
- [FAIL] colony: no placed event resolves to 'Sierra Leone'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1950-1951
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

