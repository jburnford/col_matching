<!-- {"case_id": "case_darling_charles-brian-auchinleck_b1905", "bio_ids": ["darling_charles-brian-auchinleck_b1905"], "stint_ids": ["Darling, C. B. A___Gold Coast___1934"]} -->
# Dossier case_darling_charles-brian-auchinleck_b1905

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 12 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `darling_charles-brian-auchinleck_b1905`

- Printed name: **DARLING, Charles Brian Auchinleck**
- Birth year: 1905 (attested in editions [1948, 1949, 1950])
- Honours: C.M.G (1949)
- Appears in editions: [1948, 1949, 1950]

### Verbatim printed entry text (OCR)

**Version `col1948-L32107.v` — printed in editions [1948, 1949, 1950]:**

> DARLING, Charles Brian Auchinleck, C.M.G. (1949).—b. 1905; ed. Framlingham Coll., Jesus Coll., Camb., B.A. (Cantab.); cadet, G.C., 1928; dist. comsnr., 1937; asst. col. sec., 1938; seconded to C.O., 1939; to D.O., 1940; asst. ch. sec., E.A.G.C. (later E.A.H.C.), 1943.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | cadet | Gold Coast | [1948, 1949, 1950] |
| 1 | 1937 | dist. comsnr | Gold Coast *(inherited from previous clause)* | [1948, 1949, 1950] |
| 2 | 1938 | asst. col. sec | Gold Coast *(inherited from previous clause)* | [1948, 1949, 1950] |
| 3 | 1939 | seconded to C.O | Gold Coast *(inherited from previous clause)* | [1948, 1949, 1950] |
| 4 | 1940 | to D.O | Gold Coast *(inherited from previous clause)* | [1948, 1949, 1950] |
| 5 | 1943 | asst. ch. sec., E.A.G.C. (later E.A.H.C.) | Gold Coast *(inherited from previous clause)* | [1948, 1949, 1950] |

## Candidate stint `Darling, C. B. A___Gold Coast___1934`

- Staff-list name: **Darling, C. B. A** | colony: **Gold Coast** | listed 1934–1936 | editions [1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | C. B. A. Darling | District Commissioner / Assistant District Commissioner | Administrative and Political Service | — | — |
| 1936 | C. B. A. Darling | District Commissioner | Civil Establishment | — | — |

### Deterministic checks: `darling_charles-brian-auchinleck_b1905` vs `Darling, C. B. A___Gold Coast___1934`

- [PASS] surname_gate: bio 'DARLING' vs stint 'Darling, C. B. A' (exact)
- [PASS] initials: bio ['C', 'B', 'A'] ~ stint ['C', 'B', 'A']
- [PASS] age_gate: stint starts 1934, birth 1905 (age 29)
- [PASS] colony: 6 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1934-1936
- [PASS] position_sim: best 69 vs bar 60: 'dist. comsnr' ~ 'District Commissioner'
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

