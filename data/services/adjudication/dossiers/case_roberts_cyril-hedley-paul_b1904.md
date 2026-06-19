<!-- {"case_id": "case_roberts_cyril-hedley-paul_b1904", "bio_ids": ["roberts_cyril-hedley-paul_b1904"], "stint_ids": ["Roberts, C. P___British Guiana___1925"]} -->
# Dossier case_roberts_cyril-hedley-paul_b1904

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 150 official(s) with this surname in the graph's staff lists; 67 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `roberts_cyril-hedley-paul_b1904`

- Printed name: **ROBERTS, Cyril Hedley Paul**
- Birth year: 1904 (attested in editions [1948, 1949])
- Appears in editions: [1948, 1949]

### Verbatim printed entry text (OCR)

**Version `col1948-L35533.v` — printed in editions [1948, 1949]:**

> ROBERTS, Cyril Hedley Paul.—b. 1904; ed. St. Michael's, St. Johns' Sch., Leatherhead and Longerenong Agric. Coll., Australia (agric. dip. (Aus.).)) trpr., Br. S.A. police, 1927; police const., N. Rhod., 1931; Pal., 1933; Berm., 1935; ch. inspr., Gam., 1939; asst. supt. 1942; Uga., 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1931 | police const. | Northern Rhodesia | [1948, 1949] |
| 1 | 1933 | police const. | Palestine | [1948, 1949] |
| 2 | 1935 | police const. | Bermuda | [1948, 1949] |
| 3 | 1939 | ch. inspr., Gam | Bermuda *(inherited from previous clause)* | [1948, 1949] |
| 4 | 1942 | asst. supt | Bermuda *(inherited from previous clause)* | [1948, 1949] |
| 5 | 1946 | asst. supt | Uganda | [1948, 1949] |

## Candidate stint `Roberts, C. P___British Guiana___1925`

- Staff-list name: **Roberts, C. P** | colony: **British Guiana** | listed 1925–1939 | editions [1925, 1927, 1928, 1929, 1930, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | C. P. Roberts | Yard Superintendent | Public Works | — | — |
| 1927 | C. P. Roberts | Yard Superintendent | Public Works | — | — |
| 1928 | C. P. Roberts | Yard Superintendent | Public Works | — | — |
| 1929 | C. P. Roberts | Yard Superintendent | Public Works | — | — |
| 1930 | C. P. Roberts | Yard Superintendent | Public Works | — | — |
| 1939 | C. P. Roberts | Yard Superintendent | Public Works | — | — |

### Deterministic checks: `roberts_cyril-hedley-paul_b1904` vs `Roberts, C. P___British Guiana___1925`

- [PASS] surname_gate: bio 'ROBERTS' vs stint 'Roberts, C. P' (exact)
- [PASS] initials: bio ['C', 'H', 'P'] ~ stint ['C', 'P']
- [PASS] age_gate: stint starts 1925, birth 1904 (age 21)
- [FAIL] colony: no placed event resolves to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1925-1939
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

