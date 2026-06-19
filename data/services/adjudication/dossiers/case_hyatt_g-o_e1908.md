<!-- {"case_id": "case_hyatt_g-o_e1908", "bio_ids": ["hyatt_g-o_e1908", "hyatt_g-o_e1908-2"], "stint_ids": ["Hyatt, G. O___Kenya___1909", "Hyatt, G. O___Uganda___1913"]} -->
# Dossier case_hyatt_g-o_e1908

## Case context

- 2 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Hyatt, G. O___Kenya___1909', 'Hyatt, G. O___Uganda___1913'] have more than one claimant biography in this case.

## Biography `hyatt_g-o_e1908`

- Printed name: **HYATT, G. O**
- Birth year: not printed
- Appears in editions: [1910, 1911, 1912, 1913, 1914, 1915]

### Verbatim printed entry text (OCR)

**Version `col1910-L46621.v` — printed in editions [1910, 1911, 1912, 1913, 1914, 1915]:**

> HYATT, G. O.—Aast. engrnr., Uganda rlyw., Jan., 1908.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1908 | Aast. engrnr., Uganda rlyw | Uganda | [1910, 1911, 1912, 1913, 1914, 1915] |

## Biography `hyatt_g-o_e1908-2`

- Printed name: **HYATT, G. O**
- Birth year: not printed
- Appears in editions: [1917, 1918, 1919, 1920, 1922]

### Verbatim printed entry text (OCR)

**Version `col1917-L50621.v` — printed in editions [1917, 1918, 1919, 1920, 1922]:**

> HYATT, G. O.—Astt. engrnr., Uganda rlyw., Jan., 1908; dist. engrnr., 1914.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1908 | Astt. engrnr., Uganda rlyw | Uganda | [1917, 1918, 1919, 1920, 1922] |
| 1 | 1914 | dist. engrnr | Uganda *(inherited from previous clause)* | [1917, 1918, 1919, 1920, 1922] |

## Candidate stint `Hyatt, G. O___Kenya___1909`

- Staff-list name: **Hyatt, G. O** | colony: **Kenya** | listed 1909–1919 | editions [1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1919]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1909 | G. O. Hyatt | Engineering | Railway | — | — |
| 1910 | G. O. Hyatt | Engineering | Engineering | — | — |
| 1911 | G. O. Hyatt | Engineering | Accounts | — | — |
| 1912 | G. O. Hyatt | Engineering | Engineering | — | — |
| 1913 | G. O. Hyatt | Engineering | Railway | — | — |
| 1914 | G. O. Hyatt | Engineering | Accounts | — | — |
| 1915 | G. O. Hyatt | District Engineer | Engineering | — | — |
| 1917 | G. O. Hyatt | District Engineers | Engineering | — | — |
| 1919 | G. O. Hyatt | District Engineer | Engineering | — | — |

### Deterministic checks: `hyatt_g-o_e1908` vs `Hyatt, G. O___Kenya___1909`

- [PASS] surname_gate: bio 'HYATT' vs stint 'Hyatt, G. O' (exact)
- [PASS] initials: bio ['G', 'O'] ~ stint ['G', 'O']
- [PASS] age_gate: stint starts 1909; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1909-1919
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `hyatt_g-o_e1908-2` vs `Hyatt, G. O___Kenya___1909`

- [PASS] surname_gate: bio 'HYATT' vs stint 'Hyatt, G. O' (exact)
- [PASS] initials: bio ['G', 'O'] ~ stint ['G', 'O']
- [PASS] age_gate: stint starts 1909; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1909-1919
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Hyatt, G. O___Uganda___1913`

- Staff-list name: **Hyatt, G. O** | colony: **Uganda** | listed 1913–1914 | editions [1913, 1914]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1913 | G. O. Hyatt | Superintendent | Busoga Railway | — | — |
| 1914 | G. O. Hyatt | Superintendent | Busoga Railway | — | — |

### Deterministic checks: `hyatt_g-o_e1908` vs `Hyatt, G. O___Uganda___1913`

- [PASS] surname_gate: bio 'HYATT' vs stint 'Hyatt, G. O' (exact)
- [PASS] initials: bio ['G', 'O'] ~ stint ['G', 'O']
- [PASS] age_gate: stint starts 1913; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1913-1914
- [FAIL] position_sim: best 32 vs bar 60: 'Aast. engrnr., Uganda rlyw' ~ 'Superintendent'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `hyatt_g-o_e1908-2` vs `Hyatt, G. O___Uganda___1913`

- [PASS] surname_gate: bio 'HYATT' vs stint 'Hyatt, G. O' (exact)
- [PASS] initials: bio ['G', 'O'] ~ stint ['G', 'O']
- [PASS] age_gate: stint starts 1913; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1913-1914
- [FAIL] position_sim: best 40 vs bar 60: 'dist. engrnr' ~ 'Superintendent'
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

