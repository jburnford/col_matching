<!-- {"case_id": "case_juner_norman-ross_b1891", "bio_ids": ["juner_norman-ross_b1891"], "stint_ids": ["Junner, N. R___Gold Coast___1934"]} -->
# Dossier case_juner_norman-ross_b1891

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `juner_norman-ross_b1891`

- Printed name: **JUNER, NORMAN ROSS**
- Birth year: 1891 (attested in editions [1937])
- Honours: D.I.C., D.Sc., M.C., M.Inst.M.M., O.B.E. (1936)
- Appears in editions: [1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1937-L62268.v` — printed in editions [1937]:**

> JUNER, MAJOR NORMAN ROSS, O.B.E. (1936), M.C., D.Sc., D.I.C., M.Inst.M.M.—B. 1891; ed. Melbourne Univ. and Imp. Coll. of Sc. and Technology; 1851 exhibn. schol. for Mel bourne Univ., 1913; lect. in geology, schol. of Mines, Ballarat, 1919-20; war serv. in France, Italy and Malta, 1914-18; geologist, Gold Coast geol. surv., 1920; dir., Sierra Leone geol. surv., 1927; dir., Gold Coast geol. surv., Oct., 1930.

**Version `col1939-L68082.v` — printed in editions [1939, 1940]:**

> JUNNER, Major Norman Ross, O.B.E. (1936), M.C., D.Sc., D.I.C., M.Inst.M.M.—B. 1891; ed. Melbourne Univ. and Imp. Coll. of Sci. and Technology; 1851 exhibn. schol. for Melbourne Univ., 1913; lect. in geology, schl. of Mines, Ballarat, 1919-20; war serv. in France, Italy and Malta, 1914-18; geologist, Gold Coast geol. surv., 1920; dir., Sierra Leone geol. surv., 1927; dir., Gold Coast geol. surv., Oct., 1930.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1913–1913 | — | — | [1937] |
| 1 | 1913–1913 | 1851 exhibn. schol. | — | [1939, 1940] |
| 2 | 1914–1918 | war serv. | — | [1937, 1939, 1940] |
| 3 | 1919–1920 | lect. in geology | — | [1937, 1939, 1940] |
| 4 | 1920–1920 | geologist | Gold Coast | [1937, 1939, 1940] |
| 5 | 1927–1927 | dir. | Sierra Leone | [1937, 1939, 1940] |
| 6 | 1930 | dir. | Gold Coast | [1937, 1939, 1940] |

## Candidate stint `Junner, N. R___Gold Coast___1934`

- Staff-list name: **Junner, N. R** | colony: **Gold Coast** | listed 1934–1936 | editions [1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | N. R. Junner | Director of Geological Survey | Geological Survey | — | Major |
| 1936 | N. R. Junner | Director of Geological Survey | Geological Survey | — | — |

### Deterministic checks: `juner_norman-ross_b1891` vs `Junner, N. R___Gold Coast___1934`

- [PASS] surname_gate: bio 'JUNER' vs stint 'Junner, N. R' (fuzzy:1)
- [PASS] initials: bio ['N', 'R'] ~ stint ['N', 'R']
- [PASS] age_gate: stint starts 1934, birth 1891 (age 43)
- [PASS] colony: 2 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1934-1936
- [FAIL] position_sim: best 19 vs bar 60: 'dir.' ~ 'Director of Geological Survey'
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

