<!-- {"case_id": "case_nolan_j-f_e1870", "bio_ids": ["nolan_j-f_e1870"], "stint_ids": ["Nolan, J. F___Victoria___1879"]} -->
# Dossier case_nolan_j-f_e1870

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `nolan_j-f_e1870`

- Printed name: **NOLAN, J. F**
- Birth year: not printed
- Appears in editions: [1886, 1888, 1889]

### Verbatim printed entry text (OCR)

**Version `col1886-L35030.v` — printed in editions [1886, 1888, 1889]:**

> NOLAN, J. F.—County court judge, Victoria, 21st March, 1870.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1870 | County court judge | Victoria | [1886, 1888, 1889] |

## Candidate stint `Nolan, J. F___Victoria___1879`

- Staff-list name: **Nolan, J. F** | colony: **Victoria** | listed 1879–1883 | editions [1879, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1879 | J. F. Nolan | Judges of County Courts, Courts of Mines, Courts of Insolvency, and Chairmen of General Sessions | County Courts, Courts of Insolvency, Courts of Mines, and General Sessions | — | — |
| 1883 | J. F. Nolan | Judges of County Courts, Courts of Mines, Courts of Insolvency, and Chairmen of General Sessions | County Courts, Courts of Insolvency, Courts of Mines, and General Sessions | — | — |

### Deterministic checks: `nolan_j-f_e1870` vs `Nolan, J. F___Victoria___1879`

- [PASS] surname_gate: bio 'NOLAN' vs stint 'Nolan, J. F' (exact)
- [PASS] initials: bio ['J', 'F'] ~ stint ['J', 'F']
- [PASS] age_gate: stint starts 1879; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Victoria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1879-1883
- [FAIL] position_sim: best 50 vs bar 60: 'County court judge' ~ 'Judges of County Courts, Courts of Mines, Courts of Insolvency, and Chairmen of General Sessions'
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

