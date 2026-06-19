<!-- {"case_id": "case_totman_walter_b1903", "bio_ids": ["totman_walter_b1903"], "stint_ids": ["Totman, W___Northern Rhodesia___1930", "Totman, W___Northern Rhodesia___1939"]} -->
# Dossier case_totman_walter_b1903

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['totman_walter_b1903'] carry a single initial only — the namesake trap applies.

## Biography `totman_walter_b1903`

- Printed name: **TOTMAN, Walter**
- Birth year: 1903 (attested in editions [1948])
- Honours: M.B.E
- Appears in editions: [1948]

### Verbatim printed entry text (OCR)

**Version `col1948-L36460.v` — printed in editions [1948]:**

> TOTMAN, Walter, M.B.E.—b. 1903; ed. Brentwood Gram. Sch.; on mil serv. 1940-46, lt.-col.; police, N. Rhod., 1927; asst. supt., 1937; supt., 1940.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | police | Northern Rhodesia | [1948] |
| 1 | 1937 | asst. supt | Northern Rhodesia *(inherited from previous clause)* | [1948] |
| 2 | 1940 | supt | Northern Rhodesia *(inherited from previous clause)* | [1948] |

## Candidate stint `Totman, W___Northern Rhodesia___1930`

- Staff-list name: **Totman, W** | colony: **Northern Rhodesia** | listed 1930–1931 | editions [1930, 1931]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1930 | W. Totman | Assistant Inspector | Civil Police Branch | — | — |
| 1931 | W. Totman | Assistant Det.-Inspectors | Criminal Investigation Department | — | — |

### Deterministic checks: `totman_walter_b1903` vs `Totman, W___Northern Rhodesia___1930`

- [PASS] surname_gate: bio 'TOTMAN' vs stint 'Totman, W' (exact)
- [PASS] initials: bio ['W'] ~ stint ['W']
- [PASS] age_gate: stint starts 1930, birth 1903 (age 27)
- [PASS] colony: 3 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1930-1931
- [FAIL] position_sim: best 16 vs bar 60: 'police' ~ 'Assistant Inspector'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Totman, W___Northern Rhodesia___1939`

- Staff-list name: **Totman, W** | colony: **Northern Rhodesia** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | W. Totman | Assistant Superintendent | Northern Rhodesia Police | — | — |
| 1940 | W. Totman | Assistant Superintendent | Northern Rhodesia Police | — | — |

### Deterministic checks: `totman_walter_b1903` vs `Totman, W___Northern Rhodesia___1939`

- [PASS] surname_gate: bio 'TOTMAN' vs stint 'Totman, W' (exact)
- [PASS] initials: bio ['W'] ~ stint ['W']
- [PASS] age_gate: stint starts 1939, birth 1903 (age 36)
- [PASS] colony: 3 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1939-1940
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

