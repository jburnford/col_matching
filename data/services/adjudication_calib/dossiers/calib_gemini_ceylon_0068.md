<!-- {"case_id": "calib_gemini_ceylon_0068", "bio_ids": ["skeen_g-j-a_e1869"], "stint_ids": ["Skeen, G. J. A___Ceylon___1877"]} -->
# Dossier calib_gemini_ceylon_0068

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `skeen_g-j-a_e1869`

- Printed name: **SKEEN, G. J. A**
- Birth year: not printed
- Appears in editions: [1886, 1889, 1898, 1899, 1900, 1905, 1906]

### Verbatim printed entry text (OCR)

**Version `col1886-L35745.v` — printed in editions [1886, 1889]:**

> SKEEN, G. J. A.—Extra assistant government printer, Ceylon, 1869; acting government printer, 22nd June, 1875; government printer, 1880.

**Version `col1898-L35933.v` — printed in editions [1898, 1899, 1900, 1905, 1906]:**

> SKEEN, G. J. A.—Extra asst. govt. printer, Ceylon, 1869; asst. govt. printer, 1872; govt. printer, 1881.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1869 | Extra assistant government printer | Ceylon | [1886, 1889, 1898, 1899, 1900, 1905, 1906] |
| 1 | 1872 | asst. govt. printer | Ceylon *(inherited from previous clause)* | [1898, 1899, 1900, 1905, 1906] |
| 2 | 1875 | acting government printer | Ceylon *(inherited from previous clause)* | [1886, 1889] |
| 3 | 1880 | government printer | Ceylon *(inherited from previous clause)* | [1886, 1889] |
| 4 | 1881 | govt. printer | Ceylon *(inherited from previous clause)* | [1898, 1899, 1900, 1905, 1906] |

## Candidate stint `Skeen, G. J. A___Ceylon___1877`

- Staff-list name: **Skeen, G. J. A** | colony: **Ceylon** | listed 1877–1906 | editions [1877, 1878, 1879, 1880, 1883, 1886, 1888, 1889, 1890, 1896, 1898, 1899, 1900, 1905, 1906]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | G. J. A. Skeen | Assistant Government Printer | Colonial Secretary's Office | — | — |
| 1878 | G. J. A. Skeen | Assistant Government Printer | Colonial Secretary's Office | — | — |
| 1879 | G. J. A. Skeen | Assistant Government Printer | Colonial Secretary's Office | — | — |
| 1880 | G. J. A. Skeen | Government Secretary | Colonial Secretary's Office | — | — |
| 1883 | G. J. A. Skeen | Government Printer | Colonial Secretary's Office | — | — |
| 1886 | G. J. A. Skeen | Government Printer | Colonial Secretary's Office | — | — |
| 1888 | G. J. A. Skeen | Government Printer | Civil Establishment | — | — |
| 1889 | G. J. A. Skeen | Government Printer | Civil Establishment | — | — |
| 1890 | G. J. A. Skeen | Government Printer | Civil Establishment | — | — |
| 1896 | G. J. A. Skeen | Government Printer | Civil Establishment | — | — |
| 1898 | G. J. A. Skeen | Government Printer | Civil Establishment | — | — |
| 1899 | G. J. A. Skeen | Government Printer | Civil Establishment | — | — |
| 1900 | G. J. A. Skeen | Government Printer | Civil Establishment | — | — |
| 1905 | G. J. A. Skeen | Government Printer | Civil Establishment | — | — |
| 1906 | G. J. A. Skeen | Government Printer | Civil Establishment | — | — |

### Deterministic checks: `skeen_g-j-a_e1869` vs `Skeen, G. J. A___Ceylon___1877`

- [PASS] surname_gate: bio 'SKEEN' vs stint 'Skeen, G. J. A' (exact)
- [PASS] initials: bio ['G', 'J', 'A'] ~ stint ['G', 'J', 'A']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 5 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1877-1906
- [PASS] position_sim: best 100 vs bar 60: 'acting government printer' ~ 'Government Printer'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 2 agreeing edition-year(s) [1886, 1889] pos~100 (bar: >=2)
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

