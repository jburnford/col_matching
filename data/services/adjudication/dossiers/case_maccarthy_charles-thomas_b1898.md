<!-- {"case_id": "case_maccarthy_charles-thomas_b1898", "bio_ids": ["maccarthy_charles-thomas_b1898"], "stint_ids": ["MacCarthy, C. T___Straits Settlements___1931"]} -->
# Dossier case_maccarthy_charles-thomas_b1898

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `maccarthy_charles-thomas_b1898`

- Printed name: **MACCARTHY, CHARLES THOMAS**
- Birth year: 1898 (attested in editions [1940])
- Honours: M.A, M.B
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L66291.v` — printed in editions [1940]:**

> MACCARTHY, CHARLES THOMAS, M.A., M.B., Ch.B., B.A.O. (Trinity Coll., Dublin), D.M.R.E. (Camb.).—B. 1898; M.O., Malaya, Dec., 1927; M.O. and radiologist, Seremban, Oct., 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | M.O. | Malaya | [1940] |
| 1 | 1937 | M.O. and radiologist, Seremban | Malaya *(inherited from previous clause)* | [1940] |

## Candidate stint `MacCarthy, C. T___Straits Settlements___1931`

- Staff-list name: **MacCarthy, C. T** | colony: **Straits Settlements** | listed 1931–1933 | editions [1931, 1932, 1933]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | C. T. MacCarthy | Medical Officer | Medical | — | — |
| 1932 | C. T. MacCarthy | Medical Officer | Medical | — | — |
| 1933 | C. T. MacCarthy | Medical Officer | Medical | — | — |

### Deterministic checks: `maccarthy_charles-thomas_b1898` vs `MacCarthy, C. T___Straits Settlements___1931`

- [PASS] surname_gate: bio 'MACCARTHY' vs stint 'MacCarthy, C. T' (exact)
- [PASS] initials: bio ['C', 'T'] ~ stint ['C', 'T']
- [PASS] age_gate: stint starts 1931, birth 1898 (age 33)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1933
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

