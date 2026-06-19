<!-- {"case_id": "case_lucie-smith_reginald-wallace_b1915", "bio_ids": ["lucie-smith_reginald-wallace_b1915"], "stint_ids": ["Lucie-Smith, R. W___Trinidad and Tobago___1939"]} -->
# Dossier case_lucie-smith_reginald-wallace_b1915

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 16 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `lucie-smith_reginald-wallace_b1915`

- Printed name: **LUCIE-SMITH, Reginald Wallace**
- Birth year: 1915 (attested in editions [1951])
- Appears in editions: [1951]

### Verbatim printed entry text (OCR)

**Version `col1951-L40263.v` — printed in editions [1951]:**

> LUCIE-SMITH, Reginald Wallace.—b. 1915; ed. St. George's Coll., Weybridge; asst. supt., police, Trin., 1937; dep. comsnr., police, Bah. (secondment), 1947; supt., Trin., 1948.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1937 | asst. supt., police | Trinidad | [1951] |
| 1 | 1947 | dep. comsnr., police, Bah. (secondment) | Bahamas | [1951] |
| 2 | 1948 | supt. | Trinidad | [1951] |

## Candidate stint `Lucie-Smith, R. W___Trinidad and Tobago___1939`

- Staff-list name: **Lucie-Smith, R. W** | colony: **Trinidad and Tobago** | listed 1939–1949 | editions [1939, 1940, 1949]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | R. W. Lucie-Smith | Assistant Superintendent | Police | — | — |
| 1940 | R. W. Lucie-Smith | Assistant Superintendent | Police | — | — |
| 1949 | R. W. Lucie-Smith | Assistant Superintendents | Police | — | — |

### Deterministic checks: `lucie-smith_reginald-wallace_b1915` vs `Lucie-Smith, R. W___Trinidad and Tobago___1939`

- [PASS] surname_gate: bio 'LUCIE-SMITH' vs stint 'Lucie-Smith, R. W' (exact)
- [PASS] initials: bio ['R', 'W'] ~ stint ['R', 'W']
- [PASS] age_gate: stint starts 1939, birth 1915 (age 24)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1939-1949
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

