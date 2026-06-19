<!-- {"case_id": "case_wauton_edric-brenton_b1883", "bio_ids": ["wauton_edric-brenton_b1883"], "stint_ids": ["Wauton, E. B___Nigeria___1915"]} -->
# Dossier case_wauton_edric-brenton_b1883

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `wauton_edric-brenton_b1883`

- Printed name: **WAUTON, EDRIC BRENTON**
- Birth year: 1883 (attested in editions [1931, 1932])
- Appears in editions: [1931, 1932]

### Verbatim printed entry text (OCR)

**Version `col1931-L69199.v` — printed in editions [1931, 1932]:**

> WAUTON, CAPT. EDRIC BRENTON, R.E.(S.R.).—B. 1883; ed. Uppingham; asst. dist. comsnr., S. Nigeria, 1909; attd., Nigerian Regt., Cameroons, 1914-15; 2nd cls. dist. offr., 1917; cls I, grade 1, admteve. serv., 1928.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1909 | asst. dist. comsnr. | Southern Nigeria | [1931, 1932] |
| 1 | 1914–1915 | attd., Nigerian Regt. | Cameroons | [1931, 1932] |
| 2 | 1917 | 2nd cls. dist. offr | Cameroons *(inherited from previous clause)* | [1931, 1932] |
| 3 | 1928 | cls I, grade 1, admteve. serv | Cameroons *(inherited from previous clause)* | [1931, 1932] |

## Candidate stint `Wauton, E. B___Nigeria___1915`

- Staff-list name: **Wauton, E. B** | colony: **Nigeria** | listed 1915–1918 | editions [1915, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1915 | E. B. Wauton | Sixty Assistant District Officers | NORTHERN PROVINCES | — | — |
| 1918 | E. B. Wauton | Assistant District Officer | Southern Provinces | — | — |

### Deterministic checks: `wauton_edric-brenton_b1883` vs `Wauton, E. B___Nigeria___1915`

- [PASS] surname_gate: bio 'WAUTON' vs stint 'Wauton, E. B' (exact)
- [PASS] initials: bio ['E', 'B'] ~ stint ['E', 'B']
- [PASS] age_gate: stint starts 1915, birth 1883 (age 32)
- [PASS] colony: 4 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1915-1918
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

