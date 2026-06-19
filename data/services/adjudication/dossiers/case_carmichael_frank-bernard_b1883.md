<!-- {"case_id": "case_carmichael_frank-bernard_b1883", "bio_ids": ["carmichael_frank-bernard_b1883"], "stint_ids": ["Carmichael, F. B___Trinidad and Tobago___1931"]} -->
# Dossier case_carmichael_frank-bernard_b1883

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 15 official(s) with this surname in the graph's staff lists; 10 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `carmichael_frank-bernard_b1883`

- Printed name: **CARMICHAEL, FRANK BERNARD**
- Birth year: 1883 (attested in editions [1936, 1937, 1940])
- Appears in editions: [1929, 1930, 1931, 1932, 1933, 1934, 1936, 1937, 1940]

### Verbatim printed entry text (OCR)

**Version `col1936-L59560.v` — printed in editions [1936, 1937, 1940]:**

> CARMICHAEL, FRANK BERNARD—B. 1883; loco. supt., Trinidad govt. rly., June, 1928; ag. supt., rly., July, 1934 to Jan., 1935, and July-Dec., 1937.

**Version `col1929-L58986.v` — printed in editions [1929, 1930, 1931, 1932, 1933, 1934]:**

> CARMICHAEL, FRANK BERNARD—B. 1883; loco., supt., Trinidad govt. rly., June, 1928.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | loco. supt., Trinidad govt. rly | Trinidad | [1929, 1930, 1931, 1932, 1933, 1934, 1936, 1937, 1940] |
| 1 | 1934–1935 | ag. supt., rly | Trinidad *(inherited from previous clause)* | [1936, 1937, 1940] |
| 2 | 1937 | July- | Trinidad *(inherited from previous clause)* | [1936, 1937, 1940] |

## Candidate stint `Carmichael, F. B___Trinidad and Tobago___1931`

- Staff-list name: **Carmichael, F. B** | colony: **Trinidad and Tobago** | listed 1931–1939 | editions [1931, 1933, 1934, 1937, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | F. B. Carmichael | Locomotive Engineer and Superintendent of Railway Steamers | Locomotive Branch | — | — |
| 1933 | F. B. Carmichael | Locomotive (Carriage and Wagon) Superintendent | Locomotive Branch | — | — |
| 1934 | F. B. Carmichael | Locomotive (Carriage and Wagon) Superintendent | Locomotive Branch | — | — |
| 1937 | F. B. Carmichael | Locomotive (Carriage and Wagon) Superintendent | Locomotive Branch | — | — |
| 1939 | F. B. Carmichael | Locomotive (Carriage and Wagon) Superintendent; also Engineer Supt. Coastal Steamers | Locomotive Branch | — | — |

### Deterministic checks: `carmichael_frank-bernard_b1883` vs `Carmichael, F. B___Trinidad and Tobago___1931`

- [PASS] surname_gate: bio 'CARMICHAEL' vs stint 'Carmichael, F. B' (exact)
- [PASS] initials: bio ['F', 'B'] ~ stint ['F', 'B']
- [PASS] age_gate: stint starts 1931, birth 1883 (age 48)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1939
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

