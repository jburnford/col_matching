<!-- {"case_id": "case_shade_winifred_b1899", "bio_ids": ["shade_winifred_b1899", "slade_walter_b1877"], "stint_ids": ["Slade, W. E___South Australia___1905", "Slade, W___Tanganyika___1922"]} -->
# Dossier case_shade_winifred_b1899

## Case context

- 2 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['shade_winifred_b1899', 'slade_walter_b1877'] carry a single initial only — the namesake trap applies.
- CONTESTED: stint(s) ['Slade, W___Tanganyika___1922'] have more than one claimant biography in this case.

## Biography `shade_winifred_b1899`

- Printed name: **SHADE, Winifred**
- Birth year: 1899 (attested in editions [1949, 1950, 1951])
- Appears in editions: [1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1949-L35554.v` — printed in editions [1949, 1950, 1951]:**

> SHADE, Winifred.—b. 1899; ed. Council Sch., and Coll., Liverpool; nursing sister, Ken., 1933.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1933 | nursing sister | Kenya | [1949, 1950, 1951] |

## Biography `slade_walter_b1877`

- Printed name: **SLADE, WALTER**
- Birth year: 1877 (attested in editions [1929, 1930, 1932])
- Appears in editions: [1929, 1930, 1932]

### Verbatim printed entry text (OCR)

**Version `col1929-L64013.v` — printed in editions [1929, 1930, 1932]:**

> SLADE, WALTER, A.M. Inst. T.—B. 1877; L. and Y. rly., 1892; minor appts., S. Africa, S. America and India; E. African milly., Riya., 1917; gen. foreman, Tanganyika rlya., Apr., 1919; asst. loco. supt., Tanganyika rlya., Mar., 1921.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1892 | L. and Y. rly | — | [1929, 1930, 1932] |
| 1 | 1917 | E. African milly., Riya | — | [1929, 1930, 1932] |
| 2 | 1919 | gen. foreman, Tanganyika rlya | Tanganyika | [1929, 1930, 1932] |
| 3 | 1921 | asst. loco. supt., Tanganyika rlya | Tanganyika | [1929, 1930, 1932] |

## Candidate stint `Slade, W. E___South Australia___1905`

- Staff-list name: **Slade, W. E** | colony: **South Australia** | listed 1905–1906 | editions [1905, 1906]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | W. E. Slade | Assistant Engineer | Engineer-in-Chief's Department | — | — |
| 1906 | W. E. Slade | Assistant Engineer | Engineer-in-Chief's Department | — | — |

### Deterministic checks: `slade_walter_b1877` vs `Slade, W. E___South Australia___1905`

- [PASS] surname_gate: bio 'SLADE' vs stint 'Slade, W. E' (exact)
- [PASS] initials: bio ['W'] ~ stint ['W', 'E']
- [PASS] age_gate: stint starts 1905, birth 1877 (age 28)
- [FAIL] colony: no placed event resolves to 'South Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1906
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Slade, W___Tanganyika___1922`

- Staff-list name: **Slade, W** | colony: **Tanganyika** | listed 1922–1925 | editions [1922, 1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | W. Slade | Assistant Locomotive Superintendents | Railways | — | — |
| 1923 | W. Slade | Assistant Locomotive Superintendents | Railways | — | — |
| 1924 | W. Slade | Assistant Locomotive Superintendents | Railways | — | — |
| 1925 | W. Slade | Assistant Locomotive Superintendents | Railways | — | — |

### Deterministic checks: `shade_winifred_b1899` vs `Slade, W___Tanganyika___1922`

- [PASS] surname_gate: bio 'SHADE' vs stint 'Slade, W' (fuzzy:1)
- [PASS] initials: bio ['W'] ~ stint ['W']
- [PASS] age_gate: stint starts 1922, birth 1899 (age 23)
- [FAIL] colony: no placed event resolves to 'Tanganyika'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1922-1925
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `slade_walter_b1877` vs `Slade, W___Tanganyika___1922`

- [PASS] surname_gate: bio 'SLADE' vs stint 'Slade, W' (exact)
- [PASS] initials: bio ['W'] ~ stint ['W']
- [PASS] age_gate: stint starts 1922, birth 1877 (age 45)
- [PASS] colony: 2 placed event(s) resolve to 'Tanganyika'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1922-1925
- [FAIL] position_sim: best 48 vs bar 60: 'asst. loco. supt., Tanganyika rlya' ~ 'Assistant Locomotive Superintendents'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

