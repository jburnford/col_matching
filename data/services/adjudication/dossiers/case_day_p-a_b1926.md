<!-- {"case_id": "case_day_p-a_b1926", "bio_ids": ["day_p-a_b1926"], "stint_ids": ["Day, P. A___St Helena___1959", "Day, P. A___St Helena___1963"]} -->
# Dossier case_day_p-a_b1926

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 47 official(s) with this surname in the graph's staff lists; 13 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `day_p-a_b1926`

- Printed name: **DAY, P. A**
- Birth year: 1926 (attested in editions [1960, 1961, 1963, 1964, 1965, 1966])
- Honours: M.B.E (1965)
- Appears in editions: [1960, 1961, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1960-L22215.v` — printed in editions [1960, 1961, 1963, 1964, 1965, 1966]:**

> DAY, P. A., M.B.E. (1965).—b. 1926; ed. King's Coll., Taunton, St. John's Coll., Oxford and Edin. Univ.; mil. serv., 1944-47, R.N.; dist. offr., Tang., 1953; secon. admnr., Tristan da Cunha, 1959-61; re-apptd. admnr., Tristan da Cunha, 1963-65.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1953 | dist. offr. | Tanganyika | [1960, 1961, 1963, 1964, 1965, 1966] |
| 1 | 1959–1961 | secon. admnr. | Tristan da Cunha | [1960, 1961, 1963, 1964, 1965, 1966] |
| 2 | 1963–1965 | re-apptd. admnr. | Tristan da Cunha | [1960, 1961, 1963, 1964, 1965, 1966] |

## Candidate stint `Day, P. A___St Helena___1959`

- Staff-list name: **Day, P. A** | colony: **St Helena** | listed 1959–1960 | editions [1959, 1960]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1959 | P. A. Day | Designated | — | — | — |
| 1960 | P. A. Day | Administrator | Civil Establishment | — | — |

### Deterministic checks: `day_p-a_b1926` vs `Day, P. A___St Helena___1959`

- [PASS] surname_gate: bio 'DAY' vs stint 'Day, P. A' (exact)
- [PASS] initials: bio ['P', 'A'] ~ stint ['P', 'A']
- [PASS] age_gate: stint starts 1959, birth 1926 (age 33)
- [FAIL] colony: no placed event resolves to 'St Helena'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1959-1960
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Day, P. A___St Helena___1963`

- Staff-list name: **Day, P. A** | colony: **St Helena** | listed 1963–1965 | editions [1963, 1964, 1965]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1963 | P. A. Day | Administrator | — | — | — |
| 1964 | P. A. Day | Administrator | Tristan da Cunha | — | — |
| 1965 | Mr. P. A. Day | Administrator | Tristan da Cunha | — | — |

### Deterministic checks: `day_p-a_b1926` vs `Day, P. A___St Helena___1963`

- [PASS] surname_gate: bio 'DAY' vs stint 'Day, P. A' (exact)
- [PASS] initials: bio ['P', 'A'] ~ stint ['P', 'A']
- [PASS] age_gate: stint starts 1963, birth 1926 (age 37)
- [FAIL] colony: no placed event resolves to 'St Helena'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1963-1965
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

