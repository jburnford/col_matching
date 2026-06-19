<!-- {"case_id": "case_dew_henry-thomas-butler_b1888", "bio_ids": ["dew_henry-thomas-butler_b1888"], "stint_ids": ["Dew, H. T. B___Nigeria___1915"]} -->
# Dossier case_dew_henry-thomas-butler_b1888

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `dew_henry-thomas-butler_b1888`

- Printed name: **DEW, HENRY THOMAS BUTLER**
- Birth year: 1888 (attested in editions [1930, 1931, 1932])
- Appears in editions: [1930, 1931, 1932]

### Verbatim printed entry text (OCR)

**Version `col1930-L63939.v` — printed in editions [1930, 1931, 1932]:**

> DEW, HENRY THOMAS BUTLER.—B. 1888; ed. Christ's Hosp. (Grecian) and Jesus Coll., Cambridge (Rustad Scholar); class. tripods II div. cl. I, 1910; admstive dept., N.W. Rhodesia, 1911; asst. dist. comsnr., S. Nigeria, July, 1912; polit. offr., Egba Patrol, June, 1918; intel. offr., Egba mily. operns., June to Aug., 1918 (A.G.S. med. and clasps); polit. offr., Igbo Patrol, Mar., 1920; dist. offr., July, 1922; res., Feb., 1929; cls. I, grade I, admstive serv., 1929.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1910 | class. tripods II div. cl. I | — | [1930, 1931, 1932] |
| 1 | 1911 | admstive dept., N.W. Rhodesia | — | [1930, 1931, 1932] |
| 2 | 1912 | asst. dist. comsnr. | Southern Nigeria | [1930, 1931, 1932] |
| 3 | 1918 | polit. offr., Egba Patrol | Southern Nigeria *(inherited from previous clause)* | [1930, 1931, 1932] |
| 4 | 1920 | polit. offr., Igbo Patrol | Southern Nigeria *(inherited from previous clause)* | [1930, 1931, 1932] |
| 5 | 1922 | dist. offr | Southern Nigeria *(inherited from previous clause)* | [1930, 1931, 1932] |
| 6 | 1929 | res | Southern Nigeria *(inherited from previous clause)* | [1930, 1931, 1932] |

## Candidate stint `Dew, H. T. B___Nigeria___1915`

- Staff-list name: **Dew, H. T. B** | colony: **Nigeria** | listed 1915–1919 | editions [1915, 1918, 1919]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1915 | H. T. B. Dew | Sixty Assistant District Officers | NORTHERN PROVINCES | — | — |
| 1918 | H. T. B. Dew | Assistant District Officer | Southern Provinces | — | — |
| 1919 | H. T. B. Dew | Sixty Assistant District Officers | SOUTHERN PROVINCES | — | — |

### Deterministic checks: `dew_henry-thomas-butler_b1888` vs `Dew, H. T. B___Nigeria___1915`

- [PASS] surname_gate: bio 'DEW' vs stint 'Dew, H. T. B' (exact)
- [PASS] initials: bio ['H', 'T', 'B'] ~ stint ['H', 'T', 'B']
- [PASS] age_gate: stint starts 1915, birth 1888 (age 27)
- [PASS] colony: 5 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1915-1919
- [FAIL] position_sim: best 48 vs bar 60: 'asst. dist. comsnr.' ~ 'Assistant District Officer'
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

