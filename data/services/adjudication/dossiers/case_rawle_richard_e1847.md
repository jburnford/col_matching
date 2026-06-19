<!-- {"case_id": "case_rawle_richard_e1847", "bio_ids": ["rawle_richard_e1847", "rawle_richard_e1872"], "stint_ids": ["Rawle, Rt. R. T___Trinidad___1877"]} -->
# Dossier case_rawle_richard_e1847

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['rawle_richard_e1847', 'rawle_richard_e1872'] carry a single initial only — the namesake trap applies.
- CONTESTED: stint(s) ['Rawle, Rt. R. T___Trinidad___1877'] have more than one claimant biography in this case.
- Phase 1 found `rawle_richard_e1847` ↔ `Rawle, Rt. R. T___Trinidad___1877` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).
- Phase 1 found `rawle_richard_e1872` ↔ `Rawle, Rt. R. T___Trinidad___1877` passed its evidence bar but dropped it as ambiguous (a comparable-strength competitor existed).

## Biography `rawle_richard_e1847`

- Printed name: **RAWLE, RICHARD**
- Birth year: not printed
- Appears in editions: [1886]

### Verbatim printed entry text (OCR)

**Version `col1886-L36038.v` — printed in editions [1886]:**

> TRINIDAD, 1st Bishop of, 1872.—RIGHT REV. RICHARD RAWLE, D.D.—Educated at Trin. Coll., Cambridge; B.A. as 3rd wrangler, 1865, and became fellow of his college; principal of Codrington College, Barbados, 1847; vicar of Tamworth, 1869-72.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1847 | principal of Codrington College | Barbados | [1886] |
| 1 | 1865 | fellow | — | [1886] |
| 2 | 1869–1872 | vicar | — | [1886] |
| 3 | 1872 | 1st Bishop | Trinidad | [1886] |

## Biography `rawle_richard_e1872`

- Printed name: **RAWLE, Richard**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L29794.v` — printed in editions [1883]:**

> TRINIDAD, BISHOP OF, 1872.—RIGHT REV. RICHARD RAWLE, M.A., formerly vicar of Tamworth.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1872 | Bishop of Trinidad | Trinidad | [1883] |

## Candidate stint `Rawle, Rt. R. T___Trinidad___1877`

- Staff-list name: **Rawle, Rt. R. T** | colony: **Trinidad** | listed 1877–1889 | editions [1877, 1878, 1879, 1880, 1886, 1888, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | R. Rawle | The Rt. Rev. | Ecclesiastical - Diocesan | — | — |
| 1878 | R. Rawle | Bishop and Rector of Holy Trinity | Ecclesiastical Establishment | — | — |
| 1879 | R. T. Rawle | Bishop of the Diocese | Ecclesiastical Establishment | — | — |
| 1880 | Rt. Rev. R. T. Rawle | Bishop of the Diocese | Church of England | M.A. | — |
| 1886 | Rt. Rev. R. Rawle | Bishop of the Diocese | Church of England | — | — |
| 1888 | Rt. Rev. R. Rawle | Bishop of the Diocese | Church of England | — | — |
| 1889 | R. Rawle | Bishop of the Diocese | — | — | — |

### Deterministic checks: `rawle_richard_e1847` vs `Rawle, Rt. R. T___Trinidad___1877`

- [PASS] surname_gate: bio 'RAWLE' vs stint 'Rawle, Rt. R. T' (exact)
- [PASS] initials: bio ['R'] ~ stint ['R', 'R', 'T']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Trinidad'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1889
- [PASS] position_sim: best 75 vs bar 60: '1st Bishop' ~ 'Bishop of the Diocese'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): 1 agreeing edition-year(s) [1886] pos~75 (bar: >=2)
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `rawle_richard_e1872` vs `Rawle, Rt. R. T___Trinidad___1877`

- [PASS] surname_gate: bio 'RAWLE' vs stint 'Rawle, Rt. R. T' (exact)
- [PASS] initials: bio ['R'] ~ stint ['R', 'R', 'T']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Trinidad'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1889
- [PASS] position_sim: best 67 vs bar 60: 'Bishop of Trinidad' ~ 'Bishop of the Diocese'
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

