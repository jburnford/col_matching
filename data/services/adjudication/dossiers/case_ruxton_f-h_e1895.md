<!-- {"case_id": "case_ruxton_f-h_e1895", "bio_ids": ["ruxton_f-h_e1895"], "stint_ids": ["Ruxton, U. F. H___Nigeria___1915", "Ruxton, U. F. H___Nigeria___1925"]} -->
# Dossier case_ruxton_f-h_e1895

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Ruxton, U. F. H___Nigeria___1915` is also gate-compatible with biography(ies) outside this case: ['ruxton_upton-fitzherbert_b1873'] (already linked elsewhere or filtered).
- NOTE: stint `Ruxton, U. F. H___Nigeria___1925` is also gate-compatible with biography(ies) outside this case: ['ruxton_upton-fitzherbert_b1873'] (already linked elsewhere or filtered).

## Biography `ruxton_f-h_e1895`

- Printed name: **RUXTON, F. H.**
- Birth year: not printed
- Honours: C.M.G. (1925)
- Appears in editions: [1914, 1917, 1918, 1919, 1920, 1921, 1923, 1924, 1925]

### Verbatim printed entry text (OCR)

**Version `col1914-L49671.v` — printed in editions [1914, 1917, 1918, 1919, 1920, 1921, 1923, 1924, 1925]:**

> RUXTON, CAPT. F. H., C.M.G. (1925); Gazetted Worcestershire Regt., 1895; seconded Royal Niger Constab., 1898-1899; served in Africa, 1900; prov. adminstr., N. Nigeria, 1901; lat. cls. res., Ist Oct., 1906.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1895 | Gazetted | — | [1914, 1917, 1918, 1919, 1920, 1921, 1923, 1924, 1925] |
| 1 | 1898–1899 | seconded | Nigeria | [1914, 1917, 1918, 1919, 1920, 1921, 1923, 1924, 1925] |
| 2 | 1900–1900 | served | Africa | [1914, 1917, 1918, 1919, 1920, 1921, 1923, 1924, 1925] |
| 3 | 1901 | prov. adminstr. | Northern Nigeria | [1914, 1917, 1918, 1919, 1920, 1921, 1923, 1924, 1925] |
| 4 | 1906 | lat. cls. res. | — | [1914, 1917, 1918, 1919, 1920, 1921, 1923, 1924, 1925] |

## Candidate stint `Ruxton, U. F. H___Nigeria___1915`

- Staff-list name: **Ruxton, U. F. H** | colony: **Nigeria** | listed 1915–1919 | editions [1915, 1917, 1918, 1919]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1915 | U. F. H. Ruxton | Five First Class Residents or Commissioners | NORTHERN PROVINCES | — | Captain |
| 1917 | U. F. H. Ruxton | First Class Resident | Northern Provinces | — | Captain |
| 1918 | U. F. H. Ruxton | First Class Resident | Northern Provinces | — | Captain |
| 1919 | Capt. U. F. H. Ruxton | Five First Class Residents | NORTHERN PROVINCES | — | Captain |

### Deterministic checks: `ruxton_f-h_e1895` vs `Ruxton, U. F. H___Nigeria___1915`

- [PASS] surname_gate: bio 'RUXTON' vs stint 'Ruxton, U. F. H' (exact)
- [PASS] initials: bio ['F', 'H'] ~ stint ['U', 'F', 'H']
- [PASS] age_gate: stint starts 1915; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Nigeria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1915-1919
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Ruxton, U. F. H___Nigeria___1925`

- Staff-list name: **Ruxton, U. F. H** | colony: **Nigeria** | listed 1925–1927 | editions [1925, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | Capt. U. F. H. Ruxton | Ten Senior Residents | Political | — | — |
| 1927 | Major U. F. H. Ruxton | Lieutenant-Governor and Administrator | Lieutenant-Governor Southern Provinces | C.M.G. | Major |

### Deterministic checks: `ruxton_f-h_e1895` vs `Ruxton, U. F. H___Nigeria___1925`

- [PASS] surname_gate: bio 'RUXTON' vs stint 'Ruxton, U. F. H' (exact)
- [PASS] initials: bio ['F', 'H'] ~ stint ['U', 'F', 'H']
- [PASS] age_gate: stint starts 1925; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Nigeria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1925-1927
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

