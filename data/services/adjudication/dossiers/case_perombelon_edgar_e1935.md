<!-- {"case_id": "case_perombelon_edgar_e1935", "bio_ids": ["perombelon_edgar_e1935"], "stint_ids": ["Perombelon, J. E___Mauritius___1927"]} -->
# Dossier case_perombelon_edgar_e1935

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['perombelon_edgar_e1935'] carry a single initial only — the namesake trap applies.

## Biography `perombelon_edgar_e1935`

- Printed name: **PEROMBELON, EDGAR**
- Birth year: not printed
- Appears in editions: [1939]

### Verbatim printed entry text (OCR)

**Version `col1939-L69753.v` — printed in editions [1939]:**

> PEROMBELON, EDGAR.—Ag. P.M.G., Mauritius, July, 1935; P.M.G., Nov., 1935.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1935 | Ag. P.M.G. | Mauritius | [1939] |

## Candidate stint `Perombelon, J. E___Mauritius___1927`

- Staff-list name: **Perombelon, J. E** | colony: **Mauritius** | listed 1927–1931 | editions [1927, 1928, 1929, 1931]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | J. E. Perombelon | Accountant, 2nd Class Clerk | Postal and Telegraph Department | — | — |
| 1928 | J. E. Perombelon | Accountant, 2nd Class Clerk | Postal and Telegraph Department | — | — |
| 1929 | J. E. Perombelon | Accountant, 2nd Class Clerk | Postal and Telegraph Department | — | — |
| 1931 | J. E. Perombelon | Accountant, 2nd Class Clerk | Postal and Telegraph Department | — | — |

### Deterministic checks: `perombelon_edgar_e1935` vs `Perombelon, J. E___Mauritius___1927`

- [PASS] surname_gate: bio 'PEROMBELON' vs stint 'Perombelon, J. E' (exact)
- [PASS] initials: bio ['E'] ~ stint ['J', 'E']
- [PASS] age_gate: stint starts 1927; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Mauritius'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1927-1931
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

