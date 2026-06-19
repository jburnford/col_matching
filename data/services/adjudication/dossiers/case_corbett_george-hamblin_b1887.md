<!-- {"case_id": "case_corbett_george-hamblin_b1887", "bio_ids": ["corbett_george-hamblin_b1887"], "stint_ids": ["Corbett, G___Cyprus___1949", "Corbett, G___Mauritius___1936"]} -->
# Dossier case_corbett_george-hamblin_b1887

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Corbett, G___Cyprus___1949` is also gate-compatible with biography(ies) outside this case: ['corbett_geoffrey_b1893'] (already linked elsewhere or filtered).
- NOTE: stint `Corbett, G___Mauritius___1936` is also gate-compatible with biography(ies) outside this case: ['corbett_geoffrey_b1893'] (already linked elsewhere or filtered).

## Biography `corbett_george-hamblin_b1887`

- Printed name: **CORBETT, GEORGE HAMBLIN**
- Birth year: 1887 (attested in editions [1933, 1934, 1935, 1936, 1937, 1939, 1940])
- Appears in editions: [1933, 1934, 1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1933-L58831.v` — printed in editions [1933, 1934, 1935, 1936, 1937, 1939, 1940]:**

> CORBETT, GEORGE HAMBLIN, B.Sc., F.R.E.S.—B. 1887; ed. King Edwards Schol., Bath, and Medin., Cornell and Harvard Unive.; govt. entomologist, F.M.S., Apr., 1920; deleg. of F.M.S. and S.S. govt., at 2nd Imp. Entomological Conference, London, June, 1925; constg. entomologist, Inst. Med. Resch., and Rubber Resch. inst., in adzn., June, 1930-Aug., 1932 and Mar., 1935.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920 | govt. entomologist | Federated Malay States | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 1 | 1925 | deleg. of F.M.S. and S.S. govt. | Federated Malay States | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 2 | 1930–1935 | constg. entomologist | — | [1933, 1934, 1935, 1936, 1937, 1939, 1940] |

## Candidate stint `Corbett, G___Cyprus___1949`

- Staff-list name: **Corbett, G** | colony: **Cyprus** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | G. Corbett | Agricultural Officer | Agriculture | — | — |
| 1951 | G. Corbett | Agricultural Officer | Agriculture | — | — |

### Deterministic checks: `corbett_george-hamblin_b1887` vs `Corbett, G___Cyprus___1949`

- [PASS] surname_gate: bio 'CORBETT' vs stint 'Corbett, G' (exact)
- [PASS] initials: bio ['G', 'H'] ~ stint ['G']
- [PASS] age_gate: stint starts 1949, birth 1887 (age 62)
- [FAIL] colony: no placed event resolves to 'Cyprus'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Corbett, G___Mauritius___1936`

- Staff-list name: **Corbett, G** | colony: **Mauritius** | listed 1936–1939 | editions [1936, 1937, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | G. Corbett | Government Tobacco Officer | Department of Agriculture | — | — |
| 1937 | G. Corbett | Government Tobacco Officer | Department of Agriculture | — | — |
| 1939 | G. Corbett | Government Tobacco Officer | Department of Agriculture | — | — |

### Deterministic checks: `corbett_george-hamblin_b1887` vs `Corbett, G___Mauritius___1936`

- [PASS] surname_gate: bio 'CORBETT' vs stint 'Corbett, G' (exact)
- [PASS] initials: bio ['G', 'H'] ~ stint ['G']
- [PASS] age_gate: stint starts 1936, birth 1887 (age 49)
- [FAIL] colony: no placed event resolves to 'Mauritius'
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

