<!-- {"case_id": "case_royer_n-w_b1906", "bio_ids": ["royer_n-w_b1906"], "stint_ids": ["Royer, N. W___Dominica___1963"]} -->
# Dossier case_royer_n-w_b1906

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `royer_n-w_b1906`

- Printed name: **ROYER, N. W**
- Birth year: 1906 (attested in editions [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1959-L27483.v` — printed in editions [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> ROYER, N. W.—b. 1906; ed. Dominica Gram. Sch.; clk., various depts., 1928-56; office manager, P.W.D., Dominica, 1957; col. postmaster, 1957.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928–1956 | clk., various depts | — | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1957 | office manager, P.W.D. | Dominica | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Royer, N. W___Dominica___1963`

- Staff-list name: **Royer, N. W** | colony: **Dominica** | listed 1963–1966 | editions [1963, 1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1963 | N. W. Royer | Colonial Postmaster | Civil Establishment | — | — |
| 1964 | N. W. Royer | Colonial Postmaster | Civil Establishment | — | — |
| 1965 | N. W. Royer | Colonial Postmaster | Civil Establishment | — | — |
| 1966 | N. W. Royer | Colonial Postmaster | Civil Establishment | — | — |

### Deterministic checks: `royer_n-w_b1906` vs `Royer, N. W___Dominica___1963`

- [PASS] surname_gate: bio 'ROYER' vs stint 'Royer, N. W' (exact)
- [PASS] initials: bio ['N', 'W'] ~ stint ['N', 'W']
- [PASS] age_gate: stint starts 1963, birth 1906 (age 57)
- [PASS] colony: 1 placed event(s) resolve to 'Dominica'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1963-1966
- [FAIL] position_sim: best 27 vs bar 60: 'office manager, P.W.D.' ~ 'Colonial Postmaster'
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

