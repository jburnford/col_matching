<!-- {"case_id": "case_chubb_e-f_e1875", "bio_ids": ["chubb_e-f_e1875"], "stint_ids": ["Chubb, E. F___British Guiana___1878"]} -->
# Dossier case_chubb_e-f_e1875

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `chubb_e-f_e1875`

- Printed name: **CHUBB, E. F.**
- Birth year: not printed
- Appears in editions: [1883, 1886, 1888, 1889, 1890, 1894]

### Verbatim printed entry text (OCR)

**Version `col1888-L32633.v` — printed in editions [1888, 1889, 1890, 1894]:**

> CHUBB, E. F.—Clerk in the central board of villages department, British Guiana, Jan., 1875; accountant in provost marshal's office, 5th Sept., 1878; acting first marshal Feb. to Sept., 1879; and Oct., 1885, to Oct., 1886, Dec., 1886, to Feb., 1887; and June, 1888, to Feb., 1889.

**Version `col1883-L26835.v` — printed in editions [1883, 1886]:**

> CHUBB, E. F.—Clerk in the central board of villages department, British Guiana, January, 1875; accountant in provost marshal's office, 5th September, 1878; acted as first marshal from 5th February to 2nd September, 1879.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1875 | Clerk in the central board of villages department | British Guiana | [1883, 1886, 1888, 1889, 1890, 1894] |
| 1 | 1878 | accountant in provost marshal's office | British Guiana *(inherited from previous clause)* | [1883, 1886, 1888, 1889, 1890, 1894] |
| 2 | 1879–1879 | acting first marshal | British Guiana *(inherited from previous clause)* | [1883, 1886, 1888, 1889, 1890, 1894] |
| 3 | 1885–1886 | acting first marshal | — | [1888, 1889, 1890, 1894] |
| 4 | 1886–1887 | acting first marshal | — | [1888, 1889, 1890, 1894] |
| 5 | 1888–1889 | acting first marshal | — | [1888, 1889, 1890, 1894] |

## Candidate stint `Chubb, E. F___British Guiana___1878`

- Staff-list name: **Chubb, E. F** | colony: **British Guiana** | listed 1878–1889 | editions [1878, 1880, 1883, 1886, 1888, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1878 | E. F. Chubb | Accountant | Villages | — | — |
| 1880 | E. F. Chubb | Accountant | Judicial Establishment | — | — |
| 1883 | E. F. Chubb | Accountant | Judicial Establishment | — | — |
| 1886 | E. F. Chubb | Ordinary Marshal | Judicial Establishment | — | — |
| 1888 | E. F. Chubb | Ordinary Marshal | Judicial Establishment | — | — |
| 1889 | E. F. Chubb | Ordinary Marshal | Judicial Establishment | — | — |

### Deterministic checks: `chubb_e-f_e1875` vs `Chubb, E. F___British Guiana___1878`

- [PASS] surname_gate: bio 'CHUBB' vs stint 'Chubb, E. F' (exact)
- [PASS] initials: bio ['E', 'F'] ~ stint ['E', 'F']
- [PASS] age_gate: stint starts 1878; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'British Guiana'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1878-1889
- [PASS] position_sim: best 100 vs bar 60: 'accountant in provost marshal's office' ~ 'Accountant'
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

