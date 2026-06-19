<!-- {"case_id": "case_hooper_john-george_b1893", "bio_ids": ["hooper_john-george_b1893"], "stint_ids": ["Hooper, J. G___Hong Kong___1936"]} -->
# Dossier case_hooper_john-george_b1893

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 21 official(s) with this surname in the graph's staff lists; 10 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hooper_john-george_b1893`

- Printed name: **HOOPER, John George**
- Birth year: 1893 (attested in editions [1950, 1951])
- Appears in editions: [1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1950-L36506.v` — printed in editions [1950, 1951]:**

> HOOPER, John George.—b. 1893; ed. secondary sch., R.S.I. cert. and dom. san. cert. of City and Guilds of Lond. Inst.; on mil. serv., 1914-19; sany. inspr., H.K., 1922; senr. health inspr., 1934; ch., 1940; supt., sany. serv., 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1922 | sany. inspr. | Hong Kong | [1950, 1951] |
| 1 | 1934 | senr. health inspr | Hong Kong *(inherited from previous clause)* | [1950, 1951] |
| 2 | 1940 | ch | Hong Kong *(inherited from previous clause)* | [1950, 1951] |
| 3 | 1947 | supt., sany. serv | Hong Kong *(inherited from previous clause)* | [1950, 1951] |

## Candidate stint `Hooper, J. G___Hong Kong___1936`

- Staff-list name: **Hooper, J. G** | colony: **Hong Kong** | listed 1936–1940 | editions [1936, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | J. G. Hooper | Senior Inspector | Sanitary Department | — | — |
| 1937 | J. G. Hooper | Senior Inspectors | Sanitary Department | — | — |
| 1939 | J. G. Hooper | Senior Inspectors | Sanitary Department | — | — |
| 1940 | J. G. Hooper | Senior Inspectors | Sanitary Department | — | — |

### Deterministic checks: `hooper_john-george_b1893` vs `Hooper, J. G___Hong Kong___1936`

- [PASS] surname_gate: bio 'HOOPER' vs stint 'Hooper, J. G' (exact)
- [PASS] initials: bio ['J', 'G'] ~ stint ['J', 'G']
- [PASS] age_gate: stint starts 1936, birth 1893 (age 43)
- [PASS] colony: 4 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1936-1940
- [PASS] position_sim: best 61 vs bar 60: 'senr. health inspr' ~ 'Senior Inspector'
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

