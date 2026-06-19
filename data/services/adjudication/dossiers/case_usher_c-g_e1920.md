<!-- {"case_id": "case_usher_c-g_e1920", "bio_ids": ["usher_c-g_e1920", "usher_c-g_e1920-2"], "stint_ids": ["Usher, C. G___Kenya___1949"]} -->
# Dossier case_usher_c-g_e1920

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 20 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Usher, C. G___Kenya___1949'] have more than one claimant biography in this case.

## Biography `usher_c-g_e1920`

- Printed name: **USHER, C. G**
- Birth year: not printed
- Appears in editions: [1924, 1925, 1927]

### Verbatim printed entry text (OCR)

**Version `col1924-L58512.v` — printed in editions [1924, 1925, 1927]:**

> USHER, Capt. C. G., M.C.—Ast. dist. comsnr., Kenya, May, 1920.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920 | Ast. dist. comsnr. | Kenya | [1924, 1925, 1927] |

## Biography `usher_c-g_e1920-2`

- Printed name: **USHER, C. G.**
- Birth year: not printed
- Honours: M.C.
- Appears in editions: [1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L71356.v` — printed in editions [1939, 1940]:**

> USHER, CAPT. C. G., M.C. — Asst. dist. comsnr., Kenya, May, 1920; dist. offr., 1923; ag. sec., secretariat, 1927 and 1931.

**Version `col1928-L70673.v` — printed in editions [1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1937]:**

> USHER, CAPT. C. G., M.C. — Asst. dist. commr., Kenya, May, 1920; ag. sec., secretariat, 1927.

**Version `col1936-L65284.v` — printed in editions [1936]:**

> USHER, CAPT. C. G., M.C.—AST. DIST. COMSNR., KENYA, MAY, 1920; AG. SEC., SECRETARIAT, 1927.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920 | Asst. dist. comsnr. | Kenya | [1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |
| 1 | 1923 | dist. offr. | — | [1939, 1940] |
| 2 | 1927 | ag. sec., secretariat | Kenya *(inherited from previous clause)* | [1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1939, 1940] |

## Candidate stint `Usher, C. G___Kenya___1949`

- Staff-list name: **Usher, C. G** | colony: **Kenya** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | C. G. Usher | Registrars of Titles | Lands | — | — |
| 1950 | C. G. Usher | Registrars of Titles | Lands | — | — |

### Deterministic checks: `usher_c-g_e1920` vs `Usher, C. G___Kenya___1949`

- [PASS] surname_gate: bio 'USHER' vs stint 'Usher, C. G' (exact)
- [PASS] initials: bio ['C', 'G'] ~ stint ['C', 'G']
- [PASS] age_gate: stint starts 1949; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1950
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `usher_c-g_e1920-2` vs `Usher, C. G___Kenya___1949`

- [PASS] surname_gate: bio 'USHER' vs stint 'Usher, C. G' (exact)
- [PASS] initials: bio ['C', 'G'] ~ stint ['C', 'G']
- [PASS] age_gate: stint starts 1949; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1950
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

