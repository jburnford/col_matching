<!-- {"case_id": "case_orpen_francis-henry-samuel_e1850", "bio_ids": ["orpen_francis-henry-samuel_e1850"], "stint_ids": ["Orpen, F. H. S___Griqualand West___1877"]} -->
# Dossier case_orpen_francis-henry-samuel_e1850

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 16 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `orpen_francis-henry-samuel_e1850`

- Printed name: **ORPEN, Francis Henry Samuel**
- Birth year: not printed
- Honours: F.R.A.S., F.R.G.S.
- Terminal: retired 1881 — “retired on pension 13th Jan., 1881, in consequence of the annexation of Griqualand West to the Cape Colony”
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L28964.v` — printed in editions [1883]:**

> ORPEN, Francis Henry Samuel, F.R.A.S., F.R.G.S.—Educated at Trinity College, Dublin; member of the commission of surveyors for the survey of the Orange River sovereignty (now Orange Free State), June, 1850; entered the service of the chief N. Waterboer as surveyor-general, and civil commissioner of Albania, 14th Sept., 1867, and on the cession of the province to the British Government, was appointed civil commissioner and resident magistrate of the division of Griquatown, with charge of the survey department, 8th November, 1871; commissioner for investigating and defining native claims to land, January to June, 1873, and October and November, 1876; commissioner for defining native locations and investigating land claims, February to June, 1877; acting registrar of deeds, June, 1878, to March, 1879; inspector of schools, January to Dec., 1879; retired on pension 13th Jan., 1881, in consequence of the annexation of Griqualand West to the Cape Colony; and was at once elected member for Barkly, of the Cape legislative assembly, in the first Cape parliament (1881), in which Griqualand was represented; and also first president of the South African institution of civil engineers, architects, and surveyors.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1850–1850 | member of the commission of surveyors | Orange Free State | [1883] |
| 1 | 1867–1867 | surveyor-general, and civil commissioner | Albania | [1883] |
| 2 | 1871–1871 | civil commissioner and resident magistrate | Griquatown | [1883] |
| 3 | 1873–1876 | commissioner for investigating and defining native claims to land | — | [1883] |
| 4 | 1877–1877 | commissioner for defining native locations and investigating land claims | — | [1883] |
| 5 | 1878–1879 | acting registrar of deeds | — | [1883] |
| 6 | 1879–1879 | inspector of schools | — | [1883] |
| 7 | 1881–1881 | member for Barkly, of the Cape legislative assembly | Cape Colony | [1883] |

## Candidate stint `Orpen, F. H. S___Griqualand West___1877`

- Staff-list name: **Orpen, F. H. S** | colony: **Griqualand West** | listed 1877–1880 | editions [1877, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | F. H. S. Orpen | Surveyor-General | Surveyor-General's Office | — | — |
| 1880 | F. H. S. Orpen | Surveyor-General | Surveyor-General's Office | — | — |

### Deterministic checks: `orpen_francis-henry-samuel_e1850` vs `Orpen, F. H. S___Griqualand West___1877`

- [PASS] surname_gate: bio 'ORPEN' vs stint 'Orpen, F. H. S' (exact)
- [PASS] initials: bio ['F', 'H', 'S'] ~ stint ['F', 'H', 'S']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Griqualand West'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1880
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

