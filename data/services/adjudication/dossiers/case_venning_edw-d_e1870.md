<!-- {"case_id": "case_venning_edw-d_e1870", "bio_ids": ["venning_edw-d_e1870"], "stint_ids": ["Venning, E___Ceylon___1877", "Venning, E___Ceylon___1898"]} -->
# Dossier case_venning_edw-d_e1870

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Venning, E___Ceylon___1877` is also gate-compatible with biography(ies) outside this case: ['venning_edward_e1870'] (already linked elsewhere or filtered).
- NOTE: stint `Venning, E___Ceylon___1898` is also gate-compatible with biography(ies) outside this case: ['venning_edward_e1870'] (already linked elsewhere or filtered).

## Biography `venning_edw-d_e1870`

- Printed name: **VENNING, EDW.D**
- Birth year: not printed
- Honours: A.M.I.C.E
- Appears in editions: [1896, 1897, 1899, 1900, 1905]

### Verbatim printed entry text (OCR)

**Version `col1896-L41766.v` — printed in editions [1896, 1897, 1899, 1900, 1905]:**

> VENNING, EDW.D., A.M.I.C.E.—Ed. Univ. Coll. Lond.; suptdg. offr. P.W. dept., Ceylon, 1870; ag. provincial asstt., 1878; provincial engr., Sabaragamuwa, 1893; financial asst to dir. of wks., 1895.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1870 | suptdg. offr. P.W. dept. | Ceylon | [1896, 1897, 1899, 1900, 1905] |
| 1 | 1878 | ag. provincial asstt | Ceylon *(inherited from previous clause)* | [1896, 1897, 1899, 1900, 1905] |
| 2 | 1893 | provincial engr., Sabaragamuwa | Ceylon *(inherited from previous clause)* | [1896, 1897, 1899, 1900, 1905] |
| 3 | 1895 | financial asst to dir. of wks | Ceylon *(inherited from previous clause)* | [1896, 1897, 1899, 1900, 1905] |

## Candidate stint `Venning, E___Ceylon___1877`

- Staff-list name: **Venning, E** | colony: **Ceylon** | listed 1877–1894 | editions [1877, 1878, 1879, 1880, 1883, 1886, 1888, 1889, 1890, 1894]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | E. Venning | Superintending Officer | Public Works Department | — | — |
| 1878 | E. Venning | Superintending Officer | Public Works Department | — | — |
| 1879 | E. Venning | Superintending Officer | Superintending Officers | — | — |
| 1880 | E. Venning | Superintending Officer | Public Works Department | — | — |
| 1883 | E. Venning | Superintending Officer | Public Works Department | — | — |
| 1886 | E. Venning | Superintending Officer, 2nd Class | Public Works Department | — | — |
| 1888 | E. Venning | District Engineer | Public Works Department | — | — |
| 1889 | E. Venning | District Engineer | Public Works Department | — | — |
| 1890 | E. Venning | District Engineer | Public Works Department | — | — |
| 1894 | E. Venning | Provl. Engineer, Province of Sabaragamuwa | Public Works Department | — | — |

### Deterministic checks: `venning_edw-d_e1870` vs `Venning, E___Ceylon___1877`

- [PASS] surname_gate: bio 'VENNING' vs stint 'Venning, E' (exact)
- [PASS] initials: bio ['E', 'D'] ~ stint ['E']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 4 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 4 event tenure(s) overlap stint years 1877-1894
- [PASS] position_sim: best 78 vs bar 60: 'provincial engr., Sabaragamuwa' ~ 'Provl. Engineer, Province of Sabaragamuwa'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Venning, E___Ceylon___1898`

- Staff-list name: **Venning, E** | colony: **Ceylon** | listed 1898–1900 | editions [1898, 1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1898 | E. Venning | Provl. Engineer | Public Works Department | — | — |
| 1899 | E. Venning | Provincial Engineer | Provincial Engineers | — | — |
| 1900 | E. Venning | Provincial Engineer | Public Work Department | — | — |

### Deterministic checks: `venning_edw-d_e1870` vs `Venning, E___Ceylon___1898`

- [PASS] surname_gate: bio 'VENNING' vs stint 'Venning, E' (exact)
- [PASS] initials: bio ['E', 'D'] ~ stint ['E']
- [PASS] age_gate: stint starts 1898; no printed birth year — UNCHECKED
- [PASS] colony: 4 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1898-1900
- [FAIL] position_sim: best 38 vs bar 60: 'financial asst to dir. of wks' ~ 'Provincial Engineer'
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

