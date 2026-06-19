<!-- {"case_id": "case_davies_b-v_b1927", "bio_ids": ["davies_b-v_b1927"], "stint_ids": ["Davies, B. V___Fiji___1965"]} -->
# Dossier case_davies_b-v_b1927

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 137 official(s) with this surname in the graph's staff lists; 84 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `davies_b-v_b1927`

- Printed name: **DAVIES, B. V**
- Birth year: 1927 (attested in editions [1963, 1964, 1965, 1966])
- Appears in editions: [1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1963-L18859.v` — printed in editions [1963, 1964, 1965, 1966]:**

> DAVIES, B. V.—b. 1927; ed. Magdalen Coll. Sch. and Worcester Coll., Oxford; mil. serv., 1945–48, lt.; admin. offr., cl. IIB, Fiji, 1952; secon. D.T.C., 1961; cl. IIA, 1962; Fiji, 1963; cl. I, 1964; asst. coll. sec., 1964.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1952 | admin. offr., cl. IIB | Fiji | [1963, 1964, 1965, 1966] |
| 1 | 1961 | secon. D.T.C | Fiji *(inherited from previous clause)* | [1963, 1964, 1965, 1966] |
| 2 | 1962 | cl. IIA | Fiji *(inherited from previous clause)* | [1963, 1964, 1965, 1966] |
| 3 | 1963 | cl. IIA | Fiji | [1963, 1964, 1965, 1966] |
| 4 | 1964 | cl. I | Fiji *(inherited from previous clause)* | [1963, 1964, 1965, 1966] |

## Candidate stint `Davies, B. V___Fiji___1965`

- Staff-list name: **Davies, B. V** | colony: **Fiji** | listed 1965–1966 | editions [1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1965 | B. V. Davies | Assistant Colonial Secretary | Civil Establishment | — | — |
| 1966 | B. V. Davies | Assistant Colonial Secretary | Civil Establishment | — | — |

### Deterministic checks: `davies_b-v_b1927` vs `Davies, B. V___Fiji___1965`

- [PASS] surname_gate: bio 'DAVIES' vs stint 'Davies, B. V' (exact)
- [PASS] initials: bio ['B', 'V'] ~ stint ['B', 'V']
- [PASS] age_gate: stint starts 1965, birth 1927 (age 38)
- [PASS] colony: 5 placed event(s) resolve to 'Fiji'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1965-1966
- [FAIL] position_sim: best 24 vs bar 60: 'cl. IIA' ~ 'Assistant Colonial Secretary'
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

