<!-- {"case_id": "case_woolley_ronald-wynne_b1905", "bio_ids": ["woolley_ronald-wynne_b1905"], "stint_ids": ["Woolley, R. W___Gold Coast___1934"]} -->
# Dossier case_woolley_ronald-wynne_b1905

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 10 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `woolley_ronald-wynne_b1905`

- Printed name: **WOOLLEY, Ronald Wynne**
- Birth year: 1905 (attested in editions [1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951, 1956, 1957]

### Verbatim printed entry text (OCR)

**Version `col1950-L40958.v` — printed in editions [1950, 1951]:**

> WOOLLEY, Ronald Wynne.—b. 1905; ed. Worcester Cathedral Choir Sch., Worcester Cathedral King’s Sch. and Christ’s Coll., Camb., M.A.; cadet admin., G.C., 1927; asst. dist. comsnr., 1928; dist. comsnr., 1937; admin. offr., cl. II, 1948.

**Version `col1956-L25137.v` — printed in editions [1956, 1957]:**

> WOOLLEY, R. W.—b. 1905; ed. King's Sch. and Camb. Univ.; cadet, G.C., 1927; dist. comsnr., 1937; admin. offr., cl. II, 1948; cl. I, G.C. local service, 1955.

**Version `col1948-L37036.v` — printed in editions [1948, 1949]:**

> WOOLLEY, Ronald Wynne.—b. 1905; ed. Worcester Cathedral, King’s Sch. and Christ’s Coll., Cambridge, M.A.; cadet., G.C., 1927; dist. comsnr., 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | cadet admin. | Gold Coast | [1948, 1949, 1950, 1951, 1956, 1957] |
| 1 | 1928 | asst. dist. comsnr | Gold Coast *(inherited from previous clause)* | [1950, 1951] |
| 2 | 1937 | dist. comsnr | Gold Coast *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1956, 1957] |
| 3 | 1948 | admin. offr., cl. II | Gold Coast *(inherited from previous clause)* | [1950, 1951, 1956, 1957] |
| 4 | 1955 | cl. I, G.C. local service | Gold Coast | [1956, 1957] |

## Candidate stint `Woolley, R. W___Gold Coast___1934`

- Staff-list name: **Woolley, R. W** | colony: **Gold Coast** | listed 1934–1936 | editions [1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | R. W. Woolley | District Commissioner / Assistant District Commissioner | Administrative and Political Service | — | — |
| 1936 | R. W. Woolley | District Commissioner | Civil Establishment | — | — |

### Deterministic checks: `woolley_ronald-wynne_b1905` vs `Woolley, R. W___Gold Coast___1934`

- [PASS] surname_gate: bio 'WOOLLEY' vs stint 'Woolley, R. W' (exact)
- [PASS] initials: bio ['R', 'W'] ~ stint ['R', 'W']
- [PASS] age_gate: stint starts 1934, birth 1905 (age 29)
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

