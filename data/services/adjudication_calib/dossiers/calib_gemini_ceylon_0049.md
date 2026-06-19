<!-- {"case_id": "calib_gemini_ceylon_0049", "bio_ids": ["templeton_robert-stanaker_b1855"], "stint_ids": ["Templeton, R. S___Ceylon___1894"]} -->
# Dossier calib_gemini_ceylon_0049

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 26 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `templeton_robert-stanaker_b1855`

- Printed name: **TEMPLETON, ROBERT STANAKER**
- Birth year: 1855 (attested in editions [1914, 1915])
- Honours: A.I.C.E, F.R.G.S
- Appears in editions: [1914, 1915]

### Verbatim printed entry text (OCR)

**Version `col1914-L50292.v` — printed in editions [1914, 1915]:**

> TEMPLETON, HON. ROBERT STANAKER, A.I.C.E., F.R.G.S.—B. 1855; asst. survr., Ceylon, 15th Oct., 1887; dist. survr., 1st Aug., 1890; supt. of topographical surveys, 1st Jan., 1899; supt. of surveys, 8th Sept. 1902; asst. survr.-gen., 23rd June, 1904; survr.-gen., 15th Oct., 1910; M.L.C.; mem. of mun. coun.; dir. of widows' and orphans' pension fund.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1887 | asst. survr. | Ceylon | [1914, 1915] |
| 1 | 1890 | dist. survr | Ceylon *(inherited from previous clause)* | [1914, 1915] |
| 2 | 1899 | supt. of topographical surveys | Ceylon *(inherited from previous clause)* | [1914, 1915] |
| 3 | 1902 | supt. of surveys | Ceylon *(inherited from previous clause)* | [1914, 1915] |
| 4 | 1904 | asst. survr.-gen | Ceylon *(inherited from previous clause)* | [1914, 1915] |
| 5 | 1910 | survr.-gen | Ceylon *(inherited from previous clause)* | [1914, 1915] |

## Candidate stint `Templeton, R. S___Ceylon___1894`

- Staff-list name: **Templeton, R. S** | colony: **Ceylon** | listed 1894–1915 | editions [1894, 1896, 1898, 1899, 1900, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | R. S. Templeton | District Surveyor | Survey Department | — | — |
| 1896 | R. S. Templeton | District Surveyor | Survey Department | — | — |
| 1898 | R. S. Templeton | District Surveyor | Survey Department | — | — |
| 1899 | R. S. Templeton | Assistant Superintendent, Topographical Branch | Survey Department | — | — |
| 1900 | R. S. Templeton | Superintendent of Survey | Survey Department | — | — |
| 1905 | R. S. Templeton | Assistant Surveyor-General | Survey Department | — | — |
| 1906 | R. S. Templeton | Assistant Surveyor-General | Survey Department | — | — |
| 1907 | R. S. Templeton | Assistant Surveyor-General | Survey Department | — | — |
| 1908 | R. S. Templeton | Assistant Surveyor-General | Survey Department | — | — |
| 1909 | R. S. Templeton | Acting Surveyor-General | Survey Department | — | — |
| 1910 | R. S. Templeton | Acting Surveyor-General | Survey Department | — | — |
| 1911 | R. S. Templeton | Surveyor-General | Survey Department | — | — |
| 1912 | R. S. Templeton | Surveyor-General | Survey Department | — | — |
| 1913 | R. S. Templeton | Surveyor-General | Survey Department | — | — |
| 1914 | R. S. Templeton | Surveyor-General | Survey Department | — | — |
| 1915 | R. S. Templeton | Surveyor-General | Survey Department | — | — |

### Deterministic checks: `templeton_robert-stanaker_b1855` vs `Templeton, R. S___Ceylon___1894`

- [PASS] surname_gate: bio 'TEMPLETON' vs stint 'Templeton, R. S' (exact)
- [PASS] initials: bio ['R', 'S'] ~ stint ['R', 'S']
- [PASS] age_gate: stint starts 1894, birth 1855 (age 39)
- [PASS] colony: 6 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 5 event tenure(s) overlap stint years 1894-1915
- [PASS] position_sim: best 100 vs bar 60: 'dist. survr' ~ 'District Surveyor'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 2 agreeing edition-year(s) [1914, 1915] pos~100 (bar: >=2)
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

