<!-- {"case_id": "case_bridgen_charles-william_b1897", "bio_ids": ["bridgen_charles-william_b1897"], "stint_ids": ["Bridgen, C. W___Palestine___1927"]} -->
# Dossier case_bridgen_charles-william_b1897

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bridgen_charles-william_b1897`

- Printed name: **BRIDGEN, Charles William**
- Birth year: 1897 (attested in editions [1948])
- Appears in editions: [1948]

### Verbatim printed entry text (OCR)

**Version `col1948-L31364.v` — printed in editions [1948]:**

> BRIDGEN, Charles William, M.C.—b. 1897; ed. Burdett Coutts and Townsend and Westminster City Sch.; on mil. serv. 1916–20, capt.; asst. sec., rlwys., Pal., 1926; stores supt., 1940.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | asst. sec., rlwys. | Palestine | [1948] |
| 1 | 1940 | stores supt | Palestine *(inherited from previous clause)* | [1948] |

## Candidate stint `Bridgen, C. W___Palestine___1927`

- Staff-list name: **Bridgen, C. W** | colony: **Palestine** | listed 1927–1940 | editions [1927, 1928, 1929, 1930, 1931, 1932, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | C. W. Bridgen | Assistant Secretary | Palestine Railways | — | — |
| 1928 | C. W. Bridgen | Assistant Secretary | Palestine Railways | — | — |
| 1929 | C. W. Bridgen | Assistant Secretary | Palestine Railways | — | — |
| 1930 | C. W. Bridgen | Assistant Secretary | Palestine Railways | — | — |
| 1931 | C. W. Bridgen | Assistant Secretary | Palestine Railways | — | — |
| 1932 | C. W. Bridgen | Assistant Secretary | Palestine Railways | — | — |
| 1940 | C. W. Bridgen | Assistant Secretary | Palestine Railways | — | — |

### Deterministic checks: `bridgen_charles-william_b1897` vs `Bridgen, C. W___Palestine___1927`

- [PASS] surname_gate: bio 'BRIDGEN' vs stint 'Bridgen, C. W' (exact)
- [PASS] initials: bio ['C', 'W'] ~ stint ['C', 'W']
- [PASS] age_gate: stint starts 1927, birth 1897 (age 30)
- [PASS] colony: 2 placed event(s) resolve to 'Palestine'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1927-1940
- [FAIL] position_sim: best 48 vs bar 60: 'asst. sec., rlwys.' ~ 'Assistant Secretary'
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

