<!-- {"case_id": "case_maile_albert-william_b1901", "bio_ids": ["maile_albert-william_b1901"], "stint_ids": ["Maile, A. W___British Guiana___1929", "Maile, A. W___British Guiana___1949"]} -->
# Dossier case_maile_albert-william_b1901

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `maile_albert-william_b1901`

- Printed name: **MAILE, Albert William**
- Birth year: 1901 (attested in editions [1949, 1950])
- Honours: A.I.E.E
- Appears in editions: [1948, 1949, 1950]

### Verbatim printed entry text (OCR)

**Version `col1949-L34108.v` — printed in editions [1949, 1950]:**

> MAILE, Albert William, Mem. Amer. I.E.E., A.I.E.E.—b. 1901; ed. Hendon County; on war serv., 1917-19, R.A.F., 1939-41, S.L. Bn. (sub.); apptd. Lond. telephone serv., 1919; teleph. inspr., B. Guiana, 1928; teleph. inspr., G.C., 1937; tel. engnr., S.L., 1939; gov. elec. inspr., B. Guiana, 1943; engnr. in ch., P.O. telecoms., 1943; visited Leeward Is. to make recommendations upon Antigua and St. Kitts telephone systems, 1946.

**Version `col1948-L34453.v` — printed in editions [1948]:**

> MAILE, Albert William, A.I.E.E., A.Amer.I.R.E.—b. 1901; on war serv., wireless obsvr., 1917; 2nd tel. inspr., 1928; inspr., 1934; telegraph inspr., G.C., 1937; telegraph engnr., S.L., 1939; engrnr.-in-ch., Br. Guiana, 1943.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1919 | apptd. Lond. telephone serv | — | [1949, 1950] |
| 1 | 1928 | teleph. inspr., B. Guiana | — | [1949, 1950] |
| 2 | 1928 | 2nd tel. inspr | — | [1948] |
| 3 | 1934 | inspr | — | [1948] |
| 4 | 1937 | teleph. inspr. | Gold Coast | [1948, 1949, 1950] |
| 5 | 1939 | tel. engnr. | Sierra Leone | [1948, 1949, 1950] |
| 6 | 1943 | gov. elec. inspr., B. Guiana | Sierra Leone *(inherited from previous clause)* | [1949, 1950] |
| 7 | 1943 | engrnr.-in-ch. | British Guiana | [1948] |
| 8 | 1946 | visited Leeward Is. to make recommendations upon Antigua and St. Kitts telephone systems | Sierra Leone *(inherited from previous clause)* | [1949, 1950] |

## Candidate stint `Maile, A. W___British Guiana___1929`

- Staff-list name: **Maile, A. W** | colony: **British Guiana** | listed 1929–1930 | editions [1929, 1930]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | A. W. Maile | 2nd Telephone Inspector | Post Office, Engineering Branch | — | — |
| 1930 | A. W. Maile | 2nd Telephone Inspector | Engineering Branch | — | — |

### Deterministic checks: `maile_albert-william_b1901` vs `Maile, A. W___British Guiana___1929`

- [PASS] surname_gate: bio 'MAILE' vs stint 'Maile, A. W' (exact)
- [PASS] initials: bio ['A', 'W'] ~ stint ['A', 'W']
- [PASS] age_gate: stint starts 1929, birth 1901 (age 28)
- [PASS] colony: 1 placed event(s) resolve to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1929-1930
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Maile, A. W___British Guiana___1949`

- Staff-list name: **Maile, A. W** | colony: **British Guiana** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | A. W. Maile | Engineer-in-Chief | Post Office Telecommunications | — | — |
| 1950 | A. W. Maile | Engineer-in-Chief | Post Office Telecommunications | — | — |

### Deterministic checks: `maile_albert-william_b1901` vs `Maile, A. W___British Guiana___1949`

- [PASS] surname_gate: bio 'MAILE' vs stint 'Maile, A. W' (exact)
- [PASS] initials: bio ['A', 'W'] ~ stint ['A', 'W']
- [PASS] age_gate: stint starts 1949, birth 1901 (age 48)
- [PASS] colony: 1 placed event(s) resolve to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1950
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

