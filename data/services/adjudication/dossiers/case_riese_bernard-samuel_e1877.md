<!-- {"case_id": "case_riese_bernard-samuel_e1877", "bio_ids": ["riese_bernard-samuel_e1877"], "stint_ids": ["Ries, B. S___British Guiana___1908"]} -->
# Dossier case_riese_bernard-samuel_e1877

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `riese_bernard-samuel_e1877`

- Printed name: **RIESE, BERNARD SAMUEL**
- Birth year: not printed
- Appears in editions: [1914]

### Verbatim printed entry text (OCR)

**Version `col1914-L49482.v` — printed in editions [1914]:**

> RIESE, BERNARD SAMUEL.—Astt. clk., imigrn. dept., Br. Guiana, Dec., 1877; on spec. duty at off. of med. offr. to imigrn. dept., Feb. to Mar., and Apr. to May, 1881; 5th cls. clk., Apr., 1891; 4th cls. clk., Mar., 1893; 3rd cls. clk., June, 1907.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1877 | Astt. clk., imigrn. dept. | British Guiana | [1914] |
| 1 | 1881 | on spec. duty at off. of med. offr. to imigrn. dept., Feb. to Mar., and | British Guiana *(inherited from previous clause)* | [1914] |
| 2 | 1891 | 5th cls. clk | British Guiana *(inherited from previous clause)* | [1914] |
| 3 | 1893 | 4th cls. clk | British Guiana *(inherited from previous clause)* | [1914] |
| 4 | 1907 | 3rd cls. clk | British Guiana *(inherited from previous clause)* | [1914] |

## Candidate stint `Ries, B. S___British Guiana___1908`

- Staff-list name: **Ries, B. S** | colony: **British Guiana** | listed 1908–1918 | editions [1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1908 | B. S. Ries | 3rd Class Clerk | Immigration Department | — | — |
| 1909 | B. S. Ries | 3rd Class Clerk | Immigration Department | — | — |
| 1910 | B. S. Ries | 3rd Class Clerk | Immigration Department | — | — |
| 1911 | B. S. Ries | 3rd Class Clerk | Immigration Department | — | — |
| 1912 | B. S. Ries | 3rd Class Clerk | Immigration Department | — | — |
| 1913 | B. S. Ries | 3rd Class Clerk | Immigration Department | — | — |
| 1914 | B. S. Ries | 3rd Class Clerk | Immigration Department | — | — |
| 1915 | B. S. Ries | 3rd Class Clerk | Immigration Department | — | — |
| 1917 | B. S. Ries | 3rd Class Clerk | Immigration Department | — | — |
| 1918 | B. S. Ries | 3rd Clerk | Immigration Department | — | — |

### Deterministic checks: `riese_bernard-samuel_e1877` vs `Ries, B. S___British Guiana___1908`

- [PASS] surname_gate: bio 'RIESE' vs stint 'Ries, B. S' (fuzzy:1)
- [PASS] initials: bio ['B', 'S'] ~ stint ['B', 'S']
- [PASS] age_gate: stint starts 1908; no printed birth year — UNCHECKED
- [PASS] colony: 5 placed event(s) resolve to 'British Guiana'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1908-1918
- [PASS] position_sim: best 70 vs bar 60: '3rd cls. clk' ~ '3rd Clerk'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): 1 agreeing edition-year(s) [1914] pos~69 (bar: >=2)
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

