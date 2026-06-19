<!-- {"case_id": "case_davison_charles-simon_e1881", "bio_ids": ["davison_charles-simon_e1881"], "stint_ids": ["Davison, C. S___British Guiana___1894"]} -->
# Dossier case_davison_charles-simon_e1881

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `davison_charles-simon_e1881`

- Printed name: **DAVISON, CHARLES SIMON**
- Birth year: not printed
- Honours: KT. BACH. (1917)
- Appears in editions: [1921]

### Verbatim printed entry text (OCR)

**Version `col1921-L55677.v` — printed in editions [1921]:**

> DAVISON, SIR CHARLES SIMON, KT. BACH. (1917), B.A., LL.D., K.C.—Ed. at Westminster and Trin. Hall, Camb.; called to the bar, Middle Temp., Jan., 1881; admitted to bar of Br. Guiana, 1882; acted as solr.-gen. on many occasions; stip. mag., 1888; solr.-gen., 1898; ag. atty.-gen., Nov., 1898, to Oct., 1899; again, Oct., 1900, to Apr., 1901, and on several other occasions; puisne judge, Mauritius, 1905; ch. just., Fiji, and ch. judicial commr., W. Pacific, 1914.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1881–1881 | called to the bar | — | [1921] |
| 1 | 1882–1882 | admitted to bar | British Guiana | [1921] |
| 2 | 1888–1888 | stip. mag. | — | [1921] |
| 3 | 1898–1898 | solr.-gen. | — | [1921] |
| 4 | 1898–1899 | ag. atty.-gen. | — | [1921] |
| 5 | 1900–1901 | ag. atty.-gen. | — | [1921] |
| 6 | 1905–1905 | puisne judge | Mauritius | [1921] |
| 7 | 1914–1914 | ch. just. and ch. judicial commr. | Fiji, Western Pacific | [1921] |

## Candidate stint `Davison, C. S___British Guiana___1894`

- Staff-list name: **Davison, C. S** | colony: **British Guiana** | listed 1894–1900 | editions [1894, 1896, 1897, 1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | C. S. Davison | Stipendiary Magistrate | Judicial Establishment | — | — |
| 1896 | C. S. Davison | Stipendiary Magistrates | Judicial Establishment | — | — |
| 1897 | C. S. Davison | Stipendiary Magistrate | Stipendiary Magistrates | — | — |
| 1899 | C. S. Davison | Solicitor-General and Registrar-General | Judicial Establishment | — | — |
| 1900 | C. S. Davison | Solicitor General and Registrar-General | Judicial Establishment | — | — |

### Deterministic checks: `davison_charles-simon_e1881` vs `Davison, C. S___British Guiana___1894`

- [PASS] surname_gate: bio 'DAVISON' vs stint 'Davison, C. S' (exact)
- [PASS] initials: bio ['C', 'S'] ~ stint ['C', 'S']
- [PASS] age_gate: stint starts 1894; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1894-1900
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

