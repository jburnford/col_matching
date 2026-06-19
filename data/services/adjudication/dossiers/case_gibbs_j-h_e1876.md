<!-- {"case_id": "case_gibbs_j-h_e1876", "bio_ids": ["gibbs_j-h_e1876", "gibbs_j-hatch_e1879"], "stint_ids": ["Gibbs, J. H___Victoria___1878"]} -->
# Dossier case_gibbs_j-h_e1876

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 31 official(s) with this surname in the graph's staff lists; 14 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Gibbs, J. H___Victoria___1878'] have more than one claimant biography in this case.
- Phase 1 found `gibbs_j-h_e1876` ↔ `Gibbs, J. H___Victoria___1878` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- Phase 1 found `gibbs_j-hatch_e1879` ↔ `Gibbs, J. H___Victoria___1878` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).

## Biography `gibbs_j-h_e1876`

- Printed name: **GIBBS, J. H**
- Birth year: not printed
- Appears in editions: [1886]

### Verbatim printed entry text (OCR)

**Version `col1886-L33665.v` — printed in editions [1886]:**

> GIBBS, J. H.—Comptroller of stamps, Victoria, 1 Jan., 1876.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1876 | Comptroller of stamps | Victoria | [1886] |

## Biography `gibbs_j-hatch_e1879`

- Printed name: **GIBBS, J. HATCH**
- Birth year: not printed
- Appears in editions: [1888]

### Verbatim printed entry text (OCR)

**Version `col1888-L33601.v` — printed in editions [1888]:**

> GIBBS, J. HATCH.—Barrister-at-law, comptroller of stamps, Victoria, Dec., 1879.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1879 | Barrister-at-law, comptroller of stamps | Victoria | [1888] |

## Candidate stint `Gibbs, J. H___Victoria___1878`

- Staff-list name: **Gibbs, J. H** | colony: **Victoria** | listed 1878–1883 | editions [1878, 1880, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1878 | J. H. Gibbs | Accountant and Inspector of Stamps | Postmaster General's Division | — | — |
| 1880 | J. H. Gibbs | Accountant and Inspector of Stamps | Postmaster General's Division | — | — |
| 1883 | J. H. Gibbs | Accountant and Comptroller of Stamps | Postmaster General's Division | — | — |

### Deterministic checks: `gibbs_j-h_e1876` vs `Gibbs, J. H___Victoria___1878`

- [PASS] surname_gate: bio 'GIBBS' vs stint 'Gibbs, J. H' (exact)
- [PASS] initials: bio ['J', 'H'] ~ stint ['J', 'H']
- [PASS] age_gate: stint starts 1878; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Victoria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1878-1883
- [PASS] position_sim: best 100 vs bar 60: 'Comptroller of stamps' ~ 'Accountant and Comptroller of Stamps'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `gibbs_j-hatch_e1879` vs `Gibbs, J. H___Victoria___1878`

- [PASS] surname_gate: bio 'GIBBS' vs stint 'Gibbs, J. H' (exact)
- [PASS] initials: bio ['J', 'H'] ~ stint ['J', 'H']
- [PASS] age_gate: stint starts 1878; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Victoria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1878-1883
- [PASS] position_sim: best 75 vs bar 60: 'Barrister-at-law, comptroller of stamps' ~ 'Accountant and Comptroller of Stamps'
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

