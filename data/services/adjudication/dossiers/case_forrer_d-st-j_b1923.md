<!-- {"case_id": "case_forrer_d-st-j_b1923", "bio_ids": ["forrer_d-st-j_b1923"], "stint_ids": ["Forrer, D. St. J___Sarawak___1950"]} -->
# Dossier case_forrer_d-st-j_b1923

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `forrer_d-st-j_b1923`

- Printed name: **FORRER, D. ST. J**
- Birth year: 1923 (attested in editions [1960, 1961, 1962, 1963, 1964])
- Honours: C.P.M (1962)
- Appears in editions: [1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1960-L22996.v` — printed in editions [1960, 1961, 1962, 1963, 1964]:**

> FORRER, D. ST. J., C.P.M. (1962).—b. 1923; ed. St. Paul's Sch., Lond.; mil. serv., 1942-48, capt.; asst. supt., Sarawak constab., 1949; secon., offr. i/c, police dist., Brun., 1951-52; dep. supt., 1956; supt., 1957; secon., supt., spec. branch, Brun., 1958; asst. comsnr., 1961-63.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1949 | asst. supt., Sarawak constab | Sarawak | [1960, 1961, 1962, 1963, 1964] |
| 1 | 1951–1952 | secon., offr. i/c, police dist. | Brunei | [1960, 1961, 1962, 1963, 1964] |
| 2 | 1956 | dep. supt | Brunei *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964] |
| 3 | 1957 | supt | Brunei *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964] |
| 4 | 1958 | secon., supt., spec. branch | Brunei | [1960, 1961, 1962, 1963, 1964] |
| 5 | 1961–1963 | asst. comsnr | Brunei *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Forrer, D. St. J___Sarawak___1950`

- Staff-list name: **Forrer, D. St. J** | colony: **Sarawak** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | D. St. J. Forrer | Assistant Commissioner | CONSTABULARY | — | — |
| 1951 | D. St. J. Forrer | Assistant Commissioner | CONSTABULARY | — | — |

### Deterministic checks: `forrer_d-st-j_b1923` vs `Forrer, D. St. J___Sarawak___1950`

- [PASS] surname_gate: bio 'FORRER' vs stint 'Forrer, D. St. J' (exact)
- [PASS] initials: bio ['D', 'S', 'J'] ~ stint ['D', 'S', 'J']
- [PASS] age_gate: stint starts 1950, birth 1923 (age 27)
- [PASS] colony: 1 placed event(s) resolve to 'Sarawak'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1950-1951
- [FAIL] position_sim: best 43 vs bar 60: 'asst. supt., Sarawak constab' ~ 'Assistant Commissioner'
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

