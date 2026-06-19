<!-- {"case_id": "case_fairfoul_d-d_b1915", "bio_ids": ["fairfoul_d-d_b1915"], "stint_ids": ["Fairfoul, D. D___North Borneo___1950"]} -->
# Dossier case_fairfoul_d-d_b1915

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `fairfoul_d-d_b1915`

- Printed name: **FAIRFOUL, D. D**
- Birth year: 1915 (attested in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Honours: C.P.M (1961)
- Appears in editions: [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1956-L21052.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> FAIRFOUL, D. D., C.P.M. (1961).—b. 1915; ed. Rosemount, Los Angeles, U.S.A. and Prestwick High Sch., Scotland; Pal. police, 1937; asst. supt., 1944; N. Borneo, 1949; dep. supt., 1954; supt., 1956; asst. comsnr., 1958.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1937 | Pal. police | Palestine | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1944 | asst. supt | Palestine *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1949 | asst. supt | North Borneo | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1954 | dep. supt | North Borneo *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 4 | 1956 | supt | North Borneo *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 5 | 1958 | asst. comsnr | North Borneo *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Fairfoul, D. D___North Borneo___1950`

- Staff-list name: **Fairfoul, D. D** | colony: **North Borneo** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | D. D. Fairfoul | Assistant Superintendent | POLICE | — | — |
| 1951 | D. D. Fairfoul | Assistant Superintendent | POLICE | — | — |

### Deterministic checks: `fairfoul_d-d_b1915` vs `Fairfoul, D. D___North Borneo___1950`

- [PASS] surname_gate: bio 'FAIRFOUL' vs stint 'Fairfoul, D. D' (exact)
- [PASS] initials: bio ['D', 'D'] ~ stint ['D', 'D']
- [PASS] age_gate: stint starts 1950, birth 1915 (age 35)
- [PASS] colony: 4 placed event(s) resolve to 'North Borneo'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1950-1951
- [FAIL] position_sim: best 55 vs bar 60: 'asst. supt' ~ 'Assistant Superintendent'
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

