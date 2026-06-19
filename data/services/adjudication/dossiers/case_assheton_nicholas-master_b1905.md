<!-- {"case_id": "case_assheton_nicholas-master_b1905", "bio_ids": ["assheton_nicholas-master_b1905"], "stint_ids": ["Asheton, N. M___Gambia___1933", "Asheton, N. M___Gambia___1949"]} -->
# Dossier case_assheton_nicholas-master_b1905

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `assheton_nicholas-master_b1905`

- Printed name: **ASSHETON, Nicholas Master**
- Birth year: 1905 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L30876.v` — printed in editions [1948, 1949, 1950, 1951]:**

> ASSHETON, Nicholas Master.—b. 1905; ed. Sherborne, Jesus Coll., Cambridge, B.A. (Cantab.); supt. of educ., Nig., 1938; asst. comsnr., Gam., 1932; comsnr., 1935; dist. comsnr., G.C. (on secondment), 1944; reverted to Gam., 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1932 | asst. comsnr., Gam | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 1 | 1935 | comsnr | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 2 | 1938 | supt. of educ. | Nigeria | [1948, 1949, 1950, 1951] |
| 3 | 1944 | dist. comsnr., G.C. (on secondment) | Gold Coast | [1948, 1949, 1950, 1951] |
| 4 | 1947 | reverted to Gam | Gold Coast *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Asheton, N. M___Gambia___1933`

- Staff-list name: **Asheton, N. M** | colony: **Gambia** | listed 1933–1940 | editions [1933, 1934, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | N. M. Asheton | Commissioner | Provincial Administration | — | — |
| 1934 | N. M. Asheton | Commissioner | Provincial Administration | — | — |
| 1937 | N. M. Asheton | Assistant Commissioner | Provincial Administration | — | — |
| 1939 | N. M. Asheton | Commissioners and Assistant Commissioners | Provincial Administration | — | — |
| 1940 | N. M. Asheton | Commissioner/Assistant Commissioner | Provincial Administration | — | — |

### Deterministic checks: `assheton_nicholas-master_b1905` vs `Asheton, N. M___Gambia___1933`

- [PASS] surname_gate: bio 'ASSHETON' vs stint 'Asheton, N. M' (fuzzy:1)
- [PASS] initials: bio ['N', 'M'] ~ stint ['N', 'M']
- [PASS] age_gate: stint starts 1933, birth 1905 (age 28)
- [FAIL] colony: no placed event resolves to 'Gambia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1933-1940
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Asheton, N. M___Gambia___1949`

- Staff-list name: **Asheton, N. M** | colony: **Gambia** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | N. M. Asheton | Commissioner | ADMINISTRATIVE SERVICE (including Secretariat) | — | — |
| 1950 | N. M. Asheton | Commissioner | Administrative Service | — | — |

### Deterministic checks: `assheton_nicholas-master_b1905` vs `Asheton, N. M___Gambia___1949`

- [PASS] surname_gate: bio 'ASSHETON' vs stint 'Asheton, N. M' (fuzzy:1)
- [PASS] initials: bio ['N', 'M'] ~ stint ['N', 'M']
- [PASS] age_gate: stint starts 1949, birth 1905 (age 44)
- [FAIL] colony: no placed event resolves to 'Gambia'
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

