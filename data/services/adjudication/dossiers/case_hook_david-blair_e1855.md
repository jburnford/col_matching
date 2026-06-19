<!-- {"case_id": "case_hook_david-blair_e1855", "bio_ids": ["hook_david-blair_e1855"], "stint_ids": ["Hook, D. B___Cape of Good Hope___1877"]} -->
# Dossier case_hook_david-blair_e1855

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Hook, D. B___Cape of Good Hope___1877` is also gate-compatible with biography(ies) outside this case: ['hook_d-b_e1879'] (already linked elsewhere or filtered).

## Biography `hook_david-blair_e1855`

- Printed name: **HOOK, DAVID BLAIR**
- Birth year: not printed
- Appears in editions: [1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900]

### Verbatim printed entry text (OCR)

**Version `col1889-L33789.v` — printed in editions [1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900]:**

> HOOK, CAPT. DAVID BLAIR.—In F.A.M.P., Cape, 1855; northern border magistrate, May, 1873; capt., C.M.R., Aug., 1878; C.C. and R.M., Herschel, 1870; commdt. troops, Quilting and Herschel districts, Basuto war, 1880; ag. chief magistrate, Transkei, Mar., 1883; R.M., Tsolo, October, 1884; R.M., Umtzimkulu, September, 1886.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1855 | In F.A.M.P. | Cape of Good Hope | [1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900] |
| 1 | 1870 | C.C. and R.M., Herschel | Cape of Good Hope *(inherited from previous clause)* | [1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900] |
| 2 | 1873 | northern border magistrate | Cape of Good Hope *(inherited from previous clause)* | [1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900] |
| 3 | 1878 | capt., C.M.R | Cape of Good Hope *(inherited from previous clause)* | [1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900] |
| 4 | 1880 | commdt. troops, Quilting and Herschel districts, Basuto war | Basutoland | [1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900] |
| 5 | 1883 | ag. chief magistrate, Transkei | Basutoland *(inherited from previous clause)* | [1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900] |
| 6 | 1884 | R.M., Tsolo | Basutoland *(inherited from previous clause)* | [1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900] |
| 7 | 1886 | R.M., Umtzimkulu | Basutoland *(inherited from previous clause)* | [1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900] |

## Candidate stint `Hook, D. B___Cape of Good Hope___1877`

- Staff-list name: **Hook, D. B** | colony: **Cape of Good Hope** | listed 1877–1880 | editions [1877, 1878, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | D. B. Hook | Special Magistrate | Northern Border Magistracy | — | — |
| 1877 | D. B. Hook | Inspector | Armed Mounted Police Force | — | — |
| 1878 | D. B. Hook | Inspector | Armed Mounted Police Force | — | — |
| 1879 | D. B. Hook | Captain | Cape Mounted Riflemen (Act No. 9 of 1878) | — | — |
| 1880 | Captain Hook | Civil Commissioner and Resident Magistrate | Division of Herschel | — | — |

### Deterministic checks: `hook_david-blair_e1855` vs `Hook, D. B___Cape of Good Hope___1877`

- [PASS] surname_gate: bio 'HOOK' vs stint 'Hook, D. B' (exact)
- [PASS] initials: bio ['D', 'B'] ~ stint ['D', 'B']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 4 placed event(s) resolve to 'Cape of Good Hope'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1877-1880
- [PASS] position_sim: best 71 vs bar 60: 'northern border magistrate' ~ 'Special Magistrate'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

