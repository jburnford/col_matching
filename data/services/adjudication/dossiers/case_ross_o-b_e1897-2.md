<!-- {"case_id": "case_ross_o-b_e1897-2", "bio_ids": ["ross_o-b_e1897-2"], "stint_ids": ["Ross, O. B___Straits Settlements___1899"]} -->
# Dossier case_ross_o-b_e1897-2

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 140 official(s) with this surname in the graph's staff lists; 64 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `ross_o-b_e1897-2`

- Printed name: **ROSS, O.B**
- Birth year: not printed
- Honours: B.A
- Appears in editions: [1905, 1906]

### Verbatim printed entry text (OCR)

**Version `col1905-L45618.v` — printed in editions [1905, 1906]:**

> ROSS, O.B., B.A., Owens Coll., Manchester.—Cadet, S. Stlttns., Oct., 1897; ag. 3rd mag., Penang, Jan.-Nov., 1900; and from Feb., 1901; passed final exam. in Chinese, Jan., 1901; 4th mag., Sing., Jan., 1902; ag. dist. offr., Penang, Sept., 1902; passed cadet, 11th Feb., 1901; 4th mag., Singapore, 1st Jan., 1902; ag. 2nd asst. prot. of Chinese, Penang, 1903; ag. 3rd mag., Sing., Mar., 1905; ag. supt., money order branch, G.P.O., Sing., June, 1905.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1897 | Cadet, S. Stlttns | — | [1905, 1906] |
| 1 | 1900 | ag. 3rd mag., Penang, Jan.- | — | [1905, 1906] |
| 2 | 1901 | and from | — | [1905, 1906] |
| 3 | 1901 | passed final exam. in Chinese | — | [1905, 1906] |
| 4 | 1901 | passed cadet | — | [1905, 1906] |
| 5 | 1902 | 4th mag., Sing | Singapore | [1905, 1906] |
| 6 | 1902 | ag. dist. offr., Penang | — | [1905, 1906] |
| 7 | 1903 | ag. 2nd asst. prot. of Chinese, Penang | Singapore *(inherited from previous clause)* | [1905, 1906] |
| 8 | 1905 | ag. 3rd mag., Sing | Singapore *(inherited from previous clause)* | [1905, 1906] |

## Candidate stint `Ross, O. B___Straits Settlements___1899`

- Staff-list name: **Ross, O. B** | colony: **Straits Settlements** | listed 1899–1905 | editions [1899, 1905]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1899 | O. B. Ross | Cadet | Colonial Secretary's Department | — | — |
| 1905 | O. B. Ross | 4th Magistrate | Judicial Department | — | — |

### Deterministic checks: `ross_o-b_e1897-2` vs `Ross, O. B___Straits Settlements___1899`

- [PASS] surname_gate: bio 'ROSS' vs stint 'Ross, O. B' (exact)
- [PASS] initials: bio ['O', 'B'] ~ stint ['O', 'B']
- [PASS] age_gate: stint starts 1899; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1899-1905
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

