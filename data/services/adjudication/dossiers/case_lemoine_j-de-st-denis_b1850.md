<!-- {"case_id": "case_lemoine_j-de-st-denis_b1850", "bio_ids": ["lemoine_j-de-st-denis_b1850"], "stint_ids": ["LeMoine, J. de St. Denis___Canada___1913"]} -->
# Dossier case_lemoine_j-de-st-denis_b1850

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `lemoine_j-de-st-denis_b1850`

- Printed name: **LEMOINE, J. DE ST. DENIS**
- Birth year: 1850 (attested in editions [1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922])
- Honours: I.S.O
- Appears in editions: [1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922]

### Verbatim printed entry text (OCR)

**Version `col1910-L47111.v` — printed in editions [1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922]:**

> LEMOINE, J. DE ST. DENIS, I.S.O.—B. 1850; ed. Quebec Seminary, and St. Mary's Coll., Montreal; ent. civ. ser., Canada, 1869; sergt.-at-arms of the Canadian Senate since 1887.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1869 | ent. civ. ser. | Canada | [1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922] |
| 1 | 1887 | sergt.-at-arms of the Canadian Senate since | Canada *(inherited from previous clause)* | [1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918, 1919, 1920, 1921, 1922] |

## Candidate stint `LeMoine, J. de St. Denis___Canada___1913`

- Staff-list name: **LeMoine, J. de St. Denis** | colony: **Canada** | listed 1913–1918 | editions [1913, 1914, 1915, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1913 | J. de St. Denis LeMoine | Serjeant-at-Arms | Senate of Canada | — | — |
| 1914 | J. de St. Denis LeMoine | Sergeant-at-Arms | Senate of Canada | — | — |
| 1915 | J. de St. Denis LeMoine | Sergeant-at-Arms | Senate of Canada | — | — |
| 1918 | J. de St. Denis LeMoine | Sergeant-at-Arms | Senate | — | — |

### Deterministic checks: `lemoine_j-de-st-denis_b1850` vs `LeMoine, J. de St. Denis___Canada___1913`

- [PASS] surname_gate: bio 'LEMOINE' vs stint 'LeMoine, J. de St. Denis' (exact)
- [PASS] initials: bio ['J', 'D', 'S', 'D'] ~ stint ['J', 'D', 'S', 'D']
- [PASS] age_gate: stint starts 1913, birth 1850 (age 63)
- [PASS] colony: 2 placed event(s) resolve to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1913-1918
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

