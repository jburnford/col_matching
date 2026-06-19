<!-- {"case_id": "case_harragin_alfred-ernest-albert_b1877", "bio_ids": ["harragin_alfred-ernest-albert_b1877"], "stint_ids": ["Harragin, A. E. A___Trinidad and Tobago___1925"]} -->
# Dossier case_harragin_alfred-ernest-albert_b1877

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 18 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `harragin_alfred-ernest-albert_b1877`

- Printed name: **HARRAGIN, ALFRED ERNEST ALBERT**
- Birth year: 1877 (attested in editions [1935, 1936, 1937, 1940])
- Honours: D.S.O
- Appears in editions: [1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1935, 1936, 1937, 1940]

### Verbatim printed entry text (OCR)

**Version `dol1935-L59251.v` — printed in editions [1935, 1936, 1937, 1940]:**

> HARRAGIN, MAJOR ALFRED ERNEST ALBERT, D.S.O., V.D.—B. 1877; sub.-inspr., constab., Trinidad, Feb., 1905; asst. supt., fire brigade, Port-of-Spain, Sept., 1910; sub. inspr., Tobago, divn., May, 1911; inspr., constab., 1912; senr. inspr., constab., Apr., 1934; dep. major-gen., 1936.

**Version `col1917-L50222.v` — printed in editions [1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925]:**

> HARRAGIN, Alfred Ernest Albert.—B. 1877; sub-instr., constab., Trinidad, 1st Feb., 1905; instr., 1st Nov., 1912; now serving with the army as temp. captain.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1905 | sub.-inspr., constab. | Trinidad | [1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1935, 1936, 1937, 1940] |
| 1 | 1910 | asst. supt., fire brigade, Port-of-Spain | Trinidad *(inherited from previous clause)* | [1935, 1936, 1937, 1940] |
| 2 | 1911 | sub. inspr., Tobago, divn | Trinidad *(inherited from previous clause)* | [1935, 1936, 1937, 1940] |
| 3 | 1912 | inspr., constab | Trinidad *(inherited from previous clause)* | [1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1935, 1936, 1937, 1940] |
| 4 | 1934 | senr. inspr., constab | Trinidad *(inherited from previous clause)* | [1935, 1936, 1937, 1940] |
| 5 | 1936 | dep. major-gen | Trinidad *(inherited from previous clause)* | [1935, 1936, 1937, 1940] |

## Candidate stint `Harragin, A. E. A___Trinidad and Tobago___1925`

- Staff-list name: **Harragin, A. E. A** | colony: **Trinidad and Tobago** | listed 1925–1937 | editions [1925, 1927, 1928, 1929, 1931, 1933, 1934, 1937]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | A. E. A. Harragin | Inspector | Constabulary and Gaols | D.S.O. | — |
| 1927 | A. E. A. Harragin | Inspector | Constabulary and Gaols | D.S.O. | — |
| 1928 | A. E. A. Harragin | Inspectors | Constabulary and Gaols | D.S.O. | — |
| 1929 | A. E. A. Harragin | Inspectors | Constabulary and Gaols | D.S.O. | — |
| 1931 | A. E. A. Harragin | Inspector | Constabulary and Gaols | D.S.O. | — |
| 1933 | A. E. A. Harragin | Inspector | Constabulary and Gaols | D.S.O. | Major |
| 1934 | A. E. A. Harragin | Inspector | Constabulary and Gaols | D.S.O. | Major |
| 1937 | Major A. E. A. Harragin | Deputy Inspector-General | Constabulary | D.S.O. | Major |

### Deterministic checks: `harragin_alfred-ernest-albert_b1877` vs `Harragin, A. E. A___Trinidad and Tobago___1925`

- [PASS] surname_gate: bio 'HARRAGIN' vs stint 'Harragin, A. E. A' (exact)
- [PASS] initials: bio ['A', 'E', 'A'] ~ stint ['A', 'E', 'A']
- [PASS] age_gate: stint starts 1925, birth 1877 (age 48)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1925-1937
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: D.S.O
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

