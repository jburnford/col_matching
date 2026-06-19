<!-- {"case_id": "case_mansel_george_e1873", "bio_ids": ["mansel_george_e1873"], "stint_ids": ["Mansel, George___Zululand___1888"]} -->
# Dossier case_mansel_george_e1873

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['mansel_george_e1873'] carry a single initial only — the namesake trap applies.
- Phase 1 found `mansel_george_e1873` ↔ `Mansel, George___Zululand___1888` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Mansel, George___Zululand___1888` is also gate-compatible with biography(ies) outside this case: ['mansel_george_e1883'] (already linked elsewhere or filtered).

## Biography `mansel_george_e1873`

- Printed name: **MANSEL, GEORGE**
- Birth year: not printed
- Honours: C.M.G. (1891)
- Terminal: retired 1906 — “ret., 1906.”
- Appears in editions: [1894, 1896, 1897, 1898, 1899, 1905, 1908, 1909, 1911, 1912, 1913]

### Verbatim printed entry text (OCR)

**Version `col1894-L32895.v` — printed in editions [1894, 1896, 1897, 1898, 1899, 1905, 1908, 1909, 1911, 1912, 1913]:**

> MANSEL, GEORGE, C.M.G. (1891).—Served in Weenen Yeomanry through the Langalibalele rebellion in 1873; served as sub-inspr. and inspr. in Natal mounted pol. through Zulu war, 1879 (medal with clasp), and Boer war, 1880 and 1881; raised and commanded the Reserve Territory Carbineers from 1883 to 1887, when the force was changed into the Zululand pol.; served in this force through all disturbances in Zululand from 1883 to 1888; twice mentioned in despatches as having shown conspicuous coolness and gallantry in action; asst. consnr., Natal pol., 1897; ag. commndt., 1902; ch. consnr., pol., Jan., 1903; ret., 1906.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1873–1873 | Weenen Yeomanry | — | [1894, 1896, 1897, 1898, 1899, 1905, 1908, 1909, 1911, 1912, 1913] |
| 1 | 1879–1881 | sub-inspr. and inspr. | Natal | [1894, 1896, 1897, 1898, 1899, 1905, 1908, 1909, 1911, 1912, 1913] |
| 2 | 1883–1887 | commanded the Reserve Territory Carbineers | — | [1894, 1896, 1897, 1898, 1899, 1905, 1908, 1909, 1911, 1912, 1913] |
| 3 | 1883–1888 | — | Zululand | [1894, 1896, 1897, 1898, 1899, 1905, 1908, 1909, 1911, 1912, 1913] |
| 4 | 1897–1897 | asst. consnr. | Natal | [1894, 1896, 1897, 1898, 1899, 1905, 1908, 1909, 1911, 1912, 1913] |
| 5 | 1902–1902 | ag. commndt. | — | [1894, 1896, 1897, 1898, 1899, 1905, 1908, 1909, 1911, 1912, 1913] |
| 6 | 1903–1903 | ch. consnr., pol. | — | [1894, 1896, 1897, 1898, 1899, 1905, 1908, 1909, 1911, 1912, 1913] |

## Candidate stint `Mansel, George___Zululand___1888`

- Staff-list name: **Mansel, George** | colony: **Zululand** | listed 1888–1898 | editions [1888, 1889, 1890, 1894, 1896, 1897, 1898]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | George Mansel | Commandant, Zululand Police | Civil Establishment | — | — |
| 1889 | George Mansel | Commandant, Zululand Police | Civil Establishment | — | — |
| 1890 | G. Mansel | Police, Commandant | Civil Establishment | — | — |
| 1894 | G. Mansel | Commandant | Zululand Police | C.M.G. | — |
| 1896 | G. Mansel | Commandant | Zululand Police | C.M.G. | — |
| 1897 | G. Mansel | Commandant | Zululand Police | C.M.G. | — |
| 1898 | G. Mansel | Commandant | Zululand Police | C.M.G. | — |

### Deterministic checks: `mansel_george_e1873` vs `Mansel, George___Zululand___1888`

- [PASS] surname_gate: bio 'MANSEL' vs stint 'Mansel, George' (exact)
- [PASS] initials: bio ['G'] ~ stint ['G']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Zululand'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1888-1898
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: C.M.G.
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

