<!-- {"case_id": "calib_gemini_fiji_0143", "bio_ids": ["warner_f-e-m_b1906"], "stint_ids": ["Warner, F. E. M___Fiji___1950", "Warner, F. E. M___Fiji___1958"]} -->
# Dossier calib_gemini_fiji_0143

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 79 official(s) with this surname in the graph's staff lists; 16 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `warner_f-e-m_b1906`

- Printed name: **WARNER, F. E. M**
- Birth year: 1906 (attested in editions [1963, 1964, 1966])
- Honours: M.B.E (1957)
- Appears in editions: [1963, 1964, 1966]

### Verbatim printed entry text (OCR)

**Version `col1963-L26042.v` — printed in editions [1963, 1964, 1966]:**

> WARNER, F. E. M., M.B.E. (1957).—b. 1906; ed. Bedford Sch., clk., Fiji, 1944; marketing offr., 1947; asst. registr., co-op. socs., 1951; registr., 1957.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947 | marketing offr | — | [1963, 1964, 1966] |
| 1 | 1951 | asst. registr., co-op. socs | — | [1963, 1964, 1966] |
| 2 | 1957 | registr | — | [1963, 1964, 1966] |

## Candidate stint `Warner, F. E. M___Fiji___1950`

- Staff-list name: **Warner, F. E. M** | colony: **Fiji** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | F. E. M. Warner | Marketing Officer | AGRICULTURE | — | — |
| 1951 | F. E. M. Warner | Marketing Officer | AGRICULTURE | — | — |

### Deterministic checks: `warner_f-e-m_b1906` vs `Warner, F. E. M___Fiji___1950`

- [PASS] surname_gate: bio 'WARNER' vs stint 'Warner, F. E. M' (exact)
- [PASS] initials: bio ['F', 'E', 'M'] ~ stint ['F', 'E', 'M']
- [PASS] age_gate: stint starts 1950, birth 1906 (age 44)
- [FAIL] colony: no placed event resolves to 'Fiji'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1950-1951
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Warner, F. E. M___Fiji___1958`

- Staff-list name: **Warner, F. E. M** | colony: **Fiji** | listed 1958–1966 | editions [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1958 | F. E. M. Warner | Registrar of Co-operatives | Civil Establishment | — | — |
| 1959 | F. E. M. Warner | Registrar of Co-operatives | Civil Establishment | — | — |
| 1960 | F. E. M. Warner | Registrar of Co-operatives | Civil Establishment | — | — |
| 1961 | F. E. M. Warner | Registrar of Co-operatives | Civil Establishment | — | — |
| 1962 | F. E. M. Warner | Registrar of Co-operatives | Civil Establishment | — | — |
| 1963 | F. E. M. Warner | Registrar of Co-operatives | Civil Establishment | — | — |
| 1964 | F. E. M. Warner | Registrar of Co-operatives | Civil Establishment | — | — |
| 1965 | F. E. M. Warner | Registrar of Co-operatives | Civil Establishment | — | — |
| 1966 | F. E. M. Warner | Registrar of Co-operatives | Civil Establishment | — | — |

### Deterministic checks: `warner_f-e-m_b1906` vs `Warner, F. E. M___Fiji___1958`

- [PASS] surname_gate: bio 'WARNER' vs stint 'Warner, F. E. M' (exact)
- [PASS] initials: bio ['F', 'E', 'M'] ~ stint ['F', 'E', 'M']
- [PASS] age_gate: stint starts 1958, birth 1906 (age 52)
- [FAIL] colony: no placed event resolves to 'Fiji'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1958-1966
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

