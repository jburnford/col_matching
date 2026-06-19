<!-- {"case_id": "case_barclay_colville-a-d_e1846", "bio_ids": ["barclay_colville-a-d_e1846"], "stint_ids": ["Barclay, A___Cyprus___1929"]} -->
# Dossier case_barclay_colville-a-d_e1846

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 10 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Barclay, A___Cyprus___1929` is also gate-compatible with biography(ies) outside this case: ['barclay_alexander-henry_e1898'] (already linked elsewhere or filtered).

## Biography `barclay_colville-a-d_e1846`

- Printed name: **BARCLAY, Colville A. D.**
- Birth year: not printed
- Honours: C.M.G. (1878)
- Terminal: Retired 1877 — “Retired, 1877.”
- Appears in editions: [1883, 1886, 1888, 1889, 1890, 1894]

### Verbatim printed entry text (OCR)

**Version `col1883-L26323.v` — printed in editions [1883, 1886, 1888, 1889, 1890, 1894]:**

> BARCLAY, Colville A. D., C.M.G. (1878).—Volunteer treasury, Mauritius, 26th March, 1846; extra clerk treasury, 21st Feb., 1848; transferred to savings bank, 15th May, 1848; manager of ditto, 1st April, 1851; acting officer of civil status, 1st Feb., 1860; officer in charge of treasury, 28th Aug., 1860; resumed duties as manager of savings bank, 1st May, 1861; acting treasurer, March, 1863; resumed duties as manager of savings bank, May, 1865; acting collector of customs, July, 1867; collector of customs, May, 1870; acting treasurer and collector of internal revenues, July, 1871; auditor-general of Ceylon, 1876. Retired, 1877.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1846 | Volunteer treasury | Mauritius | [1883, 1886, 1888, 1889, 1890, 1894] |
| 1 | 1848 | extra clerk treasury | — | [1883, 1886, 1888, 1889, 1890, 1894] |
| 2 | 1848 | transferred to savings bank | — | [1883, 1886, 1888, 1889, 1890, 1894] |
| 3 | 1851 | manager of ditto | — | [1883, 1886, 1888, 1889, 1890, 1894] |
| 4 | 1860 | acting officer of civil status | — | [1883, 1886, 1888, 1889, 1890, 1894] |
| 5 | 1860 | officer in charge of treasury | — | [1883, 1886, 1888, 1889, 1890, 1894] |
| 6 | 1861 | resumed duties as manager of savings bank | — | [1883, 1886, 1888, 1889, 1890, 1894] |
| 7 | 1863 | acting treasurer | — | [1883, 1886, 1888, 1889, 1890, 1894] |
| 8 | 1865 | resumed duties as manager of savings bank | — | [1883, 1886, 1888, 1889, 1890, 1894] |
| 9 | 1867 | acting collector of customs | — | [1883, 1886, 1888, 1889, 1890, 1894] |
| 10 | 1870 | collector of customs | — | [1883, 1886, 1888, 1889, 1890, 1894] |
| 11 | 1871 | acting treasurer and collector of internal revenues | — | [1883, 1886, 1888, 1889, 1890, 1894] |
| 12 | 1876 | auditor-general | Ceylon | [1883, 1886, 1888, 1889, 1890, 1894] |

## Candidate stint `Barclay, A___Cyprus___1929`

- Staff-list name: **Barclay, A** | colony: **Cyprus** | listed 1929–1934 | editions [1929, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | Miss A. Barclay | Nursing Sister | Department of Health | — | — |
| 1934 | A. Barclay | Matrons | Department of Health | — | — |

### Deterministic checks: `barclay_colville-a-d_e1846` vs `Barclay, A___Cyprus___1929`

- [PASS] surname_gate: bio 'BARCLAY' vs stint 'Barclay, A' (exact)
- [PASS] initials: bio ['C', 'A', 'D'] ~ stint ['A']
- [PASS] age_gate: stint starts 1929; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Cyprus'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1929-1934
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

