<!-- {"case_id": "case_muir-mackenzie_k-j_e1907", "bio_ids": ["muir-mackenzie_k-j_e1907"], "stint_ids": ["Muir-Mackenzie, K. J___Fiji___1923"]} -->
# Dossier case_muir-mackenzie_k-j_e1907

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `muir-mackenzie_k-j_e1907`

- Printed name: **MUIR-MACKENZIE, K. J**
- Birth year: not printed
- Appears in editions: [1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931]

### Verbatim printed entry text (OCR)

**Version `col1923-L56878.v` — printed in editions [1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931]:**

> MUIR-MACKENZIE, CAPT. K. J.—Ed. St Paul's Schl. and Jesus Coll., Cambridge; called to bar, 1907; practised until 1914; served European war, 1914-19; crown counsel, Kenya Col., 1919; ag. solr. gen., mem., leg. coun. and atty. gen., Fiji, 1922; mem., exec. coun., ag. ch. just. and ch. judi. oomsnr., W. Pacific, 1922; acctnt., Colombo Port comsn., Feb., 1923; puisne judge, Tanganyika Territory, 1927.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1907 | called to bar | — | [1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931] |
| 1 | 1914 | practised until | — | [1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931] |
| 2 | 1914–1919 | served European war | — | [1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931] |
| 3 | 1919 | crown counsel | Kenya | [1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931] |
| 4 | 1922 | ag. solr. gen., mem., leg. coun. and atty. gen. | Fiji | [1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931] |
| 5 | 1923 | acctnt., Colombo Port comsn | Fiji *(inherited from previous clause)* | [1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931] |
| 6 | 1927 | puisne judge, Tanganyika Territory | Tanganyika | [1923, 1924, 1925, 1927, 1928, 1929, 1930, 1931] |

## Candidate stint `Muir-Mackenzie, K. J___Fiji___1923`

- Staff-list name: **Muir-Mackenzie, K. J** | colony: **Fiji** | listed 1923–1927 | editions [1923, 1924, 1925, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1923 | K. J. Muir-Mackenzie | Attorney-General | Department of Justice | — | — |
| 1924 | K. J. Muir-Mackenzie | Attorney-General | Judicial and Legal Department | — | — |
| 1925 | K. J. Muir-Mackenzie | Attorney-General | Judicial and Legal Department | — | — |
| 1927 | K. J. Muir-Mackenzie | Attorney-General | Judicial and Legal Department | — | — |

### Deterministic checks: `muir-mackenzie_k-j_e1907` vs `Muir-Mackenzie, K. J___Fiji___1923`

- [PASS] surname_gate: bio 'MUIR-MACKENZIE' vs stint 'Muir-Mackenzie, K. J' (exact)
- [PASS] initials: bio ['K', 'J'] ~ stint ['K', 'J']
- [PASS] age_gate: stint starts 1923; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Fiji'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1923-1927
- [FAIL] position_sim: best 42 vs bar 60: 'ag. solr. gen., mem., leg. coun. and atty. gen.' ~ 'Attorney-General'
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

