<!-- {"case_id": "case_andrews_richard-bullock_e1855", "bio_ids": ["andrews_richard-bullock_e1855"], "stint_ids": ["Andrews, R. B___South Australia___1877", "Andrews, R. B___South Australia___1894", "Andrews, R___Trinidad and Tobago___1900"]} -->
# Dossier case_andrews_richard-bullock_e1855

## Case context

- 1 biography(ies) and 3 candidate stint(s) are entangled in this case.
- Corpus context: 65 official(s) with this surname in the graph's staff lists; 15 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `andrews_richard-bullock_e1855`

- Printed name: **ANDREWS, RICHARD BULLOCK**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L26198.v` — printed in editions [1883]:**

> ANDREWS, RICHARD BULLOCK, Q.C.—Was called to the South Australian bar in 1855; entered Parliament in that colony in 1857, and held the office of attorney-general in the Torrens ministry in that year; Queen's counsel March 13, 1865; from that time till the resignation of the Ayres ministry in Nov., 1868, he from time to time held the office of attorney-general in several ministries, and retired from Parliament in Jan., 1870, when he was appointed to the office of crown solicitor and public prosecutor.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1855 | barrister | South Australia | [1883] |
| 1 | 1857 | member of Parliament | South Australia | [1883] |
| 2 | 1865 | Queen's counsel | — | [1883] |
| 3 | 1865 | attorney-general | South Australia | [1883] |
| 4 | 1870 | member of Parliament | South Australia | [1883] |

## Candidate stint `Andrews, R. B___South Australia___1877`

- Staff-list name: **Andrews, R. B** | colony: **South Australia** | listed 1877–1880 | editions [1877, 1878, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | R. B. Andrews | Crown Solicitor | Law Officers' Department | — | — |
| 1878 | R. B. Andrews | Crown Solicitor | Law Officers' Department | — | — |
| 1879 | R. B. Andrews | Crown Solicitor | Law Officers' Department | — | — |
| 1880 | Hon. R. B. Andrews | Crown Solicitor | Law Officers' Department | — | — |

### Deterministic checks: `andrews_richard-bullock_e1855` vs `Andrews, R. B___South Australia___1877`

- [PASS] surname_gate: bio 'ANDREWS' vs stint 'Andrews, R. B' (exact)
- [PASS] initials: bio ['R', 'B'] ~ stint ['R', 'B']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 4 placed event(s) resolve to 'South Australia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1880
- [FAIL] position_sim: best 34 vs bar 60: 'member of Parliament' ~ 'Crown Solicitor'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Andrews, R. B___South Australia___1894`

- Staff-list name: **Andrews, R. B** | colony: **South Australia** | listed 1894–1897 | editions [1894, 1896, 1897]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | R. B. Andrews | Third Associate | Supreme Court Department | — | — |
| 1896 | R. B. Andrews | Second Associate to Judges | Supreme Court Department | — | — |
| 1897 | R. B. Andrews | Associate Judge | Supreme Court Department | — | — |

### Deterministic checks: `andrews_richard-bullock_e1855` vs `Andrews, R. B___South Australia___1894`

- [PASS] surname_gate: bio 'ANDREWS' vs stint 'Andrews, R. B' (exact)
- [PASS] initials: bio ['R', 'B'] ~ stint ['R', 'B']
- [PASS] age_gate: stint starts 1894; no printed birth year — UNCHECKED
- [PASS] colony: 4 placed event(s) resolve to 'South Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1894-1897
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Andrews, R___Trinidad and Tobago___1900`

- Staff-list name: **Andrews, R** | colony: **Trinidad and Tobago** | listed 1900–1906 | editions [1900, 1905, 1906]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1900 | R. Andrews | Reverend | Baptist Church | — | — |
| 1905 | R. Andrews | Rev. | Baptist Church | — | — |
| 1906 | R. Andrews | Reverend | Religious | — | — |

### Deterministic checks: `andrews_richard-bullock_e1855` vs `Andrews, R___Trinidad and Tobago___1900`

- [PASS] surname_gate: bio 'ANDREWS' vs stint 'Andrews, R' (exact)
- [PASS] initials: bio ['R', 'B'] ~ stint ['R']
- [PASS] age_gate: stint starts 1900; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1900-1906
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

