<!-- {"case_id": "case_barkley_henry_e1845", "bio_ids": ["barkley_henry_e1845"], "stint_ids": ["Bartley, A. H___British Guiana___1878", "Bartley, A. H___British Honduras___1949"]} -->
# Dossier case_barkley_henry_e1845

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['barkley_henry_e1845'] carry a single initial only — the namesake trap applies.

## Biography `barkley_henry_e1845`

- Printed name: **BARKLEY, HENRY**
- Birth year: not printed
- Honours: G.C.M.G. (1874), K.C.B. (Civil) (1853)
- Terminal: retired (year not printed) — “retired on pension”
- Appears in editions: [1894]

### Verbatim printed entry text (OCR)

**Version `col1894-L30169.v` — printed in editions [1894]:**

> BARKLEY, SIR HENRY, G.C.M.G. (1874), K.C.B. (Civil 1853).—Was M.P. for Leominster from April, 1845, to Feb., 1849; governor and commander-in-chief of British Guiana, Dec., 1848; capt.-general and governor-in-chief of Jamaica, Aug., 1853; governor of Victoria, 1856; received the order of the Bath after services in British Guiana governor of Mauritius, August, 1863; governor, Cape of Good Hope, 1870, to 31st March, 1877; retired on pension. Was a member of the Royal Commission on the defence of British possessions and commerce abroad, 8th September, 1879.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1845–1849 | M.P. | Leominster | [1894] |
| 1 | 1848 | governor and commander-in-chief | British Guiana | [1894] |
| 2 | 1853 | capt.-general and governor-in-chief | Jamaica | [1894] |
| 3 | 1856 | governor | Victoria | [1894] |
| 4 | 1863 | governor | Mauritius | [1894] |
| 5 | 1870–1877 | governor | Cape of Good Hope | [1894] |
| 6 | 1879 | member of the Royal Commission on the defence of British possessions and commerce abroad | — | [1894] |

## Candidate stint `Bartley, A. H___British Guiana___1878`

- Staff-list name: **Bartley, A. H** | colony: **British Guiana** | listed 1878–1890 | editions [1878, 1879, 1880, 1883, 1886, 1888, 1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1878 | A. H. Bartley | Secretary to Board of Education | Education | — | — |
| 1879 | A. H. Bartley | Assistant Inspectors and District Educational Officers | Education | — | — |
| 1880 | A. H. Bartley | Assistant Inspectors and District Educational Officers | Education | — | — |
| 1883 | A. H. Bartley | Assistant Inspector and District Educational Officer | Education | — | — |
| 1886 | A. H. Bartley | Assistant Inspector and District Educational Officer | Education | — | — |
| 1888 | A. H. Bartley | Assistant Inspector and District Educational Officer | Education | — | — |
| 1889 | A. H. Bartley | Assistant Inspector and District Educational Officer | Education | — | — |
| 1890 | A. H. Bartley | Assistant Inspector | Education | — | — |

### Deterministic checks: `barkley_henry_e1845` vs `Bartley, A. H___British Guiana___1878`

- [PASS] surname_gate: bio 'BARKLEY' vs stint 'Bartley, A. H' (fuzzy:1)
- [PASS] initials: bio ['H'] ~ stint ['A', 'H']
- [PASS] age_gate: stint starts 1878; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1878-1890
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Bartley, A. H___British Honduras___1949`

- Staff-list name: **Bartley, A. H** | colony: **British Honduras** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | A. H. Bartley | Medical Officer | MEDICAL | — | — |
| 1950 | A. H. Bartley | Medical Officer | Medical | — | — |

### Deterministic checks: `barkley_henry_e1845` vs `Bartley, A. H___British Honduras___1949`

- [PASS] surname_gate: bio 'BARKLEY' vs stint 'Bartley, A. H' (fuzzy:1)
- [PASS] initials: bio ['H'] ~ stint ['A', 'H']
- [PASS] age_gate: stint starts 1949; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'British Honduras'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1950
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

