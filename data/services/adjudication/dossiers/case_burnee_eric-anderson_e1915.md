<!-- {"case_id": "case_burnee_eric-anderson_e1915", "bio_ids": ["burnee_eric-anderson_e1915"], "stint_ids": ["Burner, E. A___Gold Coast___1927", "Burner, E. A___Gold Coast___1934", "Burnet, Amos___Transvaal___1906"]} -->
# Dossier case_burnee_eric-anderson_e1915

## Case context

- 1 biography(ies) and 3 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Burner, E. A___Gold Coast___1927` is also gate-compatible with biography(ies) outside this case: ['burner_eric-anderson_e1915'] (already linked elsewhere or filtered).
- NOTE: stint `Burner, E. A___Gold Coast___1934` is also gate-compatible with biography(ies) outside this case: ['burner_eric-anderson_e1915'] (already linked elsewhere or filtered).

## Biography `burnee_eric-anderson_e1915`

- Printed name: **BURNEE, ERIC ANDERSON**
- Birth year: not printed
- Appears in editions: [1933]

### Verbatim printed entry text (OCR)

**Version `col1933-L58358.v` — printed in editions [1933]:**

> BURNEE, ERIC ANDERSON.—Ed. at Felsted Schl.; command., R.F.A., France, Belgium and Germany, 1915-18; asst. dist. comsnr., Gold Coast, 1920; dist. comsnr., 1924.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915–1918 | command., R.F.A., France, Belgium and Germany | — | [1933] |
| 1 | 1920 | asst. dist. comsnr. | Gold Coast | [1933] |
| 2 | 1924 | dist. comsnr | Gold Coast *(inherited from previous clause)* | [1933] |

## Candidate stint `Burner, E. A___Gold Coast___1927`

- Staff-list name: **Burner, E. A** | colony: **Gold Coast** | listed 1927–1929 | editions [1927, 1929]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | E. A. Burner | District Commissioner | Administrative and Political Service | — | — |
| 1929 | E. A. Burner | District Commissioner / Assistant District Commissioner | Administrative and Political Service | — | — |

### Deterministic checks: `burnee_eric-anderson_e1915` vs `Burner, E. A___Gold Coast___1927`

- [PASS] surname_gate: bio 'BURNEE' vs stint 'Burner, E. A' (fuzzy:1)
- [PASS] initials: bio ['E', 'A'] ~ stint ['E', 'A']
- [PASS] age_gate: stint starts 1927; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1927-1929
- [PASS] position_sim: best 69 vs bar 60: 'dist. comsnr' ~ 'District Commissioner'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Burner, E. A___Gold Coast___1934`

- Staff-list name: **Burner, E. A** | colony: **Gold Coast** | listed 1934–1936 | editions [1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | E. A. Burner | District Commissioner / Assistant District Commissioner | Administrative and Political Service | — | — |
| 1936 | E. A. Burner | District Commissioner | Civil Establishment | — | — |

### Deterministic checks: `burnee_eric-anderson_e1915` vs `Burner, E. A___Gold Coast___1934`

- [PASS] surname_gate: bio 'BURNEE' vs stint 'Burner, E. A' (fuzzy:1)
- [PASS] initials: bio ['E', 'A'] ~ stint ['E', 'A']
- [PASS] age_gate: stint starts 1934; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1934-1936
- [PASS] position_sim: best 69 vs bar 60: 'dist. comsnr' ~ 'District Commissioner'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Burnet, Amos___Transvaal___1906`

- Staff-list name: **Burnet, Amos** | colony: **Transvaal** | listed 1906–1908 | editions [1906, 1907, 1908]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1906 | Amos Burnet | President Wesleyan-Methodist Conference | Ecclesiastical | — | — |
| 1907 | Amos Burnet | President Wesleyan-Methodist Conference | Ecclesiastical | — | — |
| 1908 | Amos Burnet | President Wesleyan-Methodist Conference | Ecclesiastical | — | — |

### Deterministic checks: `burnee_eric-anderson_e1915` vs `Burnet, Amos___Transvaal___1906`

- [PASS] surname_gate: bio 'BURNEE' vs stint 'Burnet, Amos' (fuzzy:1)
- [PASS] initials: bio ['E', 'A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1906; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Transvaal'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1906-1908
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

