<!-- {"case_id": "case_padmore_w_e1839", "bio_ids": ["padmore_w_e1839"], "stint_ids": ["Padmore, William___Leeward Islands___1877"]} -->
# Dossier case_padmore_w_e1839

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['padmore_w_e1839'] carry a single initial only — the namesake trap applies.

## Biography `padmore_w_e1839`

- Printed name: **PADMORE, W.**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L28989.v` — printed in editions [1883]:**

> PADMORE, W.—Clerk in customs, Jamaica, 1839; clerk and warehouse keeper, St. Christopher, 1842; acted as collector of customs, 1845 and 1848; clerk and assistant comptroller of customs and navigation laws, Barbados, 1853; acted as comptroller, 1854; pensioned, Jan. 1855, on abolition of customs in West Indies; notary public, St. Christopher, 1858; superintendent of immigrants, 1858; private secretary to Sir B. C. C. Pine; clerk to executive council and administrative committee, 17th June, 1865; clerk to office of auditor-general, 1866; provost-marshal, 1868; registrar of the supreme court, May, 1875, in conjunction with office of provost-marshal.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1839–1839 | Clerk in customs | Jamaica | [1883] |
| 1 | 1842–1842 | clerk and warehouse keeper | St. Christopher | [1883] |
| 2 | 1845–1848 | acted as collector of customs | — | [1883] |
| 3 | 1853–1853 | clerk and assistant comptroller of customs and navigation laws | Barbados | [1883] |
| 4 | 1854–1854 | acted as comptroller | — | [1883] |
| 5 | 1855–1855 | pensioned | West Indies | [1883] |
| 6 | 1858–1858 | notary public | St. Christopher | [1883] |
| 7 | 1858–1858 | superintendent of immigrants | — | [1883] |
| 8 | 1865–1865 | clerk to executive council and administrative committee | — | [1883] |
| 9 | 1866–1866 | clerk to office of auditor-general | — | [1883] |
| 10 | 1868–1868 | provost-marshal | — | [1883] |
| 11 | 1875–1875 | registrar of the supreme court | — | [1883] |

## Candidate stint `Padmore, William___Leeward Islands___1877`

- Staff-list name: **Padmore, William** | colony: **Leeward Islands** | listed 1877–1886 | editions [1877, 1878, 1879, 1880, 1883, 1886]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | W. Padmore | Provost Marshal and Registrar | Civil Establishment | — | — |
| 1877 | William Padmore | — | Board of Health | — | — |
| 1878 | W. Padmore | Provost Marshal and Registrar | Civil Establishment | — | — |
| 1878 | William Padmore | Board member | Board of Health Act, 145, 1858 | — | — |
| 1879 | W. Padmore | Provost Marshal and Registrar | Civil Establishment | — | — |
| 1879 | William Padmore | Board Member | Board of Health | — | — |
| 1880 | W. Padmore | Provost Marshal and Registrar | Civil Establishment | — | — |
| 1880 | William Padmore | Board Member | Board of Health Act, 145, 1858 | — | — |
| 1883 | William Padmore | Esquire | Quarantine Board | — | — |
| 1883 | William Padmore | Board Member | Board of Health Act, No. 145, 1858 | — | — |
| 1886 | William Padmore | — | — | — | — |
| 1886 | William Padmore | Member | Board of Health Act | — | — |

### Deterministic checks: `padmore_w_e1839` vs `Padmore, William___Leeward Islands___1877`

- [PASS] surname_gate: bio 'PADMORE' vs stint 'Padmore, William' (exact)
- [PASS] initials: bio ['W'] ~ stint ['W']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1886
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

