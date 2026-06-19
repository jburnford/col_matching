<!-- {"case_id": "case_mignault_pierre-basile_b1854", "bio_ids": ["mignault_pierre-basile_b1854"], "stint_ids": ["Mignault, Pierre B___Canada___1917"]} -->
# Dossier case_mignault_pierre-basile_b1854

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mignault_pierre-basile_b1854`

- Printed name: **MIGNAULT, PIERRE BASILE**
- Birth year: 1854 (attested in editions [1929])
- Honours: B.C.L, K.C
- Appears in editions: [1929]

### Verbatim printed entry text (OCR)

**Version `col1929-L62471.v` — printed in editions [1929]:**

> MIGNAULT, HON. PIERRE BASILE, K.C., B.C.L., LL.D., A.M.—B. 1854; ed. Worcester; St. Mary's Jesuit Coll., Montreal; St. Francis Xavier Coll., New York (A.M.); McGill Univ. (B.C.L., 1877); hon. LL.D., Laval Univ., 1904; called to bar, 1878; K.C. (Earl of Derby), 1893; K.C. (Prov. of Quebeco), 1899; Syndic, 1905; bâtonnier of Montreal bar, 1906; pres., Montreal Bar Assoc., 1908; prof., civ. law, McGill Univ.; just., sup. ct., Canada, 1918; author of "Manuel de Droit Parlementaire" (1888); "Code de Procedure Civile Annote" (1891); "Droit Paroissial" (1893); "Le Droit Civil Canadien" (completed in 9 vols.); fellow, Royal Soc. of Canada, 1908; mem., International Joint Coman., 1914.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1877 | McGill Univ. (B.C.L | — | [1929] |
| 1 | 1878 | called to bar | — | [1929] |
| 2 | 1888 | author of "Manuel de Droit Parlementaire" ( | Canada *(inherited from previous clause)* | [1929] |
| 3 | 1891 | "Code de Procedure Civile Annote" ( | Canada *(inherited from previous clause)* | [1929] |
| 4 | 1893 | K.C. (Earl of Derby) | — | [1929] |
| 5 | 1893 | "Droit Paroissial" ( | Canada *(inherited from previous clause)* | [1929] |
| 6 | 1899 | K.C. (Prov. of Quebeco) | — | [1929] |
| 7 | 1904 | hon. LL.D., Laval Univ | — | [1929] |
| 8 | 1905 | Syndic | — | [1929] |
| 9 | 1906 | bâtonnier of Montreal bar | — | [1929] |
| 10 | 1908 | pres., Montreal Bar Assoc | — | [1929] |
| 11 | 1908 | fellow, Royal Soc. of Canada | Canada *(inherited from previous clause)* | [1929] |
| 12 | 1914 | mem., International Joint Coman | Canada *(inherited from previous clause)* | [1929] |
| 13 | 1918 | just., sup. ct. | Canada | [1929] |

## Candidate stint `Mignault, Pierre B___Canada___1917`

- Staff-list name: **Mignault, Pierre B** | colony: **Canada** | listed 1917–1922 | editions [1917, 1918, 1919, 1920, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1917 | Pierre B. Mignault | Commissioner | International Joint Commission, Canadian Section | — | — |
| 1918 | Pierre B. Mignault | Commissioner | International Joint Commission, Canadian Section | — | — |
| 1919 | Pierre B. Mignault | Commissioner | International Joint Commission, Canadian Section | — | — |
| 1919 | Pierre B. Mignault | Puisne Judges | Supreme Court of Canada | — | — |
| 1920 | Pierre B. Mignault | Puisne Judges | Supreme Court of Canada | — | — |
| 1922 | Pierre B. Mignault | Puisne Judge | Supreme Court of Canada | — | — |

### Deterministic checks: `mignault_pierre-basile_b1854` vs `Mignault, Pierre B___Canada___1917`

- [PASS] surname_gate: bio 'MIGNAULT' vs stint 'Mignault, Pierre B' (exact)
- [PASS] initials: bio ['P', 'B'] ~ stint ['P', 'B']
- [PASS] age_gate: stint starts 1917, birth 1854 (age 63)
- [PASS] colony: 6 placed event(s) resolve to 'Canada'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1917-1922
- [FAIL] position_sim: best 42 vs bar 60: 'just., sup. ct.' ~ 'Puisne Judges'
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

