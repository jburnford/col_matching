<!-- {"case_id": "case_lees_charles-william_e1906", "bio_ids": ["lees_charles-william_e1906"], "stint_ids": ["Lees, William___Canada___1880"]} -->
# Dossier case_lees_charles-william_e1906

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 15 official(s) with this surname in the graph's staff lists; 10 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `lees_charles-william_e1906`

- Printed name: **LEES, CHARLES WILLIAM**
- Birth year: not printed
- Appears in editions: [1917, 1918, 1922, 1928]

### Verbatim printed entry text (OCR)

**Version `col1917-L51200.v` — printed in editions [1917, 1918, 1922, 1928]:**

> LEES, CHARLES WILLIAM.—Asst. dist. comanr., S. Nigeria, Sept., 1906; transf'd. to treasy. dept., 1907; acted as supervisor of customs, 1908, and as junior asst. sec. in 1911; served as finan. offr., Cameroons Expedy. Force, 1916; dep. treas., 1921; ag. treas., May to Dec., 1921 and June to Dec., 1923; treas., G. Coast, 1924; ag. col. sec., Sept.-Nov., 1925 and from Oct., 1926 to Mar., 1927; gov't. dep., on various occasions in 1926 and 1927.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1906–1906 | Asst. dist. comanr. | Southern Nigeria | [1917, 1918, 1922, 1928] |
| 1 | 1907–1907 | transf'd. to treasy. dept. | — | [1917, 1918, 1922, 1928] |
| 2 | 1908–1911 | acted as supervisor of customs, and as junior asst. sec. | — | [1917, 1918, 1922, 1928] |
| 3 | 1916–1916 | finan. offr., Cameroons Expedy. Force | Cameroons | [1917, 1918, 1922, 1928] |
| 4 | 1921–1921 | dep. treas. | — | [1917, 1918, 1922, 1928] |
| 5 | 1924–1924 | treas. | Gold Coast | [1917, 1918, 1922, 1928] |
| 6 | 1925–1927 | ag. col. sec. | — | [1917, 1918, 1922, 1928] |
| 7 | 1926–1927 | gov't. dep. | — | [1917, 1918, 1922, 1928] |

## Candidate stint `Lees, William___Canada___1880`

- Staff-list name: **Lees, William** | colony: **Canada** | listed 1880–1888 | editions [1880, 1883, 1886, 1888]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1880 | William Lees | Member | Legislative Assembly | — | — |
| 1883 | William Lees | Member | Members | — | — |
| 1886 | William Lees | Member | Legislative Assembly | — | — |
| 1888 | William Lees | — | Members | — | — |

### Deterministic checks: `lees_charles-william_e1906` vs `Lees, William___Canada___1880`

- [PASS] surname_gate: bio 'LEES' vs stint 'Lees, William' (exact)
- [PASS] initials: bio ['C', 'W'] ~ stint ['W']
- [PASS] age_gate: stint starts 1880; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1880-1888
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

