<!-- {"case_id": "case_sharples_ovid-edgar-leland_b1878", "bio_ids": ["sharples_ovid-edgar-leland_b1878"], "stint_ids": ["Sharples, O. E. L___British Guiana___1911"]} -->
# Dossier case_sharples_ovid-edgar-leland_b1878

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `sharples_ovid-edgar-leland_b1878`

- Printed name: **SHARPLES, OVID EDGAR LELAND**
- Birth year: 1878 (attested in editions [1917, 1918])
- Appears in editions: [1917, 1918]

### Verbatim printed entry text (OCR)

**Version `col1917-L53086.v` — printed in editions [1917, 1918]:**

> SHARPLES, OVID EDGAR LELAND.—B. 1878; ed. private schl., Kent, and St. John's Coll., Camb.; B.A., LL.B., 1899; M.A., 1902; called to the bar, Middle Temple, 1902; practised at bar, Br. Guiana; ag. stip. mag., Br. Guiana, 1906; stip. mag., 1910; comsrr. for oaths, 1912; ag. solr.-gen., 1914; acted at various times as registering offr., revising barrister and returning offr.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1899 | B.A., LL.B | — | [1917, 1918] |
| 1 | 1902 | M.A | — | [1917, 1918] |
| 2 | 1902 | called to the bar, Middle Temple | — | [1917, 1918] |
| 3 | 1906 | ag. stip. mag. | British Guiana | [1917, 1918] |
| 4 | 1910 | stip. mag | British Guiana *(inherited from previous clause)* | [1917, 1918] |
| 5 | 1912 | comsrr. for oaths | British Guiana *(inherited from previous clause)* | [1917, 1918] |
| 6 | 1914 | ag. solr.-gen | British Guiana *(inherited from previous clause)* | [1917, 1918] |

## Candidate stint `Sharples, O. E. L___British Guiana___1911`

- Staff-list name: **Sharples, O. E. L** | colony: **British Guiana** | listed 1911–1917 | editions [1911, 1912, 1913, 1914, 1915, 1917]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1911 | O. E. L. Sharples | Stipendiary Magistrates | Judicial Establishment | — | — |
| 1912 | O. E. L. Sharples | Stipendiary Magistrate | Judicial Establishment | — | — |
| 1913 | O. E. L. Sharples | Stipendiary Magistrates | Judicial Establishment | — | — |
| 1914 | O. E. L. Sharples | Stipendiary Magistrate | Judicial Establishment | — | — |
| 1915 | O. E. L. Sharples | Stipendiary Magistrate | Judicial Establishment | — | — |
| 1917 | O. E. L. Sharples | District Stipendiary Magistrate | Judicial Establishment | — | — |

### Deterministic checks: `sharples_ovid-edgar-leland_b1878` vs `Sharples, O. E. L___British Guiana___1911`

- [PASS] surname_gate: bio 'SHARPLES' vs stint 'Sharples, O. E. L' (exact)
- [PASS] initials: bio ['O', 'E', 'L'] ~ stint ['O', 'E', 'L']
- [PASS] age_gate: stint starts 1911, birth 1878 (age 33)
- [PASS] colony: 4 placed event(s) resolve to 'British Guiana'
- [PASS] tenure_overlap: 4 event tenure(s) overlap stint years 1911-1917
- [FAIL] position_sim: best 53 vs bar 60: 'stip. mag' ~ 'Stipendiary Magistrate'
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

