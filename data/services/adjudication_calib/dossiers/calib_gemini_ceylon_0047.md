<!-- {"case_id": "calib_gemini_ceylon_0047", "bio_ids": ["balfour_john-aylmer_b1874"], "stint_ids": ["Balfour, J. A___Ceylon___1905"]} -->
# Dossier calib_gemini_ceylon_0047

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 15 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `balfour_john-aylmer_b1874`

- Printed name: **BALFOUR, JOHN AYLMER**
- Birth year: 1874 (attested in editions [1914, 1917, 1918])
- Appears in editions: [1911, 1912, 1913, 1914, 1915, 1917, 1918]

### Verbatim printed entry text (OCR)

**Version `col1914-L44431.v` — printed in editions [1914, 1917, 1918]:**

> BALFOUR, JOHN AYLMER, A.M.I.C.E.—B. 1874; irrigtn. engrnr., Ceylon, 1900; ag. asst. dir. of irrigtn. in 1907 and 1908; asst. dir. of irrigtn., June, 1909; ag. dir., Feb., 1910, Nov., 1911, and from 15th May, 1913; dir. of irrigtn., 14th Aug., 1913.

**Version `col1915-L45029.v` — printed in editions [1915]:**

> BALEFOUR, JOHN AYLMER, A.M.I.C.E.—B. 1874; irrigtn. engrnr., Ceylon, 1900; ag. asst. dir. of irrigtn., in 1907 and 1908; asst. dir. of irrigtn., June, 1909; ag. dir., Feb., 1910, Nov., 1911, and from 15th May, 1913; dir. of irrigtn., 14th Aug., 1913.

**Version `col1911-L42950.v` — printed in editions [1911, 1912, 1913]:**

> BALFOUR, JOHN AYLMER.—B. 1874; A.M.I.C.E.; educ. abroad; trained as civil engr., London; two-and-a-half years' subsequent experience in England; irrigtn. engr., Ceylon, Aug. 1900; ag. asst. dir. of irrigtn., Ceylon, 1908; asst. dir. of irrigtn., 1909; ag. dir., Feb., 1910; asst. dir., Nov., 1910.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1900–1900 | irrigtn. engrnr. | Ceylon | [1911, 1912, 1913, 1914, 1915, 1917, 1918] |
| 1 | 1907–1908 | ag. asst. dir. of irrigtn. | — | [1914, 1915, 1917, 1918] |
| 2 | 1908 | ag. asst. dir. of irrigtn. | Ceylon | [1911, 1912, 1913] |
| 3 | 1909–1909 | asst. dir. of irrigtn. | Ceylon *(inherited from previous clause)* | [1911, 1912, 1913, 1914, 1915, 1917, 1918] |
| 4 | 1910–1913 | ag. dir. | Ceylon *(inherited from previous clause)* | [1911, 1912, 1913, 1914, 1915, 1917, 1918] |
| 5 | 1913–1913 | dir. of irrigtn. | — | [1914, 1915, 1917, 1918] |

## Candidate stint `Balfour, J. A___Ceylon___1905`

- Staff-list name: **Balfour, J. A** | colony: **Ceylon** | listed 1905–1918 | editions [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | J. A. Balfour | Irrigation Engineer | Irrigation Department | — | — |
| 1906 | J. A. Balfour | Irrigation Engineer | Irrigation Department | — | — |
| 1907 | J. A. Balfour | Irrigation Engineer | Irrigation Department | — | — |
| 1908 | J. A. Balfour | Irrigation Engineer | Irrigation Department | — | — |
| 1909 | J. A. Balfour | Assistant Director of Irrigation (acting) | Irrigation Department | — | — |
| 1910 | J. A. Balfour | Assistant Director of Irrigation | Irrigation Department | — | — |
| 1911 | J. A. Balfour | Assistant Director of Irrigation | Irrigation Department | — | — |
| 1912 | J. A. Balfour | Assistant Director of Irrigation | Irrigation Department | — | — |
| 1913 | J. A. Balfour | Assistant Director of Irrigation | Irrigation Department | — | — |
| 1914 | J. A. Balfour | Director of Irrigation | Irrigation Department | — | — |
| 1915 | J. A. Balfour | Director of Irrigation | Irrigation Department | — | — |
| 1917 | J. A. Balfour | Director of Irrigation | Irrigation Department | — | — |
| 1918 | J. A. Balfour | Director of Irrigation | Irrigation Department | — | — |

### Deterministic checks: `balfour_john-aylmer_b1874` vs `Balfour, J. A___Ceylon___1905`

- [PASS] surname_gate: bio 'BALFOUR' vs stint 'Balfour, J. A' (exact)
- [PASS] initials: bio ['J', 'A'] ~ stint ['J', 'A']
- [PASS] age_gate: stint starts 1905, birth 1874 (age 31)
- [PASS] colony: 4 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1905-1918
- [PASS] position_sim: best 100 vs bar 60: 'ag. dir.' ~ 'Assistant Director of Irrigation (acting)'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 5 agreeing edition-year(s) [1911, 1912, 1913, 1914, 1915] pos~70 (bar: >=2)
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

