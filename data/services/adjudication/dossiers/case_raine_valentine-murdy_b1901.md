<!-- {"case_id": "case_raine_valentine-murdy_b1901", "bio_ids": ["raine_valentine-murdy_b1901"], "stint_ids": ["Raine, V. M___Sierra Leone___1930"]} -->
# Dossier case_raine_valentine-murdy_b1901

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `raine_valentine-murdy_b1901`

- Printed name: **RAINE, Valentine Murdy**
- Birth year: 1901 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L35398.v` — printed in editions [1948, 1949, 1950, 1951]:**

> RAINE, Valentine Murdy.—b. 1901; ed. elem. and pte, 1st cl. Bd. of Trade engrn. (steam and diesel); on war serv. 1918–19; apptd. elec. dept., S.L., 1929; Nig., 1940; mech. engr., gr. II, 1947; compiled report on palm oil as diesel fuel, S.L., 1940.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | apptd. elec. dept. | Sierra Leone | [1948, 1949, 1950, 1951] |
| 1 | 1940 | apptd. elec. dept. | Nigeria | [1948, 1949, 1950, 1951] |
| 2 | 1940 | compiled report on palm oil as diesel fuel | Sierra Leone | [1948, 1949, 1950, 1951] |
| 3 | 1947 | mech. engr., gr. II | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Raine, V. M___Sierra Leone___1930`

- Staff-list name: **Raine, V. M** | colony: **Sierra Leone** | listed 1930–1931 | editions [1930, 1931]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1930 | V. M. Raine | Shift Foreman (Electricity Sub-Dept.) | Public Works Department | — | — |
| 1931 | V. M. Raine | Shift Foreman (Electricity Sub-Dept.) | Public Works Department | — | — |

### Deterministic checks: `raine_valentine-murdy_b1901` vs `Raine, V. M___Sierra Leone___1930`

- [PASS] surname_gate: bio 'RAINE' vs stint 'Raine, V. M' (exact)
- [PASS] initials: bio ['V', 'M'] ~ stint ['V', 'M']
- [PASS] age_gate: stint starts 1930, birth 1901 (age 29)
- [PASS] colony: 2 placed event(s) resolve to 'Sierra Leone'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1930-1931
- [FAIL] position_sim: best 29 vs bar 60: 'apptd. elec. dept.' ~ 'Shift Foreman (Electricity Sub-Dept.)'
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

