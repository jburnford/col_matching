<!-- {"case_id": "case_casperson_bernard-vincent_b1867", "bio_ids": ["casperson_bernard-vincent_b1867"], "stint_ids": ["Caspersz, B. V___Ceylon___1919"]} -->
# Dossier case_casperson_bernard-vincent_b1867

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Caspersz, B. V___Ceylon___1919` is also gate-compatible with biography(ies) outside this case: ['caspersz_bernardin-vincent_b1867'] (already linked elsewhere or filtered).

## Biography `casperson_bernard-vincent_b1867`

- Printed name: **CASPERSON, BERNARD VINCENT**
- Birth year: 1867 (attested in editions [1923])
- Appears in editions: [1923]

### Verbatim printed entry text (OCR)

**Version `col1923-L53121.v` — printed in editions [1923]:**

> CASPERSON, BERNARD VINCENT.—B. 1867; ch. clk., col. sec.'s office, Ceylon, Oct., 1914; apptd. to cls. V. of civ. serv., local divn., July, 1919; office assist. to col. sec., Jan., 1921.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914 | ch. clk., col. sec.'s office | Ceylon | [1923] |
| 1 | 1919 | apptd. to cls. V. of civ. serv., local divn | Ceylon *(inherited from previous clause)* | [1923] |
| 2 | 1921 | office assist. to col. sec | Ceylon *(inherited from previous clause)* | [1923] |

## Candidate stint `Caspersz, B. V___Ceylon___1919`

- Staff-list name: **Caspersz, B. V** | colony: **Ceylon** | listed 1919–1922 | editions [1919, 1920, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1919 | B. V. Caspersz | Chief Clerk | Civil Establishment | — | — |
| 1920 | B. V. Caspersz | Chief Clerk | Civil Establishment | — | — |
| 1922 | B. V. Caspersz | Office Assistants | Civil Establishment | — | — |

### Deterministic checks: `casperson_bernard-vincent_b1867` vs `Caspersz, B. V___Ceylon___1919`

- [PASS] surname_gate: bio 'CASPERSON' vs stint 'Caspersz, B. V' (fuzzy:2)
- [PASS] initials: bio ['B', 'V'] ~ stint ['B', 'V']
- [PASS] age_gate: stint starts 1919, birth 1867 (age 52)
- [PASS] colony: 3 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1919-1922
- [PASS] position_sim: best 68 vs bar 60: 'office assist. to col. sec' ~ 'Office Assistants'
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

