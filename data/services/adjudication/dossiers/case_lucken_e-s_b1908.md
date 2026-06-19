<!-- {"case_id": "case_lucken_e-s_b1908", "bio_ids": ["lucken_e-s_b1908"], "stint_ids": ["Lucken, E. S___Hong Kong___1950"]} -->
# Dossier case_lucken_e-s_b1908

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `lucken_e-s_b1908`

- Printed name: **LUCKEN, E. S**
- Birth year: 1908 (attested in editions [1960, 1961, 1962, 1963, 1964])
- Appears in editions: [1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1960-L25423.v` — printed in editions [1960, 1961, 1962, 1963, 1964]:**

> LUCKEN, Miss E. S.—b. 1908; ed. London Univ.; English lect., govt. women's trng. coll., Pal., 1946; educ. offr., H.K., 1948-63.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | English lect., govt. women's trng. coll. | Palestine | [1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Lucken, E. S___Hong Kong___1950`

- Staff-list name: **Lucken, E. S** | colony: **Hong Kong** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | E. S. Lucken | Mistresses | Education | — | — |
| 1951 | E. S. Lucken | Mistresses | Education | — | — |

### Deterministic checks: `lucken_e-s_b1908` vs `Lucken, E. S___Hong Kong___1950`

- [PASS] surname_gate: bio 'LUCKEN' vs stint 'Lucken, E. S' (exact)
- [PASS] initials: bio ['E', 'S'] ~ stint ['E', 'S']
- [PASS] age_gate: stint starts 1950, birth 1908 (age 42)
- [FAIL] colony: no placed event resolves to 'Hong Kong'
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

