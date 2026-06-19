<!-- {"case_id": "case_le-blanc_pierre-everiste_b1853", "bio_ids": ["le-blanc_pierre-everiste_b1853"], "stint_ids": ["Le Blanc, Pierre Evariste___Canada___1918"]} -->
# Dossier case_le-blanc_pierre-everiste_b1853

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `le-blanc_pierre-everiste_b1853`

- Printed name: **LE BLANC, PIERRE EVERISTE**
- Birth year: 1853 (attested in editions [1918])
- Honours: K.C., K.C.M.G. (1916)
- Appears in editions: [1918]

### Verbatim printed entry text (OCR)

**Version `col1918-L52128.v` — printed in editions [1918]:**

> LE BLANC, SIR PIERRE EVERISTE, K.C.M.G. (1916), K.C.—B. 1853; called to the bar, Quebec, 1879; elec. to legie. ass., Quebec, bye-elec., 1884; g.e., 1886, 1888, 1890, 1892, 1897, 1900, and 1904; speaker of assembly under three govt.s; lieut.-gov., Quebec, 1915.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1879–1879 | called to the bar | Quebec | [1918] |
| 1 | 1884–1884 | elec. to legie. ass. | Quebec | [1918] |
| 2 | 1886–1904 | g.e. | — | [1918] |
| 3 | 1915 | lieut.-gov. | Quebec | [1918] |

## Candidate stint `Le Blanc, Pierre Evariste___Canada___1918`

- Staff-list name: **Le Blanc, Pierre Evariste** | colony: **Canada** | listed 1918–1922 | editions [1918, 1919, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1918 | Sir Pierre Evariste Le Blanc | Lieutenant-Governor | Province of Quebec | K.C.M.G. | — |
| 1919 | Sir Pierre Evariste Le Blanc | Lieutenant-Governor | Province of Quebec | K.C.M.G. | — |
| 1922 | Pierre Evariste Le Blanc | Lieutenant-Governor | Lieutenant-Governors | K.C.M.G. | — |

### Deterministic checks: `le-blanc_pierre-everiste_b1853` vs `Le Blanc, Pierre Evariste___Canada___1918`

- [PASS] surname_gate: bio 'LE BLANC' vs stint 'Le Blanc, Pierre Evariste' (exact)
- [PASS] initials: bio ['P', 'E'] ~ stint ['P', 'E']
- [PASS] age_gate: stint starts 1918, birth 1853 (age 65)
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1918-1922
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: K.C.M.G.
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

