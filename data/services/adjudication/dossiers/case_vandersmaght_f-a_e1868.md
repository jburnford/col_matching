<!-- {"case_id": "case_vandersmaght_f-a_e1868", "bio_ids": ["vandersmaght_f-a_e1868", "vandersmaght_f-a_e1868-2"], "stint_ids": ["Van Dersmagt, F. A___Ceylon___1877"]} -->
# Dossier case_vandersmaght_f-a_e1868

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Van Dersmagt, F. A___Ceylon___1877'] have more than one claimant biography in this case.
- Phase 1 found `vandersmaght_f-a_e1868` ↔ `Van Dersmagt, F. A___Ceylon___1877` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- Phase 1 found `vandersmaght_f-a_e1868-2` ↔ `Van Dersmagt, F. A___Ceylon___1877` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).

## Biography `vandersmaght_f-a_e1868`

- Printed name: **VANDERSMAGHT, F. A**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L29834.v` — printed in editions [1883]:**

> VANDERSMAGHT, F. A., M.D.—Assistant colonial surgeon, Ceylon, 1868.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1868 | Assistant colonial surgeon | Ceylon | [1883] |

## Biography `vandersmaght_f-a_e1868-2`

- Printed name: **VANDERSMAGHT, F. A**
- Birth year: not printed
- Appears in editions: [1886, 1888, 1890, 1896]

### Verbatim printed entry text (OCR)

**Version `col1886-L36088.v` — printed in editions [1886, 1888, 1890, 1896]:**

> VANDERSMAGHT, F. A., M.D.—Assistant colonial surgeon, Ceylon, 1868; acting colonial surgeon, July, 1882.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1868 | Assistant colonial surgeon | Ceylon | [1886, 1888, 1890, 1896] |
| 1 | 1882 | acting colonial surgeon | Ceylon *(inherited from previous clause)* | [1886, 1888, 1890, 1896] |

## Candidate stint `Van Dersmagt, F. A___Ceylon___1877`

- Staff-list name: **Van Dersmagt, F. A** | colony: **Ceylon** | listed 1877–1880 | editions [1877, 1878, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | F. A. Van Dersmagt | Assistant Colonial Surgeons | Medical Department | — | — |
| 1878 | F. A. Van Dersmagt | Assistant Colonial Surgeons | Medical Department | — | — |
| 1879 | F. A. Van Dersmagt | Assistant Colonial Surgeons | Medical Department | — | — |
| 1880 | F. A. Van Dersmagt | Assistant Colonial Surgeons | Medical Department | — | — |

### Deterministic checks: `vandersmaght_f-a_e1868` vs `Van Dersmagt, F. A___Ceylon___1877`

- [PASS] surname_gate: bio 'VANDERSMAGHT' vs stint 'Van Dersmagt, F. A' (fuzzy:2)
- [PASS] initials: bio ['F', 'A'] ~ stint ['F', 'A']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1880
- [PASS] position_sim: best 98 vs bar 60: 'Assistant colonial surgeon' ~ 'Assistant Colonial Surgeons'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `vandersmaght_f-a_e1868-2` vs `Van Dersmagt, F. A___Ceylon___1877`

- [PASS] surname_gate: bio 'VANDERSMAGHT' vs stint 'Van Dersmagt, F. A' (fuzzy:2)
- [PASS] initials: bio ['F', 'A'] ~ stint ['F', 'A']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1880
- [PASS] position_sim: best 98 vs bar 60: 'Assistant colonial surgeon' ~ 'Assistant Colonial Surgeons'
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

