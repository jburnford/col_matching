<!-- {"case_id": "case_goyder_g-woodroffe_e1852", "bio_ids": ["goyder_g-woodroffe_e1852"], "stint_ids": ["Goyder, G. W___South Australia___1877", "Goyder, G. W___South Australia___1888"]} -->
# Dossier case_goyder_g-woodroffe_e1852

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `goyder_g-woodroffe_e1852`

- Printed name: **GOYDER, G. WOODROFFE**
- Birth year: not printed
- Honours: C.M.G (1889)
- Appears in editions: [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898]

### Verbatim printed entry text (OCR)

**Version `col1888-L33698.v` — printed in editions [1888, 1889, 1890, 1894, 1896, 1897, 1898]:**

> GOYDER, G. WOODROFFE, C.M.G. (1889).—Draftsman, engineer's department, South Australia, 1852; chief clerk, land office, 1858; deputy surveyor general, 1855; surveyor general, 1861; also inspector of mines and valuer of runs.

**Version `col1883-L27716.v` — printed in editions [1883, 1886]:**

> GOYDER, G. WOODROFFE.—Chief clerk, land office, South Australia, 1853; deputy surveyor general, 1855; surveyor general, 1861; also inspector of mines and valuer of runs.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1852 | Draftsman, engineer's department | South Australia | [1888, 1889, 1890, 1894, 1896, 1897, 1898] |
| 1 | 1853 | Chief clerk, land office | South Australia | [1883, 1886] |
| 2 | 1855 | deputy surveyor general | South Australia *(inherited from previous clause)* | [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898] |
| 3 | 1858 | chief clerk, land office | South Australia *(inherited from previous clause)* | [1888, 1889, 1890, 1894, 1896, 1897, 1898] |
| 4 | 1861 | surveyor general | South Australia *(inherited from previous clause)* | [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898] |

## Candidate stint `Goyder, G. W___South Australia___1877`

- Staff-list name: **Goyder, G. W** | colony: **South Australia** | listed 1877–1880 | editions [1877, 1878, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | G. W. Goyder | Surveyor-General and Inspector of Mines | Survey Department | — | — |
| 1878 | G. W. Goyder | Surveyor-General and Inspector of Mines | Survey Department | — | — |
| 1880 | G. W. Goyder | Chairman | Forest Board | — | — |
| 1880 | G. W. Goyder | Surveyor-General and Inspector of Mines | Survey Department | — | — |

### Deterministic checks: `goyder_g-woodroffe_e1852` vs `Goyder, G. W___South Australia___1877`

- [PASS] surname_gate: bio 'GOYDER' vs stint 'Goyder, G. W' (exact)
- [PASS] initials: bio ['G', 'W'] ~ stint ['G', 'W']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 5 placed event(s) resolve to 'South Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1880
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Goyder, G. W___South Australia___1888`

- Staff-list name: **Goyder, G. W** | colony: **South Australia** | listed 1888–1894 | editions [1888, 1889, 1890, 1894]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | G. W. Goyder | Surveyor-General and Inspector of Mines | Survey Department | — | — |
| 1889 | G. W. Goyder | Surveyor-General and Inspector of Mines | Survey Department | C.M.G. | — |
| 1890 | G. W. Goyder | Surveyor-General and Inspector of Mines | Survey Department | C.M.G. | — |
| 1894 | G. W. Goyder | Surveyor-General | Survey Department | C.M.G. | — |

### Deterministic checks: `goyder_g-woodroffe_e1852` vs `Goyder, G. W___South Australia___1888`

- [PASS] surname_gate: bio 'GOYDER' vs stint 'Goyder, G. W' (exact)
- [PASS] initials: bio ['G', 'W'] ~ stint ['G', 'W']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [PASS] colony: 5 placed event(s) resolve to 'South Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1888-1894
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: C.M.G
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

