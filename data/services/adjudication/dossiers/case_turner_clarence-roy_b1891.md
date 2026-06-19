<!-- {"case_id": "case_turner_clarence-roy_b1891", "bio_ids": ["turner_clarence-roy_b1891"], "stint_ids": ["Turner, C. R___Gold Coast___1932"]} -->
# Dossier case_turner_clarence-roy_b1891

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 107 official(s) with this surname in the graph's staff lists; 43 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `turner_clarence-roy_b1891`

- Printed name: **TURNER, CLARENCE ROY**
- Birth year: 1891 (attested in editions [1939, 1940])
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L71321.v` — printed in editions [1939, 1940]:**

> TURNER, MAJ. CLARENCE ROY, A.M.I.Mech.R., Chartered Mech. Eng.—B. 1891; ed. Brompton Pub. Schl. and Schl. of Mines, Adelaide, S. Australia; Australian Imp. Forces, 1914-19; Gallipoli and France (mentd. in despa.); majr., Apr., 1917; now majr., Reg. Army R. of O.; asst. loco. supt., Gt. Southern of Spain rly., Nov., 1919 to Aug., 1921; asst. loco. supt., rly. constrn., Nigeria, Jan., 1923; asst. loco. supt., Gold Coast rly., Jan., 1925; dist. loco. supt., Jan., 1927; run. supt., Jan., 1932; ch. mech. engnr., Feb., 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914–1919 | Australian Imp. Forces | — | [1939, 1940] |
| 1 | 1917 | majr | — | [1939, 1940] |
| 2 | 1919–1921 | asst. loco. supt., Gt. Southern of Spain rly | — | [1939, 1940] |
| 3 | 1923 | asst. loco. supt., rly. constrn. | Nigeria | [1939, 1940] |
| 4 | 1925 | asst. loco. supt., Gold Coast rly | Gold Coast | [1939, 1940] |
| 5 | 1927 | dist. loco. supt | Gold Coast *(inherited from previous clause)* | [1939, 1940] |
| 6 | 1932 | run. supt | Gold Coast *(inherited from previous clause)* | [1939, 1940] |
| 7 | 1937 | ch. mech. engnr | Gold Coast *(inherited from previous clause)* | [1939, 1940] |

## Candidate stint `Turner, C. R___Gold Coast___1932`

- Staff-list name: **Turner, C. R** | colony: **Gold Coast** | listed 1932–1936 | editions [1932, 1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1932 | C. R. Turner | District Locomotive Superintendents | Railway and Harbour Department | — | Major |
| 1934 | C. R. Turner | Running Superintendent | Railway and Harbour Department | — | Major |
| 1936 | C. R. Turner | Running Superintendent | Railway and Harbour Department | — | Major |

### Deterministic checks: `turner_clarence-roy_b1891` vs `Turner, C. R___Gold Coast___1932`

- [PASS] surname_gate: bio 'TURNER' vs stint 'Turner, C. R' (exact)
- [PASS] initials: bio ['C', 'R'] ~ stint ['C', 'R']
- [PASS] age_gate: stint starts 1932, birth 1891 (age 41)
- [PASS] colony: 4 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1932-1936
- [FAIL] position_sim: best 57 vs bar 60: 'dist. loco. supt' ~ 'District Locomotive Superintendents'
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

