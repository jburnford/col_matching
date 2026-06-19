<!-- {"case_id": "case_nurock_max_b1893", "bio_ids": ["nurock_max_b1893"], "stint_ids": ["Nurock, M___Palestine___1924"]} -->
# Dossier case_nurock_max_b1893

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['nurock_max_b1893'] carry a single initial only — the namesake trap applies.

## Biography `nurock_max_b1893`

- Printed name: **NUROCK, MAX**
- Birth year: 1893 (attested in editions [1936, 1939, 1940])
- Honours: O.B.E (1932)
- Appears in editions: [1936, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1936-L63431.v` — printed in editions [1936, 1939, 1940]:**

> NUROCK, MAX, O.B.E. (1932), M.A. (Dublin)—B. 1893; mily. serv., 1915-19; asst. pvt. sec., Palestine, 1920; junr. asst. sec., 1922; asst. sec., 1926; sec. to standing comte., for commerce and industry, 1928; ag. asst. ch. sec. on various occasions and once as ch. sec.; clk., exec. coun. in addn., 1934; asst. ch. sec., Uganda, 1937; ag. dep. ch. sec., July-Dec., 1937 and Mar.-Nov., 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915–1919 | mily. serv | — | [1936, 1939, 1940] |
| 1 | 1920 | asst. pvt. sec. | Palestine | [1936, 1939, 1940] |
| 2 | 1922 | junr. asst. sec | Palestine *(inherited from previous clause)* | [1936, 1939, 1940] |
| 3 | 1926 | asst. sec | Palestine *(inherited from previous clause)* | [1936, 1939, 1940] |
| 4 | 1928 | sec. to standing comte., for commerce and industry | Palestine *(inherited from previous clause)* | [1936, 1939, 1940] |
| 5 | 1934 | clk., exec. coun. in addn | Palestine *(inherited from previous clause)* | [1936, 1939, 1940] |
| 6 | 1937 | asst. ch. sec. | Uganda | [1936, 1939, 1940] |
| 7 | 1938 | Mar.- | Uganda *(inherited from previous clause)* | [1936, 1939, 1940] |

## Candidate stint `Nurock, M___Palestine___1924`

- Staff-list name: **Nurock, M** | colony: **Palestine** | listed 1924–1931 | editions [1924, 1925, 1927, 1928, 1930, 1931]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1924 | M. Nurock | Junior Assistant Secretary | Secretariat | — | — |
| 1925 | M. Nurock | Junior Assistant Secretary | Secretariat | — | — |
| 1927 | M. Nurock | Assistant Secretaries | Secretariat | — | — |
| 1928 | M. Nurock | Assistant Secretary | Secretariat | — | — |
| 1930 | M. Nurock | Assistant Secretary | Secretariat | — | — |
| 1931 | M. Nurock | Assistant Secretary | Secretariat | — | — |

### Deterministic checks: `nurock_max_b1893` vs `Nurock, M___Palestine___1924`

- [PASS] surname_gate: bio 'NUROCK' vs stint 'Nurock, M' (exact)
- [PASS] initials: bio ['M'] ~ stint ['M']
- [PASS] age_gate: stint starts 1924, birth 1893 (age 31)
- [PASS] colony: 5 placed event(s) resolve to 'Palestine'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1924-1931
- [PASS] position_sim: best 67 vs bar 60: 'junr. asst. sec' ~ 'Junior Assistant Secretary'
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

