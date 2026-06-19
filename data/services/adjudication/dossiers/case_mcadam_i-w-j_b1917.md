<!-- {"case_id": "case_mcadam_i-w-j_b1917", "bio_ids": ["mcadam_i-w-j_b1917"], "stint_ids": ["McAdam, I. W. J___Uganda___1949"]} -->
# Dossier case_mcadam_i-w-j_b1917

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mcadam_i-w-j_b1917`

- Printed name: **McADAM, I. W. J**
- Birth year: 1917 (attested in editions [1958, 1959, 1960, 1961])
- Honours: O.B.E (1960)
- Appears in editions: [1958, 1959, 1960, 1961]

### Verbatim printed entry text (OCR)

**Version `col1958-L24799.v` — printed in editions [1958, 1959, 1960, 1961]:**

> McADAM, I. W. J., O.B.E. (1960).—b. 1917; ed. Plumtree Sch., S. Rhod., Edin. and Camb. Univs.; M.O., Uga., 1946; specialist (surgeon) 1948; senr. specialist, 1957-60.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | M.O. | Uganda | [1958, 1959, 1960, 1961] |
| 1 | 1948 | specialist (surgeon) | Uganda *(inherited from previous clause)* | [1958, 1959, 1960, 1961] |
| 2 | 1957–1960 | senr. specialist | Uganda *(inherited from previous clause)* | [1958, 1959, 1960, 1961] |

## Candidate stint `McAdam, I. W. J___Uganda___1949`

- Staff-list name: **McAdam, I. W. J** | colony: **Uganda** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | I. W. J. McAdam | Surgeons | Medical | — | — |
| 1951 | I. W. J. McAdam | Surgeons | MEDICAL | — | — |

### Deterministic checks: `mcadam_i-w-j_b1917` vs `McAdam, I. W. J___Uganda___1949`

- [PASS] surname_gate: bio 'McADAM' vs stint 'McAdam, I. W. J' (exact)
- [PASS] initials: bio ['I', 'W', 'J'] ~ stint ['I', 'W', 'J']
- [PASS] age_gate: stint starts 1949, birth 1917 (age 32)
- [PASS] colony: 3 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 54 vs bar 60: 'specialist (surgeon)' ~ 'Surgeons'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

