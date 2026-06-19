<!-- {"case_id": "case_rowbotham_edwin-ramsay_b1906", "bio_ids": ["rowbotham_edwin-ramsay_b1906"], "stint_ids": ["Rowbotham, E. R___Windward Islands___1950"]} -->
# Dossier case_rowbotham_edwin-ramsay_b1906

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `rowbotham_edwin-ramsay_b1906`

- Printed name: **ROWBOTHAM, Edwin Ramsay**
- Birth year: 1906 (attested in editions [1949, 1950, 1951])
- Appears in editions: [1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1949-L35370.v` — printed in editions [1949, 1950, 1951]:**

> ROWBOTHAM, Edwin Ramsay.—b. 1906; ed. Radley Coll. and Christ's Coll., Camb., B.A. (hon.); M.A. (Cantab.); on mil. serv., 1939-46, lt.-col.; dir. of wks., Dominica, 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947 | dir. of wks. | Dominica | [1949, 1950, 1951] |

## Candidate stint `Rowbotham, E. R___Windward Islands___1950`

- Staff-list name: **Rowbotham, E. R** | colony: **Windward Islands** | listed 1950–1952 | editions [1950, 1952]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | E. R. Rowbotham | Director of Works | Public Works | — | — |
| 1952 | E. R. Rowbotham | Director of Works | Civil Establishment | — | Lieut.-Col. |

### Deterministic checks: `rowbotham_edwin-ramsay_b1906` vs `Rowbotham, E. R___Windward Islands___1950`

- [PASS] surname_gate: bio 'ROWBOTHAM' vs stint 'Rowbotham, E. R' (exact)
- [PASS] initials: bio ['E', 'R'] ~ stint ['E', 'R']
- [PASS] age_gate: stint starts 1950, birth 1906 (age 44)
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1950-1952
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

