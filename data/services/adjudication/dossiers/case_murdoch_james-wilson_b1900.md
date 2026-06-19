<!-- {"case_id": "case_murdoch_james-wilson_b1900", "bio_ids": ["murdoch_james-wilson_b1900"], "stint_ids": ["Murdoch, J. W___Straits Settlements___1931"]} -->
# Dossier case_murdoch_james-wilson_b1900

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `murdoch_james-wilson_b1900`

- Printed name: **MURDOCH, JAMES WILSON**
- Birth year: 1900 (attested in editions [1934, 1935, 1936, 1937, 1939, 1940])
- Honours: M.B
- Appears in editions: [1934, 1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1934-L61832.v` — printed in editions [1934, 1935, 1936, 1937, 1939, 1940]:**

> MURDOCH, JAMES WILSON, M.B., Ch.B. (Aberdeen).—B. 1900; 2nd asst. med. supt., ment. hosp., T. Rambutan, F.M.S., Jan., 1926; med. supt., do., July, 1931.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | 2nd asst. med. supt., ment. hosp., T. Rambutan | Federated Malay States | [1934, 1935, 1936, 1937, 1939, 1940] |
| 1 | 1931 | med. supt. | Dominions Office | [1934, 1935, 1936, 1937, 1939, 1940] |

## Candidate stint `Murdoch, J. W___Straits Settlements___1931`

- Staff-list name: **Murdoch, J. W** | colony: **Straits Settlements** | listed 1931–1933 | editions [1931, 1932, 1933]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | J. W. Murdoch | Assistant Medical Assistant | Public Works | — | — |
| 1931 | J. W. Murdoch | Assistant Medical Superintendent | Central Mental Hospital | — | — |
| 1932 | J. W. Murdoch | Medical Superintendent (acting) | Central Mental Hospital | — | — |
| 1933 | J. W. Murdoch | Medical Superintendent | Central Mental Hospital | — | — |

### Deterministic checks: `murdoch_james-wilson_b1900` vs `Murdoch, J. W___Straits Settlements___1931`

- [PASS] surname_gate: bio 'MURDOCH' vs stint 'Murdoch, J. W' (exact)
- [PASS] initials: bio ['J', 'W'] ~ stint ['J', 'W']
- [PASS] age_gate: stint starts 1931, birth 1900 (age 31)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1933
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

