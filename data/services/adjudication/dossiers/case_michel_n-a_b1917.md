<!-- {"case_id": "case_michel_n-a_b1917", "bio_ids": ["michel_n-a_b1917"], "stint_ids": ["Michel, N. A___Seychelles___1959"]} -->
# Dossier case_michel_n-a_b1917

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `michel_n-a_b1917`

- Printed name: **MICHEL, N. A**
- Birth year: 1917 (attested in editions [1961, 1962, 1963, 1964])
- Honours: M.B.E (1962)
- Appears in editions: [1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1961-L25288.v` — printed in editions [1961, 1962, 1963, 1964]:**

> MICHEL, N. A., M.B.E. (1962).—b. 1917; ed. St. Louis Coll., Seychelles; mil. serv., 1951-46, capt.; asst. supt., police, Sey., 1947; dep. supt., 1960-63.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947 | asst. supt., police | Seychelles | [1961, 1962, 1963, 1964] |
| 1 | 1960–1963 | dep. supt | Seychelles *(inherited from previous clause)* | [1961, 1962, 1963, 1964] |

## Candidate stint `Michel, N. A___Seychelles___1959`

- Staff-list name: **Michel, N. A** | colony: **Seychelles** | listed 1959–1966 | editions [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1959 | N. A. Michel | Aide-de-Camp | Civil Establishment | — | Captain |
| 1960 | N. A. Michel | Aide-de-Camp | Civil Establishment | — | Captain |
| 1961 | N. A. Michel | Aide-de-Camp | Civil Establishment | — | Captain |
| 1962 | Capt. N. A. Michel | Aide-de-Camp | Civil Establishment | — | Captain |
| 1963 | Capt. N. A. Michel | Aide-de-Camp | Civil Establishment | — | Captain |
| 1964 | N. A. Michel. | Aide-de-Camp | Civil Establishment | — | Captain |
| 1965 | Capt. N. A. Michel | Aide-de-Camp | Civil Establishment | — | Captain |
| 1966 | Capt. N. A. Michel | Aide-de-Camp | Civil Establishment | — | Captain |

### Deterministic checks: `michel_n-a_b1917` vs `Michel, N. A___Seychelles___1959`

- [PASS] surname_gate: bio 'MICHEL' vs stint 'Michel, N. A' (exact)
- [PASS] initials: bio ['N', 'A'] ~ stint ['N', 'A']
- [PASS] age_gate: stint starts 1959, birth 1917 (age 42)
- [PASS] colony: 2 placed event(s) resolve to 'Seychelles'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1959-1966
- [FAIL] position_sim: best 33 vs bar 60: 'dep. supt' ~ 'Aide-de-Camp'
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

