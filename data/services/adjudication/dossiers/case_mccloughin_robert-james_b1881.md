<!-- {"case_id": "case_mccloughin_robert-james_b1881", "bio_ids": ["mccloughin_robert-james_b1881"], "stint_ids": ["McLoughlin, R. J___Gold Coast___1910"]} -->
# Dossier case_mccloughin_robert-james_b1881

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mccloughin_robert-james_b1881`

- Printed name: **McCLOUGHIN, ROBERT JAMES**
- Birth year: 1881 (attested in editions [1913, 1919, 1923])
- Appears in editions: [1913, 1917, 1919, 1920, 1923]

### Verbatim printed entry text (OCR)

**Version `col1913-L47708.v` — printed in editions [1913, 1919, 1923]:**

> McCLOUGHIN, ROBERT JAMES.—B. 1881; ed. privately; St. Thomas's Hosp., Lond., 1898-1902; lieut., 3rd King's Own Scottish Borderers, 1902-1905; lieut., Beds. regt., 1905; seconded to W.A.F.F., 1909-1910; priv. sec. and A.D.C. to gov't., Gold Coast, 1911.

**Version `col1917-L51424.v` — printed in editions [1917, 1920]:**

> McCOUGHIN, ROBERT JAMES.—B. 1881; ed. privately; St. Thomas's Hosp., Lond., 1898-1902; lieut., 3rd King's Own Scottish Borderers, 1902-1905; lieut., Beds. regt., 1905; seconded to W.A.F.F., 1909-1910; priv. sec. and A.D.C. to gov'r., Gold Coast, 1911.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1898–1902 | St. Thomas's Hosp., Lond | — | [1913, 1917, 1919, 1920, 1923] |
| 1 | 1902–1905 | lieut., 3rd King's Own Scottish Borderers | — | [1913, 1917, 1919, 1920, 1923] |
| 2 | 1905 | lieut., Beds. regt | — | [1913, 1917, 1919, 1920, 1923] |
| 3 | 1909–1910 | seconded to W.A.F.F | — | [1913, 1917, 1919, 1920, 1923] |
| 4 | 1911 | priv. sec. and A.D.C. to gov't. | Gold Coast | [1913, 1917, 1919, 1920, 1923] |

## Candidate stint `McLoughlin, R. J___Gold Coast___1910`

- Staff-list name: **McLoughlin, R. J** | colony: **Gold Coast** | listed 1910–1911 | editions [1910, 1911]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1910 | R. J. McLoughlin | Lieutenant | Gold Coast Regiment | — | Lieutenant |
| 1911 | R. J. McLoughlin | Lieutenant | Gold Coast Regiment | — | — |

### Deterministic checks: `mccloughin_robert-james_b1881` vs `McLoughlin, R. J___Gold Coast___1910`

- [PASS] surname_gate: bio 'McCLOUGHIN' vs stint 'McLoughlin, R. J' (fuzzy:2)
- [PASS] initials: bio ['R', 'J'] ~ stint ['R', 'J']
- [PASS] age_gate: stint starts 1910, birth 1881 (age 29)
- [PASS] colony: 1 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1910-1911
- [FAIL] position_sim: best 18 vs bar 60: 'priv. sec. and A.D.C. to gov't.' ~ 'Lieutenant'
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

