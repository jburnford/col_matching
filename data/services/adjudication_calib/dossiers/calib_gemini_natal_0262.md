<!-- {"case_id": "calib_gemini_natal_0262", "bio_ids": ["russell_robert_e1866"], "stint_ids": ["Russell, Robert___Natal___1879"]} -->
# Dossier calib_gemini_natal_0262

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 178 official(s) with this surname in the graph's staff lists; 58 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['russell_robert_e1866'] carry a single initial only — the namesake trap applies.

## Biography `russell_robert_e1866`

- Printed name: **RUSSELL, ROBERT**
- Birth year: not printed
- Appears in editions: [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897, 1899]

### Verbatim printed entry text (OCR)

**Version `col1899-L37138.v` — printed in editions [1899]:**

> RUSSELL, ROBERT.—Ed. at Edin. Univ. and Church of Scotland Training Coll.; headmtr., govt. high schl., Durban, Natal, May, 1866; inspr. of schls., Jan., 1875; suptdg. inspr., Jan., 1878; sec. coun. of educn., 1878-84; sup't of educn., Aug., 1898; mem. of the univ. coun. of Cape Col.; author of "Natal: The Land and its Story."

**Version `col1883-L29367.v` — printed in editions [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897]:**

> RUSSELL, ROBERT.—Educated at Edinburgh Univ. and Church of Scotland training college; appointed headmaster government high school, Durban, Natal, May, 1866; inspector of schools, Jan., 1875; superintending inspector, Jan., 1878.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1866 | headmtr., govt. high schl., Durban | Natal | [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897, 1899] |
| 1 | 1875 | inspr. of schls | Natal *(inherited from previous clause)* | [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897, 1899] |
| 2 | 1878 | suptdg. inspr | Natal *(inherited from previous clause)* | [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897, 1899] |
| 3 | 1898 | sup't of educn | Natal *(inherited from previous clause)* | [1899] |

## Candidate stint `Russell, Robert___Natal___1879`

- Staff-list name: **Russell, Robert** | colony: **Natal** | listed 1879–1927 | editions [1879, 1880, 1883, 1886, 1888, 1889, 1890, 1894, 1896, 1898, 1899, 1900, 1905, 1906, 1907, 1910, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1879 | R. Russell | Superintending Inspector of Schools | Education Department | — | — |
| 1880 | R. Russell | Superintendent Inspector of Schools | Education Department | — | — |
| 1883 | R. Russell | Superintending Inspector of Schools | Education Department | — | — |
| 1886 | R. Russell | Superintending Inspector of Schools | Education Department | — | — |
| 1888 | R. Russell | Superintending Inspector of Schools | Education Department | — | — |
| 1889 | R. Russell | Superintending Inspector of Schools | Education Department | — | — |
| 1890 | R. Russell | Superintending Inspector of Schools | Education Department | — | — |
| 1894 | R. Russell | Superintending Inspector of Schools | Education Department | — | — |
| 1896 | R. Russell | Superintending Inspector of Schools | Education Department | — | — |
| 1898 | R. Russell | Superintending Inspector of Schools | Education Department | — | — |
| 1899 | R. Russell | Superintendent of Education | Education Department | — | — |
| 1899 | Robert Russell | Secretary | Civil Service Board | — | — |
| 1900 | Robert Russell | Secretary | Civil Service Board | — | — |
| 1900 | R. Russell | Superintendent of Education | Education Department | — | — |
| 1905 | Robert Russell | Secretary | Agent-General's Office | — | — |
| 1906 | Robert Russell | Secretary | Agent-General's Office | — | — |
| 1907 | Robert Russell | Secretary | Agent-General's Office | — | — |
| 1910 | Robert Russell | Agent-General for Natal (acting) | Agent-General's Office | — | — |
| 1927 | R. W. Russell | Inspector of Claims, Barkly West | Department of Mines and Industries | — | — |

### Deterministic checks: `russell_robert_e1866` vs `Russell, Robert___Natal___1879`

- [PASS] surname_gate: bio 'RUSSELL' vs stint 'Russell, Robert' (exact)
- [PASS] initials: bio ['R'] ~ stint ['R']
- [PASS] age_gate: stint starts 1879; no printed birth year — UNCHECKED
- [PASS] colony: 4 placed event(s) resolve to 'Natal'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1879-1927
- [PASS] position_sim: best 92 vs bar 60: 'sup't of educn' ~ 'Superintendent of Education'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 6 agreeing edition-year(s) [1883, 1886, 1888, 1889, 1890, 1899] pos~75 (bar: >=2)
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

