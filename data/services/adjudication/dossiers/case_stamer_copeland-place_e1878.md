<!-- {"case_id": "case_stamer_copeland-place_e1878", "bio_ids": ["stamer_copeland-place_e1878"], "stint_ids": ["Stamers, C.P___Turks and Caicos Islands___1877", "Stamers, C.P___Turks and Caicos Islands___1889"]} -->
# Dossier case_stamer_copeland-place_e1878

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- Phase 1 found `stamer_copeland-place_e1878` ↔ `Stamers, C.P___Turks and Caicos Islands___1877` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Stamers, C.P___Turks and Caicos Islands___1877` is also gate-compatible with biography(ies) outside this case: ['stamers_coppeland-place_e1873'] (already linked elsewhere or filtered).
- NOTE: stint `Stamers, C.P___Turks and Caicos Islands___1889` is also gate-compatible with biography(ies) outside this case: ['stamers_coppeland-place_e1873'] (already linked elsewhere or filtered).

## Biography `stamer_copeland-place_e1878`

- Printed name: **STAMER, COPELAND PLACE**
- Birth year: not printed
- Appears in editions: [1896]

### Verbatim printed entry text (OCR)

**Version `col1896-L41462.v` — printed in editions [1896]:**

> STAMER, COPELAND PLACE.—Rev. officer, Salt Cay, Turks and Caicos Islands, Mar., 1878; ag. asst. commssnr., Cockburn Harbr., Sept., 1879, to 1880, and Aug., 1882 to May, 1883 and March, 1884; confirmed, April, 1885; asst. commssnr., Salt Cay, May, 1890.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1878 | Rev. officer | Turks and Caicos Islands | [1896] |
| 1 | 1879–1884 | ag. asst. commssnr. | — | [1896] |
| 2 | 1885–1885 | confirmed | — | [1896] |
| 3 | 1890 | asst. commssnr. | — | [1896] |

## Candidate stint `Stamers, C.P___Turks and Caicos Islands___1877`

- Staff-list name: **Stamers, C.P** | colony: **Turks and Caicos Islands** | listed 1877–1880 | editions [1877, 1878, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | C. P. Stamers | Boarding Officer and Locker at Grand Turk | Civil Establishment | — | — |
| 1878 | C. P. Stamers | Boarding Officer and Locker | Civil Establishment | — | — |
| 1879 | C. P. Stamers | Boarding Officer and Locker | Civil Establishment | — | — |
| 1880 | C. P. Stamers | Boarding Officer and Locker at Salt Cay | Civil Establishment | — | — |

### Deterministic checks: `stamer_copeland-place_e1878` vs `Stamers, C.P___Turks and Caicos Islands___1877`

- [PASS] surname_gate: bio 'STAMER' vs stint 'Stamers, C.P' (fuzzy:1)
- [PASS] initials: bio ['C', 'P'] ~ stint ['C', 'P']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Turks and Caicos Islands'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1880
- [PASS] position_sim: best 78 vs bar 60: 'Rev. officer' ~ 'Boarding Officer and Locker'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Stamers, C.P___Turks and Caicos Islands___1889`

- Staff-list name: **Stamers, C.P** | colony: **Turks and Caicos Islands** | listed 1889–1900 | editions [1889, 1890, 1896, 1898, 1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1889 | C. P. Stamers | Assistant Commissioner at Cockburn Harbour | Civil Establishment | — | — |
| 1890 | C. P. Stamers | Assistant Commissioner | Civil Establishment | — | — |
| 1896 | C.P. Stamers | Assistant Commissioner | Civil Establishment | — | — |
| 1898 | C. P. Stamers | Assistant Commissioner | Civil Establishment | — | — |
| 1899 | C. P. Stamers | Assistant Commissioner | Civil Establishment | — | — |
| 1900 | C. P. Stamers | Assistant Commissioner | Civil Establishment | — | — |

### Deterministic checks: `stamer_copeland-place_e1878` vs `Stamers, C.P___Turks and Caicos Islands___1889`

- [PASS] surname_gate: bio 'STAMER' vs stint 'Stamers, C.P' (fuzzy:1)
- [PASS] initials: bio ['C', 'P'] ~ stint ['C', 'P']
- [PASS] age_gate: stint starts 1889; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Turks and Caicos Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1889-1900
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

