<!-- {"case_id": "case_peterswald_w-j_e1873", "bio_ids": ["peterswald_w-j_e1873"], "stint_ids": ["Peterswald, William J___South Australia___1877", "Peterswald, William J___South Australia___1888"]} -->
# Dossier case_peterswald_w-j_e1873

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `peterswald_w-j_e1873`

- Printed name: **PETERSWALD, W. J**
- Birth year: not printed
- Appears in editions: [1886, 1888, 1889, 1890, 1894, 1896]

### Verbatim printed entry text (OCR)

**Version `col1886-L35263.v` — printed in editions [1886, 1888, 1889, 1890, 1894, 1896]:**

> PETERSWALD, W. J.—Commissioner of police, South Australia, 20 Aug., 1873.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1873 | Commissioner of police | South Australia | [1886, 1888, 1889, 1890, 1894, 1896] |

## Candidate stint `Peterswald, William J___South Australia___1877`

- Staff-list name: **Peterswald, William J** | colony: **South Australia** | listed 1877–1880 | editions [1877, 1878, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | W. J. Peterswald | Superintendent of Foot Police | Police Department | — | — |
| 1878 | W. J. Peterswald | Superintendent of Foot Police | Police Department | — | — |
| 1879 | W. J. Peterswald | Superintendent of Foot Police | Police Department | — | — |
| 1880 | W. J. Peterswald | Superintendent of Foot Police | Police Department | — | — |

### Deterministic checks: `peterswald_w-j_e1873` vs `Peterswald, William J___South Australia___1877`

- [PASS] surname_gate: bio 'PETERSWALD' vs stint 'Peterswald, William J' (exact)
- [PASS] initials: bio ['W', 'J'] ~ stint ['W', 'J']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'South Australia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1880
- [FAIL] position_sim: best 59 vs bar 60: 'Commissioner of police' ~ 'Superintendent of Foot Police'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Peterswald, William J___South Australia___1888`

- Staff-list name: **Peterswald, William J** | colony: **South Australia** | listed 1888–1897 | editions [1888, 1890, 1894, 1896, 1897]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | William J. Peterswald | Commissioner of Police | Police Department | — | — |
| 1890 | W. J. Peterswald J.P. | Commissioner of Police | Police Department | — | — |
| 1894 | W. J. Peterswald | Commissioner of Police | Police Department | — | — |
| 1896 | W. J. Peterswald J.P. | Commissioner of Police | Police Department | — | — |
| 1897 | William J. Peterswald J. P. | Commissioner of Police | Police Department | — | — |

### Deterministic checks: `peterswald_w-j_e1873` vs `Peterswald, William J___South Australia___1888`

- [PASS] surname_gate: bio 'PETERSWALD' vs stint 'Peterswald, William J' (exact)
- [PASS] initials: bio ['W', 'J'] ~ stint ['W', 'J']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'South Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1888-1897
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

