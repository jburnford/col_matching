<!-- {"case_id": "case_keast_sydney-banks_b1884", "bio_ids": ["keast_sydney-banks_b1884"], "stint_ids": ["Keast, S. Banks___Gold Coast___1932"]} -->
# Dossier case_keast_sydney-banks_b1884

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `keast_sydney-banks_b1884`

- Printed name: **KEAST, SYDNEY BANKS**
- Birth year: 1884 (attested in editions [1933, 1934, 1935, 1936, 1937])
- Honours: O.B.E (1937)
- Appears in editions: [1933, 1934, 1935, 1936, 1937]

### Verbatim printed entry text (OCR)

**Version `col1933-L61190.v` — printed in editions [1933, 1934, 1935, 1936, 1937]:**

> KEAST, MAJOR SYDNEY BANKS, O.B.E. (1937), R.E. (R. of O.), M.C. and Bar, French Croix de Guerre.—B. 1884; ed. City of London Sch.; Sudan P.W.D., 1906-13; aspt. suptg. sanry. engr., P.W.D., Gold Coast, 1913; Cameroons E.F., 1915-16; B.E.F., 1916-19; senr. pub. health engr., 1924; asst., D.P.W., 1926; dep. D.P.W., 1928; D.P.W., 1932; lt.-col. commdg. Gold Coast Defence Force, 1931.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1906–1913 | Sudan P.W.D | — | [1933, 1934, 1935, 1936, 1937] |
| 1 | 1913 | aspt. suptg. sanry. engr., P.W.D. | Gold Coast | [1933, 1934, 1935, 1936, 1937] |
| 2 | 1915–1916 | Cameroons E.F | Cameroons | [1933, 1934, 1935, 1936, 1937] |
| 3 | 1916–1919 | B.E.F | Cameroons *(inherited from previous clause)* | [1933, 1934, 1935, 1936, 1937] |
| 4 | 1924 | senr. pub. health engr | Cameroons *(inherited from previous clause)* | [1933, 1934, 1935, 1936, 1937] |
| 5 | 1926 | asst., D.P.W | Cameroons *(inherited from previous clause)* | [1933, 1934, 1935, 1936, 1937] |
| 6 | 1928 | dep. D.P.W | Cameroons *(inherited from previous clause)* | [1933, 1934, 1935, 1936, 1937] |
| 7 | 1931 | lt.-col. commdg. Gold Coast Defence Force | Cameroons *(inherited from previous clause)* | [1933, 1934, 1935, 1936, 1937] |
| 8 | 1932 | D.P.W | Cameroons *(inherited from previous clause)* | [1933, 1934, 1935, 1936, 1937] |

## Candidate stint `Keast, S. Banks___Gold Coast___1932`

- Staff-list name: **Keast, S. Banks** | colony: **Gold Coast** | listed 1932–1936 | editions [1932, 1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1932 | S. Banks Keast | Deputy Director of Public Works | Public Works Department | — | Major |
| 1934 | S. B. Keast | Officer Commanding | The Gold Coast Defence Force | — | Lt.-Colonel |
| 1936 | S. Banks Keast | Director of Public Works | Public Works Department | — | Major |

### Deterministic checks: `keast_sydney-banks_b1884` vs `Keast, S. Banks___Gold Coast___1932`

- [PASS] surname_gate: bio 'KEAST' vs stint 'Keast, S. Banks' (exact)
- [PASS] initials: bio ['S', 'B'] ~ stint ['S', 'B']
- [PASS] age_gate: stint starts 1932, birth 1884 (age 48)
- [PASS] colony: 1 placed event(s) resolve to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1932-1936
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

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

