<!-- {"case_id": "case_gawthorn_w-r_e1847", "bio_ids": ["gawthorn_w-r_e1847"], "stint_ids": ["Gawthorn, W___Trinidad___1877"]} -->
# Dossier case_gawthorn_w-r_e1847

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `gawthorn_w-r_e1847`

- Printed name: **GAWTHORN, W. R.**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L27618.v` — printed in editions [1883]:**

> GAWTHORN, W. R.—Clerk in the Colonial Land and Emigration Office, 1847; private secretary and librarian to Cardinal Wiseman, April, 1852; private secretary to Archbishop English (Trinidad), Nov., 1861; chief clerk of the health office, Port of Spain, Nov., 1871; acting corresponding clerk of the public works department, July, 1873; chief clerk of the petty civil court of Port of Spain, Aug., 1872; was editor of the Star of the West newspaper for thirteen years, and of the Grenadian for six months; received a gratuity from the government of Trinidad, in 1872, for his services during the small pox epidemic in that colony; professor of English at the college and convent for five years.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1847 | Clerk in the Colonial Land and Emigration Office | — | [1883] |
| 1 | 1852 | private secretary and librarian to Cardinal Wiseman | — | [1883] |
| 2 | 1861 | private secretary to Archbishop English | Trinidad | [1883] |
| 3 | 1871 | chief clerk of the health office | Trinidad | [1883] |
| 4 | 1872 | chief clerk of the petty civil court of Port of Spain | Trinidad | [1883] |
| 5 | 1873 | acting corresponding clerk of the public works department | — | [1883] |

## Candidate stint `Gawthorn, W___Trinidad___1877`

- Staff-list name: **Gawthorn, W** | colony: **Trinidad** | listed 1877–1880 | editions [1877, 1878, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | W. Gawthorn | 1st Clerk | Judicial Department | — | — |
| 1878 | W. Gawthorn | 1st Clerk | Judicial Department | — | — |
| 1879 | W. Gawthorn | 1st Clerk | Judicial Department | — | — |
| 1880 | W. Gawthorn | 1st Clerk | Judicial Department | — | — |

### Deterministic checks: `gawthorn_w-r_e1847` vs `Gawthorn, W___Trinidad___1877`

- [PASS] surname_gate: bio 'GAWTHORN' vs stint 'Gawthorn, W' (exact)
- [PASS] initials: bio ['W', 'R'] ~ stint ['W']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'Trinidad'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1880
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

