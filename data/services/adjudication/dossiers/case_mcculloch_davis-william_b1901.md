<!-- {"case_id": "case_mcculloch_davis-william_b1901", "bio_ids": ["mcculloch_davis-william_b1901"], "stint_ids": ["McCulloch, D. W___Gold Coast___1930", "McCulloch, D. W___Gold Coast___1949"]} -->
# Dossier case_mcculloch_davis-william_b1901

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mcculloch_davis-william_b1901`

- Printed name: **McCULLOCH, Davis William**
- Birth year: 1901 (attested in editions [1948, 1949])
- Honours: A.I.W.E
- Appears in editions: [1948, 1949]

### Verbatim printed entry text (OCR)

**Version `col1948-L34232.v` — printed in editions [1948, 1949]:**

> McCULLOCH, Davis William, A.I.W.E.—b. 1901; asst. engrnr., Kumasi water supply, G.C., 1924; maintenance engrnr., water wks., 1930; exec. engrnr., 1939; senr. pub. health engrnr., 1943; asst. D.P.W., 1945; D.D.P.W., 1948.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1924 | asst. engrnr., Kumasi water supply | Gold Coast | [1948, 1949] |
| 1 | 1930 | maintenance engrnr., water wks | Gold Coast *(inherited from previous clause)* | [1948, 1949] |
| 2 | 1939 | exec. engrnr | Gold Coast *(inherited from previous clause)* | [1948, 1949] |
| 3 | 1943 | senr. pub. health engrnr | Gold Coast *(inherited from previous clause)* | [1948, 1949] |
| 4 | 1945 | asst. D.P.W | Gold Coast *(inherited from previous clause)* | [1948, 1949] |
| 5 | 1948 | D.D.P.W | Gold Coast *(inherited from previous clause)* | [1948, 1949] |

## Candidate stint `McCulloch, D. W___Gold Coast___1930`

- Staff-list name: **McCulloch, D. W** | colony: **Gold Coast** | listed 1930–1936 | editions [1930, 1932, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1930 | D. W. McCulloch | Executive Engineers | II. Provincial Engineering Staff | — | — |
| 1932 | D. W. McCulloch | Maintenance Engineer (Waterworks) | Public Works Department | — | — |
| 1936 | D. W. McCulloch | Maintenance Engineer | Public Works Department | — | — |

### Deterministic checks: `mcculloch_davis-william_b1901` vs `McCulloch, D. W___Gold Coast___1930`

- [PASS] surname_gate: bio 'McCULLOCH' vs stint 'McCulloch, D. W' (exact)
- [PASS] initials: bio ['D', 'W'] ~ stint ['D', 'W']
- [PASS] age_gate: stint starts 1930, birth 1901 (age 29)
- [PASS] colony: 6 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1930-1936
- [PASS] position_sim: best 88 vs bar 60: 'maintenance engrnr., water wks' ~ 'Maintenance Engineer (Waterworks)'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `McCulloch, D. W___Gold Coast___1949`

- Staff-list name: **McCulloch, D. W** | colony: **Gold Coast** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | D. W. McCulloch | Deputy Director of Public Works | Public Works | — | — |
| 1951 | D. W. McCulloch | Deputy Director of Public Works | Public Works | — | — |

### Deterministic checks: `mcculloch_davis-william_b1901` vs `McCulloch, D. W___Gold Coast___1949`

- [PASS] surname_gate: bio 'McCULLOCH' vs stint 'McCulloch, D. W' (exact)
- [PASS] initials: bio ['D', 'W'] ~ stint ['D', 'W']
- [PASS] age_gate: stint starts 1949, birth 1901 (age 48)
- [PASS] colony: 6 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 26 vs bar 60: 'asst. D.P.W' ~ 'Deputy Director of Public Works'
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

