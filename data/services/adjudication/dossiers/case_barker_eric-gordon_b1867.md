<!-- {"case_id": "case_barker_eric-gordon_b1867", "bio_ids": ["barker_eric-gordon_b1867"], "stint_ids": ["Barker, E. G___Sierra Leone___1906", "Barker, E___Fiji___1919"]} -->
# Dossier case_barker_eric-gordon_b1867

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 55 official(s) with this surname in the graph's staff lists; 15 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Barker, E___Fiji___1919` is also gate-compatible with biography(ies) outside this case: ['barker_frederick-eustace_b1838'] (already linked elsewhere or filtered).

## Biography `barker_eric-gordon_b1867`

- Printed name: **BARKER, ERIC GORDON**
- Birth year: 1867 (attested in editions [1923])
- Appears in editions: [1923]

### Verbatim printed entry text (OCR)

**Version `col1923-L52268.v` — printed in editions [1923]:**

> BARKER, ERIC GORDON, M.I.Mech.E.—B. 1867; ed. Birkenhead Schol. and Owen's Coll., Manchester; loco. supt., Sierra Leone Govt. Rly., 29th Oct., 1904; ag. gen. man., 1919 and 1921; gen. man., 8th Mar., 1922.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1904 | loco. supt. | Sierra Leone | [1923] |
| 1 | 1919–1921 | ag. gen. man. | — | [1923] |
| 2 | 1922 | gen. man. | — | [1923] |

## Candidate stint `Barker, E. G___Sierra Leone___1906`

- Staff-list name: **Barker, E. G** | colony: **Sierra Leone** | listed 1906–1923 | editions [1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922, 1923]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1906 | E. Barker | Locomotive Superintendent | Railway Department | — | — |
| 1907 | E. Barker | Locomotive Superintendent | Railway Department | — | — |
| 1908 | E. G. Barker | Locomotive Superintendent | Railway Department | — | — |
| 1909 | E. G. Barker | Locomotive Superintendent | Railway Department | — | — |
| 1910 | E. G. Barker | Locomotive Superintendent | Railway Department | — | — |
| 1911 | E. G. Barker | Locomotive Superintendent | Railway Department | — | — |
| 1912 | E. G. Barker | Locomotive Superintendent | Railway Department | — | — |
| 1913 | E. G. Barker | Locomotive Superintendent | Railway Department | — | — |
| 1914 | E. G. Barker | Locomotive Superintendent | Railway Department | — | — |
| 1915 | E. G. Barker | Locomotive Superintendent | Railway Department | — | — |
| 1917 | E. G. Barker | Locomotive Superintendent | Railway Department | — | — |
| 1918 | E. G. Barker | Locomotive Superintendent | Railway Department | — | — |
| 1919 | E. G. Barker | Locomotive Superintendent | Railway Department | — | — |
| 1920 | E. G. Barker | Locomotive Superintendent | Railway Department | — | — |
| 1921 | E. G. Barker | Chief Mechanical Engineer | Railway Department | — | — |
| 1922 | E. G. Barker | Chief Mechanical Engineer | Railway Department | — | — |
| 1923 | E. G. Barker | General Manager, Chief Mechanical Engineer | Railway Department | — | — |

### Deterministic checks: `barker_eric-gordon_b1867` vs `Barker, E. G___Sierra Leone___1906`

- [PASS] surname_gate: bio 'BARKER' vs stint 'Barker, E. G' (exact)
- [PASS] initials: bio ['E', 'G'] ~ stint ['E', 'G']
- [PASS] age_gate: stint starts 1906, birth 1867 (age 39)
- [PASS] colony: 1 placed event(s) resolve to 'Sierra Leone'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1906-1923
- [FAIL] position_sim: best 53 vs bar 60: 'loco. supt.' ~ 'Locomotive Superintendent'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Barker, E___Fiji___1919`

- Staff-list name: **Barker, E** | colony: **Fiji** | listed 1919–1921 | editions [1919, 1920, 1921]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1919 | E. Barker | Assistant Mistresses | Education Department | — | — |
| 1920 | E. Barker | Assistant Mistresses | Education Department | — | — |
| 1921 | E. Barker | Assistant Mistresses | Education Department | — | — |

### Deterministic checks: `barker_eric-gordon_b1867` vs `Barker, E___Fiji___1919`

- [PASS] surname_gate: bio 'BARKER' vs stint 'Barker, E' (exact)
- [PASS] initials: bio ['E', 'G'] ~ stint ['E']
- [PASS] age_gate: stint starts 1919, birth 1867 (age 52)
- [FAIL] colony: no placed event resolves to 'Fiji'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1919-1921
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

