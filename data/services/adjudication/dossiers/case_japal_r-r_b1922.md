<!-- {"case_id": "case_japal_r-r_b1922", "bio_ids": ["japal_r-r_b1922"], "stint_ids": ["Japal, R. R___St Lucia___1964"]} -->
# Dossier case_japal_r-r_b1922

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `japal_r-r_b1922`

- Printed name: **JAPAL, R. R**
- Birth year: 1922 (attested in editions [1963, 1964, 1965, 1966])
- Appears in editions: [1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1963-L21327.v` — printed in editions [1963, 1964, 1965, 1966]:**

> JAPAL, R. R.—b. 1922; ed. Gren. Boys' Sec. Sch., McGill Univ., B'ham Univ. and St. George's Hosp. Med. Sch.; Royal Inst. Publ. Health & Hyg.; M.O., Windward Is., 1952; S.M.O., St. V., 1962; C.M.O., St. L., 1964.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1952 | M.O., Windward Is | — | [1963, 1964, 1965, 1966] |
| 1 | 1962 | S.M.O. | St. Vincent | [1963, 1964, 1965, 1966] |
| 2 | 1964 | C.M.O. | St. Lucia | [1963, 1964, 1965, 1966] |

## Candidate stint `Japal, R. R___St Lucia___1964`

- Staff-list name: **Japal, R. R** | colony: **St Lucia** | listed 1964–1965 | editions [1964, 1965]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1964 | R. R. Japal | Chief Medical Officer | Civil Establishment | — | — |
| 1965 | R. R. Japal | Chief Medical Officer | Civil Establishment | — | — |

### Deterministic checks: `japal_r-r_b1922` vs `Japal, R. R___St Lucia___1964`

- [PASS] surname_gate: bio 'JAPAL' vs stint 'Japal, R. R' (exact)
- [PASS] initials: bio ['R', 'R'] ~ stint ['R', 'R']
- [PASS] age_gate: stint starts 1964, birth 1922 (age 42)
- [PASS] colony: 1 placed event(s) resolve to 'St Lucia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1964-1965
- [FAIL] position_sim: best 25 vs bar 60: 'C.M.O.' ~ 'Chief Medical Officer'
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

