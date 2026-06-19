<!-- {"case_id": "case_welmer_gerard-wilfred_e1883", "bio_ids": ["welmer_gerard-wilfred_e1883"], "stint_ids": ["Weller, G___Sierra Leone___1921", "Welner, G___Straits Settlements___1877"]} -->
# Dossier case_welmer_gerard-wilfred_e1883

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `welmer_gerard-wilfred_e1883`

- Printed name: **WELMER, GERARD WILFRED**
- Birth year: not printed
- Appears in editions: [1896, 1897, 1898, 1899, 1900, 1905, 1907]

### Verbatim printed entry text (OCR)

**Version `col1896-L41877.v` — printed in editions [1896, 1897, 1898, 1899, 1900, 1905, 1907]:**

> WELMER, GERARD WILFRED.—Ed. Oscote Coll., Birmingham; asst. mag., Matang, Perak, May, 1883; mag., Thaiping, 1884-9; ag. state treas., Nov., 1886, to Mar., 1887; ag. collr. and mag., Krian, Jan., 1889, to May, 1890; ag. chief mag. and commr. of Ids., Selangor, May, 1890; gov't sec'y., Selangor, Nov., 1890.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1883 | asst. mag. | Perak | [1896, 1897, 1898, 1899, 1900, 1905, 1907] |
| 1 | 1884–1889 | mag. | — | [1896, 1897, 1898, 1899, 1900, 1905, 1907] |
| 2 | 1886–1887 | ag. state treas. | — | [1896, 1897, 1898, 1899, 1900, 1905, 1907] |
| 3 | 1889–1890 | ag. collr. and mag. | — | [1896, 1897, 1898, 1899, 1900, 1905, 1907] |
| 4 | 1890–1890 | ag. chief mag. and commr. of Ids. | Selangor | [1896, 1897, 1898, 1899, 1900, 1905, 1907] |

## Candidate stint `Weller, G___Sierra Leone___1921`

- Staff-list name: **Weller, G** | colony: **Sierra Leone** | listed 1921–1923 | editions [1921, 1923]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | G. Weller | Roads Foreman | Public Works Department | — | — |
| 1923 | G. Weller | Roads Foremen | Public Works Department | — | — |

### Deterministic checks: `welmer_gerard-wilfred_e1883` vs `Weller, G___Sierra Leone___1921`

- [PASS] surname_gate: bio 'WELMER' vs stint 'Weller, G' (fuzzy:1)
- [PASS] initials: bio ['G', 'W'] ~ stint ['G']
- [PASS] age_gate: stint starts 1921; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Sierra Leone'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1921-1923
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Welner, G___Straits Settlements___1877`

- Staff-list name: **Welner, G** | colony: **Straits Settlements** | listed 1877–1878 | editions [1877, 1878]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | G. Welner | Commander of Government Steamer "Pluto" | Marine Department | — | — |
| 1878 | G. Welner | Commander of Government Steamer "Pluto" | Marine Department | — | — |

### Deterministic checks: `welmer_gerard-wilfred_e1883` vs `Welner, G___Straits Settlements___1877`

- [PASS] surname_gate: bio 'WELMER' vs stint 'Welner, G' (fuzzy:1)
- [PASS] initials: bio ['G', 'W'] ~ stint ['G']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1878
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

