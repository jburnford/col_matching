<!-- {"case_id": "case_turlay_henry_b1859", "bio_ids": ["turlay_henry_b1859"], "stint_ids": ["Turley, H___Commonwealth Of Australia___1905"]} -->
# Dossier case_turlay_henry_b1859

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['turlay_henry_b1859'] carry a single initial only — the namesake trap applies.

## Biography `turlay_henry_b1859`

- Printed name: **TURLAY, HENRY**
- Birth year: 1859 (attested in editions [1912])
- Appears in editions: [1912, 1913, 1914, 1915, 1917, 1918, 1919]

### Verbatim printed entry text (OCR)

**Version `col1912-L48104.v` — printed in editions [1912]:**

> TURLAY, HON. HENRY.—B. 1859; M.L.A., Queensland, 1893-1902; elected to the Senate, C. A., 1903; pres. of Senate, July, 1910.

**Version `col1913-L49921.v` — printed in editions [1913, 1914, 1915, 1917, 1919]:**

> TURLEY, HON. HENRY.—B. 1859; M.L.A., Queensland, 1893-1902; elected to the Senate, C. of A., 1903; pres. of Senate, July, 1910-1913.

**Version `col1918-L54958.v` — printed in editions [1918]:**

> TURNLEY, HON. HENRY.—B. 1859; M.L.A., Queensland, 1893-1902; elected to the Senate, C. of A., 1903; pres. of Senate, July, 1910-1913.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1893–1902 | M.L.A. | Queensland | [1912, 1913, 1914, 1915, 1917, 1918, 1919] |
| 1 | 1903 | elected to the Senate, C. A | Queensland *(inherited from previous clause)* | [1912, 1913, 1914, 1915, 1917, 1918, 1919] |
| 2 | 1910 | pres. of Senate | Queensland *(inherited from previous clause)* | [1912, 1913, 1914, 1915, 1917, 1918, 1919] |

## Candidate stint `Turley, H___Commonwealth Of Australia___1905`

- Staff-list name: **Turley, H** | colony: **Commonwealth Of Australia** | listed 1905–1907 | editions [1905, 1907]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | H. Turley | Senator | Senate | — | — |
| 1907 | H. Turley | Senator | Senate | — | — |

### Deterministic checks: `turlay_henry_b1859` vs `Turley, H___Commonwealth Of Australia___1905`

- [PASS] surname_gate: bio 'TURLAY' vs stint 'Turley, H' (fuzzy:1)
- [PASS] initials: bio ['H'] ~ stint ['H']
- [PASS] age_gate: stint starts 1905, birth 1859 (age 46)
- [FAIL] colony: no placed event resolves to 'Commonwealth Of Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1907
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

