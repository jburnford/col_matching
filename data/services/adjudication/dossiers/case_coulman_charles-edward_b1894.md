<!-- {"case_id": "case_coulman_charles-edward_b1894", "bio_ids": ["coulman_charles-edward_b1894"], "stint_ids": ["Coulman, C. E___Palestine___1927"]} -->
# Dossier case_coulman_charles-edward_b1894

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `coulman_charles-edward_b1894`

- Printed name: **COULMAN, Charles Edward**
- Birth year: 1894 (attested in editions [1948])
- Appears in editions: [1948]

### Verbatim printed entry text (OCR)

**Version `col1948-L31936.v` — printed in editions [1948]:**

> COULMAN, Charles Edward.—b. 1894; ed. Portland Coll., Chiswick, Latymer Found. Sch., Hogarth Sch., London Sch. of Econ.; off. supt. rlwys., Pal., 1926; asst. dist. traf. supt., 1932; commercial asst., 1938; asst. supt., 1942.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | off. supt. rlwys. | Palestine | [1948] |
| 1 | 1932 | asst. dist. traf. supt | Palestine *(inherited from previous clause)* | [1948] |
| 2 | 1938 | commercial asst | Palestine *(inherited from previous clause)* | [1948] |
| 3 | 1942 | asst. supt | Palestine *(inherited from previous clause)* | [1948] |

## Candidate stint `Coulman, C. E___Palestine___1927`

- Staff-list name: **Coulman, C. E** | colony: **Palestine** | listed 1927–1940 | editions [1927, 1928, 1929, 1930, 1931, 1932, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | C. E. Coulman | Office Superintendent | Palestine Railways | — | — |
| 1928 | C. E. Coulman | Chief Clerk | Palestine Railways | — | — |
| 1929 | C. E. Coulman | Chief Clerk | Palestine Railways | — | — |
| 1930 | C. E. Coulman | Chief Clerk | Palestine Railways | — | — |
| 1931 | C. E. Coulman | Chief Clerk | Palestine Railways | — | — |
| 1932 | C. E. Coulman | Chief Clerk | Palestine Railways | — | — |
| 1940 | C. E. Coulman | Commercial Assistant | Palestine Railways | — | — |

### Deterministic checks: `coulman_charles-edward_b1894` vs `Coulman, C. E___Palestine___1927`

- [PASS] surname_gate: bio 'COULMAN' vs stint 'Coulman, C. E' (exact)
- [PASS] initials: bio ['C', 'E'] ~ stint ['C', 'E']
- [PASS] age_gate: stint starts 1927, birth 1894 (age 33)
- [PASS] colony: 4 placed event(s) resolve to 'Palestine'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1927-1940
- [PASS] position_sim: best 86 vs bar 60: 'commercial asst' ~ 'Commercial Assistant'
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

