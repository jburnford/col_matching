<!-- {"case_id": "case_judd_leonard-warner_b1895", "bio_ids": ["judd_leonard-warner_b1895"], "stint_ids": ["Judd, L. W___Gold Coast___1927", "Judd, L. W___Gold Coast___1934", "Judd, L. W___Togoland___1920"]} -->
# Dossier case_judd_leonard-warner_b1895

## Case context

- 1 biography(ies) and 3 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `judd_leonard-warner_b1895`

- Printed name: **JUDD, Leonard Warner**
- Birth year: 1895 (attested in editions [1948, 1950, 1951])
- Appears in editions: [1948, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L33754.v` — printed in editions [1948, 1950, 1951]:**

> JUDD, Leonard Warner.—b. 1895; ed. Colchester Gram. Sch.; on mil. serv. 1914-19; asst. dist. comsnr., G.C., 1919; dist. comsnr., 1924; dep. prov. comsnr., 1939; prov. comsnr., 1942.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1919 | asst. dist. comsnr. | Gold Coast | [1948, 1950, 1951] |
| 1 | 1924 | dist. comsnr | Gold Coast *(inherited from previous clause)* | [1948, 1950, 1951] |
| 2 | 1939 | dep. prov. comsnr | Gold Coast *(inherited from previous clause)* | [1948, 1950, 1951] |
| 3 | 1942 | prov. comsnr | Gold Coast *(inherited from previous clause)* | [1948, 1950, 1951] |

## Candidate stint `Judd, L. W___Gold Coast___1927`

- Staff-list name: **Judd, L. W** | colony: **Gold Coast** | listed 1927–1929 | editions [1927, 1929]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | L. W. Judd | District Commissioner | Administrative and Political Service | — | — |
| 1929 | L. W. Judd | District Commissioner / Assistant District Commissioner | Administrative and Political Service | — | — |

### Deterministic checks: `judd_leonard-warner_b1895` vs `Judd, L. W___Gold Coast___1927`

- [PASS] surname_gate: bio 'JUDD' vs stint 'Judd, L. W' (exact)
- [PASS] initials: bio ['L', 'W'] ~ stint ['L', 'W']
- [PASS] age_gate: stint starts 1927, birth 1895 (age 32)
- [PASS] colony: 4 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1927-1929
- [PASS] position_sim: best 69 vs bar 60: 'dist. comsnr' ~ 'District Commissioner'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Judd, L. W___Gold Coast___1934`

- Staff-list name: **Judd, L. W** | colony: **Gold Coast** | listed 1934–1936 | editions [1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | L. W. Judd | District Commissioner / Assistant District Commissioner | Administrative and Political Service | — | — |
| 1936 | L. W. Judd | District Commissioner | Civil Establishment | — | — |

### Deterministic checks: `judd_leonard-warner_b1895` vs `Judd, L. W___Gold Coast___1934`

- [PASS] surname_gate: bio 'JUDD' vs stint 'Judd, L. W' (exact)
- [PASS] initials: bio ['L', 'W'] ~ stint ['L', 'W']
- [PASS] age_gate: stint starts 1934, birth 1895 (age 39)
- [PASS] colony: 4 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1934-1936
- [PASS] position_sim: best 69 vs bar 60: 'dist. comsnr' ~ 'District Commissioner'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Judd, L. W___Togoland___1920`

- Staff-list name: **Judd, L. W** | colony: **Togoland** | listed 1920–1925 | editions [1920, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1920 | L. W. Judd | Assistant District Commissioner | Administrative and Political Department | — | — |
| 1925 | L. W. Judd | District Commissioner / Assistant District Commissioner | Administrative and Political Service | — | — |

### Deterministic checks: `judd_leonard-warner_b1895` vs `Judd, L. W___Togoland___1920`

- [PASS] surname_gate: bio 'JUDD' vs stint 'Judd, L. W' (exact)
- [PASS] initials: bio ['L', 'W'] ~ stint ['L', 'W']
- [PASS] age_gate: stint starts 1920, birth 1895 (age 25)
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

