<!-- {"case_id": "case_raffray_j-r_b1903", "bio_ids": ["raffray_j-r_b1903"], "stint_ids": ["Raffray, J. R___Mauritius___1958"]} -->
# Dossier case_raffray_j-r_b1903

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `raffray_j-r_b1903`

- Printed name: **RAFFRAY, J. R**
- Birth year: 1903 (attested in editions [1959, 1960, 1961])
- Appears in editions: [1959, 1960, 1961]

### Verbatim printed entry text (OCR)

**Version `col1959-L27054.v` — printed in editions [1959, 1960, 1961]:**

> RAFFRAY, J. R.—b. 1903; ed. Royal Coll., Maur., and Paris Univ.; mil. serv., 1939–47, major; M.O., Maur., 1947; D.D.M.S., 1957.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947 | M.O. | Mauritius | [1959, 1960, 1961] |
| 1 | 1957 | D.D.M.S | Mauritius *(inherited from previous clause)* | [1959, 1960, 1961] |

## Candidate stint `Raffray, J. R___Mauritius___1958`

- Staff-list name: **Raffray, J. R** | colony: **Mauritius** | listed 1958–1962 | editions [1958, 1959, 1960, 1961, 1962]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1958 | J. R. Raffray | Deputy Directors of Medical Services | Civil Establishment | — | — |
| 1959 | J. R. Raffray | Deputy Director of Medical Services | Civil Establishment | — | — |
| 1960 | J. R. Raffray | Deputy Director of Medical Services | Civil Establishment | — | — |
| 1961 | J. R. Raffray | Deputy Director of Medical Services | Civil Establishment | — | — |
| 1962 | J. R. Raffray | Director of Medical Services | CIVIL ESTABLISHMENT | — | — |

### Deterministic checks: `raffray_j-r_b1903` vs `Raffray, J. R___Mauritius___1958`

- [PASS] surname_gate: bio 'RAFFRAY' vs stint 'Raffray, J. R' (exact)
- [PASS] initials: bio ['J', 'R'] ~ stint ['J', 'R']
- [PASS] age_gate: stint starts 1958, birth 1903 (age 55)
- [PASS] colony: 2 placed event(s) resolve to 'Mauritius'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1958-1962
- [FAIL] position_sim: best 21 vs bar 60: 'D.D.M.S' ~ 'Deputy Director of Medical Services'
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

