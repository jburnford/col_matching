<!-- {"case_id": "case_sampson_victor_e1881", "bio_ids": ["sampson_victor_e1881"], "stint_ids": ["Sampson, Victor___Cape of Good Hope___1877", "Sampson, Victor___Cape of Good Hope___1899"]} -->
# Dossier case_sampson_victor_e1881

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 18 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['sampson_victor_e1881'] carry a single initial only — the namesake trap applies.

## Biography `sampson_victor_e1881`

- Printed name: **SAMPSON, VICTOR**
- Birth year: not printed
- Honours: K.C.
- Appears in editions: [1920, 1921, 1922, 1923, 1924, 1925]

### Verbatim printed entry text (OCR)

**Version `col1920-L56936.v` — printed in editions [1920, 1921, 1922, 1923, 1924, 1925]:**

> SAMPSON, HON. VICTOR, K.C.—Served for 10 years in Cape civil serv.; passed B.A. and LL.B. exams., and obtained first Chancellor's medal, Cape Univ.; called to the bar, 1881; holder of special retainer to De Beers, 1898, and later, director; returned to Cape parlmt., 1898; attorney-gen., 1904; ag. puisne judge, Eastern dist., 1911-12; puisne judge, Eastern Dist., 15th July, 1915.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1881 | called to the bar | — | [1920, 1921, 1922, 1923, 1924, 1925] |
| 1 | 1898 | holder of special retainer to De Beers | — | [1920, 1921, 1922, 1923, 1924, 1925] |
| 2 | 1898 | returned to Cape parlmt. | Cape | [1920, 1921, 1922, 1923, 1924, 1925] |
| 3 | 1904 | attorney-gen. | — | [1920, 1921, 1922, 1923, 1924, 1925] |
| 4 | 1911–1912 | ag. puisne judge | — | [1920, 1921, 1922, 1923, 1924, 1925] |
| 5 | 1915 | puisne judge | — | [1920, 1921, 1922, 1923, 1924, 1925] |

## Candidate stint `Sampson, Victor___Cape of Good Hope___1877`

- Staff-list name: **Sampson, Victor** | colony: **Cape of Good Hope** | listed 1877–1879 | editions [1877, 1878, 1879]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | V. Sampson | Assistant-Examiner of Accounts | Expenditure Branch | — | — |
| 1878 | V. Sampson | — | Expenditure Branch | — | — |
| 1879 | V. Sampson | — | Expenditure Branch | — | — |

### Deterministic checks: `sampson_victor_e1881` vs `Sampson, Victor___Cape of Good Hope___1877`

- [PASS] surname_gate: bio 'SAMPSON' vs stint 'Sampson, Victor' (exact)
- [PASS] initials: bio ['V'] ~ stint ['V']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1879
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Sampson, Victor___Cape of Good Hope___1899`

- Staff-list name: **Sampson, Victor** | colony: **Cape of Good Hope** | listed 1899–1907 | editions [1899, 1900, 1905, 1906, 1907]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1899 | Victor Sampson | Member | Constituency Members | — | — |
| 1900 | Victor Sampson | Member | Constituencies | — | — |
| 1905 | Victor Sampson | Attorney-General | Attorney-General's Office | — | — |
| 1906 | Victor Sampson | Attorney-General | Attorney-General's Office | — | — |
| 1907 | The Hon. Victor Sampson | Attorney-General | Attorney-General's Office | — | — |
| 1907 | Hon. Victor Sampson | Member | Constituency | — | — |

### Deterministic checks: `sampson_victor_e1881` vs `Sampson, Victor___Cape of Good Hope___1899`

- [PASS] surname_gate: bio 'SAMPSON' vs stint 'Sampson, Victor' (exact)
- [PASS] initials: bio ['V'] ~ stint ['V']
- [PASS] age_gate: stint starts 1899; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Cape of Good Hope'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1899-1907
- [FAIL] position_sim: best 32 vs bar 60: 'returned to Cape parlmt.' ~ 'Attorney-General'
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

