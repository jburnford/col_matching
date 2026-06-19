<!-- {"case_id": "case_grieve_w_b1912", "bio_ids": ["grieve_w_b1912"], "stint_ids": ["Grieve, D. W___Gambia___1949"]} -->
# Dossier case_grieve_w_b1912

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['grieve_w_b1912'] carry a single initial only — the namesake trap applies.

## Biography `grieve_w_b1912`

- Printed name: **GRIEVE, W**
- Birth year: 1912 (attested in editions [1964, 1965, 1966])
- Appears in editions: [1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1964-L17606.v` — printed in editions [1964, 1965, 1966]:**

> GRIEVE, W.—b. 1912; surv. of ships, H.K., 1950; asst. dir. marine, 1962.

**Version `col1963-L20359.v` — printed in editions [1963]:**

> GRIEVE, W.—b. 1912; surv. of ships, H.K., 1950.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1950 | surv. of ships | Hong Kong | [1963, 1964, 1965, 1966] |
| 1 | 1962 | asst. dir. marine | Hong Kong *(inherited from previous clause)* | [1964, 1965, 1966] |

## Candidate stint `Grieve, D. W___Gambia___1949`

- Staff-list name: **Grieve, D. W** | colony: **Gambia** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | D. W. Grieve | Education Officer (Principal, Armitage School) | EDUCATION | — | — |
| 1950 | D. W. Grieve | Education Officers | Education | — | — |
| 1951 | D. W. Grieve | Education Officer | Education | — | — |

### Deterministic checks: `grieve_w_b1912` vs `Grieve, D. W___Gambia___1949`

- [PASS] surname_gate: bio 'GRIEVE' vs stint 'Grieve, D. W' (exact)
- [PASS] initials: bio ['W'] ~ stint ['D', 'W']
- [PASS] age_gate: stint starts 1949, birth 1912 (age 37)
- [FAIL] colony: no placed event resolves to 'Gambia'
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

