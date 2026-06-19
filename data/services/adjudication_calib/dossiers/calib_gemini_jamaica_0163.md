<!-- {"case_id": "calib_gemini_jamaica_0163", "bio_ids": ["hartwell_e-h-b_e1851"], "stint_ids": ["Hartwell, E. H. B___Jamaica___1879"]} -->
# Dossier calib_gemini_jamaica_0163

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hartwell_e-h-b_e1851`

- Printed name: **HARTWELL, E. H. B.**
- Birth year: not printed
- Appears in editions: [1886, 1888, 1889, 1894]

### Verbatim printed entry text (OCR)

**Version `col1886-L33944.v` — printed in editions [1886, 1888, 1889, 1894]:**

> HARTWELL, CAPTAIN (Retired) E. H. B., R.N.—Entered the royal navy, July, 1851; served in Black Sea and Baltic during Crimean War; subsequently on the Pacific, Mediterranean, and East Indian stations; promoted to lieutenant, 1859, commander, 1868; retired, 1873, being then in command of a coast guard in Ireland; appointed inspector-general of police, Jamaica, Aug. 1878; consul for South Italy, Feb., 1886.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1851 | royal navy | — | [1886, 1888, 1889, 1894] |
| 1 | 1859 | lieutenant | — | [1886, 1888, 1889, 1894] |
| 2 | 1868 | commander | — | [1886, 1888, 1889, 1894] |
| 3 | 1873 | command of a coast guard | Ireland | [1886, 1888, 1889, 1894] |
| 4 | 1878 | inspector-general of police | Jamaica | [1886, 1888, 1889, 1894] |
| 5 | 1886 | consul | South Italy | [1886, 1888, 1889, 1894] |
| 6 | ? | — | — | [1886, 1888, 1889, 1894] |
| 7 | ? | — | — | [1886, 1888, 1889, 1894] |

## Candidate stint `Hartwell, E. H. B___Jamaica___1879`

- Staff-list name: **Hartwell, E. H. B** | colony: **Jamaica** | listed 1879–1886 | editions [1879, 1880, 1883, 1886]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1879 | E. H. B. Hartwell | Inspector General | Jamaica Constabulary | — | Captain |
| 1880 | E. H. B. Hartwell | Inspector General | Jamaica Constabulary | — | Captain |
| 1883 | E. H. B. Hartwell | Inspector General | Jamaica Constabulary | — | Captain |
| 1886 | E H. B. Hartwell | Inspector General | Jamaica Constabulary | — | Captain |

### Deterministic checks: `hartwell_e-h-b_e1851` vs `Hartwell, E. H. B___Jamaica___1879`

- [PASS] surname_gate: bio 'HARTWELL' vs stint 'Hartwell, E. H. B' (exact)
- [PASS] initials: bio ['E', 'H', 'B'] ~ stint ['E', 'H', 'B']
- [PASS] age_gate: stint starts 1879; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Jamaica'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1879-1886
- [PASS] position_sim: best 100 vs bar 60: 'inspector-general of police' ~ 'Inspector General'
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

