<!-- {"case_id": "case_rosedale_john-lewis_b1889", "bio_ids": ["rosedale_john-lewis_b1889", "rosedale_john-lkws_b1889"], "stint_ids": ["Rosedale, J. L___Straits Settlements___1931"]} -->
# Dossier case_rosedale_john-lewis_b1889

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Rosedale, J. L___Straits Settlements___1931'] have more than one claimant biography in this case.

## Biography `rosedale_john-lewis_b1889`

- Printed name: **ROSEDALE, JOHN LEWIS**
- Birth year: 1889 (attested in editions [1934, 1935, 1936, 1937, 1939, 1940])
- Honours: F.I.C
- Appears in editions: [1934, 1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1934-L62699.v` — printed in editions [1934, 1935, 1936, 1937, 1939, 1940]:**

> ROSEDALE, JOHN LEWIS, Ph.D. (Bonn), D.Sc. (Aberdeen), F.I.C.—B. 1889; prof. of biochemistry, King Edward VII Medical Coll., Singapore, Apr., 1927; offl. deleg. to 8th cong. of Far Eastern Asso. of Trop. Med., Bangkok, Dec., 1930; offl. deleg. to 9th cong., F.E.A.T.M., Nanking, Sept., 1934.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | prof. of biochemistry, King Edward VII Medical Coll. | Singapore | [1934, 1935, 1936, 1937, 1939, 1940] |
| 1 | 1930 | offl. deleg. to 8th cong. of Far Eastern Asso. of Trop. Med., Bangkok | Singapore *(inherited from previous clause)* | [1934, 1935, 1936, 1937, 1939, 1940] |
| 2 | 1934 | offl. deleg. to 9th cong., F.E.A.T.M., Nanking | Singapore *(inherited from previous clause)* | [1934, 1935, 1936, 1937, 1939, 1940] |

## Biography `rosedale_john-lkws_b1889`

- Printed name: **ROSEDALE, JOHN LKWS**
- Birth year: 1889 (attested in editions [1932, 1933])
- Appears in editions: [1932, 1933]

### Verbatim printed entry text (OCR)

**Version `col1932-L63609.v` — printed in editions [1932, 1933]:**

> ROSEDALE, JOHN LKWS.—B. 1889; prof. of biochemistry, King Edward VII Medical Coll., Singapore, Apr., 1927.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | prof. of biochemistry, King Edward VII Medical Coll. | Singapore | [1932, 1933] |

## Candidate stint `Rosedale, J. L___Straits Settlements___1931`

- Staff-list name: **Rosedale, J. L** | colony: **Straits Settlements** | listed 1931–1936 | editions [1931, 1933, 1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | J. L. Rosedale | Professor of Bio-Chemistry | King Edward VII College of Medicine | — | — |
| 1933 | J. L. Rosedale | Professor of Bio-Chemistry | King Edward VII College of Medicine | — | — |
| 1934 | J. L. Rosedale | Professor of Bio-Chemistry | King Edward VII College of Medicine, Singapore | — | — |
| 1936 | J. L. Rosedale | Professor of Bio-Chemistry | Medical | — | — |

### Deterministic checks: `rosedale_john-lewis_b1889` vs `Rosedale, J. L___Straits Settlements___1931`

- [PASS] surname_gate: bio 'ROSEDALE' vs stint 'Rosedale, J. L' (exact)
- [PASS] initials: bio ['J', 'L'] ~ stint ['J', 'L']
- [PASS] age_gate: stint starts 1931, birth 1889 (age 42)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1936
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `rosedale_john-lkws_b1889` vs `Rosedale, J. L___Straits Settlements___1931`

- [PASS] surname_gate: bio 'ROSEDALE' vs stint 'Rosedale, J. L' (exact)
- [PASS] initials: bio ['J', 'L'] ~ stint ['J', 'L']
- [PASS] age_gate: stint starts 1931, birth 1889 (age 42)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1936
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

