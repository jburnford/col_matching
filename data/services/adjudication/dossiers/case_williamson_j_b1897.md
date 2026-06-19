<!-- {"case_id": "case_williamson_j_b1897", "bio_ids": ["williamson_j_b1897"], "stint_ids": ["Williamson, J. C___New Zealand___1915"]} -->
# Dossier case_williamson_j_b1897

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 17 official(s) with this surname in the graph's staff lists; 14 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['williamson_j_b1897'] carry a single initial only — the namesake trap applies.

## Biography `williamson_j_b1897`

- Printed name: **WILLIAMSON, J**
- Birth year: 1897 (attested in editions [1933, 1934, 1935, 1937, 1939, 1940])
- Honours: M.B
- Appears in editions: [1933, 1934, 1935, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1933-L64523.v` — printed in editions [1933, 1934, 1935, 1937, 1939, 1940]:**

> WILLIAMSON, J., M.B., Ch.B. (Edin.), Cert., Lond. S. Hyg. & T.M. (distinc.)—B. 1897; mily. serv., 1915-19; med. offr., Tanganyika Territory, 1926.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915–1919 | mily. serv | — | [1933, 1934, 1935, 1937, 1939, 1940] |
| 1 | 1926 | med. offr., Tanganyika Territory | Tanganyika | [1933, 1934, 1935, 1937, 1939, 1940] |

## Candidate stint `Williamson, J. C___New Zealand___1915`

- Staff-list name: **Williamson, J. C** | colony: **New Zealand** | listed 1915–1920 | editions [1915, 1917, 1918, 1919, 1920]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1915 | J. C. Williamson | Chief Clerk | Post and Telegraph Department | — | — |
| 1917 | J. C. Williamson | Chief Postmaster | Post and Telegraph Department | — | — |
| 1918 | J. C. Williamson | Chief Postmaster | Post and Telegraph Department | — | — |
| 1919 | J. C. Williamson | Chief Postmaster | Post and Telegraph Department | — | — |
| 1920 | J. C. Williamson | Chief Inspector | Post and Telegraph Department | — | — |

### Deterministic checks: `williamson_j_b1897` vs `Williamson, J. C___New Zealand___1915`

- [PASS] surname_gate: bio 'WILLIAMSON' vs stint 'Williamson, J. C' (exact)
- [PASS] initials: bio ['J'] ~ stint ['J', 'C']
- [PASS] age_gate: stint starts 1915, birth 1897 (age 18)
- [FAIL] colony: no placed event resolves to 'New Zealand'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1915-1920
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

