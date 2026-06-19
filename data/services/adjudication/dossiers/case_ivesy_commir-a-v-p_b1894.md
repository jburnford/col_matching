<!-- {"case_id": "case_ivesy_commir-a-v-p_b1894", "bio_ids": ["ivesy_commir-a-v-p_b1894"], "stint_ids": ["Ivey, A. V. P___Nigeria___1927"]} -->
# Dossier case_ivesy_commir-a-v-p_b1894

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- Phase 1 found `ivesy_commir-a-v-p_b1894` ↔ `Ivey, A. V. P___Nigeria___1927` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Ivey, A. V. P___Nigeria___1927` is also gate-compatible with biography(ies) outside this case: ['ivey_commde-a-v-p_b1894'] (already linked elsewhere or filtered).

## Biography `ivesy_commir-a-v-p_b1894`

- Printed name: **IVESY, COMMIR. A. V. P**
- Birth year: 1894 (attested in editions [1940])
- Honours: R.D
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L65508.v` — printed in editions [1940]:**

> IVESY, COMMIR. A. V. P., R.D., R.N.R.; M.Inst.T.—B.1894; Royal Navy,1915; sub.lieut., R.N.R., 1917; lieut. commdr., 1927; commdr. (ret. list), 1935; Cameroons expedy. force, 1915-16; Harwich force destroyers, 1916-17; commanded Torpedo boats, 1918; commanded H.M. river gunboat "Robin" on West River, China, 1919; marine offr., Nigeria, 1920; harb. mast., Port Harcourt, 1926; prin. marine offr., 1930; ag. dir., marine, Oct., 1934 to May, 1935; dir., marine, 1935; el. younger brother, Trinity House, 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915 | Royal Navy | — | [1940] |
| 1 | 1915–1916 | Cameroons expedy. force | Cameroons | [1940] |
| 2 | 1916–1917 | Harwich force destroyers | Cameroons *(inherited from previous clause)* | [1940] |
| 3 | 1917 | sub.lieut., R.N.R | — | [1940] |
| 4 | 1918 | commanded Torpedo boats | Cameroons *(inherited from previous clause)* | [1940] |
| 5 | 1919 | commanded H.M. river gunboat "Robin" on West River, China | Cameroons *(inherited from previous clause)* | [1940] |
| 6 | 1920 | marine offr. | Nigeria | [1940] |
| 7 | 1926 | harb. mast., Port Harcourt | Nigeria *(inherited from previous clause)* | [1940] |
| 8 | 1927 | lieut. commdr | — | [1940] |
| 9 | 1930 | prin. marine offr | Nigeria *(inherited from previous clause)* | [1940] |
| 10 | 1934–1935 | ag. dir., marine | Nigeria *(inherited from previous clause)* | [1940] |
| 11 | 1935 | commdr. (ret. list) | — | [1940] |
| 12 | 1935 | dir., marine | Nigeria *(inherited from previous clause)* | [1940] |
| 13 | 1937 | el. younger brother, Trinity House | Nigeria *(inherited from previous clause)* | [1940] |

## Candidate stint `Ivey, A. V. P___Nigeria___1927`

- Staff-list name: **Ivey, A. V. P** | colony: **Nigeria** | listed 1927–1934 | editions [1927, 1929, 1933, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | A. V. P. Ivey | Senior Marine Officer | Marine | R.N.R. | Lieutenant |
| 1929 | Lieut. A. V. P. Ivey | Marine Officers, Grade I | Marine | — | — |
| 1933 | A. V. P. Ivey | Principal Marine Officer | Marine | — | — |
| 1934 | A. V. P. Ivey | Principal Marine Officers | Marine | — | — |

### Deterministic checks: `ivesy_commir-a-v-p_b1894` vs `Ivey, A. V. P___Nigeria___1927`

- [PASS] surname_gate: bio 'IVESY' vs stint 'Ivey, A. V. P' (fuzzy:1)
- [PASS] initials: bio ['C', 'A', 'V', 'P'] ~ stint ['A', 'V', 'P']
- [PASS] age_gate: stint starts 1927, birth 1894 (age 33)
- [PASS] colony: 10 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 5 event tenure(s) overlap stint years 1927-1934
- [PASS] position_sim: best 80 vs bar 60: 'prin. marine offr' ~ 'Principal Marine Officer'
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

