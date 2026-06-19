<!-- {"case_id": "case_scarte_william-bain_e1895", "bio_ids": ["scarte_william-bain_e1895"], "stint_ids": ["Scarth, W. B___Canada___1888"]} -->
# Dossier case_scarte_william-bain_e1895

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Scarth, W. B___Canada___1888` is also gate-compatible with biography(ies) outside this case: ['scarth_william-bain_e1895'] (already linked elsewhere or filtered).

## Biography `scarte_william-bain_e1895`

- Printed name: **SCARTE, WILLIAM BAIN**
- Birth year: not printed
- Appears in editions: [1905]

### Verbatim printed entry text (OCR)

**Version `col1905-L45717.v` — printed in editions [1905]:**

> SCARTE, WILLIAM BAIN.—Dep. min. of agricnl. and statistics, Canada, Dec., 1895; dep. commnr. of patents, Mar., 1897.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1895 | Dep. min. of agricnl. and statistics | Canada | [1905] |
| 1 | 1897 | dep. commnr. of patents | Canada *(inherited from previous clause)* | [1905] |

## Candidate stint `Scarth, W. B___Canada___1888`

- Staff-list name: **Scarth, W. B** | colony: **Canada** | listed 1888–1900 | editions [1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | W. B. Scarth | — | — | — | — |
| 1889 | W. B. Scarth | — | — | — | — |
| 1890 | W. B. Scarth | — | — | — | — |
| 1894 | W. B. Scarth | Lieutenant-Governor | Lieutenant-Governors | — | — |
| 1894 | W. B. Scarth | Lieut.-Governor | Seat of Government, Winnipeg | — | — |
| 1896 | W. B. Scarth | Deputy | DEPARTMENT OF AGRICULTURE AND STATISTICS | — | — |
| 1896 | W. B. Scarth | Deputy | Department of Agriculture and Statistics | — | — |
| 1897 | W. B. Scarth | Deputy | Agriculture and Statistics | — | — |
| 1898 | W. B. Scarth | Deputy | Department of Agriculture and Statistics | — | — |
| 1899 | W. B. Scarth | Deputy | DEPARTMENT OF AGRICULTURE AND STATISTICS. | — | — |
| 1900 | W. B. Scarth | Deputy | Agriculture and Statistics | — | — |

### Deterministic checks: `scarte_william-bain_e1895` vs `Scarth, W. B___Canada___1888`

- [PASS] surname_gate: bio 'SCARTE' vs stint 'Scarth, W. B' (fuzzy:1)
- [PASS] initials: bio ['W', 'B'] ~ stint ['W', 'B']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Canada'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1888-1900
- [FAIL] position_sim: best 30 vs bar 60: 'dep. commnr. of patents' ~ 'Deputy'
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

