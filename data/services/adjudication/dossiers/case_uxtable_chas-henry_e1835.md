<!-- {"case_id": "case_uxtable_chas-henry_e1835", "bio_ids": ["uxtable_chas-henry_e1835"], "stint_ids": ["Huxtable, C. H___Tasmania___1888"]} -->
# Dossier case_uxtable_chas-henry_e1835

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `uxtable_chas-henry_e1835`

- Printed name: **UXTABLE, CHAS. HENRY**
- Birth year: not printed
- Appears in editions: [1897]

### Verbatim printed entry text (OCR)

**Version `col1897-L32658.v` — printed in editions [1897]:**

> UXTABLE, CHAS. HENRY.—Clerk in British Consulate, Terceira, Azores, 1835-9; entered civil service in Tasmania in accntt. of stores, Aug., 1856; colonial storekeeper, Jan., 1860; dist. offr., Sth. Malacca, June, 1880; ditto, N. Malacca, June, 1890; assist. Indian immigration agent, Malacca, June, 1889; ag. collr. land rev. and magis., Malacca, June to Nov., 1892; passed exam. in Dutch, 1893; ag. collr. land rev., Singapore, Feb., 1894, acted also as mag., Oct., 1894 to July 1895, and as offl. assignee, and reg. of deeds, July to Oct., 1895; ag. asst. col. sec., Oct. to Dec., 1895; ag. collr. land rev. and offl. in charge of treas., also ag. mag. and dep. regr. sup. et al., Malacca, Mar., 1896.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1835–1839 | Clerk | Azores | [1897] |
| 1 | 1856 | civil service | Tasmania | [1897] |
| 2 | 1860 | colonial storekeeper | — | [1897] |
| 3 | 1880 | dist. offr. | Malacca | [1897] |
| 4 | 1889 | assist. Indian immigration agent | Malacca | [1897] |
| 5 | 1890 | dist. offr. | Malacca | [1897] |
| 6 | 1892–1892 | ag. collr. land rev. and magis. | Malacca | [1897] |
| 7 | 1893 | — | — | [1897] |
| 8 | 1894 | ag. collr. land rev. | Singapore | [1897] |
| 9 | 1894–1895 | mag. | — | [1897] |
| 10 | 1895–1895 | offl. assignee, and reg. of deeds | — | [1897] |
| 11 | 1895–1895 | ag. asst. col. sec. | — | [1897] |
| 12 | 1896 | ag. collr. land rev. and offl. in charge of treas., also ag. mag. and dep. regr. sup. et al. | Malacca | [1897] |

## Candidate stint `Huxtable, C. H___Tasmania___1888`

- Staff-list name: **Huxtable, C. H** | colony: **Tasmania** | listed 1888–1889 | editions [1888, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | C. H. Huxtable | Colonial Storekeeper | Office of Stores | — | — |
| 1889 | C. H. Huxtable | Colonial Storekeeper | Offices of Stores | — | — |

### Deterministic checks: `uxtable_chas-henry_e1835` vs `Huxtable, C. H___Tasmania___1888`

- [PASS] surname_gate: bio 'UXTABLE' vs stint 'Huxtable, C. H' (fuzzy:1)
- [PASS] initials: bio ['C', 'H'] ~ stint ['C', 'H']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Tasmania'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1888-1889
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

