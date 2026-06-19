<!-- {"case_id": "case_walne_j-w-w_b1922", "bio_ids": ["walne_j-w-w_b1922"], "stint_ids": ["Walne, J. W. W___North Borneo___1949"]} -->
# Dossier case_walne_j-w-w_b1922

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `walne_j-w-w_b1922`

- Printed name: **WALNE, J. W. W**
- Birth year: 1922 (attested in editions [1963, 1964, 1965])
- Honours: C.P.M (1961)
- Appears in editions: [1963, 1964, 1965]

### Verbatim printed entry text (OCR)

**Version `col1963-L26003.v` — printed in editions [1963, 1964, 1965]:**

> WALNE, J. W. W., C.P.M. (1961).—b. 1922; ed. Sydney H. Sch., Aust.; mil. serv., 1941-46, A.I.F., capt.; asst. supt. police, N. Borneo, 1946; Mal., 1948-49; asst. supt., N. Borneo, 1951; dep. supt., 1958-64.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | asst. supt. police | North Borneo | [1963, 1964, 1965] |
| 1 | 1948–1949 | asst. supt. police | Malaya | [1963, 1964, 1965] |
| 2 | 1951 | asst. supt. | North Borneo | [1963, 1964, 1965] |
| 3 | 1958–1964 | dep. supt | North Borneo *(inherited from previous clause)* | [1963, 1964, 1965] |

## Candidate stint `Walne, J. W. W___North Borneo___1949`

- Staff-list name: **Walne, J. W. W** | colony: **North Borneo** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | J. W. W. Walne | Adjutant (m) | CONSTABULARY | — | — |
| 1950 | J. W. Walne | Assistant Superintendent | POLICE | — | — |
| 1951 | J. W. Walne | Assistant Superintendent | POLICE | — | — |

### Deterministic checks: `walne_j-w-w_b1922` vs `Walne, J. W. W___North Borneo___1949`

- [PASS] surname_gate: bio 'WALNE' vs stint 'Walne, J. W. W' (exact)
- [PASS] initials: bio ['J', 'W', 'W'] ~ stint ['J', 'W', 'W']
- [PASS] age_gate: stint starts 1949, birth 1922 (age 27)
- [PASS] colony: 3 placed event(s) resolve to 'North Borneo'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 55 vs bar 60: 'asst. supt.' ~ 'Assistant Superintendent'
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

