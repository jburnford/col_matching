<!-- {"case_id": "case_searle_lancelot-alban_b1915", "bio_ids": ["searle_lancelot-alban_b1915", "searle_lancelot-alhan_b1915"], "stint_ids": ["Searle, L. A___Hong Kong___1937"]} -->
# Dossier case_searle_lancelot-alban_b1915

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Searle, L. A___Hong Kong___1937'] have more than one claimant biography in this case.
- Phase 1 found `searle_lancelot-alban_b1915` ↔ `Searle, L. A___Hong Kong___1937` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- Phase 1 found `searle_lancelot-alhan_b1915` ↔ `Searle, L. A___Hong Kong___1937` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).

## Biography `searle_lancelot-alban_b1915`

- Printed name: **SEARLE, Lancelot Alban**
- Birth year: 1915 (attested in editions [1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1950-L39386.v` — printed in editions [1950, 1951]:**

> SEARLE, Lancelot Alban.—b. 1915; ed. Imp. Serv. Coll. and Jesus Coll., Camb., M.A. (Cantab.), 3rd cl. law trip, hon.; police probr., H.K., 1936; asst. supt., 1938; supt. (later asst. supt.), 1946.

**Version `col1948-L35778.v` — printed in editions [1948, 1949]:**

> SEARLE, Lancelot Alban.—b. 1915; ed. Imp. Serv. Coll. and Jesus Coll., Cambridge, M.A. (Cantab.) 3rd cl. law trip., hon.; ag. supt. of police, H.K., 1936; supt., 1945.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1936 | police probr. | Hong Kong | [1948, 1949, 1950, 1951] |
| 1 | 1938 | asst. supt | Hong Kong *(inherited from previous clause)* | [1950, 1951] |
| 2 | 1945 | supt | Hong Kong *(inherited from previous clause)* | [1948, 1949] |
| 3 | 1946 | supt. (later asst. supt.) | Hong Kong *(inherited from previous clause)* | [1950, 1951] |

## Biography `searle_lancelot-alhan_b1915`

- Printed name: **SEARLE, Lancelot Alhan**
- Birth year: 1915 (attested in editions [1940])
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L68297.v` — printed in editions [1940]:**

> SEARLE, Lancelot Alhan.—B. 1915; pol. probnr., Hong Kong, 1936; ast. supt., 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1936 | pol. probnr. | Hong Kong | [1940] |
| 1 | 1938 | ast. supt | Hong Kong *(inherited from previous clause)* | [1940] |

## Candidate stint `Searle, L. A___Hong Kong___1937`

- Staff-list name: **Searle, L. A** | colony: **Hong Kong** | listed 1937–1940 | editions [1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1937 | L. A. Searle | Police Probationer | Police Department | — | — |
| 1939 | L. A. Searle | Police Probationer | Police Department | — | — |
| 1940 | L. A. Searle | Assistant Superintendents | Police Department | — | — |

### Deterministic checks: `searle_lancelot-alban_b1915` vs `Searle, L. A___Hong Kong___1937`

- [PASS] surname_gate: bio 'SEARLE' vs stint 'Searle, L. A' (exact)
- [PASS] initials: bio ['L', 'A'] ~ stint ['L', 'A']
- [PASS] age_gate: stint starts 1937, birth 1915 (age 22)
- [PASS] colony: 4 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1937-1940
- [PASS] position_sim: best 80 vs bar 60: 'police probr.' ~ 'Police Probationer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `searle_lancelot-alhan_b1915` vs `Searle, L. A___Hong Kong___1937`

- [PASS] surname_gate: bio 'SEARLE' vs stint 'Searle, L. A' (exact)
- [PASS] initials: bio ['L', 'A'] ~ stint ['L', 'A']
- [PASS] age_gate: stint starts 1937, birth 1915 (age 22)
- [PASS] colony: 2 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1937-1940
- [PASS] position_sim: best 71 vs bar 60: 'pol. probnr.' ~ 'Police Probationer'
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

