<!-- {"case_id": "case_cleland_john-douglas_b1896", "bio_ids": ["cleland_john-douglas_b1896"], "stint_ids": ["Cleland, J. D___Tanganyika___1922"]} -->
# Dossier case_cleland_john-douglas_b1896

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 10 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `cleland_john-douglas_b1896`

- Printed name: **CLELAND, John Douglas**
- Birth year: 1896 (attested in editions [1930, 1931, 1932])
- Appears in editions: [1930, 1931, 1932]

### Verbatim printed entry text (OCR)

**Version `col1930-L63426.v` — printed in editions [1930, 1931, 1932]:**

> CLELAND, John Douglas.—B. 1896; B.Sc., Glasgow, 1920; ast. engrnr., Tanganyika Rly., Feb., 1921; dist. engrnr., Apr., 1928.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920 | B.Sc., Glasgow | — | [1930, 1931, 1932] |
| 1 | 1921 | ast. engrnr., Tanganyika Rly | Tanganyika | [1930, 1931, 1932] |
| 2 | 1928 | dist. engrnr | Tanganyika *(inherited from previous clause)* | [1930, 1931, 1932] |

## Candidate stint `Cleland, J. D___Tanganyika___1922`

- Staff-list name: **Cleland, J. D** | colony: **Tanganyika** | listed 1922–1925 | editions [1922, 1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | J. D. Cleland | Assistant Engineers | Railways | — | — |
| 1923 | J. D. Cleland | Assistant Engineers | Railways | — | — |
| 1924 | J. D. Cleland | Assistant Engineers | Railways | — | — |
| 1925 | J. D. Cleland | Assistant Engineers | Railways | — | — |

### Deterministic checks: `cleland_john-douglas_b1896` vs `Cleland, J. D___Tanganyika___1922`

- [PASS] surname_gate: bio 'CLELAND' vs stint 'Cleland, J. D' (exact)
- [PASS] initials: bio ['J', 'D'] ~ stint ['J', 'D']
- [PASS] age_gate: stint starts 1922, birth 1896 (age 26)
- [PASS] colony: 2 placed event(s) resolve to 'Tanganyika'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1922-1925
- [FAIL] position_sim: best 41 vs bar 60: 'ast. engrnr., Tanganyika Rly' ~ 'Assistant Engineers'
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

