<!-- {"case_id": "case_flutter_anthony-thomas_b1898", "bio_ids": ["flutter_anthony-thomas_b1898"], "stint_ids": ["Flutter, A. T___Gold Coast___1949", "Flutter, A. T___Northern Rhodesia___1930"]} -->
# Dossier case_flutter_anthony-thomas_b1898

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `flutter_anthony-thomas_b1898`

- Printed name: **FLUTTER, Anthony Thomas**
- Birth year: 1898 (attested in editions [1953, 1954])
- Honours: A.R.I.B.A
- Appears in editions: [1950, 1951, 1953, 1954]

### Verbatim printed entry text (OCR)

**Version `col1953-L17323.v` — printed in editions [1953, 1954]:**

> FLUTTER, A. T.—b. 1898; mil. serv., 1915-18; apptd. Nig., 1927; N. Rhod., 1929; G.C., 1937; town engnr., Accra, 1939; senr. exec. engnr., dept. of soc. welf. and housing, 1947; dir., housing, 1950.

**Version `col1950-L35454.v` — printed in editions [1950, 1951]:**

> FLUTTER, Anthony Thomas, A.R.I.B.A.—b. 1898; on war serv., 1915–18; apptd. Nig., 1927; N. Rhod., 1929; G.C., 1937; town engrn., Accra, 1939; senr. exec. engrn., dept. of soc. welf. and housing, 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | apptd. Nig | — | [1950, 1951, 1953, 1954] |
| 1 | 1929 | apptd. Nig | Northern Rhodesia | [1950, 1951, 1953, 1954] |
| 2 | 1937 | apptd. Nig | Gold Coast | [1950, 1951, 1953, 1954] |
| 3 | 1939 | town engnr., Accra | Gold Coast *(inherited from previous clause)* | [1950, 1951, 1953, 1954] |
| 4 | 1947 | senr. exec. engnr., dept. of soc. welf. and housing | Gold Coast *(inherited from previous clause)* | [1950, 1951, 1953, 1954] |
| 5 | 1950 | dir., housing | Gold Coast *(inherited from previous clause)* | [1953, 1954] |

## Candidate stint `Flutter, A. T___Gold Coast___1949`

- Staff-list name: **Flutter, A. T** | colony: **Gold Coast** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | A. T. Flutter | Senior Executive Engineer | Housing | — | — |
| 1951 | A. T. Flutter | Chief Executive Engineer | HOUSING | — | — |

### Deterministic checks: `flutter_anthony-thomas_b1898` vs `Flutter, A. T___Gold Coast___1949`

- [PASS] surname_gate: bio 'FLUTTER' vs stint 'Flutter, A. T' (exact)
- [PASS] initials: bio ['A', 'T'] ~ stint ['A', 'T']
- [PASS] age_gate: stint starts 1949, birth 1898 (age 51)
- [PASS] colony: 4 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 49 vs bar 60: 'senr. exec. engnr., dept. of soc. welf. and housing' ~ 'Senior Executive Engineer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Flutter, A. T___Northern Rhodesia___1930`

- Staff-list name: **Flutter, A. T** | colony: **Northern Rhodesia** | listed 1930–1936 | editions [1930, 1931, 1933, 1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1930 | A. T. Flutter | Architect | Public Works Department | — | — |
| 1931 | A. T. Flutter | Architect | Loan Staff (Headquarters) Buildings | — | — |
| 1933 | A. T. Flutter | Architect | Loan Staff (Headquarters), Buildings | — | — |
| 1934 | A. T. Flutter | Architect | Public Works Department | — | — |
| 1936 | A. T. Flutter | Architect | Public Works Department | — | — |

### Deterministic checks: `flutter_anthony-thomas_b1898` vs `Flutter, A. T___Northern Rhodesia___1930`

- [PASS] surname_gate: bio 'FLUTTER' vs stint 'Flutter, A. T' (exact)
- [PASS] initials: bio ['A', 'T'] ~ stint ['A', 'T']
- [PASS] age_gate: stint starts 1930, birth 1898 (age 32)
- [PASS] colony: 1 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1930-1936
- [FAIL] position_sim: best 22 vs bar 60: 'apptd. Nig' ~ 'Architect'
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

