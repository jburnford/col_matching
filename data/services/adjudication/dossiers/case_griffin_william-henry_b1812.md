<!-- {"case_id": "case_griffin_william-henry_b1812", "bio_ids": ["griffin_william-henry_b1812"], "stint_ids": ["Griffin, William H___Canada___1877"]} -->
# Dossier case_griffin_william-henry_b1812

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 40 official(s) with this surname in the graph's staff lists; 22 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `griffin_william-henry_b1812`

- Printed name: **GRIFFIN, WILLIAM HENRY**
- Birth year: 1812 (attested in editions [1888])
- Appears in editions: [1888]

### Verbatim printed entry text (OCR)

**Version `col1888-L33768.v` — printed in editions [1888]:**

> GRIFFIN, WILLIAM HENRY.—Born 7th Aug., 1812; entered Imperial public service as a clerk in the office of the deputy postmaster-general, Canada, 24th April, 1831; promoted to be surveyor of post offices east of Kingston, 1st May, 1835; appointed Secretary of post office on its transfer to provincial control, 1851; deputy postmaster-general, Canada, 12th June, 1857; deputy postmaster-general of the Dominion, 30th May, 1868; appointed a commissioner for the re-organization of the civil service, 1868; was also a member of the Civil Service Commission, 1862; has been a member of the board of audit since its first establishment, 1858, and of the board of customs, excise, and stamps, since 1864; negotiated the postal convention with the United States, 1875; is vice-president of the Civil Service League and Savings Society, and chairman of the Civil Service board.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1831–1831 | clerk in the office of the deputy postmaster-general | Canada | [1888] |
| 1 | 1835–1835 | surveyor of post offices east of Kingston | — | [1888] |
| 2 | 1851–1851 | Secretary of post office | — | [1888] |
| 3 | 1857–1857 | deputy postmaster-general | Canada | [1888] |
| 4 | 1858 | member of the board of audit | — | [1888] |
| 5 | 1862–1862 | member of the Civil Service Commission | — | [1888] |
| 6 | 1864 | member of the board of customs, excise, and stamps | — | [1888] |
| 7 | 1868–1868 | deputy postmaster-general of the Dominion | Canada | [1888] |
| 8 | 1868–1868 | commissioner for the re-organization of the civil service | — | [1888] |
| 9 | 1875–1875 | — | United States | [1888] |

## Candidate stint `Griffin, William H___Canada___1877`

- Staff-list name: **Griffin, William H** | colony: **Canada** | listed 1877–1888 | editions [1877, 1878, 1879, 1880, 1883, 1886, 1888]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | William H. Griffin | Deputy Postmaster-General | Post-Office Department | — | — |
| 1878 | William H. Griffin | Deputy Postmaster-General | Post-Office Department | — | — |
| 1879 | W. H. Griffin | Deputy Postmaster-General | POST-OFFICE DEPARTMENT | — | — |
| 1880 | W. H. Griffin | Deputy Postmaster-General | POST-OFFICE DEPARTMENT. | — | — |
| 1883 | W. H. Griffin | Deputy Postmaster-General | Post Office Department | — | — |
| 1886 | W. H. Griffin | Deputy Postmaster-General | Post Office Department | — | — |
| 1888 | W. H. Griffin | Deputy Postmaster-General | Post Office Department | — | — |

### Deterministic checks: `griffin_william-henry_b1812` vs `Griffin, William H___Canada___1877`

- [PASS] surname_gate: bio 'GRIFFIN' vs stint 'Griffin, William H' (exact)
- [PASS] initials: bio ['W', 'H'] ~ stint ['W', 'H']
- [PASS] age_gate: stint starts 1877, birth 1812 (age 65)
- [PASS] colony: 3 placed event(s) resolve to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1888
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

