<!-- {"case_id": "case_manssel_william-du-pre_e1895", "bio_ids": ["manssel_william-du-pre_e1895"], "stint_ids": ["Mansel, William Du Pre___Basutoland___1897", "Mansel___Canada___1889"]} -->
# Dossier case_manssel_william-du-pre_e1895

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- Phase 1 found `manssel_william-du-pre_e1895` ↔ `Mansel, William Du Pre___Basutoland___1897` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Mansel, William Du Pre___Basutoland___1897` is also gate-compatible with biography(ies) outside this case: ['mansel_william-du-pre_e1893'] (already linked elsewhere or filtered).
- NOTE: stint `Mansel___Canada___1889` is also gate-compatible with biography(ies) outside this case: ['mansel_george_e1873', 'mansel_george_e1883', 'mansel_william-du-pre_e1893'] (already linked elsewhere or filtered).

## Biography `manssel_william-du-pre_e1895`

- Printed name: **MANSSEL, WILLIAM DU PRE**
- Birth year: not printed
- Appears in editions: [1917]

### Verbatim printed entry text (OCR)

**Version `col1917-L51636.v` — printed in editions [1917]:**

> MANSSEL, WILLIAM DU PRE.—Sub-inspr., Basutoland mounted police, 1895; ass't comanr., 1905.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1895 | Sub-inspr., Basutoland mounted police | Basutoland | [1917] |
| 1 | 1905 | ass't comanr | Basutoland *(inherited from previous clause)* | [1917] |

## Candidate stint `Mansel, William Du Pre___Basutoland___1897`

- Staff-list name: **Mansel, William Du Pre** | colony: **Basutoland** | listed 1897–1911 | editions [1897, 1898, 1899, 1900, 1905, 1906, 1907, 1909, 1910, 1911]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1897 | W. D. P. Mansel | Sub-Inspector of Police | Establishment | — | — |
| 1898 | W. D. P. Mansel | Sub-Inspector of Police | Establishment | — | — |
| 1899 | W. D. P. Mansel | Sub-Inspector of Police | Establishment | — | — |
| 1900 | W. D. Mansel | Sub-Inspector of Police | Establishment | — | — |
| 1905 | W. D. P. Mansel | Inspector of Police | Establishment | — | — |
| 1906 | W. Du Pre Mansel | Assistant Commissioner | Civil Establishment | — | — |
| 1907 | W. Du Pre Mansel | Assistant Commissioner | Establishment | — | — |
| 1909 | William Du Pre Mansel | Assistant Commissioner | Establishment | — | — |
| 1910 | William Du Pre Mansel | Assistant Commissioner | Civil Establishment | — | — |
| 1911 | William Du Pre Mansel | Assistant Commissioner | Establishment | — | — |

### Deterministic checks: `manssel_william-du-pre_e1895` vs `Mansel, William Du Pre___Basutoland___1897`

- [PASS] surname_gate: bio 'MANSSEL' vs stint 'Mansel, William Du Pre' (fuzzy:1)
- [PASS] initials: bio ['W', 'D', 'P'] ~ stint ['W', 'D', 'P']
- [PASS] age_gate: stint starts 1897; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Basutoland'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1897-1911
- [PASS] position_sim: best 61 vs bar 60: 'Sub-inspr., Basutoland mounted police' ~ 'Sub-Inspector of Police'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Mansel___Canada___1889`

- Staff-list name: **Mansel** | colony: **Canada** | listed 1889–1890 | editions [1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1889 | Mansel | Assist. Military Secretary | Imperial Military Establishment | — | Major |
| 1890 | Mansel | Assist. Military Secretary | Imperial Military Establishment | — | Major |

### Deterministic checks: `manssel_william-du-pre_e1895` vs `Mansel___Canada___1889`

- [PASS] surname_gate: bio 'MANSSEL' vs stint 'Mansel' (fuzzy:1)
- [PASS] initials: bio ['W', 'D', 'P'] ~ stint ['?']
- [PASS] age_gate: stint starts 1889; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1889-1890
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

