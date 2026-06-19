<!-- {"case_id": "case_prick-jones_william_e1917", "bio_ids": ["prick-jones_william_e1917"], "stint_ids": ["Price-Jones, W___Gold Coast___1927", "Price-Jones, W___Togoland___1920"]} -->
# Dossier case_prick-jones_william_e1917

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['prick-jones_william_e1917'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Price-Jones, W___Gold Coast___1927` is also gate-compatible with biography(ies) outside this case: ['price-jones_william_e1917'] (already linked elsewhere or filtered).
- NOTE: stint `Price-Jones, W___Togoland___1920` is also gate-compatible with biography(ies) outside this case: ['price-jones_william_e1917'] (already linked elsewhere or filtered).

## Biography `prick-jones_william_e1917`

- Printed name: **PRICK-JONES, WILLIAM**
- Birth year: not printed
- Appears in editions: [1933]

### Verbatim printed entry text (OCR)

**Version `col1933-L62785.v` — printed in editions [1933]:**

> PRICK-JONES, CAPT. WILLIAM.—Served during Great War in France; awarded M.C., 1917; asst. dist. comsnr., Gold Coast, Aug., 1919; dist. comsnr., Apr., 1924; called to bar, Gray's Inn, Nov., 1926; pol. mag., 1928.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1917 | awarded M.C | — | [1933] |
| 1 | 1919 | asst. dist. comsnr. | Gold Coast | [1933] |
| 2 | 1924 | dist. comsnr | Gold Coast *(inherited from previous clause)* | [1933] |
| 3 | 1926 | called to bar, Gray's Inn | Gold Coast *(inherited from previous clause)* | [1933] |
| 4 | 1928 | pol. mag | Gold Coast *(inherited from previous clause)* | [1933] |

## Candidate stint `Price-Jones, W___Gold Coast___1927`

- Staff-list name: **Price-Jones, W** | colony: **Gold Coast** | listed 1927–1936 | editions [1927, 1929, 1930, 1932, 1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | W. Price-Jones | District Commissioner | Administrative and Political Service | — | Captain |
| 1929 | W. Price-Jones | Police Magistrate | Judicial Department | — | Captain |
| 1930 | W. Price-Jones | Police Magistrate | Judicial Department | — | Captain |
| 1932 | W. Price-Jones | Police Magistrate | Judicial Department | — | Captain |
| 1934 | W. Price-Jones | Police Magistrate | Judicial Department | — | Captain |
| 1936 | W. Price-Jones | District Magistrate | Judicial Department | — | Captain |

### Deterministic checks: `prick-jones_william_e1917` vs `Price-Jones, W___Gold Coast___1927`

- [PASS] surname_gate: bio 'PRICK-JONES' vs stint 'Price-Jones, W' (fuzzy:1)
- [PASS] initials: bio ['W'] ~ stint ['W']
- [PASS] age_gate: stint starts 1927; no printed birth year — UNCHECKED
- [PASS] colony: 4 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1927-1936
- [PASS] position_sim: best 69 vs bar 60: 'dist. comsnr' ~ 'District Commissioner'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Price-Jones, W___Togoland___1920`

- Staff-list name: **Price-Jones, W** | colony: **Togoland** | listed 1920–1925 | editions [1920, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1920 | W. Price-Jones | Assistant District Commissioner | Administrative and Political Department | — | Captain |
| 1925 | Capt. W. Price-Jones | District Commissioner / Assistant District Commissioner | Administrative and Political Service | — | Captain |

### Deterministic checks: `prick-jones_william_e1917` vs `Price-Jones, W___Togoland___1920`

- [PASS] surname_gate: bio 'PRICK-JONES' vs stint 'Price-Jones, W' (fuzzy:1)
- [PASS] initials: bio ['W'] ~ stint ['W']
- [PASS] age_gate: stint starts 1920; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Togoland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1920-1925
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

