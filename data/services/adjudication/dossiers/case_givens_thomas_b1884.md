<!-- {"case_id": "case_givens_thomas_b1884", "bio_ids": ["givens_thomas_b1884"], "stint_ids": ["Givens, T___Commonwealth Of Australia___1905"]} -->
# Dossier case_givens_thomas_b1884

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['givens_thomas_b1884'] carry a single initial only — the namesake trap applies.

## Biography `givens_thomas_b1884`

- Printed name: **GIVENS, THOMAS**
- Birth year: 1884 (attested in editions [1915, 1917, 1918, 1919])
- Appears in editions: [1915, 1917, 1918, 1919]

### Verbatim printed entry text (OCR)

**Version `col1915-L47255.v` — printed in editions [1915, 1917, 1918, 1919]:**

> GIVENS, HON. THOMAS.—B. 1884; elected M.L.A., Queensland, 1899; senator for Queensland in Commonwealth parl., 1903; pres. of senate since 9th July, 1913.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1899 | elected M.L.A. | Queensland | [1915, 1917, 1918, 1919] |
| 1 | 1903 | senator for Queensland in Commonwealth parl | Queensland *(inherited from previous clause)* | [1915, 1917, 1918, 1919] |
| 2 | 1913 | pres. of senate since | Queensland *(inherited from previous clause)* | [1915, 1917, 1918, 1919] |

## Candidate stint `Givens, T___Commonwealth Of Australia___1905`

- Staff-list name: **Givens, T** | colony: **Commonwealth Of Australia** | listed 1905–1907 | editions [1905, 1907]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | T. Givens | Senator | Senate | — | — |
| 1907 | T. Givens | Senator | Senate | — | — |

### Deterministic checks: `givens_thomas_b1884` vs `Givens, T___Commonwealth Of Australia___1905`

- [PASS] surname_gate: bio 'GIVENS' vs stint 'Givens, T' (exact)
- [PASS] initials: bio ['T'] ~ stint ['T']
- [PASS] age_gate: stint starts 1905, birth 1884 (age 21)
- [FAIL] colony: no placed event resolves to 'Commonwealth Of Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1907
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

