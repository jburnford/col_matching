<!-- {"case_id": "case_woodward_e-c_b1907", "bio_ids": ["woodward_e-c_b1907"], "stint_ids": ["Woodward, E. C___Fiji___1929"]} -->
# Dossier case_woodward_e-c_b1907

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 22 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `woodward_e-c_b1907`

- Printed name: **WOODWARD, E. C**
- Birth year: 1907 (attested in editions [1956, 1957])
- Appears in editions: [1956, 1957]

### Verbatim printed entry text (OCR)

**Version `col1956-L25129.v` — printed in editions [1956, 1957]:**

> WOODWARD, E. C.—b. 1907; clk., registr.-gen's dept., Fiji, 1928; dep. registr. of titles, 1946; senr. asst. registr.-gen., 1952.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | clk., registr.-gen's dept. | Fiji | [1956, 1957] |
| 1 | 1946 | dep. registr. of titles | Fiji *(inherited from previous clause)* | [1956, 1957] |
| 2 | 1952 | senr. asst. registr.-gen | Fiji *(inherited from previous clause)* | [1956, 1957] |

## Candidate stint `Woodward, E. C___Fiji___1929`

- Staff-list name: **Woodward, E. C** | colony: **Fiji** | listed 1929–1932 | editions [1929, 1930, 1932]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | E. C. Woodward | 2nd Class Clerk | Judicial and Legal Department | — | — |
| 1930 | E. C. Woodward | 2nd Class Clerk | Judicial and Legal Department | — | — |
| 1932 | E. C. Woodward | Draughtsman and Clerk | Judicial and Legal Departments | — | — |

### Deterministic checks: `woodward_e-c_b1907` vs `Woodward, E. C___Fiji___1929`

- [PASS] surname_gate: bio 'WOODWARD' vs stint 'Woodward, E. C' (exact)
- [PASS] initials: bio ['E', 'C'] ~ stint ['E', 'C']
- [PASS] age_gate: stint starts 1929, birth 1907 (age 22)
- [PASS] colony: 3 placed event(s) resolve to 'Fiji'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1929-1932
- [FAIL] position_sim: best 44 vs bar 60: 'clk., registr.-gen's dept.' ~ 'Draughtsman and Clerk'
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

