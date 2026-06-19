<!-- {"case_id": "case_hamblin_fred-hardcourt_e1857", "bio_ids": ["hamblin_fred-hardcourt_e1857"], "stint_ids": ["Hamblin, F. H___Trinidad___1877"]} -->
# Dossier case_hamblin_fred-hardcourt_e1857

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hamblin_fred-hardcourt_e1857`

- Printed name: **HAMBLIN, FRED., HARDCOURT**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L27833.v` — printed in editions [1883]:**

> HAMBLIN, FRED., HARDCOURT.—Private secretary to Mr. Longden during his administration of the Government of British Honduras from November, 1857, to May, 1870, and accompanied him in the same capacity to Trinidad, and served till March, 1874, when he again accompanied Mr. Longden as private secretary to British Guiana. Was private secretary to Lieut.-Governor Rennie during his administration of the Government of Trinidad in 1872-73; stipendiary magistrate, county Caroni, May, 1875; now stipendiary magistrate, Eastern District, county St. George.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1857–1870 | Private secretary | British Honduras | [1883] |
| 1 | 1870–1874 | private secretary | Trinidad | [1883] |
| 2 | 1872–1873 | private secretary | Trinidad | [1883] |
| 3 | 1874 | private secretary | British Guiana | [1883] |
| 4 | 1875 | stipendiary magistrate | — | [1883] |
| 5 | ? | stipendiary magistrate | — | [1883] |

## Candidate stint `Hamblin, F. H___Trinidad___1877`

- Staff-list name: **Hamblin, F. H** | colony: **Trinidad** | listed 1877–1879 | editions [1877, 1878, 1879]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | F. H. Hamblin | Stipendiary Justice, County Caroni | Judicial Department | — | — |
| 1878 | F. H. Hamblin | Stipendiary Justice | Stipendiary Justices | — | — |
| 1879 | F. H. Hamblin | Stipendiary Justice | Stipendiary Justices | — | — |

### Deterministic checks: `hamblin_fred-hardcourt_e1857` vs `Hamblin, F. H___Trinidad___1877`

- [PASS] surname_gate: bio 'HAMBLIN' vs stint 'Hamblin, F. H' (exact)
- [PASS] initials: bio ['F', 'H'] ~ stint ['F', 'H']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Trinidad'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1879
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

