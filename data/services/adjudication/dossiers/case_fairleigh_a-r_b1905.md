<!-- {"case_id": "case_fairleigh_a-r_b1905", "bio_ids": ["fairleigh_a-r_b1905"], "stint_ids": ["Fairleigh, A. R___North Borneo___1950"]} -->
# Dossier case_fairleigh_a-r_b1905

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `fairleigh_a-r_b1905`

- Printed name: **FAIRLEIGH, A. R**
- Birth year: 1905 (attested in editions [1956, 1957])
- Appears in editions: [1956, 1957]

### Verbatim printed entry text (OCR)

**Version `col1956-L21054.v` — printed in editions [1956, 1957]:**

> FAIRLEIGH, A. R.—b. 1905; ed. Lansdowne Sch., Seven Kings, and Sutton County Sch.; mil. serv., 1942–46, lieut.; Pal. police, 1929; inspr., 1938; supt., Maur., 1946; asst. supt., N. Borneo, 1949; dep. supt., 1953.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | Pal. police | Palestine | [1956, 1957] |
| 1 | 1938 | inspr | Palestine *(inherited from previous clause)* | [1956, 1957] |
| 2 | 1946 | supt. | Mauritius | [1956, 1957] |
| 3 | 1949 | asst. supt. | North Borneo | [1956, 1957] |
| 4 | 1953 | dep. supt | North Borneo *(inherited from previous clause)* | [1956, 1957] |

## Candidate stint `Fairleigh, A. R___North Borneo___1950`

- Staff-list name: **Fairleigh, A. R** | colony: **North Borneo** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | A. R. Fairleigh | Assistant Superintendent | POLICE | — | — |
| 1951 | A. R. Fairleigh | Assistant Superintendent | POLICE | — | — |

### Deterministic checks: `fairleigh_a-r_b1905` vs `Fairleigh, A. R___North Borneo___1950`

- [PASS] surname_gate: bio 'FAIRLEIGH' vs stint 'Fairleigh, A. R' (exact)
- [PASS] initials: bio ['A', 'R'] ~ stint ['A', 'R']
- [PASS] age_gate: stint starts 1950, birth 1905 (age 45)
- [PASS] colony: 2 placed event(s) resolve to 'North Borneo'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1950-1951
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

