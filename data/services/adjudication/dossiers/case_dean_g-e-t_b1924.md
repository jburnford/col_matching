<!-- {"case_id": "case_dean_g-e-t_b1924", "bio_ids": ["dean_g-e-t_b1924"], "stint_ids": ["Dean, G. E. T___Brunei___1956"]} -->
# Dossier case_dean_g-e-t_b1924

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 18 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `dean_g-e-t_b1924`

- Printed name: **DEAN, G. E. T**
- Birth year: 1924 (attested in editions [1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1962-L20348.v` — printed in editions [1962, 1963, 1964, 1965, 1966]:**

> DEAN, G. E. T.—b. 1924; ed. East Ham Gram. Sch.; asst. audr., N.B., 1951; audr., 1954; audr., Sarawak, 1955; state audr., Brun., 1955; senr. audr., Mal., 1956; senr. audr., Ken., 1959–65. (Ken. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1951 | asst. audr., N.B | — | [1962, 1963, 1964, 1965, 1966] |
| 1 | 1954 | audr | — | [1962, 1963, 1964, 1965, 1966] |
| 2 | 1955 | audr. | Sarawak | [1962, 1963, 1964, 1965, 1966] |
| 3 | 1956 | senr. audr. | Malaya | [1962, 1963, 1964, 1965, 1966] |
| 4 | 1959–1965 | senr. audr. | Kenya | [1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Dean, G. E. T___Brunei___1956`

- Staff-list name: **Dean, G. E. T** | colony: **Brunei** | listed 1956–1958 | editions [1956, 1957, 1958]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1956 | G. E. T. Dean | State Auditor | Civil Establishment | — | — |
| 1957 | G. E. T. Dean | State Auditor | Civil Establishment | — | — |
| 1958 | G. E. T. Dean | State Auditor | Civil Establishment | — | — |

### Deterministic checks: `dean_g-e-t_b1924` vs `Dean, G. E. T___Brunei___1956`

- [PASS] surname_gate: bio 'DEAN' vs stint 'Dean, G. E. T' (exact)
- [PASS] initials: bio ['G', 'E', 'T'] ~ stint ['G', 'E', 'T']
- [PASS] age_gate: stint starts 1956, birth 1924 (age 32)
- [FAIL] colony: no placed event resolves to 'Brunei'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1956-1958
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

