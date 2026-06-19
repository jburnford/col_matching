<!-- {"case_id": "calib_gemini_ceylon_0053", "bio_ids": ["dutton_thomas-edward_b1877"], "stint_ids": ["Dutton, T. E___Ceylon___1915"]} -->
# Dossier calib_gemini_ceylon_0053

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 37 official(s) with this surname in the graph's staff lists; 13 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `dutton_thomas-edward_b1877`

- Printed name: **DUTTON, THOMAS EDWARD**
- Birth year: 1877 (attested in editions [1924, 1925, 1930, 1932])
- Appears in editions: [1924, 1925, 1930, 1932]

### Verbatim printed entry text (OCR)

**Version `col1924-L53950.v` — printed in editions [1924, 1925, 1930, 1932]:**

> DUTTON, THOMAS EDWARD, M. Inst. T.—B. 1877; traffic supt., Ceylon, 2nd Oct., 1913; designation altered to traffic man., 1916; gen. man., Ceylon Govt. Rlys., July, 1923; mem., legis. coun.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1913 | traffic supt. | Ceylon | [1924, 1925, 1930, 1932] |
| 1 | 1916 | designation altered to traffic man | Ceylon *(inherited from previous clause)* | [1924, 1925, 1930, 1932] |
| 2 | 1923 | gen. man., Ceylon Govt. Rlys | Ceylon | [1924, 1925, 1930, 1932] |

## Candidate stint `Dutton, T. E___Ceylon___1915`

- Staff-list name: **Dutton, T. E** | colony: **Ceylon** | listed 1915–1931 | editions [1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1925, 1927, 1928, 1929, 1931]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1915 | T. E. Dutton | Traffic Superintendent | Railway Department | — | — |
| 1917 | T. E. Dutton | Traffic Manager | Railway Department | — | — |
| 1918 | T. E. Dutton | Traffic Manager | Railway Department | — | — |
| 1919 | T. E. Dutton | Traffic Manager | Railway Department | — | — |
| 1920 | T. E. Dutton | Traffic Manager | Railway Department | — | — |
| 1921 | T. E. Dutton | Traffic Manager | Railway Department | — | — |
| 1922 | T. E. Dutton | Traffic Manager | Railway Department | — | — |
| 1923 | T. E. Dutton | Traffic Manager | Railway Department | — | — |
| 1925 | T. E. Dutton | General Manager | Railway Department | — | — |
| 1927 | T. E. Dutton | General Manager | Railway Department | — | — |
| 1928 | T. E. Dutton | General Manager | Railway Department | — | — |
| 1929 | T. E. Dutton | General Manager | Railway Department | — | — |
| 1931 | T. E. Dutton | General Manager | Railway Department | — | — |

### Deterministic checks: `dutton_thomas-edward_b1877` vs `Dutton, T. E___Ceylon___1915`

- [PASS] surname_gate: bio 'DUTTON' vs stint 'Dutton, T. E' (exact)
- [PASS] initials: bio ['T', 'E'] ~ stint ['T', 'E']
- [PASS] age_gate: stint starts 1915, birth 1877 (age 38)
- [PASS] colony: 3 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1915-1931
- [PASS] position_sim: best 100 vs bar 60: 'traffic supt.' ~ 'Traffic Superintendent'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): 1 agreeing edition-year(s) [1925] pos~64 (bar: >=2)
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

