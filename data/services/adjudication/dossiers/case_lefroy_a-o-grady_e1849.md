<!-- {"case_id": "case_lefroy_a-o-grady_e1849", "bio_ids": ["lefroy_a-o-grady_e1849"], "stint_ids": ["Lefroy, A. O. Grady___Western Australia___1877"]} -->
# Dossier case_lefroy_a-o-grady_e1849

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `lefroy_a-o-grady_e1849`

- Printed name: **LEFROY, A. O'GRADY**
- Birth year: not printed
- Honours: C.M.G. (1878)
- Appears in editions: [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897]

### Verbatim printed entry text (OCR)

**Version `col1883-L28352.v` — printed in editions [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897]:**

> LEFROY, A. O'GRADY, C.M.G. (1878).—Treasurer of Western Australia, 1856; was private secretary to Governor Fitzgerald, 1849 to 1855; acting colonial secretary, 1875, to August, 1879; now colonial treasurer.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1849–1855 | private secretary to Governor Fitzgerald | — | [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897] |
| 1 | 1856–1856 | Treasurer | Western Australia | [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897] |
| 2 | 1875–1879 | acting colonial secretary | — | [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897] |

## Candidate stint `Lefroy, A. O. Grady___Western Australia___1877`

- Staff-list name: **Lefroy, A. O. Grady** | colony: **Western Australia** | listed 1877–1880 | editions [1877, 1878, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | A. O'G. Lefroy | Treasurer | Civil Establishment | — | — |
| 1878 | A. O'G. Lefroy | Treasurer | Civil Establishment | — | — |
| 1879 | A. O. Grady Lefroy | Colonial Treasurer | Treasury | C.M.G. | — |
| 1880 | A. O. Grady Lefroy | Colonial Treasurer | Treasury Department | — | — |

### Deterministic checks: `lefroy_a-o-grady_e1849` vs `Lefroy, A. O. Grady___Western Australia___1877`

- [PASS] surname_gate: bio 'LEFROY' vs stint 'Lefroy, A. O. Grady' (exact)
- [PASS] initials: bio ['A', 'O'] ~ stint ['A', 'O', 'G']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Western Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1880
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: C.M.G.
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

