<!-- {"case_id": "case_stevens_charles-guy_b1903", "bio_ids": ["stevens_charles-guy_b1903"], "stint_ids": ["Stevens, C. G. B___Gibraltar___1923", "Stevens, C. G___Northern Rhodesia___1936"]} -->
# Dossier case_stevens_charles-guy_b1903

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 66 official(s) with this surname in the graph's staff lists; 28 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `stevens_charles-guy_b1903`

- Printed name: **STEVENS, Charles Guy**
- Birth year: 1903 (attested in editions [1948, 1949])
- Appears in editions: [1948, 1949]

### Verbatim printed entry text (OCR)

**Version `col1948-L36133.v` — printed in editions [1948, 1949]:**

> STEVENS, Charles Guy.—b. 1903; ed. Winchester Coll. (schol.) and New Coll., Oxford (schol.), 1st cl. hons. mod., 3rd cl. lit. hum., B.A.; on war serv. 1941-44; cadet, N. Rhod., 1931; seconded to C.O., 1937-39; clk. of coun., 1944; sec., African housing comsn., 1944; 1st ed. native newspaper Mutende, 1935; author of The Zimbabwe Temple, jt. author of St. Catherine's Hill (Hants. Field Club; report on four years excavations).

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1931 | cadet | Northern Rhodesia | [1948, 1949] |
| 1 | 1935 | 1st ed. native newspaper Mutende | Northern Rhodesia *(inherited from previous clause)* | [1948, 1949] |
| 2 | 1937–1939 | seconded to C.O | Northern Rhodesia *(inherited from previous clause)* | [1948, 1949] |
| 3 | 1944 | clk. of coun | Northern Rhodesia *(inherited from previous clause)* | [1948, 1949] |

## Candidate stint `Stevens, C. G. B___Gibraltar___1923`

- Staff-list name: **Stevens, C. G. B** | colony: **Gibraltar** | listed 1923–1924 | editions [1923, 1924]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1923 | C. G. B. Stevens | Assistant Military Secretary | Chief Military and Naval Officers | — | Captain |
| 1924 | C. G. B. Stevens | Assistant Military Secretary | Chief Military and Naval Officers | — | Captain |

### Deterministic checks: `stevens_charles-guy_b1903` vs `Stevens, C. G. B___Gibraltar___1923`

- [PASS] surname_gate: bio 'STEVENS' vs stint 'Stevens, C. G. B' (exact)
- [PASS] initials: bio ['C', 'G'] ~ stint ['C', 'G', 'B']
- [PASS] age_gate: stint starts 1923, birth 1903 (age 20)
- [FAIL] colony: no placed event resolves to 'Gibraltar'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1923-1924
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Stevens, C. G___Northern Rhodesia___1936`

- Staff-list name: **Stevens, C. G** | colony: **Northern Rhodesia** | listed 1936–1940 | editions [1936, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | C. G. Stevens | District Officers | District Administration | — | — |
| 1939 | C. G. Stevens | District Officer | District Administration | — | — |
| 1940 | C. G. Stevens | District Officer | District Administration | — | — |

### Deterministic checks: `stevens_charles-guy_b1903` vs `Stevens, C. G___Northern Rhodesia___1936`

- [PASS] surname_gate: bio 'STEVENS' vs stint 'Stevens, C. G' (exact)
- [PASS] initials: bio ['C', 'G'] ~ stint ['C', 'G']
- [PASS] age_gate: stint starts 1936, birth 1903 (age 33)
- [PASS] colony: 4 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1936-1940
- [FAIL] position_sim: best 30 vs bar 60: '1st ed. native newspaper Mutende' ~ 'District Officer'
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

