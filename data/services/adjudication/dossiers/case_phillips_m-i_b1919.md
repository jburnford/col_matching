<!-- {"case_id": "case_phillips_m-i_b1919", "bio_ids": ["phillips_m-i_b1919"], "stint_ids": ["Phillips, M. I___Barbados___1963"]} -->
# Dossier case_phillips_m-i_b1919

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 119 official(s) with this surname in the graph's staff lists; 54 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `phillips_m-i_b1919`

- Printed name: **PHILLIPS, M. I**
- Birth year: 1919 (attested in editions [1959, 1960, 1961, 1962])
- Appears in editions: [1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1959-L26847.v` — printed in editions [1959, 1960, 1961, 1962]:**

> PHILLIPS, M. I.—b. 1919; ed. Harrison Coll., Barb.; clk., Barb., 1938; asst. sec., 1954; acctnt.-gen., 1958.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1938 | clk. | Barbados | [1959, 1960, 1961, 1962] |
| 1 | 1954 | asst. sec | Barbados *(inherited from previous clause)* | [1959, 1960, 1961, 1962] |
| 2 | 1958 | acctnt.-gen | Barbados *(inherited from previous clause)* | [1959, 1960, 1961, 1962] |

## Candidate stint `Phillips, M. I___Barbados___1963`

- Staff-list name: **Phillips, M. I** | colony: **Barbados** | listed 1963–1965 | editions [1963, 1964, 1965]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1963 | M. I. Phillips | Accountant General | Civil Establishment | — | — |
| 1964 | M. I. Phillips | Accountant General | Civil Establishment | — | — |
| 1965 | M. I. Phillips | Accountant General | Civil Establishment | — | — |

### Deterministic checks: `phillips_m-i_b1919` vs `Phillips, M. I___Barbados___1963`

- [PASS] surname_gate: bio 'PHILLIPS' vs stint 'Phillips, M. I' (exact)
- [PASS] initials: bio ['M', 'I'] ~ stint ['M', 'I']
- [PASS] age_gate: stint starts 1963, birth 1919 (age 44)
- [PASS] colony: 3 placed event(s) resolve to 'Barbados'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1963-1965
- [PASS] position_sim: best 67 vs bar 60: 'acctnt.-gen' ~ 'Accountant General'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

