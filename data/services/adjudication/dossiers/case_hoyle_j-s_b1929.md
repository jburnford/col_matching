<!-- {"case_id": "case_hoyle_j-s_b1929", "bio_ids": ["hoyle_j-s_b1929"], "stint_ids": ["Hoyle, J___Uganda___1949"]} -->
# Dossier case_hoyle_j-s_b1929

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hoyle_j-s_b1929`

- Printed name: **HOYLE, J. S.**
- Birth year: 1929 (attested in editions [1964, 1965, 1966])
- Appears in editions: [1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1964-L18244.v` — printed in editions [1964, 1965, 1966]:**

> HOYLE, J. S.—b. 1929; ed. Wallington County Gram. Sch. and London Univ.; mil. serv., 1948-49, R.A.F.; ed. offr., Uga., 1953. (Uga. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1948–1949 | mil. serv. | — | [1964, 1965, 1966] |
| 1 | 1953 | ed. offr. | Uganda | [1964, 1965, 1966] |

## Candidate stint `Hoyle, J___Uganda___1949`

- Staff-list name: **Hoyle, J** | colony: **Uganda** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | J. Hoyle | Assistant Hospital Superintendent | Medical | — | — |
| 1951 | J. Hoyle | Assistant Hospital Superintendent | MEDICAL | — | — |

### Deterministic checks: `hoyle_j-s_b1929` vs `Hoyle, J___Uganda___1949`

- [PASS] surname_gate: bio 'HOYLE' vs stint 'Hoyle, J' (exact)
- [PASS] initials: bio ['J', 'S'] ~ stint ['J']
- [PASS] age_gate: stint starts 1949, birth 1929 (age 20)
- [PASS] colony: 1 placed event(s) resolve to 'Uganda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
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

