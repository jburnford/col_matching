<!-- {"case_id": "case_burkill_martin_b1868", "bio_ids": ["burkill_martin_b1868"], "stint_ids": ["Burkill, H. M___Singapore___1958"]} -->
# Dossier case_burkill_martin_b1868

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['burkill_martin_b1868'] carry a single initial only — the namesake trap applies.

## Biography `burkill_martin_b1868`

- Printed name: **BURKILL, Martin**
- Birth year: 1868 (attested in editions [1931])
- Appears in editions: [1931]

### Verbatim printed entry text (OCR)

**Version `col1931-L62943.v` — printed in editions [1931]:**

> BURKILL, Hon. Martin.—B. 1868; ed. St. John's Coll., Hurstpierpoint; fruit farmer in Niagara Peninsula fourteen years; moved to B. Columbia, 1900; apptd. mem. bd. of horticulture, B. Columbia; editor, Grand Forks Gazette; mayor, Grand Forks, 1903; fruit comsmd. and lecturer in England for B.C. Govt., 1907-08; elected to H. of C., Canada, for Yale-Cariboo, 1908; re-elected, 1911 and 1917; mem. of the Privy Council for Canada and min. of agric. in Mr. Borden's cabinet, Oct., 1911; sec. of state and min. of mines, Oct., 1917; joint libr. of parlmt., July, 1920.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1900–1900 | — | British Columbia | [1931] |
| 1 | 1903–1903 | mayor | — | [1931] |
| 2 | 1907–1908 | fruit comsmd. and lecturer | British Columbia | [1931] |
| 3 | 1908–1908 | elected to H. of C. | Canada | [1931] |
| 4 | 1911–1917 | re-elected | — | [1931] |
| 5 | 1911–1911 | mem. of the Privy Council and min. of agric. | Canada | [1931] |
| 6 | 1917–1917 | sec. of state and min. of mines | — | [1931] |
| 7 | 1920–1920 | joint libr. of parlmt. | — | [1931] |

## Candidate stint `Burkill, H. M___Singapore___1958`

- Staff-list name: **Burkill, H. M** | colony: **Singapore** | listed 1958–1963 | editions [1958, 1959, 1960, 1963]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1958 | H. M. Burkill | Director of Botanic Gardens | Civil Establishment | — | — |
| 1959 | H. M. Burkill | Director of Botanic Gardens | Civil Establishment | — | — |
| 1960 | H. M. Burkill | Director of Botanic Gardens | Ministry of National Development | — | — |
| 1963 | H. M. Burkill | Director of Botanic Gardens | MINISTRY OF NATIONAL DEVELOPMENT | — | — |

### Deterministic checks: `burkill_martin_b1868` vs `Burkill, H. M___Singapore___1958`

- [PASS] surname_gate: bio 'BURKILL' vs stint 'Burkill, H. M' (exact)
- [PASS] initials: bio ['M'] ~ stint ['H', 'M']
- [PASS] age_gate: stint starts 1958, birth 1868 (age 90)
- [FAIL] colony: no placed event resolves to 'Singapore'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1958-1963
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

