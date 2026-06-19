<!-- {"case_id": "case_lynch_frank-piers_b1883", "bio_ids": ["lynch_frank-piers_b1883"], "stint_ids": ["Lynch, F. P___Nigeria___1915"]} -->
# Dossier case_lynch_frank-piers_b1883

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 36 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `lynch_frank-piers_b1883`

- Printed name: **LYNCH, FRANK PIERS**
- Birth year: 1883 (attested in editions [1931, 1932])
- Appears in editions: [1931, 1932]

### Verbatim printed entry text (OCR)

**Version `col1931-L66267.v` — printed in editions [1931, 1932]:**

> LYNCH, FRANK PIERS, B.A. (Dublin).—B. 1883; ed. Downside Coll., Somerset and Trinity Coll., Dublin; asst. dist. commr., S. Nigeria, 1908; polit. offr., Okpoto Patrol and ag. dist. commr., 1912; polit. offr. to No. 1 column, Udi Patrol, 1914-15; polit. offr. to Umunze (Awka) Patrol, 1915; 2nd cls. dist. offr., 1915; cls. I, grade I, admive. serv., 1925; ag. sec., S. Provs., 1930; staff grade, Aug., 1930.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1908 | asst. dist. commr. | Southern Nigeria | [1931, 1932] |
| 1 | 1912 | polit. offr., Okpoto Patrol and ag. dist. commr | Southern Nigeria *(inherited from previous clause)* | [1931, 1932] |
| 2 | 1914–1915 | polit. offr. to No. 1 column, Udi Patrol | Southern Nigeria *(inherited from previous clause)* | [1931, 1932] |
| 3 | 1915 | polit. offr. to Umunze (Awka) Patrol | Southern Nigeria *(inherited from previous clause)* | [1931, 1932] |
| 4 | 1925 | cls. I, grade I, admive. serv | Southern Nigeria *(inherited from previous clause)* | [1931, 1932] |
| 5 | 1930 | ag. sec., S. Provs | Southern Nigeria *(inherited from previous clause)* | [1931, 1932] |

## Candidate stint `Lynch, F. P___Nigeria___1915`

- Staff-list name: **Lynch, F. P** | colony: **Nigeria** | listed 1915–1919 | editions [1915, 1918, 1919]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1915 | F. P. Lynch | Sixty Assistant District Officers | NORTHERN PROVINCES | — | — |
| 1918 | F. P. Lynch | Second Class District Officer | Southern Provinces | — | — |
| 1919 | F. P. Lynch | Thirty Second Class District Officers | SOUTHERN PROVINCES | — | — |

### Deterministic checks: `lynch_frank-piers_b1883` vs `Lynch, F. P___Nigeria___1915`

- [PASS] surname_gate: bio 'LYNCH' vs stint 'Lynch, F. P' (exact)
- [PASS] initials: bio ['F', 'P'] ~ stint ['F', 'P']
- [PASS] age_gate: stint starts 1915, birth 1883 (age 32)
- [PASS] colony: 6 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1915-1919
- [FAIL] position_sim: best 43 vs bar 60: 'polit. offr., Okpoto Patrol and ag. dist. commr' ~ 'Thirty Second Class District Officers'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

