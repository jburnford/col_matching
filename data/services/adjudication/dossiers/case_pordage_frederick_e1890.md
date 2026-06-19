<!-- {"case_id": "case_pordage_frederick_e1890", "bio_ids": ["pordage_frederick_e1890", "pordege_frederick_e1890"], "stint_ids": ["Pordage, F___Uganda___1906"]} -->
# Dossier case_pordage_frederick_e1890

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['pordage_frederick_e1890', 'pordege_frederick_e1890'] carry a single initial only — the namesake trap applies.
- CONTESTED: stint(s) ['Pordage, F___Uganda___1906'] have more than one claimant biography in this case.

## Biography `pordage_frederick_e1890`

- Printed name: **PORDAGE, FREDERICK**
- Birth year: not printed
- Appears in editions: [1907, 1908]

### Verbatim printed entry text (OCR)

**Version `col1907-L46337.v` — printed in editions [1907, 1908]:**

> PORDAGE, FREDERICK.—Ed. Queen Elizabeth Gram. Schl., London; Jesus Coll.; St. Pierre, Eglise; supt., P.W.D., Imperial Brit. E. Africa Co.; Mombasa, Aug., 1890, to Jan., 1893; consulting and sanitary engr., Zanzibar govt., 1893-1895; asst., Uganda adminstr., 1895; supt., P.W.D., 1899; (Uganda Mutiny medal).

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1890–1893 | supt., P.W.D. | Mombasa | [1907, 1908] |
| 1 | 1893–1895 | consulting and sanitary engr. | Zanzibar | [1907, 1908] |
| 2 | 1895 | asst. | Uganda | [1907, 1908] |
| 3 | 1899 | supt., P.W.D. | — | [1907, 1908] |

## Biography `pordege_frederick_e1890`

- Printed name: **PORDEGE, FREDERICK**
- Birth year: not printed
- Appears in editions: [1906]

### Verbatim printed entry text (OCR)

**Version `col1906-L47447.v` — printed in editions [1906]:**

> PORDEGE, FREDERICK.—Ed. Queen Elizabeth Gram. Schl., London, Jesus Coll., St. Pierre, Eglise; supt., P.W.D., Imperial Brit. E. Africa Co., Mombasa, Aug., 1890, to Jan., 1893; consulting and sanitary engnr., Zanzibar govt., 1893-1895; asst., Uganda admnstr., 1895; supt., P.W.D., 1899; (Uganda Mutiny medal).

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1890–1893 | supt., P.W.D. | Mombasa | [1906] |
| 1 | 1893–1895 | consulting and sanitary engnr. | Zanzibar | [1906] |
| 2 | 1895–1895 | asst. | Uganda | [1906] |
| 3 | 1899–1899 | supt., P.W.D. | — | [1906] |

## Candidate stint `Pordage, F___Uganda___1906`

- Staff-list name: **Pordage, F** | colony: **Uganda** | listed 1906–1907 | editions [1906, 1907]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1906 | F. Pordage | Superintendent of Public Works | Public Works | — | — |
| 1907 | F. Pordage | Director of Public Works | Public Works | — | — |

### Deterministic checks: `pordage_frederick_e1890` vs `Pordage, F___Uganda___1906`

- [PASS] surname_gate: bio 'PORDAGE' vs stint 'Pordage, F' (exact)
- [PASS] initials: bio ['F'] ~ stint ['F']
- [PASS] age_gate: stint starts 1906; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Uganda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1906-1907
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `pordege_frederick_e1890` vs `Pordage, F___Uganda___1906`

- [PASS] surname_gate: bio 'PORDEGE' vs stint 'Pordage, F' (fuzzy:1)
- [PASS] initials: bio ['F'] ~ stint ['F']
- [PASS] age_gate: stint starts 1906; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Uganda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1906-1907
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

