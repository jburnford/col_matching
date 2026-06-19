<!-- {"case_id": "case_selander_john-kinar_b1873", "bio_ids": ["selander_john-kinar_b1873"], "stint_ids": ["Selander, J___Tanganyika___1922"]} -->
# Dossier case_selander_john-kinar_b1873

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `selander_john-kinar_b1873`

- Printed name: **SELANDER, JOHN KINAR**
- Birth year: 1873 (attested in editions [1924, 1925, 1927])
- Honours: M.I.C.E
- Appears in editions: [1924, 1925, 1927]

### Verbatim printed entry text (OCR)

**Version `col1924-L57816.v` — printed in editions [1924, 1925, 1927]:**

> SELANDER, JOHN KINAR, M.I.C.E.—B. 1873; rly. surveys and constrn., Cape Colony, 1896-1908; Nigerian rly., 1908-1920; exec. engr., P.W.D., N. Nigeria; served in Boer War and European War; temp. major, R.E.; ment. in desps.; dir., pub. wks., Tanganyika Territory, 1920.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1896–1908 | rly. surveys and constrn. | Cape of Good Hope | [1924, 1925, 1927] |
| 1 | 1908–1920 | Nigerian rly | Cape of Good Hope *(inherited from previous clause)* | [1924, 1925, 1927] |
| 2 | 1920 | dir., pub. wks., Tanganyika Territory | Tanganyika | [1924, 1925, 1927] |

## Candidate stint `Selander, J___Tanganyika___1922`

- Staff-list name: **Selander, J** | colony: **Tanganyika** | listed 1922–1925 | editions [1922, 1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | J. Selander | Director of Public Works | Public Works Department | — | — |
| 1923 | J. Selander | Director of Public Works | Public Works Department | — | — |
| 1924 | J. Selander | Director of Public Works | Public Works Department | — | — |
| 1925 | J. Selander | Director of Public Works | Public Works Department | — | — |

### Deterministic checks: `selander_john-kinar_b1873` vs `Selander, J___Tanganyika___1922`

- [PASS] surname_gate: bio 'SELANDER' vs stint 'Selander, J' (exact)
- [PASS] initials: bio ['J', 'K'] ~ stint ['J']
- [PASS] age_gate: stint starts 1922, birth 1873 (age 49)
- [PASS] colony: 1 placed event(s) resolve to 'Tanganyika'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1922-1925
- [FAIL] position_sim: best 46 vs bar 60: 'dir., pub. wks., Tanganyika Territory' ~ 'Director of Public Works'
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

