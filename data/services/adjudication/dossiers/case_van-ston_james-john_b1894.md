<!-- {"case_id": "case_van-ston_james-john_b1894", "bio_ids": ["van-ston_james-john_b1894"], "stint_ids": ["Vanston, J. J___Straits Settlements___1931"]} -->
# Dossier case_van-ston_james-john_b1894

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Vanston, J. J___Straits Settlements___1931` is also gate-compatible with biography(ies) outside this case: ['vanston_james-john_b1896'] (already linked elsewhere or filtered).

## Biography `van-ston_james-john_b1894`

- Printed name: **VAN STON, JAMES JOHN**
- Birth year: 1894 (attested in editions [1939, 1940])
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L71394.v` — printed in editions [1939, 1940]:**

> VAN STON, JAMES JOHN, M.I.Mar.E.—B. 1894; ed. Diocesan Boys' Schi., Hong Kong; survr., ships, S.S., May, 1923; do., S'pore, May, 1927; do., Penang, Feb., 1932; do., S'pore, Oct., 1935.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1923 | survr., ships | Straits Settlements | [1939, 1940] |
| 1 | 1927 | do., S'pore | Straits Settlements *(inherited from previous clause)* | [1939, 1940] |
| 2 | 1932 | do., Penang | Straits Settlements *(inherited from previous clause)* | [1939, 1940] |
| 3 | 1935 | do., S'pore | Straits Settlements *(inherited from previous clause)* | [1939, 1940] |

## Candidate stint `Vanston, J. J___Straits Settlements___1931`

- Staff-list name: **Vanston, J. J** | colony: **Straits Settlements** | listed 1931–1939 | editions [1931, 1933, 1934, 1936, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | J. J. Vanston | Surveyors of Ships | Marine Surveys | — | — |
| 1933 | J. J. Vanston | Surveyors of Ships | Marine Surveyors | — | — |
| 1934 | J. J. Vanston | Surveyors of Ships | Marine Surveys | — | — |
| 1936 | J. J. Vanston | Surveyors of Ships, S.S. | Marine Surveys | — | — |
| 1939 | J. J. Vanston | Surveyors of Ships | Marine Surveys | — | — |

### Deterministic checks: `van-ston_james-john_b1894` vs `Vanston, J. J___Straits Settlements___1931`

- [PASS] surname_gate: bio 'VAN STON' vs stint 'Vanston, J. J' (fuzzy:1)
- [PASS] initials: bio ['J', 'J'] ~ stint ['J', 'J']
- [PASS] age_gate: stint starts 1931, birth 1894 (age 37)
- [PASS] colony: 4 placed event(s) resolve to 'Straits Settlements'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1931-1939
- [FAIL] position_sim: best 46 vs bar 60: 'do., S'pore' ~ 'Surveyors of Ships'
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

