<!-- {"case_id": "case_ballard_r_e1878-2", "bio_ids": ["ballard_r_e1878-2"], "stint_ids": ["Ballard, R. H___Falkland Islands___1929", "Ballard, Robert___Queensland___1878"]} -->
# Dossier case_ballard_r_e1878-2

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['ballard_r_e1878-2'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Ballard, R. H___Falkland Islands___1929` is also gate-compatible with biography(ies) outside this case: ['ballard_r_e1878'] (already linked elsewhere or filtered).
- Phase 1 found `ballard_r_e1878-2` ↔ `Ballard, Robert___Queensland___1878` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Ballard, Robert___Queensland___1878` is also gate-compatible with biography(ies) outside this case: ['ballard_r_e1878'] (already linked elsewhere or filtered).

## Biography `ballard_r_e1878-2`

- Printed name: **BALLARD, R**
- Birth year: not printed
- Appears in editions: [1898]

### Verbatim printed entry text (OCR)

**Version `col1898-L32053.v` — printed in editions [1898]:**

> BALLARD, R.—Ch. engur. of Cent. and N. Rlys., Queensland, 1878.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1878 | Ch. engur. of Cent. and N. Rlys. | Queensland | [1898] |

## Candidate stint `Ballard, R. H___Falkland Islands___1929`

- Staff-list name: **Ballard, R. H** | colony: **Falkland Islands** | listed 1929–1930 | editions [1929, 1930]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | R. H. Ballard | Blacksmith and Motor Mechanic | Public Works | — | — |
| 1930 | R. H. Ballard | Blacksmith and Motor Mechanic | Public Works | — | — |

### Deterministic checks: `ballard_r_e1878-2` vs `Ballard, R. H___Falkland Islands___1929`

- [PASS] surname_gate: bio 'BALLARD' vs stint 'Ballard, R. H' (exact)
- [PASS] initials: bio ['R'] ~ stint ['R', 'H']
- [PASS] age_gate: stint starts 1929; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Falkland Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1929-1930
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Ballard, Robert___Queensland___1878`

- Staff-list name: **Ballard, Robert** | colony: **Queensland** | listed 1878–1886 | editions [1878, 1879, 1880, 1883, 1886]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1878 | Robert Ballard | Chief Engineer, Northern Railway | Department of Public Works | — | — |
| 1879 | Robert Ballard | Chief Engineer, Northern Railway | Department of Public Works | — | — |
| 1880 | Robert Ballard | Chief Engineer, Northern Railway | Department of Public Works | — | — |
| 1883 | Robert Ballard | Chief Engineer, Northern Railway | Department of Public Works | — | — |
| 1886 | Robert Ballard | Chief Engineer, Central and Northern Railway | Department of Public Works | — | — |

### Deterministic checks: `ballard_r_e1878-2` vs `Ballard, Robert___Queensland___1878`

- [PASS] surname_gate: bio 'BALLARD' vs stint 'Ballard, Robert' (exact)
- [PASS] initials: bio ['R'] ~ stint ['R']
- [PASS] age_gate: stint starts 1878; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Queensland'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1878-1886
- [PASS] position_sim: best 66 vs bar 60: 'Ch. engur. of Cent. and N. Rlys.' ~ 'Chief Engineer, Central and Northern Railway'
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

