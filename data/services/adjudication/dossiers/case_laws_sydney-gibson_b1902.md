<!-- {"case_id": "case_laws_sydney-gibson_b1902", "bio_ids": ["laws_sydney-gibson_b1902"], "stint_ids": ["Laws, S. G___Uganda___1933"]} -->
# Dossier case_laws_sydney-gibson_b1902

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `laws_sydney-gibson_b1902`

- Printed name: **LAWS, Sydney Gibson**
- Birth year: 1902 (attested in editions [1950, 1951])
- Honours: F.I.M.L.T
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1950-L37188.v` — printed in editions [1950, 1951]:**

> LAWS, Sydney Gibson, F.I.M.L.T.—b. 1902; ed. Brighton Avenue (Primary) and Gateshead Sec. Schs.; apptd. med. serv., Sudan, 1924; tech. offr., med. dept., Uga., 1927; vet. dept. res. lab., Entebbe, 1932; serv. on C.O. expdn. to Br. Hond. to invest. undiagnosed fevers, 1923; author of numerous articles on vet. matters for tech. jour.

**Version `col1948-L33965.v` — printed in editions [1948, 1949]:**

> LAWS, Sydney Gibson.—b. 1902; ed. Brighton Avenue (Primary) and Gateshead Sec. Schs., fellow inst. of med. lab. tech.; apptd. med. serv., Sudan, 1927; tech. offr., med. dept., Uga., 1927; vet. dept., 1932; lab. asslt., Entebbe; author of numerous articles on veterinary matters for technical journals.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1923 | serv. on C.O. expdn. to Br. Hond. to invest. undiagnosed fevers | Colonial Office | [1950, 1951] |
| 1 | 1924 | apptd. med. serv., Sudan | — | [1950, 1951] |
| 2 | 1927 | tech. offr., med. dept. | Uganda | [1948, 1949, 1950, 1951] |
| 3 | 1927 | apptd. med. serv., Sudan | — | [1948, 1949] |
| 4 | 1932 | vet. dept. res. lab., Entebbe | Uganda *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Laws, S. G___Uganda___1933`

- Staff-list name: **Laws, S. G** | colony: **Uganda** | listed 1933–1951 | editions [1933, 1937, 1940, 1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | S. G. Laws | Laboratory Assistant | Veterinary Department | — | — |
| 1937 | S. G. Laws | Laboratory Assistant | Veterinary Department | — | — |
| 1940 | S. G. Laws | Laboratory Assistant | Veterinary Department | — | — |
| 1949 | S. G. Laws | Laboratory Assistant | Veterinary | — | — |
| 1951 | S. G. Laws | Laboratory Assistant | Veterinary | — | — |

### Deterministic checks: `laws_sydney-gibson_b1902` vs `Laws, S. G___Uganda___1933`

- [PASS] surname_gate: bio 'LAWS' vs stint 'Laws, S. G' (exact)
- [PASS] initials: bio ['S', 'G'] ~ stint ['S', 'G']
- [PASS] age_gate: stint starts 1933, birth 1902 (age 31)
- [PASS] colony: 2 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1933-1951
- [FAIL] position_sim: best 41 vs bar 60: 'vet. dept. res. lab., Entebbe' ~ 'Laboratory Assistant'
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

