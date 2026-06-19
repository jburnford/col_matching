<!-- {"case_id": "case_stewart_duncan-george_b1904", "bio_ids": ["stewart_duncan-george_b1904"], "stint_ids": ["Stewart, D. G___Nigeria___1934"]} -->
# Dossier case_stewart_duncan-george_b1904

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 100 official(s) with this surname in the graph's staff lists; 53 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Stewart, D. G___Nigeria___1934` is also gate-compatible with biography(ies) outside this case: ['stewart_d_e1879'] (already linked elsewhere or filtered).

## Biography `stewart_duncan-george_b1904`

- Printed name: **STEWART, Duncan George**
- Birth year: 1904 (attested in editions [1948, 1949])
- Honours: C.M.G (1948)
- Appears in editions: [1948, 1949]

### Verbatim printed entry text (OCR)

**Version `col1948-L36154.v` — printed in editions [1948, 1949]:**

> STEWART, Duncan George, C.M.G. (1948).—b. 1904; ed. Winchester and Oriel Coll., Oxford, B.A.; cadet, Nig., 1928; asst. dist. offr., 1931; dist. offr., 1938; col. sec., Bahamas, 1944; fin. sec., Pal., 1947; p.s. lieut. gov., N.P., Nig., 1930-31; sec., W.A. gov. confce., 1939.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | cadet | Nigeria | [1948, 1949] |
| 1 | 1930–1931 | p.s. lieut. gov., N.P. | Nigeria | [1948, 1949] |
| 2 | 1931 | asst. dist. offr | Nigeria *(inherited from previous clause)* | [1948, 1949] |
| 3 | 1938 | dist. offr | Nigeria *(inherited from previous clause)* | [1948, 1949] |
| 4 | 1939 | sec., W.A. gov. confce | Nigeria *(inherited from previous clause)* | [1948, 1949] |
| 5 | 1944 | col. sec. | Bahamas | [1948, 1949] |
| 6 | 1947 | fin. sec. | Palestine | [1948, 1949] |

## Candidate stint `Stewart, D. G___Nigeria___1934`

- Staff-list name: **Stewart, D. G** | colony: **Nigeria** | listed 1934–1939 | editions [1934, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | D. G. Stewart | — | Administrative Service | — | — |
| 1939 | D. G. Stewart | Assistant Secretary | Nigerian Secretariat | — | — |

### Deterministic checks: `stewart_duncan-george_b1904` vs `Stewart, D. G___Nigeria___1934`

- [PASS] surname_gate: bio 'STEWART' vs stint 'Stewart, D. G' (exact)
- [PASS] initials: bio ['D', 'G'] ~ stint ['D', 'G']
- [PASS] age_gate: stint starts 1934, birth 1904 (age 30)
- [PASS] colony: 5 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1934-1939
- [FAIL] position_sim: best 48 vs bar 60: 'asst. dist. offr' ~ 'Assistant Secretary'
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

