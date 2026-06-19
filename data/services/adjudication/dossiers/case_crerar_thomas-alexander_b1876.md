<!-- {"case_id": "case_crerar_thomas-alexander_b1876", "bio_ids": ["crerar_thomas-alexander_b1876"], "stint_ids": ["Crerar, Thomas Alexander___Canada___1918"]} -->
# Dossier case_crerar_thomas-alexander_b1876

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `crerar_thomas-alexander_b1876`

- Printed name: **CRERAR, THOMAS ALEXANDER**
- Birth year: 1876 (attested in editions [1919, 1920, 1921, 1922])
- Appears in editions: [1918, 1919, 1920, 1921, 1922, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1936-L60011.v` — printed in editions [1936, 1937, 1939, 1940]:**

> CRERAR, HON. THOMAS ALEXANDER—Ed., pub. schls. and Collegiate, Portage la Prairie, Manitoba; teacher, farmer, grain elevator operator; invited to enter Union govt., 1917; P.C., Canada, 1917; min. of agr., 1917-19; M.P., Marquette, Manitoba, 1917-25; leader, progressive party, 1921-22; M.P., Brandon, 1930; min. of ryls. and canals, 1929-30; defeated, g.e. 1930; re-ele., g.e. 1935 as M.P. for Churchill; min. of mines, min. of immigrn. and colonization, min. of interior, and supt. gen., Indian affrs. in Mackenzie King cabinet, Oct., 1935.

**Version `col1919-L51536.v` — printed in editions [1919, 1920, 1921, 1922]:**

> CRERAR, HON. THOMAS ALEXANDER.—B. 1876; ed. pub. schl. and coll. inst. Portage la Prairie, Manitoba, and Manitoba Coll., Winnipeg; farmer; dir. of the Grain Growers Grain Co. Ltd., Winnipeg; now pres. of United Grain Growers Ltd.; joined fed. union govt., Canada as min. of agriculture, Oct., 1917; resigned portfolio, 1919; el. for Marquette, g.e., 1917; re-el. 1921; leader of the progressive party in H.C.

**Version `col1918-L49632.v` — printed in editions [1918]:**

> CREERAR, HON. THOMAS ALEXANDER.—B. 1876; ed. pub. schl. and coll. inst., Portage la Prairie, Manitoba, and Manitoba Coll., Winnipeg; farmer: dir. of the Grain Growers Grain Co., Ltd., Winnipeg; now pres. of United Grain Growers Ltd.; joined fed. union govt., Canada, as min. of agriculture, Oct., 1917.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1917 | invited to enter Union govt. | — | [1936, 1937, 1939, 1940] |
| 1 | 1917 | P.C. | Canada | [1919, 1920, 1921, 1922, 1936, 1937, 1939, 1940] |
| 2 | 1917–1919 | min. of agr. | — | [1918, 1936, 1937, 1939, 1940] |
| 3 | 1917–1925 | M.P., Marquette | Manitoba | [1936, 1937, 1939, 1940] |
| 4 | 1919 | resigned portfolio | Canada *(inherited from previous clause)* | [1919, 1920, 1921, 1922] |
| 5 | 1921–1922 | leader, progressive party | — | [1936, 1937, 1939, 1940] |
| 6 | 1921 | re-el | Canada *(inherited from previous clause)* | [1919, 1920, 1921, 1922] |
| 7 | 1929–1930 | min. of ryls. and canals | — | [1936, 1937, 1939, 1940] |
| 8 | 1930 | M.P., Brandon | — | [1936, 1937, 1939, 1940] |
| 9 | 1930 | defeated, g.e. | — | [1936, 1937, 1939, 1940] |
| 10 | 1935 | re-ele., g.e. as M.P. for Churchill | — | [1936, 1937, 1939, 1940] |
| 11 | 1935 | min. of mines, min. of immigrn. and colonization, min. of interior, and supt. gen., Indian affrs. in Mackenzie King cabinet | — | [1936, 1937, 1939, 1940] |

## Candidate stint `Crerar, Thomas Alexander___Canada___1918`

- Staff-list name: **Crerar, Thomas Alexander** | colony: **Canada** | listed 1918–1922 | editions [1918, 1919, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1918 | Thomas Alexander Crerar | Minister of Agriculture | The King's Privy Council for Canada | — | — |
| 1918 | Thomas A. Crerar | Minister of Agriculture | Agriculture and Statistics | — | — |
| 1919 | Thomas Alexander Crerar | Minister of Agriculture | Ministry | — | — |
| 1919 | Thomas A. Crerar | Minister of Agriculture | Agriculture and Statistics | — | — |
| 1922 | Thomas Alexander Crerar | Privy Councillor | Privy Council | — | — |

### Deterministic checks: `crerar_thomas-alexander_b1876` vs `Crerar, Thomas Alexander___Canada___1918`

- [PASS] surname_gate: bio 'CRERAR' vs stint 'Crerar, Thomas Alexander' (exact)
- [PASS] initials: bio ['T', 'A'] ~ stint ['T', 'A']
- [PASS] age_gate: stint starts 1918, birth 1876 (age 42)
- [PASS] colony: 3 placed event(s) resolve to 'Canada'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1918-1922
- [FAIL] position_sim: best 35 vs bar 60: 'resigned portfolio' ~ 'Privy Councillor'
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

