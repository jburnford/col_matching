<!-- {"case_id": "case_etienne_j-t_b1906", "bio_ids": ["etienne_j-t_b1906"], "stint_ids": ["Etienne, J. T___Mauritius___1949"]} -->
# Dossier case_etienne_j-t_b1906

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `etienne_j-t_b1906`

- Printed name: **ETIENNE, J. T**
- Birth year: 1906 (attested in editions [1958, 1959, 1960, 1961, 1962, 1963, 1965, 1966])
- Honours: C.P.M
- Appears in editions: [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1958-L22348.v` — printed in editions [1958, 1959, 1960, 1961, 1962, 1963, 1965, 1966]:**

> ETIENNE, J. T., C.P.M.—b. 1906; ed. Royal Coll., Maur.; police constable, Maur., 1932; 1st cl. sgt., 1944; asst. supt., 1947; supt., police, 1952.

**Version `col1964-L16778.v` — printed in editions [1964]:**

> ETTIENNE, J. T., C.P.M.—b. 1906; ed. Royal Coll., Maur.; police constable, Maur., 1932; 1st cl. sgt., 1944; asst. supt., 1947; supt., police, 1952.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1932 | police constable | Mauritius | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1944 | 1st cl. sgt | Mauritius *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1947 | asst. supt | Mauritius *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1952 | supt., police | Mauritius *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Etienne, J. T___Mauritius___1949`

- Staff-list name: **Etienne, J. T** | colony: **Mauritius** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | J. T. Etienne | Assistant Superintendent | Police | — | — |
| 1950 | J. T. Etienne | Assistant Superintendent | Police | — | — |

### Deterministic checks: `etienne_j-t_b1906` vs `Etienne, J. T___Mauritius___1949`

- [PASS] surname_gate: bio 'ETIENNE' vs stint 'Etienne, J. T' (exact)
- [PASS] initials: bio ['J', 'T'] ~ stint ['J', 'T']
- [PASS] age_gate: stint starts 1949, birth 1906 (age 43)
- [PASS] colony: 4 placed event(s) resolve to 'Mauritius'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1950
- [FAIL] position_sim: best 55 vs bar 60: 'asst. supt' ~ 'Assistant Superintendent'
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

