<!-- {"case_id": "case_whiteman_g-j-d_b1917", "bio_ids": ["whiteman_g-j-d_b1917"], "stint_ids": ["Whiteman, G. J. D___Gold Coast___1949"]} -->
# Dossier case_whiteman_g-j-d_b1917

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `whiteman_g-j-d_b1917`

- Printed name: **WHITEMAN, G. J. D**
- Birth year: 1917 (attested in editions [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1959-L29219.v` — printed in editions [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> WHITEMAN, G. J. D.—b. 1917; ed. Luton Gram. Sch. and Tech. Coll.; mil. serv., 1941-46, capt., R.E.M.E.; area mech. engrn., G.C., 1948; engrn., (mech.) Ken., 1952; dep. chief mech. engrn., 1953; chief mech. engrn., Uga., 1958. (Uga. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1948 | area mech. engrn. | Gold Coast | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1952 | engrn., (mech.) Ken | Gold Coast *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1953 | dep. chief mech. engrn | Gold Coast *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1958 | chief mech. engrn. | Uganda | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Whiteman, G. J. D___Gold Coast___1949`

- Staff-list name: **Whiteman, G. J. D** | colony: **Gold Coast** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | G. J. D. Whiteman | Mechanical Engineers | Public Works | — | — |
| 1951 | G. J. D. Whiteman | Mechanical Engineers | Mechanical Branch | — | — |

### Deterministic checks: `whiteman_g-j-d_b1917` vs `Whiteman, G. J. D___Gold Coast___1949`

- [PASS] surname_gate: bio 'WHITEMAN' vs stint 'Whiteman, G. J. D' (exact)
- [PASS] initials: bio ['G', 'J', 'D'] ~ stint ['G', 'J', 'D']
- [PASS] age_gate: stint starts 1949, birth 1917 (age 32)
- [PASS] colony: 3 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 59 vs bar 60: 'engrn., (mech.) Ken' ~ 'Mechanical Engineers'
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

