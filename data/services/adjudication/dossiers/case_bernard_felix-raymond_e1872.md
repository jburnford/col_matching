<!-- {"case_id": "case_bernard_felix-raymond_e1872", "bio_ids": ["bernard_felix-raymond_e1872"], "stint_ids": ["Bernard, F. R___Trinidad___1878"]} -->
# Dossier case_bernard_felix-raymond_e1872

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 12 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bernard_felix-raymond_e1872`

- Printed name: **BERNARD, FELIX RAYMOND**
- Birth year: not printed
- Appears in editions: [1886, 1888]

### Verbatim printed entry text (OCR)

**Version `col1886-L32154.v` — printed in editions [1886, 1888]:**

> BERNARD, FELIX RAYMOND.—Educated at Beaumont College, Berkshire; matriculated at the London University, 1872; first B.A., with honours in French, 1873; clerk in the audit office, Trinidad, 1st July, 1876; chief clerk to the registrar of the courts, 1st January, 1877; chief clerk in the surgeon-general's department, 4th Feb., 1878; acted as third master, Queen's Royal College, from 27 June, 1881, to 4 Oct., 1882.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1872–1872 | — | — | [1886, 1888] |
| 1 | 1873–1873 | — | — | [1886, 1888] |
| 2 | 1876–1876 | clerk in the audit office | Trinidad | [1886, 1888] |
| 3 | 1877–1877 | chief clerk to the registrar of the courts | — | [1886, 1888] |
| 4 | 1878–1878 | chief clerk in the surgeon-general's department | — | [1886, 1888] |
| 5 | 1881–1882 | third master | — | [1886, 1888] |

## Candidate stint `Bernard, F. R___Trinidad___1878`

- Staff-list name: **Bernard, F. R** | colony: **Trinidad** | listed 1878–1883 | editions [1878, 1880, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1878 | F. Bernard | Clerks to the Registrar | Judicial Department | — | — |
| 1880 | F. R. Bernard | 1st Clerk | Medical Establishment | — | — |
| 1883 | F. R. Bernard | 1st Clerk | Medical Establishment | — | — |

### Deterministic checks: `bernard_felix-raymond_e1872` vs `Bernard, F. R___Trinidad___1878`

- [PASS] surname_gate: bio 'BERNARD' vs stint 'Bernard, F. R' (exact)
- [PASS] initials: bio ['F', 'R'] ~ stint ['F', 'R']
- [PASS] age_gate: stint starts 1878; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Trinidad'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1878-1883
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

