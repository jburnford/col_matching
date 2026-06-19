<!-- {"case_id": "case_hutton_alexander-mcdonald-bruce_b1904", "bio_ids": ["hutton_alexander-mcdonald-bruce_b1904"], "stint_ids": ["Hutton, A. B___Antigua___1921"]} -->
# Dossier case_hutton_alexander-mcdonald-bruce_b1904

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 24 official(s) with this surname in the graph's staff lists; 12 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hutton_alexander-mcdonald-bruce_b1904`

- Printed name: **HUTTON, ALEXANDER MCDONALD BRUCE**
- Birth year: 1904 (attested in editions [1933])
- Appears in editions: [1933]

### Verbatim printed entry text (OCR)

**Version `col1933-L60910.v` — printed in editions [1933]:**

> HUTTON, ALEXANDER MCDONALD BRUCE.—B. 1904; ed. St. Andrew's Coll., Grahamstown, S.A.; Univ. Coll., Oxford; B.A. (English lit.); cadet, Tanganyika Territory, Jan., 1926; asst. dist. offr., Jan., 1928; ag. dist. offr., May, 1932.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | cadet, Tanganyika Territory | Tanganyika | [1933] |
| 1 | 1928 | asst. dist. offr | Tanganyika *(inherited from previous clause)* | [1933] |
| 2 | 1932 | ag. dist. offr | Tanganyika *(inherited from previous clause)* | [1933] |

## Candidate stint `Hutton, A. B___Antigua___1921`

- Staff-list name: **Hutton, A. B** | colony: **Antigua** | listed 1921–1929 | editions [1921, 1929]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | A. B. Hutton | Moravian Supt. | Clergy | — | — |
| 1929 | A. B. Hutton | Moravian Supt. | Clergy | — | — |

### Deterministic checks: `hutton_alexander-mcdonald-bruce_b1904` vs `Hutton, A. B___Antigua___1921`

- [PASS] surname_gate: bio 'HUTTON' vs stint 'Hutton, A. B' (exact)
- [PASS] initials: bio ['A', 'M', 'B'] ~ stint ['A', 'B']
- [PASS] age_gate: stint starts 1921, birth 1904 (age 17)
- [FAIL] colony: no placed event resolves to 'Antigua'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1921-1929
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

