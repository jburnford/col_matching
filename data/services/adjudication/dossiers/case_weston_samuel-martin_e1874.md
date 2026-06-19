<!-- {"case_id": "case_weston_samuel-martin_e1874", "bio_ids": ["weston_samuel-martin_e1874"], "stint_ids": ["Weston, Mrs___Leeward Islands___1911", "Weston, S___Trinidad___1880"]} -->
# Dossier case_weston_samuel-martin_e1874

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 17 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `weston_samuel-martin_e1874`

- Printed name: **WESTON, SAMUEL MARTIN**
- Birth year: not printed
- Appears in editions: [1894, 1896, 1897, 1898, 1899, 1900, 1905]

### Verbatim printed entry text (OCR)

**Version `col1894-L34494.v` — printed in editions [1894, 1896, 1897, 1898, 1899, 1900, 1905]:**

> WESTON, SAMUEL MARTIN.—Clk. to wardens, N. and S. Naparima ward unions, Trinidad, 1874; clk. to consmr., S. prov., 1879; sec. to dist. agricul. bd., Naparima ward union, 1886; acted as warden of the union, Oct., 1887; additional supervisor of the union, Feb., 1888; clk. to warden, Naparima, 1890.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1874 | Clk. to wardens, N. and S. Naparima ward unions | Trinidad | [1894, 1896, 1897, 1898, 1899, 1900, 1905] |
| 1 | 1879 | clk. to consmr., S. prov | Trinidad *(inherited from previous clause)* | [1894, 1896, 1897, 1898, 1899, 1900, 1905] |
| 2 | 1886 | sec. to dist. agricul. bd., Naparima ward union | Trinidad *(inherited from previous clause)* | [1894, 1896, 1897, 1898, 1899, 1900, 1905] |
| 3 | 1887 | acted as warden of the union | Trinidad *(inherited from previous clause)* | [1894, 1896, 1897, 1898, 1899, 1900, 1905] |
| 4 | 1888 | additional supervisor of the union | Trinidad *(inherited from previous clause)* | [1894, 1896, 1897, 1898, 1899, 1900, 1905] |
| 5 | 1890 | clk. to warden, Naparima | Trinidad *(inherited from previous clause)* | [1894, 1896, 1897, 1898, 1899, 1900, 1905] |

## Candidate stint `Weston, Mrs___Leeward Islands___1911`

- Staff-list name: **Weston, Mrs** | colony: **Leeward Islands** | listed 1911–1918 | editions [1911, 1912, 1913, 1914, 1915, 1917, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1911 | Mrs. Weston | Matron | Lunatic and Leper Asylums | — | — |
| 1912 | Mrs. Weston | Matron | Lunatic and Leper Asylums | — | — |
| 1913 | Mrs. Weston | Matron | Lunatic and Lepre Asylums | — | — |
| 1914 | Mrs. Weston | Matron | Lunatic and Leper Asylums | — | — |
| 1915 | Mrs. Weston | Matron | Lunatic and Leper Asylums | — | — |
| 1917 | Mrs. Weston | Matron | Lunatic and Leper Asylums | — | — |
| 1918 | Mrs. Weston | Matron | Lunatic and Leper Asylums | — | — |

### Deterministic checks: `weston_samuel-martin_e1874` vs `Weston, Mrs___Leeward Islands___1911`

- [PASS] surname_gate: bio 'WESTON' vs stint 'Weston, Mrs' (exact)
- [PASS] initials: bio ['S', 'M'] ~ stint ['M']
- [PASS] age_gate: stint starts 1911; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1911-1918
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Weston, S___Trinidad___1880`

- Staff-list name: **Weston, S** | colony: **Trinidad** | listed 1880–1889 | editions [1880, 1883, 1886, 1888, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1880 | S. Weston | Clerk to Commissioner | Wardens | — | — |
| 1883 | S. Weston | Clerk to Commissioner | Wardens | — | — |
| 1886 | S. Weston | Clerk to Commissioner | Wardens | — | — |
| 1888 | S. Weston | Clerk to Commissioner | Wardens | — | — |
| 1889 | S. Weston | Clerk to Commissioner | Customs Department | — | — |

### Deterministic checks: `weston_samuel-martin_e1874` vs `Weston, S___Trinidad___1880`

- [PASS] surname_gate: bio 'WESTON' vs stint 'Weston, S' (exact)
- [PASS] initials: bio ['S', 'M'] ~ stint ['S']
- [PASS] age_gate: stint starts 1880; no printed birth year — UNCHECKED
- [PASS] colony: 6 placed event(s) resolve to 'Trinidad'
- [PASS] tenure_overlap: 6 event tenure(s) overlap stint years 1880-1889
- [FAIL] position_sim: best 54 vs bar 60: 'clk. to consmr., S. prov' ~ 'Clerk to Commissioner'
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

