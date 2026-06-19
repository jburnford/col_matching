<!-- {"case_id": "case_closel_j-a-r_b1922", "bio_ids": ["closel_j-a-r_b1922"], "stint_ids": ["Cloisel, J. A. R___Mauritius___1962", "Clozel, J. A. R___Mauritius___1960"]} -->
# Dossier case_closel_j-a-r_b1922

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- Phase 1 found `closel_j-a-r_b1922` ↔ `Cloisel, J. A. R___Mauritius___1962` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- Phase 1 found `closel_j-a-r_b1922` ↔ `Clozel, J. A. R___Mauritius___1960` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).

## Biography `closel_j-a-r_b1922`

- Printed name: **CLOSEL, J. A. R**
- Birth year: 1922 (attested in editions [1957, 1958, 1959, 1960, 1961, 1963, 1964, 1965])
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]

### Verbatim printed entry text (OCR)

**Version `col1957-L22001.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1963, 1964, 1965]:**

> CLOSEL, J. A. R.—b. 1922; ed. Royal Coll., Maur., and Witwatersrand Univ.; works manager, rlwy., Maur., 1948; general man., 1958.

**Version `col1962-L19811.v` — printed in editions [1962]:**

> CLOSSEL, J. A. R.—b. 1922; ed. Royal Coll., Maur., and Witwatersrand Univ.; wks. man., rwy., Maur., 1948; gen. man., 1958.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1948 | works manager, rlwy. | Mauritius | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 1 | 1958 | general man | Mauritius *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |

## Candidate stint `Cloisel, J. A. R___Mauritius___1962`

- Staff-list name: **Cloisel, J. A. R** | colony: **Mauritius** | listed 1962–1965 | editions [1962, 1964, 1965]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1962 | J. A. R. Cloisel | General Manager, Railways | CIVIL ESTABLISHMENT | — | — |
| 1964 | J. A. R. Cloisel | General Manager, Railways | Seats | — | — |
| 1965 | J. A. R. Cloisel | General Manager, Railways | Civil Establishment | — | — |

### Deterministic checks: `closel_j-a-r_b1922` vs `Cloisel, J. A. R___Mauritius___1962`

- [PASS] surname_gate: bio 'CLOSEL' vs stint 'Cloisel, J. A. R' (fuzzy:1)
- [PASS] initials: bio ['J', 'A', 'R'] ~ stint ['J', 'A', 'R']
- [PASS] age_gate: stint starts 1962, birth 1922 (age 40)
- [PASS] colony: 2 placed event(s) resolve to 'Mauritius'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1962-1965
- [PASS] position_sim: best 78 vs bar 60: 'general man' ~ 'General Manager, Railways'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 3 agreeing edition-year(s) [1962, 1964, 1965] pos~78 (bar: >=2)
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Clozel, J. A. R___Mauritius___1960`

- Staff-list name: **Clozel, J. A. R** | colony: **Mauritius** | listed 1960–1961 | editions [1960, 1961]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1960 | J. A. R. Clozel | General Manager, Railways | Civil Establishment | — | — |
| 1961 | J. A. R. Clozel | General Manager, Railways | Civil Establishment | — | — |

### Deterministic checks: `closel_j-a-r_b1922` vs `Clozel, J. A. R___Mauritius___1960`

- [PASS] surname_gate: bio 'CLOSEL' vs stint 'Clozel, J. A. R' (fuzzy:1)
- [PASS] initials: bio ['J', 'A', 'R'] ~ stint ['J', 'A', 'R']
- [PASS] age_gate: stint starts 1960, birth 1922 (age 38)
- [PASS] colony: 2 placed event(s) resolve to 'Mauritius'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1960-1961
- [PASS] position_sim: best 78 vs bar 60: 'general man' ~ 'General Manager, Railways'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 2 agreeing edition-year(s) [1960, 1961] pos~78 (bar: >=2)
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

