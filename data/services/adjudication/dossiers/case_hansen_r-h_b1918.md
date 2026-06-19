<!-- {"case_id": "case_hansen_r-h_b1918", "bio_ids": ["hansen_r-h_b1918"], "stint_ids": ["Hansen, R. H___North Borneo___1949"]} -->
# Dossier case_hansen_r-h_b1918

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 12 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hansen_r-h_b1918`

- Printed name: **HANSEN, R. H**
- Birth year: 1918 (attested in editions [1958, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Honours: C.P.M (1960), M.B.E
- Appears in editions: [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1958-L23324.v` — printed in editions [1958, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> HANSEN, R. H., M.B.E., C.P.M. (1960).—b. 1918; ed. Lawrence Coll., Muree, N. India; mil. serv., 1939-45, sqdn. ldr.; B.M.A., N. Borneo, 1946; asst. supt., police, 1947; dep. supt., 1957; supt., 1958-65.

**Version `col1959-L23821.v` — printed in editions [1959]:**

> HANSON, R. H., M.B.E.—b. 1918; ed. Lawrence Coll., Murree, N. India; mil. serv., 1939-45, sqdn. ldr.; B.M.A., N. Borneo, 1946; asst. supt., police, 1947; dep. supt., 1957.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | B.M.A. | North Borneo | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1947 | asst. supt., police | North Borneo *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1957 | dep. supt | North Borneo *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1958–1965 | supt | North Borneo *(inherited from previous clause)* | [1958, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Hansen, R. H___North Borneo___1949`

- Staff-list name: **Hansen, R. H** | colony: **North Borneo** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | R. H. Hansen | Assistant Superintendents (m) | CONSTABULARY | — | — |
| 1950 | R. H. Hansen | Assistant Superintendent | POLICE | — | — |
| 1951 | R. H. Hansen | Assistant Superintendent | POLICE | M.B.E. | — |

### Deterministic checks: `hansen_r-h_b1918` vs `Hansen, R. H___North Borneo___1949`

- [PASS] surname_gate: bio 'HANSEN' vs stint 'Hansen, R. H' (exact)
- [PASS] initials: bio ['R', 'H'] ~ stint ['R', 'H']
- [PASS] age_gate: stint starts 1949, birth 1918 (age 31)
- [PASS] colony: 4 placed event(s) resolve to 'North Borneo'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 47 vs bar 60: 'asst. supt., police' ~ 'Assistant Superintendents (m)'
- [PASS] honour: shared: M.B.E
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

