<!-- {"case_id": "case_curnow_f-n_e1864", "bio_ids": ["curnow_f-n_e1864"], "stint_ids": ["Curnow, F___Queensland___1886"]} -->
# Dossier case_curnow_f-n_e1864

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `curnow_f-n_e1864`

- Printed name: **CURNOW, F. N**
- Birth year: not printed
- Appears in editions: [1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1888-L32913.v` — printed in editions [1888, 1889, 1890]:**

> CURNOW, F. N.—District clerk and paymaster, roads department, Ipswich, Queensland, Mar., 1864; organising railway store department from Nov., 1865; railway storekeeper, June, 1866; also administrator, locomotive branch, June, 1876; chief clerk of railways, Jan., 1877; acting commissioner for railways, Jan., 1884; confirmed Mar., 1885.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1864 | District clerk and paymaster, roads department, Ipswich | Queensland | [1888, 1889, 1890] |
| 1 | 1865 | organising railway store department from | Queensland *(inherited from previous clause)* | [1888, 1889, 1890] |
| 2 | 1866 | railway storekeeper | Queensland *(inherited from previous clause)* | [1888, 1889, 1890] |
| 3 | 1876 | also administrator, locomotive branch | Queensland *(inherited from previous clause)* | [1888, 1889, 1890] |
| 4 | 1877 | chief clerk of railways | Queensland *(inherited from previous clause)* | [1888, 1889, 1890] |
| 5 | 1884 | acting commissioner for railways | Queensland *(inherited from previous clause)* | [1888, 1889, 1890] |
| 6 | 1885 | confirmed | Queensland *(inherited from previous clause)* | [1888, 1889, 1890] |

## Candidate stint `Curnow, F___Queensland___1886`

- Staff-list name: **Curnow, F** | colony: **Queensland** | listed 1886–1889 | editions [1886, 1888, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1886 | F. Curnow | Commissioner for Railways | Department of Public Works | — | — |
| 1888 | F. Curnow | Commissioner for Railways | Public Works and Mines | — | — |
| 1889 | F. Curnow | Commissioner for Railways | Department of Railways | — | — |

### Deterministic checks: `curnow_f-n_e1864` vs `Curnow, F___Queensland___1886`

- [PASS] surname_gate: bio 'CURNOW' vs stint 'Curnow, F' (exact)
- [PASS] initials: bio ['F', 'N'] ~ stint ['F']
- [PASS] age_gate: stint starts 1886; no printed birth year — UNCHECKED
- [PASS] colony: 7 placed event(s) resolve to 'Queensland'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1886-1889
- [PASS] position_sim: best 100 vs bar 60: 'acting commissioner for railways' ~ 'Commissioner for Railways'
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

