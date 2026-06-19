<!-- {"case_id": "case_schultz_eugene-frederick_b1904", "bio_ids": ["schultz_eugene-frederick_b1904"], "stint_ids": ["Schultz, E. F___Northern Rhodesia___1929", "Schultz, E. F___Northern Rhodesia___1949"]} -->
# Dossier case_schultz_eugene-frederick_b1904

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `schultz_eugene-frederick_b1904`

- Printed name: **SCHULTZ, Eugene Frederick**
- Birth year: 1904 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L35755.v` — printed in editions [1948, 1949, 1950, 1951]:**

> SCHULTZ, Eugene Frederick.—b. 1904; ed. St. George's Coll. and Chaplin High Sch., S. Rhodesia; on mil. serv., 1939-41; lieut.; police const., N. Rhod., 1928; sergt., 1928; clk., 1928; asst. acctnt., 1942; labour offr., 1945.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | police const. | Northern Rhodesia | [1948, 1949, 1950, 1951] |
| 1 | 1942 | asst. acctnt | Northern Rhodesia *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 2 | 1945 | labour offr | Northern Rhodesia *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Schultz, E. F___Northern Rhodesia___1929`

- Staff-list name: **Schultz, E. F** | colony: **Northern Rhodesia** | listed 1929–1934 | editions [1929, 1930, 1931, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | E. F. Schultz | Sgts. | Northern Rhodesia Police - Headquarters Staff | — | — |
| 1930 | E. F. Schultz | Clerk | Survey | — | — |
| 1931 | E. F. Schultz | Clerk | Survey | — | — |
| 1934 | E. F. Schultz | Clerk (1) | Survey | — | — |

### Deterministic checks: `schultz_eugene-frederick_b1904` vs `Schultz, E. F___Northern Rhodesia___1929`

- [PASS] surname_gate: bio 'SCHULTZ' vs stint 'Schultz, E. F' (exact)
- [PASS] initials: bio ['E', 'F'] ~ stint ['E', 'F']
- [PASS] age_gate: stint starts 1929, birth 1904 (age 25)
- [PASS] colony: 3 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1929-1934
- [FAIL] position_sim: best 35 vs bar 60: 'police const.' ~ 'Clerk'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Schultz, E. F___Northern Rhodesia___1949`

- Staff-list name: **Schultz, E. F** | colony: **Northern Rhodesia** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | E. F. Schultz | — | Mines and Labour | — | — |
| 1951 | E. F. Schultz | — | Labour and Mines | — | — |

### Deterministic checks: `schultz_eugene-frederick_b1904` vs `Schultz, E. F___Northern Rhodesia___1949`

- [PASS] surname_gate: bio 'SCHULTZ' vs stint 'Schultz, E. F' (exact)
- [PASS] initials: bio ['E', 'F'] ~ stint ['E', 'F']
- [PASS] age_gate: stint starts 1949, birth 1904 (age 45)
- [PASS] colony: 3 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: no overlapping placed event to compare
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

