<!-- {"case_id": "case_black_kenneth-major_b1879", "bio_ids": ["black_kenneth-major_b1879"], "stint_ids": ["Black, K___Straits Settlements___1922"]} -->
# Dossier case_black_kenneth-major_b1879

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 60 official(s) with this surname in the graph's staff lists; 29 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `black_kenneth-major_b1879`

- Printed name: **BLACK, KENNETH MAJOR**
- Birth year: 1879 (attested in editions [1932, 1933, 1935])
- Appears in editions: [1932, 1933, 1934, 1935]

### Verbatim printed entry text (OCR)

**Version `col1932-L58425.v` — printed in editions [1932, 1933, 1935]:**

> BLACK, KENNETH MAJOR, F.R.C.S. (Eng.)—B. 1879; ed. St. Paul's Schl. and Guy's and St. Thomas's hosps.; med. offr., gen. hosp., S'pore, Apr., 1921; surg., native hosps., Aug., 1921; ophthalmologist, gen. hosp., in addn., Sept., 1921; prof., surgery, med. coll., S'pore, Apr., 1922; ag. sur. surgn., S'pore, Aug., 1923, Feb., 1926, June, 1928 and Apr., 1931.

**Version `col1934-L56720.v` — printed in editions [1934]:**

> BLACK, KENNETH MAJOR, F.R.C.S. B. 1879; ed. St. Paul's Schl. and Guy's Thomas's hosps.; med. offr., gen. hosp., Apr., 1921; surg., native hosps., Ag. ophthalmologist, gen. hosp., in addn. Sec. prot., surgery, med. coll., S'pore, Ag. ag. surg., S'pore, Aug., 1923; Fr. June, 1928 and Apr., 1931.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | med. offr., gen. hosp. | Singapore | [1932, 1933, 1934, 1935] |
| 1 | 1921 | surg., native hosps. | — | [1932, 1933, 1935] |
| 2 | 1921 | ophthalmologist, gen. hosp., in addn. | — | [1932, 1933, 1935] |
| 3 | 1922 | prof., surgery, med. coll. | Singapore | [1932, 1933, 1935] |
| 4 | 1923–1931 | ag. sur. surgn. | Singapore | [1932, 1933, 1934, 1935] |
| 5 | 1928–1931 | — | — | [1934] |

## Candidate stint `Black, K___Straits Settlements___1922`

- Staff-list name: **Black, K** | colony: **Straits Settlements** | listed 1922–1934 | editions [1922, 1923, 1925, 1931, 1933, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | K. Black | Medical Officer and Health Officer | Medical | — | — |
| 1923 | K. Black | Professor of Surgery | King Edward VII College of Medicine | — | — |
| 1925 | K. Black | Professor of Surgery | King Edward VII College of Medicine | — | — |
| 1931 | K. Black | Professor of Surgery | King Edward VII College of Medicine | — | — |
| 1933 | K. Black | Professor of Surgery | King Edward VII College of Medicine | — | — |
| 1934 | K. Black | Professor of Surgery | King Edward VII College of Medicine, Singapore | — | — |

### Deterministic checks: `black_kenneth-major_b1879` vs `Black, K___Straits Settlements___1922`

- [PASS] surname_gate: bio 'BLACK' vs stint 'Black, K' (exact)
- [PASS] initials: bio ['K', 'M'] ~ stint ['K']
- [PASS] age_gate: stint starts 1922, birth 1879 (age 43)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1922-1934
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

