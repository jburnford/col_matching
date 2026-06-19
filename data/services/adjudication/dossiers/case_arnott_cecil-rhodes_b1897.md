<!-- {"case_id": "case_arnott_cecil-rhodes_b1897", "bio_ids": ["arnott_cecil-rhodes_b1897"], "stint_ids": ["Arnott, C. R___Northern Rhodesia___1925"]} -->
# Dossier case_arnott_cecil-rhodes_b1897

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `arnott_cecil-rhodes_b1897`

- Printed name: **ARNOTT, Cecil Rhodes**
- Birth year: 1897 (attested in editions [1948])
- Appears in editions: [1948]

### Verbatim printed entry text (OCR)

**Version `col1948-L30855.v` — printed in editions [1948]:**

> ARNOTT, Cecil Rhodes, M.C.—b. 1897; ed. Sec. Sch., Edward VI's Gram. Sch., Stafford; on mil. serv., 1914-20, lieut.; apptd. to B.S.A.P., S. Rhod., 1920; N. Rhod. police, 1922; det. sgt., 1924; det. inspr., 1928; asst. supt., 1931; supt., 1933; asst. comsnr. for migration, Pal., 1934; dir. of dept. of migration, 1947; seconded as asst. contrlr. of supplies, 1940, and asst. food contrlr., 1942; dep. food contrlr., 1944; resumed duty in dept. of migration, 1945.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920 | apptd. to B.S.A.P. | Southern Rhodesia | [1948] |
| 1 | 1922 | N. Rhod. police | Northern Rhodesia | [1948] |
| 2 | 1924 | det. sgt | Northern Rhodesia *(inherited from previous clause)* | [1948] |
| 3 | 1928 | det. inspr | Northern Rhodesia *(inherited from previous clause)* | [1948] |
| 4 | 1931 | asst. supt | Northern Rhodesia *(inherited from previous clause)* | [1948] |
| 5 | 1933 | supt | Northern Rhodesia *(inherited from previous clause)* | [1948] |
| 6 | 1934 | asst. comsnr. for migration | Palestine | [1948] |
| 7 | 1940 | seconded as asst. contrlr. of supplies | Palestine *(inherited from previous clause)* | [1948] |
| 8 | 1942 | asst. food contrlr | Palestine *(inherited from previous clause)* | [1948] |
| 9 | 1944 | dep. food contrlr | Palestine *(inherited from previous clause)* | [1948] |
| 10 | 1945 | resumed duty in dept. of migration | Palestine *(inherited from previous clause)* | [1948] |
| 11 | 1947 | dir. of dept. of migration | Palestine *(inherited from previous clause)* | [1948] |

## Candidate stint `Arnott, C. R___Northern Rhodesia___1925`

- Staff-list name: **Arnott, C. R** | colony: **Northern Rhodesia** | listed 1925–1934 | editions [1925, 1927, 1928, 1929, 1930, 1931, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | C. R. Arnott | Det.-Sergents | Criminal Investigation Department | — | — |
| 1927 | C. R. Arnott | Det.-Sergtants | Criminal Investigation Department | — | — |
| 1928 | C. R. Arnott | Det.-Sergeant (2nd class) | Criminal Investigation Department | — | — |
| 1929 | C. R. Arnott | Assistant Det.-Inspectors | Criminal Investigation Department | — | — |
| 1930 | C. R. Arnott | Assistant Det.-Inspectors | Criminal Investigation Department | — | — |
| 1931 | C. R. Arnott | Detective-Inspector | Criminal Investigation Department | — | — |
| 1934 | C. R. Arnott | Superintendent | Northern Rhodesia Police | M.C. | — |

### Deterministic checks: `arnott_cecil-rhodes_b1897` vs `Arnott, C. R___Northern Rhodesia___1925`

- [PASS] surname_gate: bio 'ARNOTT' vs stint 'Arnott, C. R' (exact)
- [PASS] initials: bio ['C', 'R'] ~ stint ['C', 'R']
- [PASS] age_gate: stint starts 1925, birth 1897 (age 28)
- [PASS] colony: 5 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 5 event tenure(s) overlap stint years 1925-1934
- [PASS] position_sim: best 67 vs bar 60: 'det. sgt' ~ 'Det.-Sergents'
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

