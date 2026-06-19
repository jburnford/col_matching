<!-- {"case_id": "calib_gemini_ceylon_0059", "bio_ids": ["gorman_w-j_e1858"], "stint_ids": ["Gorman, W. J___Ceylon___1877"]} -->
# Dossier calib_gemini_ceylon_0059

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 14 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `gorman_w-j_e1858`

- Printed name: **GORMAN, W. J.**
- Birth year: not printed
- Appears in editions: [1883, 1886, 1888, 1889, 1890, 1894, 1896]

### Verbatim printed entry text (OCR)

**Version `col1883-L27701.v` — printed in editions [1883, 1886, 1888, 1889, 1890, 1894, 1896]:**

> GORMAN, W. J.—Captain, late of the Ceylon Rifles; assistant commissary-general, Ceylon, 1858; acting deputy commissary-general, 1863, resumed duties, 1864; acting deputy commissary-general, 1866; colonial storekeeper, Sept., 1867; is a J.P. for the island: lieut.-col. commanding Ceylon volunteers, June, 1882.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1858 | assistant commissary-general | Ceylon | [1883, 1886, 1888, 1889, 1890, 1894, 1896] |
| 1 | 1863 | acting deputy commissary-general | — | [1883, 1886, 1888, 1889, 1890, 1894, 1896] |
| 2 | 1864 | resumed duties | — | [1883, 1886, 1888, 1889, 1890, 1894, 1896] |
| 3 | 1866 | acting deputy commissary-general | — | [1883, 1886, 1888, 1889, 1890, 1894, 1896] |
| 4 | 1867 | colonial storekeeper | — | [1883, 1886, 1888, 1889, 1890, 1894, 1896] |
| 5 | 1882 | lieut.-col. commanding Ceylon volunteers | Ceylon | [1883, 1886, 1888, 1889, 1890, 1894, 1896] |

## Candidate stint `Gorman, W. J___Ceylon___1877`

- Staff-list name: **Gorman, W. J** | colony: **Ceylon** | listed 1877–1896 | editions [1877, 1878, 1879, 1880, 1883, 1886, 1888, 1889, 1890, 1894, 1896]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | W. J. Gorman | Colonial Storekeeper | Colonial Store Department | — | Captain |
| 1878 | W. J. Gorman | Colonial Storekeeper | Colonial Store Department | — | Captain |
| 1879 | W. J. Gorman | Colonial Storekeeper | Colonial Store Department | — | Captain |
| 1880 | W. J. Gorman | Colonial Storekeeper | Colonial Store Department | — | Captain |
| 1883 | W. J. Gorman | Colonial Storekeeper | Colonial Store Department | — | — |
| 1886 | W. J. Gorman | Colonial Storekeeper | Colonial Store Department | — | — |
| 1888 | W. J. Gorman | Colonial Storekeeper | Colonial Store Department | — | — |
| 1889 | W. J. Gorman | Colonial Storekeeper | Colonial Store Department | — | — |
| 1890 | W. J. Gorman | Colonial Storekeeper | Colonial Store Department | — | — |
| 1894 | W. J. Gorman | Colonial Storekeeper | Colonial Store Department | — | — |
| 1896 | W. J. Gorman | Colonial Storekeeper | Colonial Store Department | — | — |

### Deterministic checks: `gorman_w-j_e1858` vs `Gorman, W. J___Ceylon___1877`

- [PASS] surname_gate: bio 'GORMAN' vs stint 'Gorman, W. J' (exact)
- [PASS] initials: bio ['W', 'J'] ~ stint ['W', 'J']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1896
- [FAIL] position_sim: best 57 vs bar 60: 'lieut.-col. commanding Ceylon volunteers' ~ 'Colonial Storekeeper'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 7 agreeing edition-year(s) [1883, 1886, 1888, 1889, 1890, 1894] pos~57 (bar: >=2)
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

