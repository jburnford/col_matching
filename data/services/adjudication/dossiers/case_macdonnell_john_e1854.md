<!-- {"case_id": "case_macdonnell_john_e1854", "bio_ids": ["macdonnell_john_e1854"], "stint_ids": ["MacDonnell, J___Ceylon___1894"]} -->
# Dossier case_macdonnell_john_e1854

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 14 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['macdonnell_john_e1854'] carry a single initial only — the namesake trap applies.

## Biography `macdonnell_john_e1854`

- Printed name: **MACDONNELL, JOHN**
- Birth year: not printed
- Appears in editions: [1906, 1908, 1909]

### Verbatim printed entry text (OCR)

**Version `col1906-L46723.v` — printed in editions [1906, 1908, 1909]:**

> MACDONNELL, JOHN.—Clk. in the imigrn. office of N. S. Wales in 1854; promoted in 1856 sen. clk. to the registr.-gen.; placed in charge of the compilation of the gen. statistics of the col. in 1858; sec. of the pol. dept. of Queensland on its separation from N.S.W., Feb., 1860; immigr. agt., Jan., 1866, inspr. of benevolent asylum and orphanages, also visiting justice to H.M.'s gaol and lun. asvl.; as well as ch. inspr. of distilleries; under-sec. and permanent head of the post and telegraph dept. in 1870; major-commdt. of the Queensland volr. forces, 1877; lieut.-col. comdt. in 1878; ret., Nov., 1879, and placed on the staff with his rank as lieut.-col.; ag. comdt. of the defence forces in Feb., 1883, to 1884; mem. of immgr., b.d., since 1865.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1854–1854 | Clk. in the imigrn. office | New South Wales | [1906, 1908, 1909] |
| 1 | 1856–1856 | sen. clk. to the registr.-gen. | — | [1906, 1908, 1909] |
| 2 | 1858–1858 | placed in charge of the compilation of the gen. statistics of the col. | — | [1906, 1908, 1909] |
| 3 | 1860–1860 | sec. of the pol. dept. | Queensland | [1906, 1908, 1909] |
| 4 | 1865 | mem. of immgr., b.d. | — | [1906, 1908, 1909] |
| 5 | 1866–1866 | immigr. agt., inspr. of benevolent asylum and orphanages, also visiting justice to H.M.'s gaol and lun. asvl.; as well as ch. inspr. of distilleries | — | [1906, 1908, 1909] |
| 6 | 1870–1870 | under-sec. and permanent head of the post and telegraph dept. | — | [1906, 1908, 1909] |
| 7 | 1877–1877 | major-commdt. of the Queensland volr. forces | Queensland | [1906, 1908, 1909] |
| 8 | 1878–1878 | lieut.-col. comdt. | — | [1906, 1908, 1909] |
| 9 | 1879–1879 | placed on the staff with his rank as lieut.-col. | — | [1906, 1908, 1909] |
| 10 | 1883–1884 | ag. comdt. of the defence forces | — | [1906, 1908, 1909] |

## Candidate stint `MacDonnell, J___Ceylon___1894`

- Staff-list name: **MacDonnell, J** | colony: **Ceylon** | listed 1894–1900 | editions [1894, 1896, 1898, 1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | J. MacDonnell | District Engineer, 1st Grade | Public Works Department | — | — |
| 1896 | J. MacDonnell | District Engineer, 1st Grade | Public Works Department | — | — |
| 1898 | J. MacDonnell | District Engineer, 1st Grade | Public Works Department | — | — |
| 1899 | J. MacDonnell | District Engineer (1st Grade) | District Engineers | — | — |
| 1900 | J. MacDonnell | Provincial Engineer | Public Work Department | — | — |

### Deterministic checks: `macdonnell_john_e1854` vs `MacDonnell, J___Ceylon___1894`

- [PASS] surname_gate: bio 'MACDONNELL' vs stint 'MacDonnell, J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1894; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1894-1900
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

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

