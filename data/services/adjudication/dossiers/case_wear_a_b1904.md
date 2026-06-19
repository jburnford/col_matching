<!-- {"case_id": "case_wear_a_b1904", "bio_ids": ["wear_a_b1904"], "stint_ids": ["Wear, A___Singapore___1953"]} -->
# Dossier case_wear_a_b1904

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['wear_a_b1904'] carry a single initial only — the namesake trap applies.

## Biography `wear_a_b1904`

- Printed name: **WEAR, A**
- Birth year: 1904 (attested in editions [1953, 1954, 1955, 1956])
- Appears in editions: [1953, 1954, 1955, 1956]

### Verbatim printed entry text (OCR)

**Version `col1953-L19475.v` — printed in editions [1953, 1954, 1955, 1956]:**

> WEAR, A.—b. 1904; ed. Oundle, and Leeds Univ.; asst. engrnr., Mal., 1926; S'pore airport, 1934; exec. engrnr., 1935; p.a. to D.P.W., 1939; senr. exec. engrnr., 1941; secon. P.W.D., Nig., 1942; maj., B.M.A., Mal., 1945; state engrnr., gr. II, 1947; gr. I, 1949; ag. D.P.W., S'pore, 1952.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | asst. engrnr. | Malaya | [1953, 1954, 1955, 1956] |
| 1 | 1934 | S'pore airport | Malaya *(inherited from previous clause)* | [1953, 1954, 1955, 1956] |
| 2 | 1935 | exec. engrnr | Malaya *(inherited from previous clause)* | [1953, 1954, 1955, 1956] |
| 3 | 1939 | p.a. to D.P.W | Malaya *(inherited from previous clause)* | [1953, 1954, 1955, 1956] |
| 4 | 1941 | senr. exec. engrnr | Malaya *(inherited from previous clause)* | [1953, 1954, 1955, 1956] |
| 5 | 1942 | secon. P.W.D. | Nigeria | [1953, 1954, 1955, 1956] |
| 6 | 1945 | maj., B.M.A. | Malaya | [1953, 1954, 1955, 1956] |
| 7 | 1947 | state engrnr., gr. II | Malaya *(inherited from previous clause)* | [1953, 1954, 1955, 1956] |
| 8 | 1949 | gr. I | Malaya *(inherited from previous clause)* | [1953, 1954, 1955, 1956] |
| 9 | 1952 | ag. D.P.W., S'pore | Malaya *(inherited from previous clause)* | [1953, 1954, 1955, 1956] |

## Candidate stint `Wear, A___Singapore___1953`

- Staff-list name: **Wear, A** | colony: **Singapore** | listed 1953–1956 | editions [1953, 1954, 1955, 1956]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1953 | A. Wear | Director of Public Works | Civil Establishment | — | — |
| 1954 | A. Wear | Director of Public Works | Civil Establishment | — | — |
| 1955 | A. Wear | Director of Public Works | Civil Establishment | — | — |
| 1956 | A. Wear | Director of Public Works | Civil Establishment | — | — |

### Deterministic checks: `wear_a_b1904` vs `Wear, A___Singapore___1953`

- [PASS] surname_gate: bio 'WEAR' vs stint 'Wear, A' (exact)
- [PASS] initials: bio ['A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1953, birth 1904 (age 49)
- [FAIL] colony: no placed event resolves to 'Singapore'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1953-1956
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

