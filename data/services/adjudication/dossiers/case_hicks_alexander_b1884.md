<!-- {"case_id": "case_hicks_alexander_b1884", "bio_ids": ["hicks_alexander_b1884"], "stint_ids": ["Hicks, A. Maxwell___Gold Coast___1928", "Hicks, T. A___Australia___1913"]} -->
# Dossier case_hicks_alexander_b1884

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['hicks_alexander_b1884'] carry a single initial only — the namesake trap applies.

## Biography `hicks_alexander_b1884`

- Printed name: **HICKS, ALEXANDER**
- Birth year: 1884 (attested in editions [1940])
- Honours: M.C
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L65148.v` — printed in editions [1940]:**

> HICKS, ALEXANDER, M.C., M.A.—B. 1884; asst. chf. inspr., schls., N.S.W., Dec., 1929; asst. under sec., dept. educn., Aug., 1930; asst. U.S. & asst. dir., educn., Feb., 1933; also supt. of tech. educn., Feb., 1936; mbr., pub. serv. bd., Sept., 1939.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | asst. chf. inspr., schls. | New South Wales | [1940] |
| 1 | 1930 | asst. under sec., dept. educn | New South Wales *(inherited from previous clause)* | [1940] |
| 2 | 1933 | asst. U.S. & asst. dir., educn | New South Wales *(inherited from previous clause)* | [1940] |
| 3 | 1936 | also supt. of tech. educn | New South Wales *(inherited from previous clause)* | [1940] |
| 4 | 1939 | mbr., pub. serv. bd | New South Wales *(inherited from previous clause)* | [1940] |

## Candidate stint `Hicks, A. Maxwell___Gold Coast___1928`

- Staff-list name: **Hicks, A. Maxwell** | colony: **Gold Coast** | listed 1928–1929 | editions [1928, 1929]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1928 | A. Maxwell Hicks | Secretary | Harbours Staff | — | — |
| 1929 | A. Maxwell Hicks | Secretary | Takoradi | — | — |

### Deterministic checks: `hicks_alexander_b1884` vs `Hicks, A. Maxwell___Gold Coast___1928`

- [PASS] surname_gate: bio 'HICKS' vs stint 'Hicks, A. Maxwell' (exact)
- [PASS] initials: bio ['A'] ~ stint ['A', 'M']
- [PASS] age_gate: stint starts 1928, birth 1884 (age 44)
- [FAIL] colony: no placed event resolves to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1928-1929
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Hicks, T. A___Australia___1913`

- Staff-list name: **Hicks, T. A** | colony: **Australia** | listed 1913–1918 | editions [1913, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1913 | T. A. Hicks | Deputy Hydraulic Engineer | Engineer-in-Chief's Department | — | — |
| 1918 | T. A. Hicks | Deputy Hydraulic Engineer | Engineering Department | — | — |

### Deterministic checks: `hicks_alexander_b1884` vs `Hicks, T. A___Australia___1913`

- [PASS] surname_gate: bio 'HICKS' vs stint 'Hicks, T. A' (exact)
- [PASS] initials: bio ['A'] ~ stint ['T', 'A']
- [PASS] age_gate: stint starts 1913, birth 1884 (age 29)
- [FAIL] colony: no placed event resolves to 'Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1913-1918
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

