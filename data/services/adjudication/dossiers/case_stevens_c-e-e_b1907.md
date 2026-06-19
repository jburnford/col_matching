<!-- {"case_id": "case_stevens_c-e-e_b1907", "bio_ids": ["stevens_c-e-e_b1907"], "stint_ids": ["Stevens, C. E. E___Leeward Islands___1950"]} -->
# Dossier case_stevens_c-e-e_b1907

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 66 official(s) with this surname in the graph's staff lists; 28 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `stevens_c-e-e_b1907`

- Printed name: **STEVENS, C. E. E**
- Birth year: 1907 (attested in editions [1953, 1954, 1955, 1956, 1957, 1958, 1959])
- Honours: M.B.E (1956)
- Appears in editions: [1953, 1954, 1955, 1956, 1957, 1958, 1959]

### Verbatim printed entry text (OCR)

**Version `col1953-L19153.v` — printed in editions [1953, 1954, 1955, 1956, 1957, 1958, 1959]:**

> STEVENS, C. E. E., M.B.E. (1956).—b. 1907; ed. Antigua Gram. Sch. and Queen's Univ., Belfast; M.O., Leeward Is., 1934; med. supt., Cunningham Hosp., St. Kitts, 1949-58.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1934 | M.O., Leeward Is | — | [1953, 1954, 1955, 1956, 1957, 1958, 1959] |
| 1 | 1949–1958 | med. supt., Cunningham Hosp. | St. Kitts | [1953, 1954, 1955, 1956, 1957, 1958, 1959] |

## Candidate stint `Stevens, C. E. E___Leeward Islands___1950`

- Staff-list name: **Stevens, C. E. E** | colony: **Leeward Islands** | listed 1950–1957 | editions [1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | C. E. E. Stevens | Medical Superintendent, Cunningham Hospital, St. Kitts | HEALTH | — | — |
| 1951 | C. E. E. Stevens | Medical Superintendent, Cunningham Hospital, St. Kitts | HEALTH | — | — |
| 1952 | C. E. E. Stevens | Medical Superintendent, Cunningham Hospital, St. Kitts | Civil Establishment | — | — |
| 1953 | C. E. Stevens | Medical Superintendent | Civil Establishment | — | — |
| 1954 | C. E. E. Stevens | Medical Superintendent, Cunningham Hospital, St. Kitts | Civil Establishment | — | — |
| 1955 | C. E. E. Stevens | Medical Superintendent | Civil Establishment | — | — |
| 1956 | C. E. E. Stevens | Medical Superintendent | Civil Establishment | — | — |
| 1957 | C. E. E. Stevens | Medical Superintendent | Civil Establishment | — | — |

### Deterministic checks: `stevens_c-e-e_b1907` vs `Stevens, C. E. E___Leeward Islands___1950`

- [PASS] surname_gate: bio 'STEVENS' vs stint 'Stevens, C. E. E' (exact)
- [PASS] initials: bio ['C', 'E', 'E'] ~ stint ['C', 'E', 'E']
- [PASS] age_gate: stint starts 1950, birth 1907 (age 43)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1950-1957
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

