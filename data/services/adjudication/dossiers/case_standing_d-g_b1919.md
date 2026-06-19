<!-- {"case_id": "case_standing_d-g_b1919", "bio_ids": ["standing_d-g_b1919"], "stint_ids": ["Standing, D. G___Bechuanaland___1965"]} -->
# Dossier case_standing_d-g_b1919

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `standing_d-g_b1919`

- Printed name: **STANDING, D. G**
- Birth year: 1919 (attested in editions [1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1961-L27608.v` — printed in editions [1961, 1962, 1963, 1964, 1965, 1966]:**

> STANDING, D. G.—b. 1919; ed. Michaelhouse, Natal, St. Andrews Univ., and Cape Town Univ.; mil. serv., 1945-46, S.A.M.C.; M.O., Basuto., 1951; senr. M.O., Bech. Prot., 1961; D.O.M.S., 1964.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1951 | M.O. | Basutoland | [1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1961 | senr. M.O. | Bechuanaland | [1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1964 | D.O.M.S | Bechuanaland *(inherited from previous clause)* | [1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Standing, D. G___Bechuanaland___1965`

- Staff-list name: **Standing, D. G** | colony: **Bechuanaland** | listed 1965–1966 | editions [1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1965 | D. G. Standing | Director of Medical Services | Secretariat | — | — |
| 1966 | D. G. Standing | Director of Medical Services | Secretariat | — | — |

### Deterministic checks: `standing_d-g_b1919` vs `Standing, D. G___Bechuanaland___1965`

- [PASS] surname_gate: bio 'STANDING' vs stint 'Standing, D. G' (exact)
- [PASS] initials: bio ['D', 'G'] ~ stint ['D', 'G']
- [PASS] age_gate: stint starts 1965, birth 1919 (age 46)
- [PASS] colony: 2 placed event(s) resolve to 'Bechuanaland'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1965-1966
- [FAIL] position_sim: best 34 vs bar 60: 'senr. M.O.' ~ 'Director of Medical Services'
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

