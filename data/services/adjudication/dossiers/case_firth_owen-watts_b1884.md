<!-- {"case_id": "case_firth_owen-watts_b1884", "bio_ids": ["firth_owen-watts_b1884"], "stint_ids": ["Firth, O. W___Nigeria___1915"]} -->
# Dossier case_firth_owen-watts_b1884

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `firth_owen-watts_b1884`

- Printed name: **FIRTH, OWEN WATTS**
- Birth year: 1884 (attested in editions [1931, 1932, 1933, 1934, 1935, 1936, 1937])
- Appears in editions: [1931, 1932, 1933, 1934, 1935, 1936, 1937]

### Verbatim printed entry text (OCR)

**Version `col1931-L64172.v` — printed in editions [1931, 1932, 1933, 1934, 1935, 1936, 1937]:**

> FIRTH, OWEN WATTS.—B. 1884; ed. Tonbridge Schl.; asst. dist. comsnr., Nigeria, 1911; polit. offr., Udi-Okiwgi Patrol, 1915; 2nd cls. dist. offr., 1919; cls. I, grade I, admstve. serv., 1927; ag. prin. ass't. sec., S. Provs., 1928; staff grade, 1932; ag. lieut.-gov., S. Provs., 1934.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1911 | asst. dist. comsnr. | Nigeria | [1931, 1932, 1933, 1934, 1935, 1936, 1937] |
| 1 | 1915 | polit. offr., Udi-Okiwgi Patrol | Nigeria *(inherited from previous clause)* | [1931, 1932, 1933, 1934, 1935, 1936, 1937] |
| 2 | 1919 | 2nd cls. dist. offr | Nigeria *(inherited from previous clause)* | [1931, 1932, 1933, 1934, 1935, 1936, 1937] |
| 3 | 1927 | cls. I, grade I, admstve. serv | Nigeria *(inherited from previous clause)* | [1931, 1932, 1933, 1934, 1935, 1936, 1937] |
| 4 | 1928 | ag. prin. ass't. sec., S. Provs | Nigeria *(inherited from previous clause)* | [1931, 1932, 1933, 1934, 1935, 1936, 1937] |
| 5 | 1932 | staff grade | Nigeria *(inherited from previous clause)* | [1931, 1932, 1933, 1934, 1935, 1936, 1937] |
| 6 | 1934 | ag. lieut.-gov., S. Provs | Nigeria *(inherited from previous clause)* | [1931, 1932, 1933, 1934, 1935, 1936, 1937] |

## Candidate stint `Firth, O. W___Nigeria___1915`

- Staff-list name: **Firth, O. W** | colony: **Nigeria** | listed 1915–1919 | editions [1915, 1918, 1919]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1915 | O. W. Firth | Sixty Assistant District Officers | NORTHERN PROVINCES | — | — |
| 1918 | O. W. Firth | Assistant District Officer | Southern Provinces | — | — |
| 1919 | O. W. Firth | Sixty Assistant District Officers | SOUTHERN PROVINCES | — | — |

### Deterministic checks: `firth_owen-watts_b1884` vs `Firth, O. W___Nigeria___1915`

- [PASS] surname_gate: bio 'FIRTH' vs stint 'Firth, O. W' (exact)
- [PASS] initials: bio ['O', 'W'] ~ stint ['O', 'W']
- [PASS] age_gate: stint starts 1915, birth 1884 (age 31)
- [PASS] colony: 7 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1915-1919
- [FAIL] position_sim: best 51 vs bar 60: '2nd cls. dist. offr' ~ 'Assistant District Officer'
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

