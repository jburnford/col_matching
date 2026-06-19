<!-- {"case_id": "case_parry_t_b1905", "bio_ids": ["parry_t_b1905"], "stint_ids": ["Parry, R. T___Antigua___1965"]} -->
# Dossier case_parry_t_b1905

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 21 official(s) with this surname in the graph's staff lists; 14 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['parry_t_b1905'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Parry, R. T___Antigua___1965` is also gate-compatible with biography(ies) outside this case: ['parry_r-t_b1902'] (already linked elsewhere or filtered).

## Biography `parry_t_b1905`

- Printed name: **PARRY, T**
- Birth year: 1905 (attested in editions [1958, 1959, 1960, 1961, 1962])
- Appears in editions: [1958, 1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1958-L25845.v` — printed in editions [1958, 1959, 1960, 1961, 1962]:**

> PARRY, T.—b. 1905; ed. Finchley Gram. Sch.; P.R.O., Uga., 1946; asst. dir., inf., 1952-61.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | P.R.O. | Uganda | [1958, 1959, 1960, 1961, 1962] |
| 1 | 1952–1961 | asst. dir., inf | Uganda *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962] |

## Candidate stint `Parry, R. T___Antigua___1965`

- Staff-list name: **Parry, R. T** | colony: **Antigua** | listed 1965–1966 | editions [1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1965 | R. T. Parry | Director of Electricity | Civil Establishment | — | — |
| 1966 | R. T. Parry | Director of Electricity | Civil Establishment | — | — |

### Deterministic checks: `parry_t_b1905` vs `Parry, R. T___Antigua___1965`

- [PASS] surname_gate: bio 'PARRY' vs stint 'Parry, R. T' (exact)
- [PASS] initials: bio ['T'] ~ stint ['R', 'T']
- [PASS] age_gate: stint starts 1965, birth 1905 (age 60)
- [FAIL] colony: no placed event resolves to 'Antigua'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1965-1966
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

