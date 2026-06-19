<!-- {"case_id": "case_rae_r-g_b1917", "bio_ids": ["rae_r-g_b1917"], "stint_ids": ["Rae, R. G___Bahamas___1957"]} -->
# Dossier case_rae_r-g_b1917

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 27 official(s) with this surname in the graph's staff lists; 10 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `rae_r-g_b1917`

- Printed name: **RAE, R. G**
- Birth year: 1917 (attested in editions [1959, 1960, 1961, 1962, 1963, 1964, 1965])
- Appears in editions: [1959, 1960, 1961, 1962, 1963, 1964, 1965]

### Verbatim printed entry text (OCR)

**Version `col1959-L27052.v` — printed in editions [1959, 1960, 1961, 1962, 1963, 1964, 1965]:**

> RAE, R. G.—b. 1917; ed. Brighton, Hove and Sussex Gram. Sch.; mil. serv., 1940–46; supt., P.W.D., Grenada, 1953; D.P.W., Bah., 1957.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1953 | supt., P.W.D. | Grenada | [1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 1 | 1957 | D.P.W. | Bahamas | [1959, 1960, 1961, 1962, 1963, 1964, 1965] |

## Candidate stint `Rae, R. G___Bahamas___1957`

- Staff-list name: **Rae, R. G** | colony: **Bahamas** | listed 1957–1965 | editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1957 | R. G. Rae | Director of Public Works | Civil Establishment | — | — |
| 1958 | R. G. Rae | Director of Public Works | Civil Establishment | — | — |
| 1959 | R. G. Rae | Director of Public Works | Civil Establishment | — | — |
| 1960 | R. G. Rae | Director of Public Works | Civil Establishment | — | — |
| 1961 | R. G. Rae | Director of Public Works | Civil Establishment | — | — |
| 1962 | R. G. Rae | Director of Public Works | Civil Establishment | — | — |
| 1963 | R. G. Rae | Director of Public Works | Civil Establishment | — | — |
| 1964 | R. G. Rae | Director of Public Works | Civil Establishment | — | — |
| 1965 | R. G. Rae | Director of Public Works | Civil Establishment | — | — |

### Deterministic checks: `rae_r-g_b1917` vs `Rae, R. G___Bahamas___1957`

- [PASS] surname_gate: bio 'RAE' vs stint 'Rae, R. G' (exact)
- [PASS] initials: bio ['R', 'G'] ~ stint ['R', 'G']
- [PASS] age_gate: stint starts 1957, birth 1917 (age 40)
- [PASS] colony: 1 placed event(s) resolve to 'Bahamas'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1957-1965
- [FAIL] position_sim: best 22 vs bar 60: 'D.P.W.' ~ 'Director of Public Works'
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

