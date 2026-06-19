<!-- {"case_id": "case_fitzsimons_robert-henry_e1865", "bio_ids": ["fitzsimons_robert-henry_e1865"], "stint_ids": ["Fitzsimons, R. H___Trinidad___1877"]} -->
# Dossier case_fitzsimons_robert-henry_e1865

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `fitzsimons_robert-henry_e1865`

- Printed name: **FITZSIMONS, ROBERT HENRY**
- Birth year: not printed
- Appears in editions: [1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1888-L33432.v` — printed in editions [1888, 1889, 1890]:**

> FITZSIMONS, ROBERT HENRY.—Formerly in Royal Irish constabulary; inspector of police, Trinidad, Feb., 1865; acting inspector of immigrants, southern division, in 1874 and 1886; senior inspector of police, 1878; acting commandant, 1883; is also sanitary inspector for San Fernando, and a J.P. for the colony.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1865 | inspector of police | Trinidad | [1888, 1889, 1890] |
| 1 | 1874–1886 | acting inspector of immigrants | — | [1888, 1889, 1890] |
| 2 | 1878 | senior inspector of police | — | [1888, 1889, 1890] |
| 3 | 1883 | acting commandant | — | [1888, 1889, 1890] |

## Candidate stint `Fitzsimons, R. H___Trinidad___1877`

- Staff-list name: **Fitzsimons, R. H** | colony: **Trinidad** | listed 1877–1890 | editions [1877, 1878, 1879, 1880, 1883, 1886, 1888, 1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | R. Fitzsimons | Sub-Inspector of Police, and Inspector of Weights and Measures | Police and Gaols | — | — |
| 1878 | R. Fitzsimons | Sub-Inspector of Police (San Fernando), and Inspector of Weights and Measures | Police and Gaols | — | — |
| 1878 | R. H. Fitzsimons | Sanitary Inspector | Public Health Department | — | — |
| 1879 | R. H. Fitzsimons | Sanitary Inspector | Public Health Department | — | — |
| 1879 | R. Fitzsimons | Inspector of Police, and Inspector of Weights and Measures | Police and Gaols | — | — |
| 1879 | R. H. Fitzsimons | Supervisor | Receiver-General's Department | — | — |
| 1880 | R. H. Fitzsimons | Sanitary Inspector | Public Health Department | — | — |
| 1880 | R. Fitzsimons | Inspector of Police (San Fernando), Inspector of Weights and Measures, and Supervisor | Police and Gaols | — | — |
| 1883 | R. Fitzsimons | Inspector of Police (San Fernando), Inspector of Weights and Measures, and Supervisor | Police and Gaols | — | — |
| 1883 | R. H. Fitzsimons | Sanitary Inspector | Public Health Department | — | — |
| 1886 | R. H. Fitzsimons | Sanitary Inspector | Public Health Department | — | — |
| 1886 | R. Fitzsimons | Inspector of Police (San Fernando), Inspector of Weights and Measures, and Supervisor | Police and Gaols | — | — |
| 1888 | R. H. Fitzsimons | Sanitary Inspector | Public Health Department | — | — |
| 1888 | R. Fitzsimons | Inspector of Police (San Fernando), Inspector of Weights and Measures, and Supervisor | Police and Gaols | — | — |
| 1889 | R. Fitzsimons | Inspector of Police (San Fernando), Inspector of Weights and Measures, and Supervisor | Police and Gaols | — | — |
| 1889 | R. H. Fitzsimons | Sanitary Inspector | Public Health Department | — | — |
| 1890 | R. Fitzsimons | Inspector of Police, Inspector of Weights and Measures, and Supervisor | Police and Gaols | — | — |
| 1890 | R. H. Fitzsimons | Inspector | Public Health Department | — | — |

### Deterministic checks: `fitzsimons_robert-henry_e1865` vs `Fitzsimons, R. H___Trinidad___1877`

- [PASS] surname_gate: bio 'FITZSIMONS' vs stint 'Fitzsimons, R. H' (exact)
- [PASS] initials: bio ['R', 'H'] ~ stint ['R', 'H']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Trinidad'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1890
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

