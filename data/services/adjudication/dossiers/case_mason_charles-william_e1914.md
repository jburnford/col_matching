<!-- {"case_id": "case_mason_charles-william_e1914", "bio_ids": ["mason_charles-william_e1914", "mason_charles-william_e1914-2"], "stint_ids": ["Mason, C. W___Nyasaland___1915"]} -->
# Dossier case_mason_charles-william_e1914

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 69 official(s) with this surname in the graph's staff lists; 25 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Mason, C. W___Nyasaland___1915'] have more than one claimant biography in this case.
- Phase 1 found `mason_charles-william_e1914` ↔ `Mason, C. W___Nyasaland___1915` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- Phase 1 found `mason_charles-william_e1914-2` ↔ `Mason, C. W___Nyasaland___1915` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).

## Biography `mason_charles-william_e1914`

- Printed name: **MASON, CHARLES WILLIAM**
- Birth year: not printed
- Appears in editions: [1915, 1917, 1919]

### Verbatim printed entry text (OCR)

**Version `col1915-L49009.v` — printed in editions [1915, 1917, 1919]:**

> MASON, CHARLES WILLIAM.—Govt. entomologist, Nyasaland Prot., Aug., 1914.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914 | Govt. entomologist | Nyasaland | [1915, 1917, 1919] |

## Biography `mason_charles-william_e1914-2`

- Printed name: **MASON, Charles William**
- Birth year: not printed
- Appears in editions: [1918]

### Verbatim printed entry text (OCR)

**Version `col1918-L52655.v` — printed in editions [1918]:**

> MASON, Charles William.—Govt. entomologist, Nyasaland Prot., Aug., 1914.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914 | Govt. entomologist | Nyasaland | [1918] |

## Candidate stint `Mason, C. W___Nyasaland___1915`

- Staff-list name: **Mason, C. W** | colony: **Nyasaland** | listed 1915–1918 | editions [1915, 1917, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1915 | C. W. Mason | Entomologist | Entomological Division | — | — |
| 1917 | C. W. Mason | Entomologist | Entomological Division | — | — |
| 1918 | C. W. Mason | Entomologist | Agricultural Department | — | — |

### Deterministic checks: `mason_charles-william_e1914` vs `Mason, C. W___Nyasaland___1915`

- [PASS] surname_gate: bio 'MASON' vs stint 'Mason, C. W' (exact)
- [PASS] initials: bio ['C', 'W'] ~ stint ['C', 'W']
- [PASS] age_gate: stint starts 1915; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Nyasaland'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1915-1918
- [PASS] position_sim: best 100 vs bar 60: 'Govt. entomologist' ~ 'Entomologist'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 2 agreeing edition-year(s) [1915, 1917] pos~100 (bar: >=2)
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `mason_charles-william_e1914-2` vs `Mason, C. W___Nyasaland___1915`

- [PASS] surname_gate: bio 'MASON' vs stint 'Mason, C. W' (exact)
- [PASS] initials: bio ['C', 'W'] ~ stint ['C', 'W']
- [PASS] age_gate: stint starts 1915; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Nyasaland'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1915-1918
- [PASS] position_sim: best 100 vs bar 60: 'Govt. entomologist' ~ 'Entomologist'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): 1 agreeing edition-year(s) [1918] pos~100 (bar: >=2)
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

