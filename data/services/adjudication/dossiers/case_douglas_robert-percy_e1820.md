<!-- {"case_id": "case_douglas_robert-percy_e1820", "bio_ids": ["douglas_robert-percy_e1820"], "stint_ids": ["Douglas, Robert___Queensland___1878"]} -->
# Dossier case_douglas_robert-percy_e1820

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 70 official(s) with this surname in the graph's staff lists; 27 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Douglas, Robert___Queensland___1878` is also gate-compatible with biography(ies) outside this case: ['douglas_francis-campbell-ross_e1940', 'douglas_r-stair_e1896'] (already linked elsewhere or filtered).

## Biography `douglas_robert-percy_e1820`

- Printed name: **DOUGLAS, Robert Percy**
- Birth year: not printed
- Honours: Bart
- Terminal: vacated 1868 — “vacated the command in 1868, after the usual term of 5 years.”
- Appears in editions: [1883, 1886, 1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1889-L32822.v` — printed in editions [1889, 1890]:**

> DOUGLAS, Sir Robert Percy, Bart.—Succeeded to the baronetcy in 1861; entered the army 1820; col. 98th Foot, 1864; lieut.-gen., 1867; general, 1874; governor of Jersey from 1856 to 1863; commanded the forces in South Africa 1863-8; lieutenant-governor of the Cape 1864-8.

**Version `col1883-L27238.v` — printed in editions [1883, 1886, 1888]:**

> DOUGLAS, SIR ROBERT PERCY, BART.—Succeeded to the baronetcy in 1861; entered the army 1820; colonel 98th Foot, 1864; lieutenant-general, 1867; general, 1874; governor of Jersey from 1858 to 1863, when he was appointed to command the forces in South Africa; in July, 1864, was appointed lieutenant-governor of that colony; vacated the command in 1868, after the usual term of 5 years.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1820 | entered the army | — | [1883, 1886, 1888, 1889, 1890] |
| 1 | 1856–1863 | governor of Jersey from | — | [1889, 1890] |
| 2 | 1858–1863 | governor | Jersey | [1883, 1886, 1888] |
| 3 | 1861 | Succeeded to the baronetcy in | — | [1889, 1890] |
| 4 | 1861–1861 | — | — | [1883, 1886, 1888] |
| 5 | 1863–1868 | commanded the forces in South Africa | — | [1889, 1890] |
| 6 | 1864 | col. 98th Foot | — | [1889, 1890] |
| 7 | 1864–1868 | lieutenant-governor of the Cape | South Africa | [1883, 1886, 1888, 1889, 1890] |
| 8 | 1864–1864 | colonel | — | [1883, 1886, 1888] |
| 9 | 1867 | lieut.-gen | — | [1889, 1890] |
| 10 | 1867–1867 | lieutenant-general | — | [1883, 1886, 1888] |
| 11 | 1874 | general | — | [1883, 1886, 1888, 1889, 1890] |

## Candidate stint `Douglas, Robert___Queensland___1878`

- Staff-list name: **Douglas, Robert** | colony: **Queensland** | listed 1878–1883 | editions [1878, 1879, 1880, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1878 | Robert Douglas | Sergeant at Arms | Legislative Assembly | — | — |
| 1879 | Robert Douglas | Sergeant at Arms | Legislative Assembly | — | — |
| 1880 | Robert Douglas | Sergeant at Arms | Legislative Assembly | — | — |
| 1883 | Robert Douglas | Sergeant at Arms | Legislative Assembly | — | — |

### Deterministic checks: `douglas_robert-percy_e1820` vs `Douglas, Robert___Queensland___1878`

- [PASS] surname_gate: bio 'DOUGLAS' vs stint 'Douglas, Robert' (exact)
- [PASS] initials: bio ['R', 'P'] ~ stint ['R']
- [PASS] age_gate: stint starts 1878; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Queensland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1878-1883
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

