<!-- {"case_id": "case_stacey_herbert-edward_b1902", "bio_ids": ["stacey_herbert-edward_b1902"], "stint_ids": ["Stacey, H. E___Kenya___1927", "Stacey, H. E___Kenya___1939"]} -->
# Dossier case_stacey_herbert-edward_b1902

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `stacey_herbert-edward_b1902`

- Printed name: **STACEY, Herbert Edward**
- Birth year: 1902 (attested in editions [1948])
- Appears in editions: [1940, 1948]

### Verbatim printed entry text (OCR)

**Version `col1948-L36086.v` — printed in editions [1948]:**

> STACEY, Herbert Edward.—b. 1902; ed. Observatory Boys' Sch., Cape Town, barrister-at-law, (Grays Inn); clk., Ken., 1926; ch. clk., 1935; leg. astt., 1937; called to bar, 1939; ag. crown coun., 1939; crown coun., Ken., 1942; leg. advsr., K.U.R. and H., and E.A. Airways Corp., 1944; ag. ch. astt. to gen. man., rhys., 1945; leg. draughtsman, Ken., 1946.

**Version `col1940-L68622.v` — printed in editions [1940]:**

> STACEY, Herbert Edward, Barrister-at-Law (Gray's Inn).—B. 1902; cler. serv., secre., Kenya, 1926; legal dept., 1928; ch. elk., 1936; legal asst., 1938; called to bar, 1939; ag. crown couns., 1939.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | clk. | Kenya | [1940, 1948] |
| 1 | 1928 | legal dept | Kenya *(inherited from previous clause)* | [1940] |
| 2 | 1935 | ch. clk | Kenya *(inherited from previous clause)* | [1948] |
| 3 | 1936 | ch. elk | Kenya *(inherited from previous clause)* | [1940] |
| 4 | 1937 | leg. astt | Kenya *(inherited from previous clause)* | [1948] |
| 5 | 1938 | legal asst | Kenya *(inherited from previous clause)* | [1940] |
| 6 | 1939 | called to bar | Kenya *(inherited from previous clause)* | [1940, 1948] |
| 7 | 1942 | crown coun. | Kenya | [1948] |
| 8 | 1944 | leg. advsr., K.U.R. and H., and E.A. Airways Corp | Kenya *(inherited from previous clause)* | [1948] |
| 9 | 1945 | ag. ch. astt. to gen. man., rhys | Kenya *(inherited from previous clause)* | [1948] |
| 10 | 1946 | leg. draughtsman | Kenya | [1948] |

## Candidate stint `Stacey, H. E___Kenya___1927`

- Staff-list name: **Stacey, H. E** | colony: **Kenya** | listed 1927–1928 | editions [1927, 1928]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | H. E. Stacey | European Clerks | Secretariat | — | — |
| 1928 | H. E. Stacey | European Clerk | Secretariat | — | — |

### Deterministic checks: `stacey_herbert-edward_b1902` vs `Stacey, H. E___Kenya___1927`

- [PASS] surname_gate: bio 'STACEY' vs stint 'Stacey, H. E' (exact)
- [PASS] initials: bio ['H', 'E'] ~ stint ['H', 'E']
- [PASS] age_gate: stint starts 1927, birth 1902 (age 25)
- [PASS] colony: 11 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1927-1928
- [FAIL] position_sim: best 35 vs bar 60: 'clk.' ~ 'European Clerk'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Stacey, H. E___Kenya___1939`

- Staff-list name: **Stacey, H. E** | colony: **Kenya** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | H. E. Stacey | Legal Assistant | Attorney General's Department | — | — |
| 1940 | H. E. Stacey | Legal Assistant | Attorney General's Department | — | — |

### Deterministic checks: `stacey_herbert-edward_b1902` vs `Stacey, H. E___Kenya___1939`

- [PASS] surname_gate: bio 'STACEY' vs stint 'Stacey, H. E' (exact)
- [PASS] initials: bio ['H', 'E'] ~ stint ['H', 'E']
- [PASS] age_gate: stint starts 1939, birth 1902 (age 37)
- [PASS] colony: 11 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1939-1940
- [PASS] position_sim: best 80 vs bar 60: 'legal asst' ~ 'Legal Assistant'
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

