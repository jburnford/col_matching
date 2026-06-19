<!-- {"case_id": "case_le-feuvre_w-s_e1853", "bio_ids": ["le-feuvre_w-s_e1853"], "stint_ids": ["Le Feuvre, W. S___Ceylon___1877"]} -->
# Dossier case_le-feuvre_w-s_e1853

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `le-feuvre_w-s_e1853`

- Printed name: **LE FEUVRE, W. S**
- Birth year: not printed
- Appears in editions: [1883, 1886, 1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1883-L28350.v` — printed in editions [1883, 1886, 1888, 1889, 1890]:**

> LE FEUVRE, W. S.—Ensign Hampshire militia, 1853; lieutenant, 1854; ensign 77th regiment, 1854; lieutenant, 1855; assistant instructor, Hythe School of Musketry, 1855; instructor of musketry to 2nd brigade light division, Crimea, 1855-6; thanked in general orders; adjutant 77th regiment, 1856; resigned 1857; captain 2nd Hants, volunteer rifles, 1860; secretary municipal council Kandy, Ceylon, 1866-73; acting superintendent of police, central province, Ceylon, 1871-1873; superintendent of police, head-quarters, Colombo; northern, eastern, and north-western provinces, Ceylon; also in charge of police stores, and pay departments, 1873.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1853 | Ensign Hampshire militia | — | [1883, 1886, 1888, 1889, 1890] |
| 1 | 1854 | lieutenant | — | [1883, 1886, 1888, 1889, 1890] |
| 2 | 1854 | ensign 77th regiment | — | [1883, 1886, 1888, 1889, 1890] |
| 3 | 1855 | lieutenant | — | [1883, 1886, 1888, 1889, 1890] |
| 4 | 1855 | assistant instructor, Hythe School of Musketry | — | [1883, 1886, 1888, 1889, 1890] |
| 5 | 1855–1856 | instructor of musketry to 2nd brigade light division, Crimea | — | [1883, 1886, 1888, 1889, 1890] |
| 6 | 1856 | adjutant 77th regiment | — | [1883, 1886, 1888, 1889, 1890] |
| 7 | 1857 | resigned | — | [1883, 1886, 1888, 1889, 1890] |
| 8 | 1860 | captain 2nd Hants, volunteer rifles | — | [1883, 1886, 1888, 1889, 1890] |
| 9 | 1866–1873 | secretary municipal council Kandy | Ceylon | [1883, 1886, 1888, 1889, 1890] |
| 10 | 1871–1873 | acting superintendent of police, central province | Ceylon | [1883, 1886, 1888, 1889, 1890] |
| 11 | 1873 | also in charge of police stores, and pay departments | Ceylon *(inherited from previous clause)* | [1883, 1886, 1888, 1889, 1890] |

## Candidate stint `Le Feuvre, W. S___Ceylon___1877`

- Staff-list name: **Le Feuvre, W. S** | colony: **Ceylon** | listed 1877–1890 | editions [1877, 1878, 1879, 1880, 1883, 1886, 1888, 1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | W. S. Le Feuvre | Superintendent | Police | — | — |
| 1878 | W. S. Le Feuvre | Superintendent | Police | — | — |
| 1879 | W. S. Le Feuvre | Superintendent | Police | — | — |
| 1880 | W. S. Le Feuvre | Superintendent | Police | — | — |
| 1883 | W. S. Le Feuvre | Superintendent | Police | — | — |
| 1886 | W. S. Le Feuvre | Superintendent | Police | — | — |
| 1888 | W. S. Le Feuvre | Superintendent | Police | — | — |
| 1889 | W. S. Le Feuvre | Superintendent | Police | — | — |
| 1890 | W. S. Le Feuvre | Superintendent | Police | — | — |

### Deterministic checks: `le-feuvre_w-s_e1853` vs `Le Feuvre, W. S___Ceylon___1877`

- [PASS] surname_gate: bio 'LE FEUVRE' vs stint 'Le Feuvre, W. S' (exact)
- [PASS] initials: bio ['W', 'S'] ~ stint ['W', 'S']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1890
- [FAIL] position_sim: best 25 vs bar 60: 'also in charge of police stores, and pay departments' ~ 'Superintendent'
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

