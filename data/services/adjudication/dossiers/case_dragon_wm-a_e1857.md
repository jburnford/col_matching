<!-- {"case_id": "case_dragon_wm-a_e1857", "bio_ids": ["dragon_wm-a_e1857"], "stint_ids": ["Dragon, W. A___Straits Settlements___1877"]} -->
# Dossier case_dragon_wm-a_e1857

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `dragon_wm-a_e1857`

- Printed name: **DRAGON, WM. A.**
- Birth year: not printed
- Appears in editions: [1883, 1886, 1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1883-L27250.v` — printed in editions [1883, 1886, 1888, 1889]:**

> DRAGON, WM. A.—March 1 to August 31, 1857, acting assistant clerk, land department, P. W. Island; Sept. 1, 1857, to Sept. 29, 1861, assistant clerk resident, councillor's office; May 1, 1861, to Nov. 21, 1862, assistant clerk, land department, province Wellesley; November 22, 1862, to March 31, 1867, chief clerk, resident councillor's office; April 1, 1867, to Dec. 31, 1869, chief clerk lieutenant-governor's office; confirmed June, 1878.

**Version `col1890-L33711.v` — printed in editions [1890]:**

> DRAGON, Wm. A.—Acting assistant clerk, land department, Penang, 1857; assistant clerk resident, councillor's office, 1857; assistant clerk, land department, province Wellesley, 1861; chief clerk, resident councillor's office, 1862; chief clerk, lieutenant-governor's office, 1878; actg. postmaster-general, Penang, 1888.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1857–1857 | acting assistant clerk, land department | Prince of Wales Island | [1883, 1886, 1888, 1889, 1890] |
| 1 | 1857–1861 | assistant clerk resident, councillor's office | — | [1883, 1886, 1888, 1889, 1890] |
| 2 | 1861–1862 | assistant clerk, land department | Province Wellesley | [1883, 1886, 1888, 1889, 1890] |
| 3 | 1862–1867 | chief clerk, resident councillor's office | — | [1883, 1886, 1888, 1889, 1890] |
| 4 | 1867–1869 | chief clerk lieutenant-governor's office | — | [1883, 1886, 1888, 1889] |
| 5 | 1878–1878 | confirmed | — | [1883, 1886, 1888, 1889] |
| 6 | 1878 | chief clerk, lieutenant-governor's office | — | [1890] |
| 7 | 1888 | actg. postmaster-general, Penang | — | [1890] |

## Candidate stint `Dragon, W. A___Straits Settlements___1877`

- Staff-list name: **Dragon, W. A** | colony: **Straits Settlements** | listed 1877–1888 | editions [1877, 1879, 1880, 1888]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | W. Dragon | Chief Clerk | Police | — | — |
| 1879 | W. A. Dragon | Chief Clerk | PENANG | — | — |
| 1880 | W. A. Dragon | Chief Clerk | Penang | — | — |
| 1888 | W. A. Dragon | Chief Clerk | Penang | — | — |

### Deterministic checks: `dragon_wm-a_e1857` vs `Dragon, W. A___Straits Settlements___1877`

- [PASS] surname_gate: bio 'DRAGON' vs stint 'Dragon, W. A' (exact)
- [PASS] initials: bio ['W', 'A'] ~ stint ['W', 'A']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
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

