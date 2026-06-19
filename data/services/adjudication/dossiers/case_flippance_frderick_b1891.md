<!-- {"case_id": "case_flippance_frderick_b1891", "bio_ids": ["flippance_frderick_b1891"], "stint_ids": ["Flippance, F___Hong Kong___1939", "Flippance, F___Straits Settlements___1925"]} -->
# Dossier case_flippance_frderick_b1891

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['flippance_frderick_b1891'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Flippance, F___Hong Kong___1939` is also gate-compatible with biography(ies) outside this case: ['flippanoe_frederick_b1891'] (already linked elsewhere or filtered).
- NOTE: stint `Flippance, F___Straits Settlements___1925` is also gate-compatible with biography(ies) outside this case: ['flippanoe_frederick_b1891'] (already linked elsewhere or filtered).

## Biography `flippance_frderick_b1891`

- Printed name: **FLIPPANCE, FRDERICK**
- Birth year: 1891 (attested in editions [1940])
- Honours: F.L.S
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L64279.v` — printed in editions [1940]:**

> FLIPPANCE, FRDERICK, F.L.S.—B. 1891; ed. Stoke schl., Surrey; edd. R. Botanic Gardens, Kew, 1913; war serv., France 1916-19; asst. curator, Botanic Gardens, S.S. (Singapore), 1919; local head of dept., Waterfall Gardens, Penang, 1921-37; supt., bot. and forestry dept., Hong Kong, 1937; mem., Nutrition Research couns., 1939; volunteer serv., capt., Malaya, S.S.U.F., 1919-38; capt., H.K.V.D.C., 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1913 | edd. R. Botanic Gardens, Kew | — | [1940] |
| 1 | 1919 | asst. curator, Botanic Gardens, S.S. (Singapore) | Straits Settlements | [1940] |
| 2 | 1919–1938 | volunteer serv., capt., Malaya, S.S.U.F | Hong Kong *(inherited from previous clause)* | [1940] |
| 3 | 1921–1937 | local head of dept., Waterfall Gardens, Penang | Straits Settlements *(inherited from previous clause)* | [1940] |
| 4 | 1937 | supt., bot. and forestry dept. | Hong Kong | [1940] |
| 5 | 1938 | capt., H.K.V.D.C | Hong Kong *(inherited from previous clause)* | [1940] |
| 6 | 1939 | mem., Nutrition Research couns | Hong Kong *(inherited from previous clause)* | [1940] |

## Candidate stint `Flippance, F___Hong Kong___1939`

- Staff-list name: **Flippance, F** | colony: **Hong Kong** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | F. Flippance | Superintendent | Botanical and Forestry Department | — | — |
| 1940 | F. Flippance | Superintendent | Botanical and Forestry Department | — | — |

### Deterministic checks: `flippance_frderick_b1891` vs `Flippance, F___Hong Kong___1939`

- [PASS] surname_gate: bio 'FLIPPANCE' vs stint 'Flippance, F' (exact)
- [PASS] initials: bio ['F'] ~ stint ['F']
- [PASS] age_gate: stint starts 1939, birth 1891 (age 48)
- [PASS] colony: 4 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 4 event tenure(s) overlap stint years 1939-1940
- [FAIL] position_sim: best 33 vs bar 60: 'mem., Nutrition Research couns' ~ 'Superintendent'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Flippance, F___Straits Settlements___1925`

- Staff-list name: **Flippance, F** | colony: **Straits Settlements** | listed 1925–1936 | editions [1925, 1931, 1932, 1933, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | F. Flippance | Assistant Curator (Penang) | Gardens | — | — |
| 1931 | F. Flippance | Assistant Curator (Penang) | Gardens | — | — |
| 1932 | F. Flippance | Assistant Curator (Penang) | Gardens | — | — |
| 1933 | F. Flippance | Assistant Curator (Penang) | Gardens | — | — |
| 1936 | F. Flippance | Assistant Curator (Penang) | Gardens | — | — |

### Deterministic checks: `flippance_frderick_b1891` vs `Flippance, F___Straits Settlements___1925`

- [PASS] surname_gate: bio 'FLIPPANCE' vs stint 'Flippance, F' (exact)
- [PASS] initials: bio ['F'] ~ stint ['F']
- [PASS] age_gate: stint starts 1925, birth 1891 (age 34)
- [PASS] colony: 2 placed event(s) resolve to 'Straits Settlements'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1925-1936
- [FAIL] position_sim: best 45 vs bar 60: 'local head of dept., Waterfall Gardens, Penang' ~ 'Assistant Curator (Penang)'
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

