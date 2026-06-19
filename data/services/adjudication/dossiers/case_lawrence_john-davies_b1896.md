<!-- {"case_id": "case_lawrence_john-davies_b1896", "bio_ids": ["lawrence_john-davies_b1896"], "stint_ids": ["Lawrence, J. C. D___Uganda___1960"]} -->
# Dossier case_lawrence_john-davies_b1896

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 58 official(s) with this surname in the graph's staff lists; 24 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Lawrence, J. C. D___Uganda___1960` is also gate-compatible with biography(ies) outside this case: ['lawrence_john-duncan_e1896'] (already linked elsewhere or filtered).

## Biography `lawrence_john-davies_b1896`

- Printed name: **LAWRENCE, JOHN DAVIES**
- Birth year: 1896 (attested in editions [1940])
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L66018.v` — printed in editions [1940]:**

> LAWRENCE, JOHN DAVIES, M.C.—B. 1896; ed. Tonbridge Schol. and R. Mily. Coll.; Manchester Regt., Egyptian Army, 1917-20; cadet, Tanganyika Territory, 1921; dist. offr., 1933.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1917–1920 | Manchester Regt., Egyptian Army | — | [1940] |
| 1 | 1921 | cadet, Tanganyika Territory | Tanganyika | [1940] |
| 2 | 1933 | dist. offr | Tanganyika *(inherited from previous clause)* | [1940] |

## Candidate stint `Lawrence, J. C. D___Uganda___1960`

- Staff-list name: **Lawrence, J. C. D** | colony: **Uganda** | listed 1960–1962 | editions [1960, 1962]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1960 | J. C. D. Lawrence | Permanent Secretary to the Ministry of Land and Mineral Development | Civil Establishment | — | — |
| 1962 | J. C. D. Lawrence | Provincial Commissioner | Civil Establishment | — | — |

### Deterministic checks: `lawrence_john-davies_b1896` vs `Lawrence, J. C. D___Uganda___1960`

- [PASS] surname_gate: bio 'LAWRENCE' vs stint 'Lawrence, J. C. D' (exact)
- [PASS] initials: bio ['J', 'D'] ~ stint ['J', 'C', 'D']
- [PASS] age_gate: stint starts 1960, birth 1896 (age 64)
- [FAIL] colony: no placed event resolves to 'Uganda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1960-1962
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

