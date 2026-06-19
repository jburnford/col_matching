<!-- {"case_id": "case_morton_stanley-park_b1894", "bio_ids": ["morton_stanley-park_b1894"], "stint_ids": ["Morton, S. P___Straits Settlements___1923"]} -->
# Dossier case_morton_stanley-park_b1894

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 24 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `morton_stanley-park_b1894`

- Printed name: **MORTON, STANLEY PARK**
- Birth year: 1894 (attested in editions [1937, 1940])
- Appears in editions: [1937, 1940]

### Verbatim printed entry text (OCR)

**Version `col1937-L63282.v` — printed in editions [1937, 1940]:**

> MORTON, STANLEY PARK.—B. 1894; ed. Allen's Endowed Schol. and Armstrong Coll., Newcastle-on-Tyne; war serv., 1914-19; U.K., G.P.O., Feb., 1914; ast. divsn. engr., S.S., Mar., 1921; engr., P. and T., S.S. and F.M.S., Oct., 1926; engr., S'pore, Nov., 1927; div-sn. engr., Aug., 1935.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914 | U.K., G.P.O | — | [1937, 1940] |
| 1 | 1921 | ast. divsn. engr. | Straits Settlements | [1937, 1940] |
| 2 | 1926 | engr., P. and T., S.S. and F.M.S | Straits Settlements | [1937, 1940] |
| 3 | 1927 | engr., S'pore | Straits Settlements *(inherited from previous clause)* | [1937, 1940] |
| 4 | 1935 | div-sn. engr | Straits Settlements *(inherited from previous clause)* | [1937, 1940] |

## Candidate stint `Morton, S. P___Straits Settlements___1923`

- Staff-list name: **Morton, S. P** | colony: **Straits Settlements** | listed 1923–1932 | editions [1923, 1925, 1932]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1923 | S. P. Morton | Assistant Divisional Engineer, Telegraphs and Telephones | Post Office | — | — |
| 1925 | S. P. Morton | Assistant Divisional Engineer, Telegraphs and Telephones | Post Office | — | — |
| 1932 | S. P. Morton | Chief Telegraph Engineer | Posts and Telegraphs | — | — |

### Deterministic checks: `morton_stanley-park_b1894` vs `Morton, S. P___Straits Settlements___1923`

- [PASS] surname_gate: bio 'MORTON' vs stint 'Morton, S. P' (exact)
- [PASS] initials: bio ['S', 'P'] ~ stint ['S', 'P']
- [PASS] age_gate: stint starts 1923, birth 1894 (age 29)
- [PASS] colony: 4 placed event(s) resolve to 'Straits Settlements'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1923-1932
- [FAIL] position_sim: best 41 vs bar 60: 'ast. divsn. engr.' ~ 'Assistant Divisional Engineer, Telegraphs and Telephones'
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

