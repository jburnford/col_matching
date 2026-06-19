<!-- {"case_id": "case_carr_george-lyon_e1880", "bio_ids": ["carr_george-lyon_e1880", "carr_george-lyon_e1880-2"], "stint_ids": ["Carr, G. W. L___Malta___1883"]} -->
# Dossier case_carr_george-lyon_e1880

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 22 official(s) with this surname in the graph's staff lists; 13 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Carr, G. W. L___Malta___1883'] have more than one claimant biography in this case.
- Phase 1 found `carr_george-lyon_e1880` ↔ `Carr, G. W. L___Malta___1883` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- Phase 1 found `carr_george-lyon_e1880-2` ↔ `Carr, G. W. L___Malta___1883` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).

## Biography `carr_george-lyon_e1880`

- Printed name: **CARR, GEORGE LYON**
- Birth year: not printed
- Appears in editions: [1886, 1890, 1894, 1896, 1897]

### Verbatim printed entry text (OCR)

**Version `col1886-L32560.v` — printed in editions [1886, 1890, 1894, 1896, 1897]:**

> CARR, CAPTAIN GEORGE LYON, R.N.—Superintendent of ports, Malta, 1880.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1880 | Superintendent of ports | Malta | [1886, 1890, 1894, 1896, 1897] |

## Biography `carr_george-lyon_e1880-2`

- Printed name: **CARR, George Lyon**
- Birth year: not printed
- Appears in editions: [1889]

### Verbatim printed entry text (OCR)

**Version `col1889-L32205.v` — printed in editions [1889]:**

> CARR, Captain George Lyon, R.N.—Superintendent of ports, Malta, 1880.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1880 | Superintendent of ports | Malta | [1889] |

## Candidate stint `Carr, G. W. L___Malta___1883`

- Staff-list name: **Carr, G. W. L** | colony: **Malta** | listed 1883–1886 | editions [1883, 1886]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1883 | Captain G. W. L. Carr, R.N. | Superintendent of the Ports | Port Department | — | Captain |
| 1886 | G. W. L. Carr | Superintendent of the Ports | Port Department | — | Captain |

### Deterministic checks: `carr_george-lyon_e1880` vs `Carr, G. W. L___Malta___1883`

- [PASS] surname_gate: bio 'CARR' vs stint 'Carr, G. W. L' (exact)
- [PASS] initials: bio ['G', 'L'] ~ stint ['G', 'W', 'L']
- [PASS] age_gate: stint starts 1883; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Malta'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1883-1886
- [PASS] position_sim: best 100 vs bar 60: 'Superintendent of ports' ~ 'Superintendent of the Ports'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): 1 agreeing edition-year(s) [1886] pos~100 (bar: >=2)
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `carr_george-lyon_e1880-2` vs `Carr, G. W. L___Malta___1883`

- [PASS] surname_gate: bio 'CARR' vs stint 'Carr, G. W. L' (exact)
- [PASS] initials: bio ['G', 'L'] ~ stint ['G', 'W', 'L']
- [PASS] age_gate: stint starts 1883; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Malta'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1883-1886
- [PASS] position_sim: best 100 vs bar 60: 'Superintendent of ports' ~ 'Superintendent of the Ports'
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

