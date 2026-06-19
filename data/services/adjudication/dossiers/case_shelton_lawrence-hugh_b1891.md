<!-- {"case_id": "case_shelton_lawrence-hugh_b1891", "bio_ids": ["shelton_lawrence-hugh_b1891"], "stint_ids": ["Shelton, L. H___Nigeria___1918", "Shelton, L. H___Nigeria___1934"]} -->
# Dossier case_shelton_lawrence-hugh_b1891

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `shelton_lawrence-hugh_b1891`

- Printed name: **SHELTON, LAWRENCE HUGH**
- Birth year: 1891 (attested in editions [1936, 1937])
- Appears in editions: [1935, 1936, 1937]

### Verbatim printed entry text (OCR)

**Version `col1936-L64546.v` — printed in editions [1936, 1937]:**

> SHELTON, LAWRENCE HUGH, M.A. (Cantab).—B. 1891; ed. St. Michael's Coll., Tenbury, Hereford Schl. and St. John's Coll., Cambridge; asst. dist. offr., S. Nigeria, 1915; cls., I, admvte., serv., 1932; ag. dep. ch. sec., Nigeria, in 1934, 1935 and 1936; prin. asst. sec., Jan., 1935; ag. ch. sec., 1936.

**Version `dol1935-L62154.v` — printed in editions [1935]:**

> SHELTON, LAWRENCE HUGH, M.A. (Cantab)—B. 1891; ed. St. Michael's Coll., Tewksbury Hereford Schi. and St. John's Coll., Cambridge; asst. dist. offr., S. Nigeria, 1915; cls. I. admin. serv., 1932.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915–1915 | asst. dist. offr. | Southern Nigeria | [1935, 1936, 1937] |
| 1 | 1932–1932 | cls., I, admvte., serv. | Southern Nigeria *(inherited from previous clause)* | [1935, 1936, 1937] |
| 2 | 1934–1936 | ag. dep. ch. sec. | Nigeria | [1936, 1937] |
| 3 | 1935–1935 | prin. asst. sec. | — | [1936, 1937] |
| 4 | 1936–1936 | ag. ch. sec. | — | [1936, 1937] |

## Candidate stint `Shelton, L. H___Nigeria___1918`

- Staff-list name: **Shelton, L. H** | colony: **Nigeria** | listed 1918–1919 | editions [1918, 1919]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1918 | L. H. Shelton | Assistant District Officer | Southern Provinces | — | — |
| 1919 | L. H. Shelton | Sixty Assistant District Officers | SOUTHERN PROVINCES | — | — |

### Deterministic checks: `shelton_lawrence-hugh_b1891` vs `Shelton, L. H___Nigeria___1918`

- [PASS] surname_gate: bio 'SHELTON' vs stint 'Shelton, L. H' (exact)
- [PASS] initials: bio ['L', 'H'] ~ stint ['L', 'H']
- [PASS] age_gate: stint starts 1918, birth 1891 (age 27)
- [PASS] colony: 3 placed event(s) resolve to 'Nigeria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1918-1919
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Shelton, L. H___Nigeria___1934`

- Staff-list name: **Shelton, L. H** | colony: **Nigeria** | listed 1934–1936 | editions [1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | L. H. Shelton | — | Administrative Service | — | — |
| 1936 | L. H. Shelton | Principal Assistant Secretary | Nigerian Secretariat | — | — |

### Deterministic checks: `shelton_lawrence-hugh_b1891` vs `Shelton, L. H___Nigeria___1934`

- [PASS] surname_gate: bio 'SHELTON' vs stint 'Shelton, L. H' (exact)
- [PASS] initials: bio ['L', 'H'] ~ stint ['L', 'H']
- [PASS] age_gate: stint starts 1934, birth 1891 (age 43)
- [PASS] colony: 3 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1934-1936
- [FAIL] position_sim: best 38 vs bar 60: 'ag. dep. ch. sec.' ~ 'Principal Assistant Secretary'
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

