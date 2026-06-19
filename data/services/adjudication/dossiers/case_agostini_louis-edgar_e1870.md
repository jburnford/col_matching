<!-- {"case_id": "case_agostini_louis-edgar_e1870", "bio_ids": ["agostini_louis-edgar_e1870"], "stint_ids": ["Agostini, Edgar___Trinidad and Tobago___1905", "Agostini, Edgar___Trinidad___1908"]} -->
# Dossier case_agostini_louis-edgar_e1870

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `agostini_louis-edgar_e1870`

- Printed name: **AGOSTINI, Louis Edgar**
- Birth year: not printed
- Appears in editions: [1907, 1908, 1909, 1910, 1911]

### Verbatim printed entry text (OCR)

**Version `col1907-L42717.v` — printed in editions [1907, 1908, 1909, 1910, 1911]:**

> AGOSTINI, Louis Edgar, K.C.—Ed. at Stonyhurst Coll., Downside Coll., and Univ. Coll., London; matric., London Univ., 1870; called to the bar, Lincoln's Inn, 1874; solr.-gen., Trinidad, 1st Oct., 1903; atty.-gen., Trinidad, 10th Sept., 1904; ag. chief just., June, 1907, to June, 1908.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1870–1870 | — | — | [1907, 1908, 1909, 1910, 1911] |
| 1 | 1874–1874 | called to the bar | — | [1907, 1908, 1909, 1910, 1911] |
| 2 | 1903–1903 | solr.-gen. | Trinidad | [1907, 1908, 1909, 1910, 1911] |
| 3 | 1904–1904 | atty.-gen. | Trinidad | [1907, 1908, 1909, 1910, 1911] |
| 4 | 1907–1908 | ag. chief just. | — | [1907, 1908, 1909, 1910, 1911] |

## Candidate stint `Agostini, Edgar___Trinidad and Tobago___1905`

- Staff-list name: **Agostini, Edgar** | colony: **Trinidad and Tobago** | listed 1905–1910 | editions [1905, 1906, 1907, 1910]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | Edgar Agostini | Attorney-General (is also Clerk of the Peace) | Registrar of the Courts, Registrar in Bankruptcy, and Marshal | — | — |
| 1906 | Edgar Agostini | Attorney-General (is also Clerk of the Peace) | Judicial Department | — | — |
| 1907 | Edgar Agostini | Attorney-General | Loyal | — | — |
| 1910 | Edgar Agostini | Attorney-General | Legal | — | — |

### Deterministic checks: `agostini_louis-edgar_e1870` vs `Agostini, Edgar___Trinidad and Tobago___1905`

- [PASS] surname_gate: bio 'AGOSTINI' vs stint 'Agostini, Edgar' (exact)
- [PASS] initials: bio ['L', 'E'] ~ stint ['E']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1910
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Agostini, Edgar___Trinidad___1908`

- Staff-list name: **Agostini, Edgar** | colony: **Trinidad** | listed 1908–1911 | editions [1908, 1911]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1908 | Edgar Agostini | Attorney-General | Legal | K.C. | — |
| 1911 | Edgar Agostini | Attorney-General | Legal | — | — |

### Deterministic checks: `agostini_louis-edgar_e1870` vs `Agostini, Edgar___Trinidad___1908`

- [PASS] surname_gate: bio 'AGOSTINI' vs stint 'Agostini, Edgar' (exact)
- [PASS] initials: bio ['L', 'E'] ~ stint ['E']
- [PASS] age_gate: stint starts 1908; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Trinidad'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1908-1911
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

