<!-- {"case_id": "case_gold_stanley-john_e1890", "bio_ids": ["gold_stanley-john_e1890"], "stint_ids": ["Gold, S. J___South Africa___1914"]} -->
# Dossier case_gold_stanley-john_e1890

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `gold_stanley-john_e1890`

- Printed name: **GOLD, STANLEY JOHN**
- Birth year: not printed
- Appears in editions: [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921]

### Verbatim printed entry text (OCR)

**Version `col1913-L46098.v` — printed in editions [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921]:**

> GOLD, STANLEY JOHN.—Entered Impl. postal service, 22nd Dec., 1890; clk., post and telegraph dept., Transvaal, 23rd Mar., 1901; sen. clk., 1st July, 1901; staff clk., 1st July, 1902; prin. clk., 1st Jan., 1903; chief clk., 1st July, 1908; ag. chief clk., posts and telegraphs, Union of S. Africa, 1910; ag. 2nd astt. under-sec., 1910; 2nd astt. under-sec., 1st Apr., 1912.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1890 | Entered Impl. postal service | — | [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921] |
| 1 | 1901 | clk., post and telegraph dept. | Transvaal | [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921] |
| 2 | 1902 | staff clk | Transvaal *(inherited from previous clause)* | [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921] |
| 3 | 1903 | prin. clk | Transvaal *(inherited from previous clause)* | [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921] |
| 4 | 1908 | chief clk | Transvaal *(inherited from previous clause)* | [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921] |
| 5 | 1910 | ag. chief clk., posts and telegraphs, Union of S. Africa | Transvaal *(inherited from previous clause)* | [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921] |
| 6 | 1912 | 2nd astt. under-sec | Transvaal *(inherited from previous clause)* | [1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921] |

## Candidate stint `Gold, S. J___South Africa___1914`

- Staff-list name: **Gold, S. J** | colony: **South Africa** | listed 1914–1918 | editions [1914, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1914 | S. J. Gold | Second Assistant Under Secretary | Department of Posts and Telegraphs | — | — |
| 1918 | S. J. Gold | Assistant Under Secretary | Posts and Telegraphs | — | — |

### Deterministic checks: `gold_stanley-john_e1890` vs `Gold, S. J___South Africa___1914`

- [PASS] surname_gate: bio 'GOLD' vs stint 'Gold, S. J' (exact)
- [PASS] initials: bio ['S', 'J'] ~ stint ['S', 'J']
- [PASS] age_gate: stint starts 1914; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1914-1918
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

