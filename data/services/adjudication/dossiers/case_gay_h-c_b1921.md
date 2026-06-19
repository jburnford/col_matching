<!-- {"case_id": "case_gay_h-c_b1921", "bio_ids": ["gay_h-c_b1921"], "stint_ids": ["Gay, H. C___North Borneo___1950"]} -->
# Dossier case_gay_h-c_b1921

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `gay_h-c_b1921`

- Printed name: **GAY, H. C**
- Birth year: 1921 (attested in editions [1960, 1961, 1962, 1963, 1964])
- Honours: C.P.M (1962)
- Appears in editions: [1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1960-L23241.v` — printed in editions [1960, 1961, 1962, 1963, 1964]:**

> GAY, H. C., C.P.M. (1962).—b. 1921; ed. Franklin Hse. Prep. Sch. and Southgate Gram. Sch.; mil. serv., 1939–46, major (Gurkhas); asst. supt., police, N. Borneo, 1949; dep. supt., 1956–63.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1949 | asst. supt., police | North Borneo | [1960, 1961, 1962, 1963, 1964] |
| 1 | 1956–1963 | dep. supt | North Borneo *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Gay, H. C___North Borneo___1950`

- Staff-list name: **Gay, H. C** | colony: **North Borneo** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | H. C. Gay | Assistant Superintendent | POLICE | — | — |
| 1951 | H. C. Gay | Assistant Superintendent | POLICE | — | — |

### Deterministic checks: `gay_h-c_b1921` vs `Gay, H. C___North Borneo___1950`

- [PASS] surname_gate: bio 'GAY' vs stint 'Gay, H. C' (exact)
- [PASS] initials: bio ['H', 'C'] ~ stint ['H', 'C']
- [PASS] age_gate: stint starts 1950, birth 1921 (age 29)
- [PASS] colony: 2 placed event(s) resolve to 'North Borneo'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1950-1951
- [FAIL] position_sim: best 45 vs bar 60: 'asst. supt., police' ~ 'Assistant Superintendent'
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

