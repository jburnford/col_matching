<!-- {"case_id": "case_lessels_raymond_b1897", "bio_ids": ["lessels_raymond_b1897"], "stint_ids": ["Lessels, R___Gold Coast___1950"]} -->
# Dossier case_lessels_raymond_b1897

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['lessels_raymond_b1897'] carry a single initial only — the namesake trap applies.

## Biography `lessels_raymond_b1897`

- Printed name: **LESSELS, RAYMOND**
- Birth year: 1897 (attested in editions [1935, 1936, 1937, 1939, 1940])
- Appears in editions: [1934, 1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `dol1935-L60251.v` — printed in editions [1935, 1936, 1937, 1939, 1940]:**

> LESSELS, RAYMOND.—B. 1897; asst. engrnr., posts and tels. dept., Nigeria, Mar., 1924; divnl. engrnr., Apr., 1933; ag. engrnr.-in-ch., 1933, 1934 and 1938.

**Version `col1934-L61076.v` — printed in editions [1934]:**

> LESSELS, RAYMOND.—B. 1897; ast. engr., posts and tels. dept., Nigeria, 1924; divnl. engnr., Apr., 1933.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1924 | asst. engrnr., posts and tels. dept. | Nigeria | [1934, 1935, 1936, 1937, 1939, 1940] |
| 1 | 1933 | divnl. engrnr. | Nigeria *(inherited from previous clause)* | [1934, 1935, 1936, 1937, 1939, 1940] |
| 2 | 1933–1938 | ag. engrnr.-in-ch. | — | [1935, 1936, 1937, 1939, 1940] |

## Candidate stint `Lessels, R___Gold Coast___1950`

- Staff-list name: **Lessels, R** | colony: **Gold Coast** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | R. Lessels | Foremen of Works | WATER SUPPLY | — | — |
| 1951 | R. Lessels | Inspectors of Works | Rural Water Development | — | — |

### Deterministic checks: `lessels_raymond_b1897` vs `Lessels, R___Gold Coast___1950`

- [PASS] surname_gate: bio 'LESSELS' vs stint 'Lessels, R' (exact)
- [PASS] initials: bio ['R'] ~ stint ['R']
- [PASS] age_gate: stint starts 1950, birth 1897 (age 53)
- [FAIL] colony: no placed event resolves to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1950-1951
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

