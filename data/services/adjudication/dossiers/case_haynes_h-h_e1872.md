<!-- {"case_id": "case_haynes_h-h_e1872", "bio_ids": ["haynes_h-h_e1872"], "stint_ids": ["Haynes, H. H___Barbados___1880"]} -->
# Dossier case_haynes_h-h_e1872

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 41 official(s) with this surname in the graph's staff lists; 10 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- Phase 1 found `haynes_h-h_e1872` ↔ `Haynes, H. H___Barbados___1880` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- NOTE: stint `Haynes, H. H___Barbados___1880` is also gate-compatible with biography(ies) outside this case: ['haynes_h-h_e1882'] (already linked elsewhere or filtered).

## Biography `haynes_h-h_e1872`

- Printed name: **HAYNES, H. H**
- Birth year: not printed
- Appears in editions: [1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1888-L33944.v` — printed in editions [1888, 1889, 1890]:**

> HAYNES, H. H.—Entered Customs, Barbados, Mar., 1872; acting inspector-general of police, 1878; acting inspector, inland revenue department, 1879; acting chief of police, St. Vincent, Feb., 1880; superintendent of harbour police, Barbados, Sept., 1880; inspector of police, Aug., 1882.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1872 | Entered Customs | Barbados | [1888, 1889, 1890] |
| 1 | 1878 | acting inspector-general of police | Barbados *(inherited from previous clause)* | [1888, 1889, 1890] |
| 2 | 1879 | acting inspector, inland revenue department | Barbados *(inherited from previous clause)* | [1888, 1889, 1890] |
| 3 | 1880 | acting chief of police | St. Vincent | [1888, 1889, 1890] |
| 4 | 1880 | superintendent of harbour police | Barbados | [1888, 1889, 1890] |
| 5 | 1882 | inspector of police | Barbados *(inherited from previous clause)* | [1888, 1889, 1890] |

## Candidate stint `Haynes, H. H___Barbados___1880`

- Staff-list name: **Haynes, H. H** | colony: **Barbados** | listed 1880–1890 | editions [1880, 1888, 1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1880 | H. H. Haynes | Inspector of Officers | Inland Revenue Department | — | — |
| 1888 | H. H. Haynes | Inspector of Police | Police and Prisons | — | — |
| 1889 | H. H. Haynes | Inspector of Police | Police and Prisons | — | — |
| 1890 | H.H. Haynes | Inspector of Police | Police and Prisons | — | — |

### Deterministic checks: `haynes_h-h_e1872` vs `Haynes, H. H___Barbados___1880`

- [PASS] surname_gate: bio 'HAYNES' vs stint 'Haynes, H. H' (exact)
- [PASS] initials: bio ['H', 'H'] ~ stint ['H', 'H']
- [PASS] age_gate: stint starts 1880; no printed birth year — UNCHECKED
- [PASS] colony: 5 placed event(s) resolve to 'Barbados'
- [PASS] tenure_overlap: 4 event tenure(s) overlap stint years 1880-1890
- [PASS] position_sim: best 100 vs bar 60: 'inspector of police' ~ 'Inspector of Police'
- [FAIL] honour: no shared honour
- [PASS] edition_cooccurrence: 3 agreeing edition-year(s) [1888, 1889, 1890] pos~100 (bar: >=2)
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

