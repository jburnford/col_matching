<!-- {"case_id": "case_coghill_j-d-mackey_e1867", "bio_ids": ["coghill_j-d-mackey_e1867"], "stint_ids": ["Coghill, J. D. M___Ceylon___1877"]} -->
# Dossier case_coghill_j-d-mackey_e1867

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `coghill_j-d-mackey_e1867`

- Printed name: **COGHILL, J. D. MACKEY**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L26908.v` — printed in editions [1883]:**

> COGHILL, J. D. MACKEY, M.D., C.M., L.R.C.P. Edinburgh, L.F.P.S.G., and L.M.—Assistant colonial surgeon, second class, Matéla, Ceylon, 29th Dec., 1867; transferred to medical charge of the Colombo convict establishments at Welikada and Huttadur, police, and judicial duties, 17th Sept., 1869; superintendent of the convict establishments, Ceylon, 1871; formerly assistant surgeon, and surgeon 2nd royal Lanarkshire militia, during embodiment; lately medical officer imperial Chinese maritime customs, Hankow; proceeded on special service to the Straits Settlements, 1878, in connection with the outbreak of cholera; resumed duties as medical inspector of coffee districts, 1874.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1867 | Assistant colonial surgeon, second class | Ceylon | [1883] |
| 1 | 1869 | medical charge of the Colombo convict establishments at Welikada and Huttadur, police, and judicial duties | Ceylon | [1883] |
| 2 | 1871 | superintendent of the convict establishments | Ceylon | [1883] |
| 3 | 1874 | medical inspector of coffee districts | — | [1883] |
| 4 | 1878 | special service | Straits Settlements | [1883] |

## Candidate stint `Coghill, J. D. M___Ceylon___1877`

- Staff-list name: **Coghill, J. D. M** | colony: **Ceylon** | listed 1877–1880 | editions [1877, 1878, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | J. D. M. Coghill | Medical Inspector, Coffee Districts | Medical Department | — | — |
| 1878 | J. D. M. Coghill | Medical Inspector, Coffee Districts | Medical Department | — | — |
| 1879 | J. D. M. Coghill | Medical Inspector, Coffee Districts | Medical Department | — | — |
| 1880 | J. D. M. Coghill | Medical Inspector, Coffee Districts | Medical Department | — | — |

### Deterministic checks: `coghill_j-d-mackey_e1867` vs `Coghill, J. D. M___Ceylon___1877`

- [PASS] surname_gate: bio 'COGHILL' vs stint 'Coghill, J. D. M' (exact)
- [PASS] initials: bio ['J', 'D', 'M'] ~ stint ['J', 'D', 'M']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1880
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

