<!-- {"case_id": "case_urquhart_duncan-hector_b1897", "bio_ids": ["urquhart_duncan-hector_b1897"], "stint_ids": ["Urquhart, D. H___Nigeria___1934", "Urquhart, D. H___Nigeria___1958"]} -->
# Dossier case_urquhart_duncan-hector_b1897

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `urquhart_duncan-hector_b1897`

- Printed name: **URQUHART, Duncan Hector**
- Birth year: 1897 (attested in editions [1948, 1950, 1951])
- Appears in editions: [1948, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L36544.v` — printed in editions [1948, 1950, 1951]:**

> URQUHART, Duncan Hector, B.Sc.—b. 1897; on mil. serv., 1914-19; ed. Edin. Univ.; supt., agric., Nig., 1924; senr. agric. offr., 1937; prin., 1940; asst. dir., 1942; dir., agric., G.C. 1945.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1924 | supt., agric. | Nigeria | [1948, 1950, 1951] |
| 1 | 1937 | senr. agric. offr | Nigeria *(inherited from previous clause)* | [1948, 1950, 1951] |
| 2 | 1940 | prin | Nigeria *(inherited from previous clause)* | [1948, 1950, 1951] |
| 3 | 1942 | asst. dir | Nigeria *(inherited from previous clause)* | [1948, 1950, 1951] |
| 4 | 1945 | dir., agric. | Gold Coast | [1948, 1950, 1951] |

## Candidate stint `Urquhart, D. H___Nigeria___1934`

- Staff-list name: **Urquhart, D. H** | colony: **Nigeria** | listed 1934–1939 | editions [1934, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | D. H. Urquhart | Superintendents | Agriculture | — | — |
| 1934 | Urquhart | Conservators and Assistant Conservators | Forestry | — | — |
| 1939 | D. H. Urquhart | Senior Agricultural Officers | Agriculture | — | — |

### Deterministic checks: `urquhart_duncan-hector_b1897` vs `Urquhart, D. H___Nigeria___1934`

- [PASS] surname_gate: bio 'URQUHART' vs stint 'Urquhart, D. H' (exact)
- [PASS] initials: bio ['D', 'H'] ~ stint ['D', 'H']
- [PASS] age_gate: stint starts 1934, birth 1897 (age 37)
- [PASS] colony: 4 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1934-1939
- [PASS] position_sim: best 70 vs bar 60: 'senr. agric. offr' ~ 'Senior Agricultural Officers'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Urquhart, D. H___Nigeria___1958`

- Staff-list name: **Urquhart, D. H** | colony: **Nigeria** | listed 1958–1960 | editions [1958, 1960]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1958 | A. Urquhart | Permanent Secretaries and Senior District Officers | Civil Establishment | — | — |
| 1960 | A. Urquhart | Deputy Governor | Civil Establishment | C.M.G. | — |

### Deterministic checks: `urquhart_duncan-hector_b1897` vs `Urquhart, D. H___Nigeria___1958`

- [PASS] surname_gate: bio 'URQUHART' vs stint 'Urquhart, D. H' (exact)
- [PASS] initials: bio ['D', 'H'] ~ stint ['D', 'H']
- [PASS] age_gate: stint starts 1958, birth 1897 (age 61)
- [PASS] colony: 4 placed event(s) resolve to 'Nigeria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1958-1960
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

