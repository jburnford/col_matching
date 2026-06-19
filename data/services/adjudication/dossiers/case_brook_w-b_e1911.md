<!-- {"case_id": "case_brook_w-b_e1911", "bio_ids": ["brook_w-b_e1911", "brook_w-b_e1911-2"], "stint_ids": ["Brook, W. B___Kenya___1909"]} -->
# Dossier case_brook_w-b_e1911

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Brook, W. B___Kenya___1909'] have more than one claimant biography in this case.
- Phase 1 found `brook_w-b_e1911` ↔ `Brook, W. B___Kenya___1909` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- Phase 1 found `brook_w-b_e1911-2` ↔ `Brook, W. B___Kenya___1909` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).

## Biography `brook_w-b_e1911`

- Printed name: **BROOK, W. B**
- Birth year: not printed
- Appears in editions: [1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922]

### Verbatim printed entry text (OCR)

**Version `col1912-L42872.v` — printed in editions [1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922]:**

> BROOK, CAPT. W. B.—Asst. dist. comanr., E.A.P., 1911.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1911 | Asst. dist. comanr. | East Africa Protectorate | [1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922] |

## Biography `brook_w-b_e1911-2`

- Printed name: **BROOK, W. B**
- Birth year: not printed
- Appears in editions: [1923, 1924, 1925, 1927, 1928, 1930, 1931, 1932, 1933]

### Verbatim printed entry text (OCR)

**Version `col1923-L52811.v` — printed in editions [1923, 1924, 1925, 1927, 1928, 1930, 1931, 1932, 1933]:**

> BROOK, CAPT. W. B.—Asst. dist. comanr., E.A.P., 1911; dist. comanr., Kenya, Jan., 1919.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1911 | Asst. dist. comanr. | East Africa Protectorate | [1923, 1924, 1925, 1927, 1928, 1930, 1931, 1932, 1933] |
| 1 | 1919 | dist. comanr. | Kenya | [1923, 1924, 1925, 1927, 1928, 1930, 1931, 1932, 1933] |

## Candidate stint `Brook, W. B___Kenya___1909`

- Staff-list name: **Brook, W. B** | colony: **Kenya** | listed 1909–1912 | editions [1909, 1910, 1912]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1909 | W. B. Brook | Company Commander | King's African Rifles - 2nd Battalion | — | — |
| 1910 | W. B. Brook | Company Commander | King's African Rifles | — | — |
| 1912 | W. B. Brook | Assistant District Commissioner | Provincial Administration | — | Captain |

### Deterministic checks: `brook_w-b_e1911` vs `Brook, W. B___Kenya___1909`

- [PASS] surname_gate: bio 'BROOK' vs stint 'Brook, W. B' (exact)
- [PASS] initials: bio ['W', 'B'] ~ stint ['W', 'B']
- [PASS] age_gate: stint starts 1909; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1909-1912
- [PASS] position_sim: best 64 vs bar 60: 'Asst. dist. comanr.' ~ 'Assistant District Commissioner'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): 1 agreeing edition-year(s) [1912] pos~64 (bar: >=2)
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `brook_w-b_e1911-2` vs `Brook, W. B___Kenya___1909`

- [PASS] surname_gate: bio 'BROOK' vs stint 'Brook, W. B' (exact)
- [PASS] initials: bio ['W', 'B'] ~ stint ['W', 'B']
- [PASS] age_gate: stint starts 1909; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1909-1912
- [PASS] position_sim: best 64 vs bar 60: 'Asst. dist. comanr.' ~ 'Assistant District Commissioner'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

