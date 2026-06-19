<!-- {"case_id": "case_macfat_p-d_e1913", "bio_ids": ["macfat_p-d_e1913", "macfeat_p-d_e1913", "macfrat_p-d_e1913"], "stint_ids": ["Macfeat, P. D___Kenya___1915"]} -->
# Dossier case_macfat_p-d_e1913

## Case context

- 3 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Macfeat, P. D___Kenya___1915'] have more than one claimant biography in this case.

## Biography `macfat_p-d_e1913`

- Printed name: **MACFAT, P. D**
- Birth year: not printed
- Appears in editions: [1919]

### Verbatim printed entry text (OCR)

**Version `col1919-L54129.v` — printed in editions [1919]:**

> MACFAT, P. D.—Exec. engnr., P.W.D., E.A.P., Oct., 1913.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1913 | Exec. engnr., P.W.D. | East Africa Protectorate | [1919] |

## Biography `macfeat_p-d_e1913`

- Printed name: **MACFEAT, P. D**
- Birth year: not printed
- Appears in editions: [1918, 1920, 1921, 1922, 1924, 1925, 1927]

### Verbatim printed entry text (OCR)

**Version `col1918-L52433.v` — printed in editions [1918, 1920, 1921, 1922, 1924, 1925, 1927]:**

> MACFEAT, P. D.—Exec. engrnr., P.W.D., E.A.P., Oct., 1913.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1913 | Exec. engrnr., P.W.D. | East Africa Protectorate | [1918, 1920, 1921, 1922, 1924, 1925, 1927] |

## Biography `macfrat_p-d_e1913`

- Printed name: **MACFRAT, P. D**
- Birth year: not printed
- Appears in editions: [1923]

### Verbatim printed entry text (OCR)

**Version `col1923-L56317.v` — printed in editions [1923]:**

> MACFRAT, P. D.—Exec. engrnr., P.W.D., E.A.P., Oct., 1913.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1913 | Exec. engrnr., P.W.D. | East Africa Protectorate | [1923] |

## Candidate stint `Macfeat, P. D___Kenya___1915`

- Staff-list name: **Macfeat, P. D** | colony: **Kenya** | listed 1915–1917 | editions [1915, 1917]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1915 | P. D. Macfeat | Assistant Engineer | Public Works | — | — |
| 1917 | P. D. Macfeat | Assistant Engineer | Public Works | — | — |

### Deterministic checks: `macfat_p-d_e1913` vs `Macfeat, P. D___Kenya___1915`

- [PASS] surname_gate: bio 'MACFAT' vs stint 'Macfeat, P. D' (fuzzy:1)
- [PASS] initials: bio ['P', 'D'] ~ stint ['P', 'D']
- [PASS] age_gate: stint starts 1915; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1915-1917
- [FAIL] position_sim: best 38 vs bar 60: 'Exec. engnr., P.W.D.' ~ 'Assistant Engineer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `macfeat_p-d_e1913` vs `Macfeat, P. D___Kenya___1915`

- [PASS] surname_gate: bio 'MACFEAT' vs stint 'Macfeat, P. D' (exact)
- [PASS] initials: bio ['P', 'D'] ~ stint ['P', 'D']
- [PASS] age_gate: stint starts 1915; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1915-1917
- [FAIL] position_sim: best 36 vs bar 60: 'Exec. engrnr., P.W.D.' ~ 'Assistant Engineer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `macfrat_p-d_e1913` vs `Macfeat, P. D___Kenya___1915`

- [PASS] surname_gate: bio 'MACFRAT' vs stint 'Macfeat, P. D' (fuzzy:1)
- [PASS] initials: bio ['P', 'D'] ~ stint ['P', 'D']
- [PASS] age_gate: stint starts 1915; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1915-1917
- [FAIL] position_sim: best 36 vs bar 60: 'Exec. engrnr., P.W.D.' ~ 'Assistant Engineer'
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

