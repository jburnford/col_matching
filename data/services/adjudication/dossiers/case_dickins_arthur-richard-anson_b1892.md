<!-- {"case_id": "case_dickins_arthur-richard-anson_b1892", "bio_ids": ["dickins_arthur-richard-anson_b1892"], "stint_ids": ["Dickins, A. R. A___Nigeria___1923", "Dickins, A. R. A___Nigeria___1934", "Dickins, R___Australia___1913"]} -->
# Dossier case_dickins_arthur-richard-anson_b1892

## Case context

- 1 biography(ies) and 3 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `dickins_arthur-richard-anson_b1892`

- Printed name: **DICKINS, ARTHUR RICHARD ANSON**
- Birth year: 1892 (attested in editions [1940])
- Appears in editions: [1940]

### Verbatim printed entry text (OCR)

**Version `col1940-L63771.v` — printed in editions [1940]:**

> DICKINS, ARTHUR RICHARD ANSON.—B. 1892; ed. St. John Coll., Oxford; passed divinity and mods.; mily. serv., 1914-19; admin. offr., Nigeria, 1921; cls. III., 1924; ag. sec., Sn. Provs., 1938; offr., cls. II., 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1914–1919 | mily. serv | — | [1940] |
| 1 | 1921 | admin. offr. | Nigeria | [1940] |
| 2 | 1924 | cls. III | Nigeria *(inherited from previous clause)* | [1940] |
| 3 | 1938 | ag. sec., Sn. Provs | Nigeria *(inherited from previous clause)* | [1940] |

## Candidate stint `Dickins, A. R. A___Nigeria___1923`

- Staff-list name: **Dickins, A. R. A** | colony: **Nigeria** | listed 1923–1927 | editions [1923, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1923 | Capt. A. R. A. Dickins | Assistant Secretary | Civil Establishment | — | Captain |
| 1927 | Capt. A. R. A. Dickins | Assistant Secretary | Secretariat, Southern Provinces and Colony | — | Captain |

### Deterministic checks: `dickins_arthur-richard-anson_b1892` vs `Dickins, A. R. A___Nigeria___1923`

- [PASS] surname_gate: bio 'DICKINS' vs stint 'Dickins, A. R. A' (exact)
- [PASS] initials: bio ['A', 'R', 'A'] ~ stint ['A', 'R', 'A']
- [PASS] age_gate: stint starts 1923, birth 1892 (age 31)
- [PASS] colony: 3 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1923-1927
- [FAIL] position_sim: best 34 vs bar 60: 'admin. offr.' ~ 'Assistant Secretary'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Dickins, A. R. A___Nigeria___1934`

- Staff-list name: **Dickins, A. R. A** | colony: **Nigeria** | listed 1934–1939 | editions [1934, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | A. R. A. Dickins | — | Administrative Service | — | Captain |
| 1939 | A. R. A. Dickins | Senior Assistant Secretary | Secretariat, Southern Provinces and Colony | — | — |

### Deterministic checks: `dickins_arthur-richard-anson_b1892` vs `Dickins, A. R. A___Nigeria___1934`

- [PASS] surname_gate: bio 'DICKINS' vs stint 'Dickins, A. R. A' (exact)
- [PASS] initials: bio ['A', 'R', 'A'] ~ stint ['A', 'R', 'A']
- [PASS] age_gate: stint starts 1934, birth 1892 (age 42)
- [PASS] colony: 3 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1934-1939
- [FAIL] position_sim: best 44 vs bar 60: 'ag. sec., Sn. Provs' ~ 'Senior Assistant Secretary'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Dickins, R___Australia___1913`

- Staff-list name: **Dickins, R** | colony: **Australia** | listed 1913–1918 | editions [1913, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1913 | R. Dickins | Member | Marine Board | — | — |
| 1918 | R. Dickins | Member | Marine Board | — | — |

### Deterministic checks: `dickins_arthur-richard-anson_b1892` vs `Dickins, R___Australia___1913`

- [PASS] surname_gate: bio 'DICKINS' vs stint 'Dickins, R' (exact)
- [PASS] initials: bio ['A', 'R', 'A'] ~ stint ['R']
- [PASS] age_gate: stint starts 1913, birth 1892 (age 21)
- [FAIL] colony: no placed event resolves to 'Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1913-1918
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

