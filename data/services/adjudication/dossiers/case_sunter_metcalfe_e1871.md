<!-- {"case_id": "case_sunter_metcalfe_e1871", "bio_ids": ["sunter_metcalfe_e1871"], "stint_ids": ["Sunter, M___Sierra Leone___1883", "Sunter, Metcalfe___Gold Coast___1889"]} -->
# Dossier case_sunter_metcalfe_e1871

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['sunter_metcalfe_e1871'] carry a single initial only — the namesake trap applies.

## Biography `sunter_metcalfe_e1871`

- Printed name: **SUNTER, METCALFE**
- Birth year: not printed
- Appears in editions: [1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1888-L36262.v` — printed in editions [1888, 1889, 1890]:**

> SUNTER, REV. METCALFE, M.A.—Master of Fourah Bay College, Sierra Leone (affiliated to the University of Durham), 1871-82; acting director of public instruction, Sierra Leone, June, 1876, to Mar., 1877; examiner for Sierra Leone civil service in same years; in charge of colonial church, June to Dec., 1881; acting colonial chaplain, Dec., 1881, to Dec., 1882; garrison chaplain, May, 1882, to Jan., 1883; inspector of schools for the West African Colonies, Sept., 1882.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1871–1882 | Master of Fourah Bay College | Sierra Leone | [1888, 1889, 1890] |
| 1 | 1876–1877 | acting director of public instruction | Sierra Leone | [1888, 1889, 1890] |
| 2 | 1881–1881 | in charge of colonial church | — | [1888, 1889, 1890] |
| 3 | 1881–1882 | acting colonial chaplain | — | [1888, 1889, 1890] |
| 4 | 1882–1883 | garrison chaplain | — | [1888, 1889, 1890] |
| 5 | 1882 | inspector of schools | West African Colonies | [1888, 1889, 1890] |

## Candidate stint `Sunter, M___Sierra Leone___1883`

- Staff-list name: **Sunter, M** | colony: **Sierra Leone** | listed 1883–1886 | editions [1883, 1886]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1883 | The Rev. M. Sunter | Inspector of Schools | Educational Establishment | — | — |
| 1886 | M. Sunter | Inspector of Schools | Educational Establishment | — | — |

### Deterministic checks: `sunter_metcalfe_e1871` vs `Sunter, M___Sierra Leone___1883`

- [PASS] surname_gate: bio 'SUNTER' vs stint 'Sunter, M' (exact)
- [PASS] initials: bio ['M'] ~ stint ['M']
- [PASS] age_gate: stint starts 1883; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Sierra Leone'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1883-1886
- [FAIL] position_sim: best 33 vs bar 60: 'Master of Fourah Bay College' ~ 'Inspector of Schools'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Sunter, Metcalfe___Gold Coast___1889`

- Staff-list name: **Sunter, Metcalfe** | colony: **Gold Coast** | listed 1889–1890 | editions [1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1889 | The Rev. Metcalfe Sunter | Inspector of Schools | Educational Department | — | — |
| 1890 | The Rev. Metcalfe Sunter | Inspector of Schools | Educational Department | — | — |

### Deterministic checks: `sunter_metcalfe_e1871` vs `Sunter, Metcalfe___Gold Coast___1889`

- [PASS] surname_gate: bio 'SUNTER' vs stint 'Sunter, Metcalfe' (exact)
- [PASS] initials: bio ['M'] ~ stint ['M']
- [PASS] age_gate: stint starts 1889; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1889-1890
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

