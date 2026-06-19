<!-- {"case_id": "case_meade_a-r_b1887", "bio_ids": ["meade_a-r_b1887"], "stint_ids": ["Meade, A. R___Leeward Islands___1911", "Meade, A. R___Montserrat___1909"]} -->
# Dossier case_meade_a-r_b1887

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `meade_a-r_b1887`

- Printed name: **MEADE, A. R**
- Birth year: 1887 (attested in editions [1912, 1913, 1914])
- Appears in editions: [1912, 1913, 1914]

### Verbatim printed entry text (OCR)

**Version `col1912-L46163.v` — printed in editions [1912, 1913, 1914]:**

> MEADE, A. R.—B. 1887; ed. at St. Kitts-Nevis gram. schl.; jun. ast. mast., St. Kitts-Nevis gram. schl., Jan. to Apr., 1907; matric., London Univ., 1908; copyist, treasy. dept., St. Kitts, June, 1907; 3rd treasy. clk., Montserrat, 16th Nov., 1907; ag. 1st treasy. clk., Dec. 1909 to Jan., 1910; ag. 2nd treasy. clk., Mar. to July, 1910; 2nd treasy. clk., July, 1910.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1907 | jun. ast. mast., St. Kitts-Nevis gram. schl | — | [1912, 1913, 1914] |
| 1 | 1907 | copyist, treasy. dept. | St. Kitts | [1912, 1913, 1914] |
| 2 | 1907 | 3rd treasy. clk. | Montserrat | [1912, 1913, 1914] |
| 3 | 1908 | matric., London Univ | — | [1912, 1913, 1914] |
| 4 | 1909–1910 | ag. 1st treasy. clk | Montserrat *(inherited from previous clause)* | [1912, 1913, 1914] |
| 5 | 1910 | ag. 2nd treasy. clk | Montserrat *(inherited from previous clause)* | [1912, 1913, 1914] |

## Candidate stint `Meade, A. R___Leeward Islands___1911`

- Staff-list name: **Meade, A. R** | colony: **Leeward Islands** | listed 1911–1914 | editions [1911, 1912, 1913, 1914]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1911 | A. R. Meade | Second Clerk | Treasury Department | — | — |
| 1912 | A. R. Meade | Second Clerk | Treasury Department | — | — |
| 1913 | A. R. Meade | Third Clerk | Treasury Department | — | — |
| 1914 | A. R. Meade | Government Officer | Treasury and Customs | — | — |

### Deterministic checks: `meade_a-r_b1887` vs `Meade, A. R___Leeward Islands___1911`

- [PASS] surname_gate: bio 'MEADE' vs stint 'Meade, A. R' (exact)
- [PASS] initials: bio ['A', 'R'] ~ stint ['A', 'R']
- [PASS] age_gate: stint starts 1911, birth 1887 (age 24)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1911-1914
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Meade, A. R___Montserrat___1909`

- Staff-list name: **Meade, A. R** | colony: **Montserrat** | listed 1909–1910 | editions [1909, 1910]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1909 | A. R. Meade | Third Clerk | Treasury Department | — | — |
| 1910 | A. R. Meade | Third Clerk | Treasury Department | — | — |

### Deterministic checks: `meade_a-r_b1887` vs `Meade, A. R___Montserrat___1909`

- [PASS] surname_gate: bio 'MEADE' vs stint 'Meade, A. R' (exact)
- [PASS] initials: bio ['A', 'R'] ~ stint ['A', 'R']
- [PASS] age_gate: stint starts 1909, birth 1887 (age 22)
- [PASS] colony: 3 placed event(s) resolve to 'Montserrat'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1909-1910
- [FAIL] position_sim: best 48 vs bar 60: '3rd treasy. clk.' ~ 'Third Clerk'
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

