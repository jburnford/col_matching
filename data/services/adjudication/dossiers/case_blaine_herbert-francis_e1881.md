<!-- {"case_id": "case_blaine_herbert-francis_e1881", "bio_ids": ["blaine_herbert-francis_e1881"], "stint_ids": ["Blaine, Herbert Francis___Orange River Colony___1905"]} -->
# Dossier case_blaine_herbert-francis_e1881

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `blaine_herbert-francis_e1881`

- Printed name: **BLAINE, HERBERT FRANCIS**
- Birth year: not printed
- Appears in editions: [1905, 1906, 1907, 1908, 1909]

### Verbatim printed entry text (OCR)

**Version `col1905-L42066.v` — printed in editions [1905, 1906, 1907, 1908, 1909]:**

> BLAINE, HERBERT FRANCIS, K.C.—Ed. at Harrow and Brasenose Coll., Oxford; called to Bar (In. Temp.), 1881; admitted advoc., sup. ct. of Cape, 1881; M.A., 1889; twice ag. sol.-gen. East dists. ct.; att.-gen., O.R.C., May, 1901; mem. I.C.C., 1903; ag. atty.-gen., Transvaal, 1905, and 1906-7; mem. exec. and legis. couns.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1881 | called to Bar (In. Temp.) | — | [1905, 1906, 1907, 1908, 1909] |
| 1 | 1881 | admitted advoc., sup. ct. of Cape | — | [1905, 1906, 1907, 1908, 1909] |
| 2 | 1889 | M.A | — | [1905, 1906, 1907, 1908, 1909] |
| 3 | 1901 | att.-gen., O.R.C | — | [1905, 1906, 1907, 1908, 1909] |
| 4 | 1903 | mem. I.C.C | — | [1905, 1906, 1907, 1908, 1909] |
| 5 | 1905 | ag. atty.-gen. | Transvaal | [1905, 1906, 1907, 1908, 1909] |
| 6 | 1906–1907 | ag. atty.-gen. | Transvaal *(inherited from previous clause)* | [1905, 1906, 1907, 1908, 1909] |

## Candidate stint `Blaine, Herbert Francis___Orange River Colony___1905`

- Staff-list name: **Blaine, Herbert Francis** | colony: **Orange River Colony** | listed 1905–1907 | editions [1905, 1906, 1907]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | H. F. Blaine | Attorney-General | Attorney-General | — | — |
| 1906 | Herbert Francis Blaine | Attorney-General | Executive Council | — | — |
| 1906 | H. F. Blaine | Attorney-General | Attorney-General's Department | K.C. | — |
| 1907 | H. F. Blaine | Attorney-General | Attorney-General's Department | — | — |
| 1907 | Herbert Francis Blaine | Attorney-General | Executive Council | K.C. | — |

### Deterministic checks: `blaine_herbert-francis_e1881` vs `Blaine, Herbert Francis___Orange River Colony___1905`

- [PASS] surname_gate: bio 'BLAINE' vs stint 'Blaine, Herbert Francis' (exact)
- [PASS] initials: bio ['H', 'F'] ~ stint ['H', 'F']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Orange River Colony'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1907
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

