<!-- {"case_id": "case_cussen_leo-finn-bernard_b1859", "bio_ids": ["cussen_leo-finn-bernard_b1859"], "stint_ids": ["Cussen, L. F. B___Australia___1913", "Cussen, L. F. B___Victoria___1907"]} -->
# Dossier case_cussen_leo-finn-bernard_b1859

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `cussen_leo-finn-bernard_b1859`

- Printed name: **CUSSEN, LEO FINN BERNARD**
- Birth year: 1859 (attested in editions [1925])
- Honours: KT. BACH. (1922)
- Appears in editions: [1925, 1927, 1933]

### Verbatim printed entry text (OCR)

**Version `col1925-L55137.v` — printed in editions [1925]:**

> CUSSEN, SIR. LEO FINN BERNARD, KT. BACH. (1922).—B. 1859; judge of sup. ct., Victoria, since Mar., 1906. Cussen, Richard Cecil.—B. 1887; B.A., Dublin; cadet, F.M.S., 1911; ag. dist. offr., Jelebu, 1912; ag. asst. collr., land rev., Seremban, 1913; ag. asst. dist. offr., Lipis, 1913; ag. asst. dist. offr., Kualas Kubu, 1914; ag. dist. offr., Batang Padang, 1915; ag. dist. offr., Kroh, 1916; ag. dist. offr., Raub, 1917 and 1920; ag. dist. offr., Dindings, 1918; ag. 3rd mag., Singapore, 1919; mag., Seremban and asst. registr., sup. ct., 1920; ag. dep. commr., trade and cust., F.M.S., 1923; ag. dep. pub. pros., Perak, Nov., 1923.

**Version `col1933-L58988.v` — printed in editions [1933]:**

> CUSSEN, Sir Leo Finn Bernard, Kt. Bach. (1922).—B. 1859; judge of sup. ct., Victoria, since Mar., 1906.

**Version `col1927-L58201.v` — printed in editions [1927]:**

> CUSSSEN, Sir Leo Finn Bernard, K.T. Bach. (1922)—B. 1859; judge of sup. ct., Victoria, since Mar., 1906.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1906 | judge of sup. ct. | Victoria | [1925, 1927, 1933] |

## Candidate stint `Cussen, L. F. B___Australia___1913`

- Staff-list name: **Cussen, L. F. B** | colony: **Australia** | listed 1913–1927 | editions [1913, 1918, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1913 | L. F. B. Cussen | Puisne Judge | Law Department | — | — |
| 1918 | L. F. B. Cussen | Puisne Judge | Law Department | — | — |
| 1927 | Sir L. F. B. Cussen | Puisne Judge | Law Department | — | — |

### Deterministic checks: `cussen_leo-finn-bernard_b1859` vs `Cussen, L. F. B___Australia___1913`

- [PASS] surname_gate: bio 'CUSSEN' vs stint 'Cussen, L. F. B' (exact)
- [PASS] initials: bio ['L', 'F', 'B'] ~ stint ['L', 'F', 'B']
- [PASS] age_gate: stint starts 1913, birth 1859 (age 54)
- [FAIL] colony: no placed event resolves to 'Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1913-1927
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Cussen, L. F. B___Victoria___1907`

- Staff-list name: **Cussen, L. F. B** | colony: **Victoria** | listed 1907–1917 | editions [1907, 1917]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1907 | L. F. B. Cussen | Puisne Judge | Law Department | — | — |
| 1917 | L. F. B. Cussen | Puisne Judge | Law Department | — | — |

### Deterministic checks: `cussen_leo-finn-bernard_b1859` vs `Cussen, L. F. B___Victoria___1907`

- [PASS] surname_gate: bio 'CUSSEN' vs stint 'Cussen, L. F. B' (exact)
- [PASS] initials: bio ['L', 'F', 'B'] ~ stint ['L', 'F', 'B']
- [PASS] age_gate: stint starts 1907, birth 1859 (age 48)
- [PASS] colony: 1 placed event(s) resolve to 'Victoria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1907-1917
- [FAIL] position_sim: best 59 vs bar 60: 'judge of sup. ct.' ~ 'Puisne Judge'
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

