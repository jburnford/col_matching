<!-- {"case_id": "calib_gemini_ceylon_0079", "bio_ids": ["hyde_george-herbert-maccarthy_b1869"], "stint_ids": ["Hyde, G. H. M___Ceylon___1905"]} -->
# Dossier calib_gemini_ceylon_0079

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 24 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hyde_george-herbert-maccarthy_b1869`

- Printed name: **HYDE, GEORGE HERBERT MACCARTHY**
- Birth year: 1869 (attested in editions [1914, 1915, 1917, 1918, 1919, 1920, 1922])
- Honours: M.I.C.E, M.I.M.E, M.I.N.A
- Appears in editions: [1914, 1915, 1917, 1918, 1919, 1920, 1922]

### Verbatim printed entry text (OCR)

**Version `col1914-L47376.v` — printed in editions [1914, 1915, 1917, 1918, 1919, 1920, 1922]:**

> HYDE, GEORGE HERBERT MACCARTHY, M.I.C.E., M.I.N.A., M.I.M.E.—B. 1869; apprenticed and asst. man. to H. Bewley, Esq., M.I.C.E., chief engrnr., Colombo Commercial Co., Ceylon; dist. and mech. engrnr., P.W.D., Ceylon, 1900; factory engrnr., with rank and duties of provincial engrnr., 1911; capt., Ceylon artillery volunteers, 1907.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1900 | dist. and mech. engrnr., P.W.D. | Ceylon | [1914, 1915, 1917, 1918, 1919, 1920, 1922] |
| 1 | 1907 | capt., Ceylon artillery volunteers | Ceylon | [1914, 1915, 1917, 1918, 1919, 1920, 1922] |
| 2 | 1911 | factory engrnr., with rank and duties of provincial engrnr | Ceylon *(inherited from previous clause)* | [1914, 1915, 1917, 1918, 1919, 1920, 1922] |

## Candidate stint `Hyde, G. H. M___Ceylon___1905`

- Staff-list name: **Hyde, G. H. M** | colony: **Ceylon** | listed 1905–1921 | editions [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1919, 1921]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | G. H. M. Hyde | Mechanical Engineer | Public Works Department | — | — |
| 1906 | G. H. M. Hyde | Mechanical Engineer | Public Works Department | — | — |
| 1907 | G. H. M. Hyde | Mechanical Engineer | Public Works Department | — | — |
| 1908 | G. H. M. Hyde | Mechanical Engineer | Public Works Department | — | — |
| 1909 | G. H. M. Hyde | Mechanical and District Engineer | Public Works Department | — | — |
| 1910 | G. H. M. Hyde | Mechanical and District Engineer | Public Works Department | — | — |
| 1911 | G. H. M. Hyde | Mechanical and District Engineer | Public Works Department | — | — |
| 1912 | G. H. M. Hyde | Factory Engineer | Public Works Department | — | — |
| 1913 | G. H. M. Hyde | Factory Engineer | Public Works Department | — | — |
| 1914 | G. H. M. Hyde | Factory Engineer | Public Works Department | — | — |
| 1915 | G. H. M. Hyde | Factory Engineer | Public Works Department | — | — |
| 1917 | G. H. M. Hyde | Factory Engineer | Public Works Department | — | — |
| 1919 | G. H. M. Hyde | Factory Engineer | Public Works Department | — | — |
| 1921 | G. H. M. Hyde | Factory Engineer | Public Works Department | — | — |

### Deterministic checks: `hyde_george-herbert-maccarthy_b1869` vs `Hyde, G. H. M___Ceylon___1905`

- [PASS] surname_gate: bio 'HYDE' vs stint 'Hyde, G. H. M' (exact)
- [PASS] initials: bio ['G', 'H', 'M'] ~ stint ['G', 'H', 'M']
- [PASS] age_gate: stint starts 1905, birth 1869 (age 36)
- [PASS] colony: 3 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1905-1921
- [PASS] position_sim: best 77 vs bar 60: 'dist. and mech. engrnr., P.W.D.' ~ 'Mechanical and District Engineer'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 4 agreeing edition-year(s) [1914, 1915, 1917, 1919] pos~61 (bar: >=2)
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

