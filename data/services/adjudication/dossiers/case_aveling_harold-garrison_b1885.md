<!-- {"case_id": "case_aveling_harold-garrison_b1885", "bio_ids": ["aveling_harold-garrison_b1885"], "stint_ids": ["Aveling, H. G___Nigeria___1915"]} -->
# Dossier case_aveling_harold-garrison_b1885

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `aveling_harold-garrison_b1885`

- Printed name: **AVELING, HAROLD GARRISON**
- Birth year: 1885 (attested in editions [1931, 1932, 1933])
- Honours: L.C.P
- Appears in editions: [1931, 1932, 1933]

### Verbatim printed entry text (OCR)

**Version `col1931-L62112.v` — printed in editions [1931, 1932, 1933]:**

> AVELING, HAROLD GARRISON, M.A. (Cantab.), L.C.P.—B. 1885; ed. Christ's Coll., Blackheath and Christ's Coll., Cambridge; ast. dist. commr., S. Nigeria, 1911; 2nd cls. dist. offr., 1919; cls. I, grade I, admnstr. serv., 1927.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1911 | ast. dist. commr. | Southern Nigeria | [1931, 1932, 1933] |
| 1 | 1919 | 2nd cls. dist. offr | Southern Nigeria *(inherited from previous clause)* | [1931, 1932, 1933] |
| 2 | 1927 | cls. I, grade I, admnstr. serv | Southern Nigeria *(inherited from previous clause)* | [1931, 1932, 1933] |

## Candidate stint `Aveling, H. G___Nigeria___1915`

- Staff-list name: **Aveling, H. G** | colony: **Nigeria** | listed 1915–1918 | editions [1915, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1915 | H. G. Aveling | Sixty Assistant District Officers | NORTHERN PROVINCES | — | — |
| 1918 | H. G. Aveling | Assistant District Officer | Southern Provinces | — | — |

### Deterministic checks: `aveling_harold-garrison_b1885` vs `Aveling, H. G___Nigeria___1915`

- [PASS] surname_gate: bio 'AVELING' vs stint 'Aveling, H. G' (exact)
- [PASS] initials: bio ['H', 'G'] ~ stint ['H', 'G']
- [PASS] age_gate: stint starts 1915, birth 1885 (age 30)
- [PASS] colony: 3 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1915-1918
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

