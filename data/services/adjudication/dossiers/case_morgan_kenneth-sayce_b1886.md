<!-- {"case_id": "case_morgan_kenneth-sayce_b1886", "bio_ids": ["morgan_kenneth-sayce_b1886"], "stint_ids": ["Morgan, S___British Guiana___1905"]} -->
# Dossier case_morgan_kenneth-sayce_b1886

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 85 official(s) with this surname in the graph's staff lists; 36 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `morgan_kenneth-sayce_b1886`

- Printed name: **MORGAN, KENNETH SAYCE**
- Birth year: 1886 (attested in editions [1939, 1940])
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L69206.v` — printed in editions [1939, 1940]:**

> MORGAN, MAJOR KENNETH SAYCE.—B. 1886; ed. City of Lond. Sch.; astt. supt., sp. br., Singapore, Feb., 1936.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1936 | astt. supt., sp. br. | Singapore | [1939, 1940] |

## Candidate stint `Morgan, S___British Guiana___1905`

- Staff-list name: **Morgan, S** | colony: **British Guiana** | listed 1905–1908 | editions [1905, 1906, 1907, 1908]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | S. Morgan | Chainbearers | Department of Lands and Mines | — | — |
| 1906 | S. Morgan | Chainbearers | Department of Lands and Mines | — | — |
| 1907 | S. Morgan | Chainbearer | Department of Lands and Mines | — | — |
| 1908 | S. Morgan | Chainbearer | Department of Lands and Mines | — | — |

### Deterministic checks: `morgan_kenneth-sayce_b1886` vs `Morgan, S___British Guiana___1905`

- [PASS] surname_gate: bio 'MORGAN' vs stint 'Morgan, S' (exact)
- [PASS] initials: bio ['K', 'S'] ~ stint ['S']
- [PASS] age_gate: stint starts 1905, birth 1886 (age 19)
- [FAIL] colony: no placed event resolves to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1908
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

