<!-- {"case_id": "case_peel_frederick_e1849", "bio_ids": ["peel_frederick_e1849"], "stint_ids": ["Peel, R. F___St Helena___1921"]} -->
# Dossier case_peel_frederick_e1849

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 12 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['peel_frederick_e1849'] carry a single initial only — the namesake trap applies.

## Biography `peel_frederick_e1849`

- Printed name: **PEEL, FREDERICK**
- Birth year: not printed
- Honours: K.C.M.G. (1869), P.C. (1857)
- Appears in editions: [1898, 1899, 1900]

### Verbatim printed entry text (OCR)

**Version `col1898-L35345.v` — printed in editions [1898, 1899, 1900]:**

> PEEL, Rt. HON. SIR FREDERICK P.C. (1857), K.C.M.G. (1869) (2nd son of the late Sir Robert Peel, 2nd Bart.),—Ed. Harrow, and at Trin. Coll., Camb., 1st class in classics, 1845; called to the bar, Inner Tem., 1849; under-secr. for the cols., Nov., 1851, to Mar., 1852, and Dec., 1852, to Feb., 1855; under-secr. for war, 1855 to 1857; is a dep.-lient. of Warwickshire; was M.P. for Leominster, Feb., 1849, to July, 1852, and for Bury, Lancashire, July, 1852, to Apr., 1857; re-elected for Bury, May, 1859, and apptd. sec. to the treasy., 1860; rly. comsnr., 1875.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1849–1849 | called to the bar | — | [1898, 1899, 1900] |
| 1 | 1849–1852 | M.P. | Leominster | [1898, 1899, 1900] |
| 2 | 1851–1852 | under-secr. for the cols. | — | [1898, 1899, 1900] |
| 3 | 1852–1855 | under-secr. for the cols. | — | [1898, 1899, 1900] |
| 4 | 1852–1857 | M.P. | Bury, Lancashire | [1898, 1899, 1900] |
| 5 | 1855–1857 | under-secr. for war | — | [1898, 1899, 1900] |
| 6 | 1859–1859 | M.P. | Bury | [1898, 1899, 1900] |
| 7 | 1860–1860 | sec. to the treasy. | — | [1898, 1899, 1900] |
| 8 | 1875–1875 | rly. comsnr. | — | [1898, 1899, 1900] |

## Candidate stint `Peel, R. F___St Helena___1921`

- Staff-list name: **Peel, R. F** | colony: **St Helena** | listed 1921–1924 | editions [1921, 1923, 1924]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | R. F. Peel | Governor and acting Chief Justice | Civil Establishment | — | Colonel |
| 1923 | R. F. Peel | Governor and acting Chief Justice | Civil Establishment | C.M.G. | Colonel |
| 1924 | R. F. Peel | Governor and acting Chief Justice | Civil Establishment | C.M.G. | Colonel |

### Deterministic checks: `peel_frederick_e1849` vs `Peel, R. F___St Helena___1921`

- [PASS] surname_gate: bio 'PEEL' vs stint 'Peel, R. F' (exact)
- [PASS] initials: bio ['F'] ~ stint ['R', 'F']
- [PASS] age_gate: stint starts 1921; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'St Helena'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1921-1924
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

