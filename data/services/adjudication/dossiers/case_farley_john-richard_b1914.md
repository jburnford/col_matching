<!-- {"case_id": "case_farley_john-richard_b1914", "bio_ids": ["farley_john-richard_b1914"], "stint_ids": ["Farley, J. R___Uganda___1939"]} -->
# Dossier case_farley_john-richard_b1914

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `farley_john-richard_b1914`

- Printed name: **FARLEY, John Richard**
- Birth year: 1914 (attested in editions [1948])
- Appears in editions: [1948]

### Verbatim printed entry text (OCR)

**Version `col1948-L32519.v` — printed in editions [1948]:**

> FARLEY, John Richard.—b. 1914; ed. St. Lawrence Coll., Ramsgate, and Sir Henry Thornton's Sch., Clapham, London; asst. inspr. of police, Uga., 1937; inspr., 1941; asst. supt., 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1937 | asst. inspr. of police | Uganda | [1948] |
| 1 | 1941 | inspr | Uganda *(inherited from previous clause)* | [1948] |
| 2 | 1946 | asst. supt | Uganda *(inherited from previous clause)* | [1948] |

## Candidate stint `Farley, J. R___Uganda___1939`

- Staff-list name: **Farley, J. R** | colony: **Uganda** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | J. R. Farley | Assistant Inspectors | Police | — | — |
| 1940 | J. R. Farley | Assistant Inspector | Police | — | — |

### Deterministic checks: `farley_john-richard_b1914` vs `Farley, J. R___Uganda___1939`

- [PASS] surname_gate: bio 'FARLEY' vs stint 'Farley, J. R' (exact)
- [PASS] initials: bio ['J', 'R'] ~ stint ['J', 'R']
- [PASS] age_gate: stint starts 1939, birth 1914 (age 25)
- [PASS] colony: 3 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1939-1940
- [FAIL] position_sim: best 51 vs bar 60: 'asst. inspr. of police' ~ 'Assistant Inspector'
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

