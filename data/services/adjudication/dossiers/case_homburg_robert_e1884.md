<!-- {"case_id": "case_homburg_robert_e1884", "bio_ids": ["homburg_robert_e1884", "homburgi_robert_e1884"], "stint_ids": ["Homburg, Robert___South Australia___1898"]} -->
# Dossier case_homburg_robert_e1884

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['homburg_robert_e1884', 'homburgi_robert_e1884'] carry a single initial only — the namesake trap applies.
- CONTESTED: stint(s) ['Homburg, Robert___South Australia___1898'] have more than one claimant biography in this case.

## Biography `homburg_robert_e1884`

- Printed name: **HOMBURG, ROBERT**
- Birth year: not printed
- Appears in editions: [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912]

### Verbatim printed entry text (OCR)

**Version `col1905-L43832.v` — printed in editions [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912]:**

> HOMBURG, ROBERT.—Mem. of H. of Ass., S. Aust., since 1884; atty.-gen., 1890-92 and 1892-3; ditto and min. of educn., 1904-5; 3rd judge of sup. ct., 1905.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1884 | Mem. of H. of Ass. | South Australia | [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912] |
| 1 | 1890–1893 | atty.-gen. | — | [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912] |
| 2 | 1904–1905 | atty.-gen. and min. of educn. | — | [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912] |
| 3 | 1905 | 3rd judge of sup. ct. | — | [1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912] |

## Biography `homburgi_robert_e1884`

- Printed name: **HOMBURGI, ROBERT**
- Birth year: not printed
- Appears in editions: [1909]

### Verbatim printed entry text (OCR)

**Version `col1909-L46071.v` — printed in editions [1909]:**

> HOMBURGI, ROBERT.—Mem. of H. of Ass., S. Aust., since 1884; atty.-gen., 1890-92 and 1892-3; ditto and min. of educn., 1904-5; 3rd judge of sup. ct., 1905.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1884 | Mem. of H. of Ass. | South Australia | [1909] |
| 1 | 1890–1893 | atty.-gen. | — | [1909] |
| 2 | 1904–1905 | ditto and min. of educn. | — | [1909] |
| 3 | 1905 | 3rd judge of sup. ct. | — | [1909] |

## Candidate stint `Homburg, Robert___South Australia___1898`

- Staff-list name: **Homburg, Robert** | colony: **South Australia** | listed 1898–1909 | editions [1898, 1900, 1905, 1906, 1907, 1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1898 | Hon. Robert Homburg | Member | House of Assembly | — | — |
| 1900 | Robert Homburg | Member, House of Assembly (Gumeracha) | House of Assembly | — | — |
| 1905 | Hon. R. Homburg, M.P. | Attorney-General and Minister of Education | Executive Council | — | — |
| 1905 | R. Homburg | Attorney-General and Minister of Education | Law Officers' and Minister of Education's Department | — | — |
| 1906 | Robert Homburg | Judge | Supreme Court | — | — |
| 1906 | Robert Homburg | Judge | — | — | — |
| 1907 | Robert Homburg | Judge | Judges of the Supreme Court | — | — |
| 1908 | Robert Homburg | Judge | Judges of the Supreme Court | — | — |
| 1909 | Robert Homburg | Judge | Judges of the Supreme Court | — | — |

### Deterministic checks: `homburg_robert_e1884` vs `Homburg, Robert___South Australia___1898`

- [PASS] surname_gate: bio 'HOMBURG' vs stint 'Homburg, Robert' (exact)
- [PASS] initials: bio ['R'] ~ stint ['R']
- [PASS] age_gate: stint starts 1898; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'South Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1898-1909
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `homburgi_robert_e1884` vs `Homburg, Robert___South Australia___1898`

- [PASS] surname_gate: bio 'HOMBURGI' vs stint 'Homburg, Robert' (fuzzy:1)
- [PASS] initials: bio ['R'] ~ stint ['R']
- [PASS] age_gate: stint starts 1898; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'South Australia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1898-1909
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

