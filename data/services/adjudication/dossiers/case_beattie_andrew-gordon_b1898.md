<!-- {"case_id": "case_beattie_andrew-gordon_b1898", "bio_ids": ["beattie_andrew-gordon_b1898"], "stint_ids": ["Beattie, A. G___Nigeria___1934"]} -->
# Dossier case_beattie_andrew-gordon_b1898

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 12 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `beattie_andrew-gordon_b1898`

- Printed name: **BEATTIE, Andrew Gordon**
- Birth year: 1898 (attested in editions [1948, 1950, 1951])
- Appears in editions: [1940, 1948, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L31056.v` — printed in editions [1948, 1950, 1951]:**

> BEATTIE, Andrew Gordon, B.Sc. (Agric.) (B.S.A.)—b. 1898; ed. Ontario Agric. Coll. and Univ. of Toronto; on war serv. 1916-19, flt.-lt.; apptd. Nig., 1923; prin. agric. offr., 1937; asst. dir. of agric., 1939; dep. dir. of agric., 1942; dir. of agric., 1945; tour of agric. instns. in India under auspices of Carnegie trust.

**Version `col1940-L62267.v` — printed in editions [1940]:**

> BEATTIE, ANDREW GORDON—B. 1898; ed. Public Schl., Collegiate Inst. and Agrl. Coll., Ontario; ent. army, 1916; served with H.M. Forces, England, France and Germany 1916-19; agrl. offr., Nigeria, 1923; prin. do., 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1916 | ent. army | — | [1940] |
| 1 | 1916–1919 | served with H.M. Forces, England, France and Germany | — | [1940] |
| 2 | 1923 | apptd. Nig | — | [1948, 1950, 1951] |
| 3 | 1923 | agrl. offr. | Nigeria | [1940] |
| 4 | 1937 | prin. agric. offr | — | [1948, 1950, 1951] |
| 5 | 1937 | prin. do | Nigeria *(inherited from previous clause)* | [1940] |
| 6 | 1939 | asst. dir. of agric | — | [1948, 1950, 1951] |
| 7 | 1942 | dep. dir. of agric | — | [1948, 1950, 1951] |
| 8 | 1945 | dir. of agric | — | [1948, 1950, 1951] |

## Candidate stint `Beattie, A. G___Nigeria___1934`

- Staff-list name: **Beattie, A. G** | colony: **Nigeria** | listed 1934–1939 | editions [1934, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | A. G. Beattie | Superintendents | Agriculture | — | — |
| 1939 | A. G. Beattie | Principal Agricultural Officers | Agriculture | — | — |

### Deterministic checks: `beattie_andrew-gordon_b1898` vs `Beattie, A. G___Nigeria___1934`

- [PASS] surname_gate: bio 'BEATTIE' vs stint 'Beattie, A. G' (exact)
- [PASS] initials: bio ['A', 'G'] ~ stint ['A', 'G']
- [PASS] age_gate: stint starts 1934, birth 1898 (age 36)
- [PASS] colony: 2 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1934-1939
- [FAIL] position_sim: best 45 vs bar 60: 'agrl. offr.' ~ 'Principal Agricultural Officers'
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

