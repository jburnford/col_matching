<!-- {"case_id": "case_trench_r-le-poer_e1880", "bio_ids": ["trench_r-le-poer_e1880"], "stint_ids": ["Trench, R. Le Poer___Victoria___1879"]} -->
# Dossier case_trench_r-le-poer_e1880

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `trench_r-le-poer_e1880`

- Printed name: **TRENCH, R. Le Poer**
- Birth year: not printed
- Appears in editions: [1886, 1888, 1889, 1890, 1894, 1896, 1898]

### Verbatim printed entry text (OCR)

**Version `col1886-L36028.v` — printed in editions [1886, 1888, 1889, 1890, 1894, 1896, 1898]:**

> TRENCH, Hon. R. Le Poer.—County court judge, Victoria, 1st April, 1880.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1880 | County court judge | Victoria | [1886, 1888, 1889, 1890, 1894, 1896, 1898] |

## Candidate stint `Trench, R. Le Poer___Victoria___1879`

- Staff-list name: **Trench, R. Le Poer** | colony: **Victoria** | listed 1879–1883 | editions [1879, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1879 | R. Le Poer Trench | Chief Commissioner | Land Tax Commission | — | — |
| 1883 | R. Le Poer Trench | Chief Commissioner | Land Tax Commission | — | — |

### Deterministic checks: `trench_r-le-poer_e1880` vs `Trench, R. Le Poer___Victoria___1879`

- [PASS] surname_gate: bio 'TRENCH' vs stint 'Trench, R. Le Poer' (exact)
- [PASS] initials: bio ['R', 'L', 'P'] ~ stint ['R', 'L', 'P']
- [PASS] age_gate: stint starts 1879; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Victoria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1879-1883
- [FAIL] position_sim: best 28 vs bar 60: 'County court judge' ~ 'Chief Commissioner'
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

