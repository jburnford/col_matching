<!-- {"case_id": "case_bent_t_e1881", "bio_ids": ["bent_t_e1881", "bent_thomas_e1881"], "stint_ids": ["Bent, Thomas___Victoria___1906"]} -->
# Dossier case_bent_t_e1881

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['bent_t_e1881', 'bent_thomas_e1881'] carry a single initial only — the namesake trap applies.
- CONTESTED: stint(s) ['Bent, Thomas___Victoria___1906'] have more than one claimant biography in this case.
- NOTE: stint `Bent, Thomas___Victoria___1906` is also gate-compatible with biography(ies) outside this case: ['bent_thomas_e1873'] (already linked elsewhere or filtered).
- NOTE: stint `Bent, Thomas___Victoria___1906` is also gate-compatible with biography(ies) outside this case: ['bent_thomas_e1873'] (already linked elsewhere or filtered).

## Biography `bent_t_e1881`

- Printed name: **BENT, T**
- Birth year: not printed
- Appears in editions: [1886, 1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1886-L32139.v` — printed in editions [1886, 1888, 1889, 1890]:**

> BENT, Hon. T.—Commissioner of railways, Victoria, 9th July, 1881; also vice-president of board of land and works.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1881 | Commissioner of railways | Victoria | [1886, 1888, 1889, 1890] |

## Biography `bent_thomas_e1881`

- Printed name: **BENT, THOMAS**
- Birth year: not printed
- Appears in editions: [1894, 1896, 1897, 1899]

### Verbatim printed entry text (OCR)

**Version `col1894-L30300.v` — printed in editions [1894, 1896, 1897, 1899]:**

> BENT, THE HON. THOMAS.—Commissioner of railways, Victoria, 9th July, 1881; also vice-president of board of land and works; afterwards speaker of legislative assembly.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1881 | Commissioner of railways | Victoria | [1894, 1896, 1897, 1899] |

## Candidate stint `Bent, Thomas___Victoria___1906`

- Staff-list name: **Bent, Thomas** | colony: **Victoria** | listed 1906–1908 | editions [1906, 1907, 1908]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1906 | The Hon. T. Bent | Treasurer | Treasurer | — | — |
| 1907 | T. Bent | Treasurer | Treasurer | — | — |
| 1907 | T. Bent | Minister of Railways | Victorian Railways | — | — |
| 1908 | T. Bent | Minister of Railways | Victorian Railways | — | — |
| 1908 | The Hon. T. Bent | Treasurer | Department of Treasurer | — | — |

### Deterministic checks: `bent_t_e1881` vs `Bent, Thomas___Victoria___1906`

- [PASS] surname_gate: bio 'BENT' vs stint 'Bent, Thomas' (exact)
- [PASS] initials: bio ['T'] ~ stint ['T']
- [PASS] age_gate: stint starts 1906; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Victoria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1906-1908
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `bent_thomas_e1881` vs `Bent, Thomas___Victoria___1906`

- [PASS] surname_gate: bio 'BENT' vs stint 'Bent, Thomas' (exact)
- [PASS] initials: bio ['T'] ~ stint ['T']
- [PASS] age_gate: stint starts 1906; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Victoria'
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

