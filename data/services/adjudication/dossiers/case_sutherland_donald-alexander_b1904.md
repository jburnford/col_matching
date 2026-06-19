<!-- {"case_id": "case_sutherland_donald-alexander_b1904", "bio_ids": ["sutherland_donald-alexander_b1904"], "stint_ids": ["Sutherland, D. A___Gold Coast___1934"]} -->
# Dossier case_sutherland_donald-alexander_b1904

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 36 official(s) with this surname in the graph's staff lists; 24 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `sutherland_donald-alexander_b1904`

- Printed name: **SUTHERLAND, Donald Alexander**
- Birth year: 1904 (attested in editions [1948, 1950, 1951])
- Appears in editions: [1948, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L36240.v` — printed in editions [1948, 1950, 1951]:**

> SUTHERLAND, Donald Alexander.—b. 1904; ed. Glasgow Univ., M.A. (hons.); cadet, admin., G.C., 1927; asst. dist. comsnr., 1928; dist. comsnr., 1937; admin. offr., cl. II, 1946; cl. I, 1946; sec. to min. of commerce and indu., 1950.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | cadet, admin. | Gold Coast | [1948, 1950, 1951] |
| 1 | 1928 | asst. dist. comsnr | Gold Coast *(inherited from previous clause)* | [1948, 1950, 1951] |
| 2 | 1937 | dist. comsnr | Gold Coast *(inherited from previous clause)* | [1948, 1950, 1951] |
| 3 | 1946 | admin. offr., cl. II | Gold Coast *(inherited from previous clause)* | [1948, 1950, 1951] |
| 4 | 1950 | sec. to min. of commerce and indu | Gold Coast *(inherited from previous clause)* | [1948, 1950, 1951] |

## Candidate stint `Sutherland, D. A___Gold Coast___1934`

- Staff-list name: **Sutherland, D. A** | colony: **Gold Coast** | listed 1934–1936 | editions [1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | D. A. Sutherland | District Commissioner / Assistant District Commissioner | Administrative and Political Service | — | — |
| 1936 | D. A. Sutherland | District Commissioner | Civil Establishment | — | — |

### Deterministic checks: `sutherland_donald-alexander_b1904` vs `Sutherland, D. A___Gold Coast___1934`

- [PASS] surname_gate: bio 'SUTHERLAND' vs stint 'Sutherland, D. A' (exact)
- [PASS] initials: bio ['D', 'A'] ~ stint ['D', 'A']
- [PASS] age_gate: stint starts 1934, birth 1904 (age 30)
- [PASS] colony: 5 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1934-1936
- [PASS] position_sim: best 69 vs bar 60: 'dist. comsnr' ~ 'District Commissioner'
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

