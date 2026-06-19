<!-- {"case_id": "case_nicol_charles-henry_b1880", "bio_ids": ["nicol_charles-henry_b1880"], "stint_ids": ["Nicol, C. H___Straits Settlements___1931"]} -->
# Dossier case_nicol_charles-henry_b1880

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 24 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `nicol_charles-henry_b1880`

- Printed name: **NICOL, CHARLES HENRY**
- Birth year: 1880 (attested in editions [1934])
- Appears in editions: [1934]

### Verbatim printed entry text (OCR)

**Version `col1934-L61959.v` — printed in editions [1934]:**

> NICOL, CHARLES HENRY.—B. 1880; joined S.S. pol., Jan., 1906; ch. inspr., cts., May, 1914; coroner, S'pore, May, 1923; ch. inspr., cts., Mar., 1924; asst. supt., pol., S.S., Nov., 1928.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1906 | joined S.S. pol | — | [1934] |
| 1 | 1914 | ch. inspr., cts | — | [1934] |
| 2 | 1923 | coroner, S'pore | — | [1934] |
| 3 | 1924 | ch. inspr., cts | — | [1934] |
| 4 | 1928 | asst. supt., pol. | Straits Settlements | [1934] |

## Candidate stint `Nicol, C. H___Straits Settlements___1931`

- Staff-list name: **Nicol, C. H** | colony: **Straits Settlements** | listed 1931–1933 | editions [1931, 1933]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | C. H. Nicol | Assistant Superintendent | Police | — | — |
| 1933 | C. H. Nicol | Assistant Superintendent | Police | — | — |

### Deterministic checks: `nicol_charles-henry_b1880` vs `Nicol, C. H___Straits Settlements___1931`

- [PASS] surname_gate: bio 'NICOL' vs stint 'Nicol, C. H' (exact)
- [PASS] initials: bio ['C', 'H'] ~ stint ['C', 'H']
- [PASS] age_gate: stint starts 1931, birth 1880 (age 51)
- [PASS] colony: 1 placed event(s) resolve to 'Straits Settlements'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1931-1933
- [FAIL] position_sim: best 49 vs bar 60: 'asst. supt., pol.' ~ 'Assistant Superintendent'
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

