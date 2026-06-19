<!-- {"case_id": "case_deravin_eugene-e_e1893", "bio_ids": ["deravin_eugene-e_e1893"], "stint_ids": ["Deravin, E___Leeward Islands___1897", "Deravin, E___St Christopher and Nevis___1896"]} -->
# Dossier case_deravin_eugene-e_e1893

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `deravin_eugene-e_e1893`

- Printed name: **DERAVIN, EUGENE E**
- Birth year: not printed
- Appears in editions: [1905, 1906, 1908, 1909, 1910]

### Verbatim printed entry text (OCR)

**Version `col1906-L45118.v` — printed in editions [1906, 1908, 1909, 1910]:**

> DERAVIN, EUGENE E.—Rev. offr., St. Kitts, 1893; 1st rev. and excise offr., 1897; ag. asst. treas., Sept., 1904, and June, 1905.

**Version `col1905-L42869.v` — printed in editions [1905]:**

> DERAVIN, EUGENE E.—Rev. offr., St. Kitts, 1893; 1st rev. and excise offr., 1897.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1893 | Rev. offr. | St. Kitts | [1905, 1906, 1908, 1909, 1910] |
| 1 | 1897 | 1st rev. and excise offr | St. Kitts *(inherited from previous clause)* | [1905, 1906, 1908, 1909, 1910] |
| 2 | 1904 | ag. asst. treas | St. Kitts *(inherited from previous clause)* | [1906, 1908, 1909, 1910] |
| 3 | 1905 | ag. asst. treas | St. Kitts *(inherited from previous clause)* | [1906, 1908, 1909, 1910] |

## Candidate stint `Deravin, E___Leeward Islands___1897`

- Staff-list name: **Deravin, E** | colony: **Leeward Islands** | listed 1897–1908 | editions [1897, 1899, 1900, 1905, 1906, 1907, 1908]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1897 | E. Deravin | Assistant Revenue Officer | Treasury | — | — |
| 1899 | E. Deravin | Revenue Officer | Treasury | — | — |
| 1900 | E. Deravin | 1st Revenue Officer | Treasury | — | — |
| 1905 | E. Deravin | Revenue Officer (St. Kitts) | Treasury and Customs | — | — |
| 1906 | E. Deravin | Revenue Officer (St. Kitts) | Treasury and Customs | — | — |
| 1907 | E. Deravin | Revenue Officer | Treasury and Customs | — | — |
| 1908 | E. Deravin | Revenue Officer | Treasury and Customs | — | — |

### Deterministic checks: `deravin_eugene-e_e1893` vs `Deravin, E___Leeward Islands___1897`

- [PASS] surname_gate: bio 'DERAVIN' vs stint 'Deravin, E' (exact)
- [PASS] initials: bio ['E', 'E'] ~ stint ['E']
- [PASS] age_gate: stint starts 1897; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1897-1908
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Deravin, E___St Christopher and Nevis___1896`

- Staff-list name: **Deravin, E** | colony: **St Christopher and Nevis** | listed 1896–1910 | editions [1896, 1898, 1910]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1896 | E. Deravin | 3rd Revenue Officer | Treasury | — | — |
| 1898 | E. Deravin | 1st Revenue Officer | Treasury | — | — |
| 1910 | E. Deravin | Revenue Officers (St. Kitts) | Treasury and Customs | — | — |

### Deterministic checks: `deravin_eugene-e_e1893` vs `Deravin, E___St Christopher and Nevis___1896`

- [PASS] surname_gate: bio 'DERAVIN' vs stint 'Deravin, E' (exact)
- [PASS] initials: bio ['E', 'E'] ~ stint ['E']
- [PASS] age_gate: stint starts 1896; no printed birth year — UNCHECKED
- [PASS] colony: 4 placed event(s) resolve to 'St Christopher and Nevis'
- [PASS] tenure_overlap: 4 event tenure(s) overlap stint years 1896-1910
- [FAIL] position_sim: best 59 vs bar 60: 'Rev. offr.' ~ '1st Revenue Officer'
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

