<!-- {"case_id": "case_morton_howard-henry_b1892", "bio_ids": ["morton_howard-henry_b1892"], "stint_ids": ["Morton, H. H___Tanganyika___1922", "Morton, H. H___Trinidad___1908"]} -->
# Dossier case_morton_howard-henry_b1892

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 24 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `morton_howard-henry_b1892`

- Printed name: **MORTON, HOWARD HENRY**
- Birth year: 1892 (attested in editions [1930, 1931])
- Appears in editions: [1930, 1931]

### Verbatim printed entry text (OCR)

**Version `col1930-L66985.v` — printed in editions [1930, 1931]:**

> MORTON, HOWARD HENRY.—B. 1892; ed. at Heriot Watt Coll.; H.M. Navy, 1915-19; astt. elec. engr., Tanganyika Territory, Mar., 1921.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915–1919 | H.M. Navy | — | [1930, 1931] |
| 1 | 1921 | astt. elec. engr., Tanganyika Territory | Tanganyika | [1930, 1931] |

## Candidate stint `Morton, H. H___Tanganyika___1922`

- Staff-list name: **Morton, H. H** | colony: **Tanganyika** | listed 1922–1925 | editions [1922, 1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | H. H. Morton | Shift Engineers | Electric Power Plant | — | — |
| 1923 | H. H. Morton | Shift Engineers | Electric Power Plant | — | — |
| 1924 | H. H. Morton | Assistant Electrical Engineers | Electric Power Plant | — | — |
| 1925 | H. H. Morton | Assistant Electrical Engineer | Electric Power Plant | — | — |

### Deterministic checks: `morton_howard-henry_b1892` vs `Morton, H. H___Tanganyika___1922`

- [PASS] surname_gate: bio 'MORTON' vs stint 'Morton, H. H' (exact)
- [PASS] initials: bio ['H', 'H'] ~ stint ['H', 'H']
- [PASS] age_gate: stint starts 1922, birth 1892 (age 30)
- [PASS] colony: 1 placed event(s) resolve to 'Tanganyika'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1922-1925
- [FAIL] position_sim: best 50 vs bar 60: 'astt. elec. engr., Tanganyika Territory' ~ 'Assistant Electrical Engineer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Morton, H. H___Trinidad___1908`

- Staff-list name: **Morton, H. H** | colony: **Trinidad** | listed 1908–1919 | editions [1908, 1911, 1918, 1919]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1908 | H. Morton | Reverend | Presbyterian Church | — | — |
| 1911 | H. Morton | Reverend | Presbyterian Church | — | — |
| 1918 | H. H. Morton | Reverend | Presbyterian Church | — | — |
| 1919 | H. H. Morton | Rev. | Presbyterian Church | — | — |

### Deterministic checks: `morton_howard-henry_b1892` vs `Morton, H. H___Trinidad___1908`

- [PASS] surname_gate: bio 'MORTON' vs stint 'Morton, H. H' (exact)
- [PASS] initials: bio ['H', 'H'] ~ stint ['H', 'H']
- [PASS] age_gate: stint starts 1908, birth 1892 (age 16)
- [FAIL] colony: no placed event resolves to 'Trinidad'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1908-1919
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

