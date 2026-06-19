<!-- {"case_id": "case_packard_edward-turner_b1868", "bio_ids": ["packard_edward-turner_b1868"], "stint_ids": ["Packard, E. T___Sierra Leone___1905"]} -->
# Dossier case_packard_edward-turner_b1868

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `packard_edward-turner_b1868`

- Printed name: **PACKARD, Edward Turner**
- Birth year: 1868 (attested in editions [1909, 1910])
- Appears in editions: [1909, 1910]

### Verbatim printed entry text (OCR)

**Version `col1909-L48857.v` — printed in editions [1909, 1910]:**

> PACKARD, Edward Turner.—B. 1868; ed. at Ipswich and Trin. Coll., Oxford; scholar at Oxford, hons. in law; called to the bar, Inner Temple, 1892; served with I.Y. in S. Africa, 1901; solr.-gen., S. Leone, 1901; atty.-gen., S. Leone, 1902; puisne judge, S. Nigeria, 1908.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1892 | called to the bar, Inner Temple | — | [1909, 1910] |
| 1 | 1901 | served with I.Y. in S. Africa | — | [1909, 1910] |
| 2 | 1901 | solr.-gen., S. Leone | — | [1909, 1910] |
| 3 | 1902 | atty.-gen., S. Leone | — | [1909, 1910] |
| 4 | 1908 | puisne judge | Southern Nigeria | [1909, 1910] |

## Candidate stint `Packard, E. T___Sierra Leone___1905`

- Staff-list name: **Packard, E. T** | colony: **Sierra Leone** | listed 1905–1908 | editions [1905, 1907, 1908]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | E. T. Packard | Attorney-General | Legal Department | — | — |
| 1907 | E. T. Packard | Attorney-General | Legal Department | — | — |
| 1908 | E. T. Packard | Attorney-General | Legal Department | — | — |

### Deterministic checks: `packard_edward-turner_b1868` vs `Packard, E. T___Sierra Leone___1905`

- [PASS] surname_gate: bio 'PACKARD' vs stint 'Packard, E. T' (exact)
- [PASS] initials: bio ['E', 'T'] ~ stint ['E', 'T']
- [PASS] age_gate: stint starts 1905, birth 1868 (age 37)
- [FAIL] colony: no placed event resolves to 'Sierra Leone'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1908
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

