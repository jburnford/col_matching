<!-- {"case_id": "case_russell_laurence-arnold_b1888", "bio_ids": ["russell_laurence-arnold_b1888"], "stint_ids": ["Russell, L. A___Jamaica___1930", "Russell, L. A___Northern Rhodesia___1936"]} -->
# Dossier case_russell_laurence-arnold_b1888

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 86 official(s) with this surname in the graph's staff lists; 58 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `russell_laurence-arnold_b1888`

- Printed name: **RUSSELL, LAURENCE ARNOLD**
- Birth year: 1888 (attested in editions [1935, 1936, 1937, 1939])
- Appears in editions: [1935, 1936, 1937, 1939]

### Verbatim printed entry text (OCR)

**Version `dol1935-L61932.v` — printed in editions [1935, 1936, 1937, 1939]:**

> RUSSELL, LAURENCE ARNOLD.—B. 1888; ed., Rossall Schl. and Hertford Coll., Oxford; probationer, N. Rhodesia, Sept., 1912; asst. native comanr., 1914; war serv.; E. Africa, 1915-19; native comanr., 1918; asst. mag., 1926; ag. prov. comanr., for short periods 1929 and 1933; prov. comanr., 1934.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1912 | probationer | Northern Rhodesia | [1935, 1936, 1937, 1939] |
| 1 | 1914 | asst. native comanr. | — | [1935, 1936, 1937, 1939] |
| 2 | 1915–1919 | — | East Africa | [1935, 1936, 1937, 1939] |
| 3 | 1918 | native comanr. | — | [1935, 1936, 1937, 1939] |
| 4 | 1926 | asst. mag. | — | [1935, 1936, 1937, 1939] |
| 5 | 1929–1933 | ag. prov. comanr. | — | [1935, 1936, 1937, 1939] |
| 6 | 1934 | prov. comanr. | — | [1935, 1936, 1937, 1939] |

## Candidate stint `Russell, L. A___Jamaica___1930`

- Staff-list name: **Russell, L. A** | colony: **Jamaica** | listed 1930–1940 | editions [1930, 1931, 1933, 1934, 1937, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1930 | L. A. Russell | Inspectors of Plant Diseases | Science and Agriculture | — | — |
| 1931 | L. A. Russell | Inspectors of Plant Diseases | Department of Science and Agriculture | — | — |
| 1933 | L. A. Russell | Inspectors of Plant Diseases | Department of Science and Agriculture | — | — |
| 1934 | L. A. Russell | Inspector of Plant Diseases | Department of Science and Agriculture | — | — |
| 1937 | L. A. Russell | Inspectors of Plant Diseases | Department of Science and Agriculture | — | — |
| 1940 | L. A. Russell | Inspector of Plant Diseases | Department of Science and Agriculture | — | — |

### Deterministic checks: `russell_laurence-arnold_b1888` vs `Russell, L. A___Jamaica___1930`

- [PASS] surname_gate: bio 'RUSSELL' vs stint 'Russell, L. A' (exact)
- [PASS] initials: bio ['L', 'A'] ~ stint ['L', 'A']
- [PASS] age_gate: stint starts 1930, birth 1888 (age 42)
- [FAIL] colony: no placed event resolves to 'Jamaica'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1930-1940
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Russell, L. A___Northern Rhodesia___1936`

- Staff-list name: **Russell, L. A** | colony: **Northern Rhodesia** | listed 1936–1939 | editions [1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | L. A. Russell | Provincial Commissioners | District Administration | — | — |
| 1939 | L. A. Russell | Provincial Commissioner | District Administration | — | — |

### Deterministic checks: `russell_laurence-arnold_b1888` vs `Russell, L. A___Northern Rhodesia___1936`

- [PASS] surname_gate: bio 'RUSSELL' vs stint 'Russell, L. A' (exact)
- [PASS] initials: bio ['L', 'A'] ~ stint ['L', 'A']
- [PASS] age_gate: stint starts 1936, birth 1888 (age 48)
- [PASS] colony: 1 placed event(s) resolve to 'Northern Rhodesia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1936-1939
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

