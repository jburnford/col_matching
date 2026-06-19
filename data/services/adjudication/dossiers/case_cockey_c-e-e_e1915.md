<!-- {"case_id": "case_cockey_c-e-e_e1915", "bio_ids": ["cockey_c-e-e_e1915"], "stint_ids": ["Cockey, C. E. E___Gold Coast___1934"]} -->
# Dossier case_cockey_c-e-e_e1915

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `cockey_c-e-e_e1915`

- Printed name: **COCKEY, C. E. E.**
- Birth year: not printed
- Appears in editions: [1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937]

### Verbatim printed entry text (OCR)

**Version `col1920-L52543.v` — printed in editions [1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937]:**

> COCKEY, C. E. E.—Ed. St. Edwards Schl. and Wadham Coll., Oxford; M.A.; served in France and Salonica; 3rd Devons, stchd. 2nd Glouce. Regt., May, 1915, to Jan., 1919; agt. capt.; mentd. in despatches; asst. dist. comsnr., Gold Coast, 13th June, 1919.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915–1919 | 3rd Devons, stchd. 2nd Glouce. Regt. | — | [1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937] |
| 1 | 1919 | asst. dist. comsnr. | Gold Coast | [1920, 1921, 1922, 1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937] |

## Candidate stint `Cockey, C. E. E___Gold Coast___1934`

- Staff-list name: **Cockey, C. E. E** | colony: **Gold Coast** | listed 1934–1936 | editions [1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | C. E. E. Cockey | District Commissioner / Assistant District Commissioner | Administrative and Political Service | — | — |
| 1936 | C. E. E. Cockey | District Commissioner | Civil Establishment | — | — |

### Deterministic checks: `cockey_c-e-e_e1915` vs `Cockey, C. E. E___Gold Coast___1934`

- [PASS] surname_gate: bio 'COCKEY' vs stint 'Cockey, C. E. E' (exact)
- [PASS] initials: bio ['C', 'E', 'E'] ~ stint ['C', 'E', 'E']
- [PASS] age_gate: stint starts 1934; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1934-1936
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

