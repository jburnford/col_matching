<!-- {"case_id": "case_perez_r-e_b1913", "bio_ids": ["perez_r-e_b1913"], "stint_ids": ["Perez, R. E___British Honduras___1953"]} -->
# Dossier case_perez_r-e_b1913

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 13 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `perez_r-e_b1913`

- Printed name: **PEREZ, R. E**
- Birth year: 1913 (attested in editions [1954])
- Appears in editions: [1954]

### Verbatim printed entry text (OCR)

**Version `col1954-L21854.v` — printed in editions [1954]:**

> PEREZ, R. E.—b. 1913; ed. St. John's Coll., Belize; clk., B. Hond., 1944; asst. supply offr. and comp. authy., 1946; dep. contrlr., imports, 1948; contrlr., 1950.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1944 | clk. | British Honduras | [1954] |
| 1 | 1946 | asst. supply offr. and comp. authy | British Honduras *(inherited from previous clause)* | [1954] |
| 2 | 1948 | dep. contrlr., imports | British Honduras *(inherited from previous clause)* | [1954] |
| 3 | 1950 | contrlr | British Honduras *(inherited from previous clause)* | [1954] |

## Candidate stint `Perez, R. E___British Honduras___1953`

- Staff-list name: **Perez, R. E** | colony: **British Honduras** | listed 1953–1954 | editions [1953, 1954]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1953 | R. E. Perez | Controller of Imports | Civil Establishment | — | — |
| 1954 | R. E. Perez | Controller of Imports | Civil Establishment | — | — |

### Deterministic checks: `perez_r-e_b1913` vs `Perez, R. E___British Honduras___1953`

- [PASS] surname_gate: bio 'PEREZ' vs stint 'Perez, R. E' (exact)
- [PASS] initials: bio ['R', 'E'] ~ stint ['R', 'E']
- [PASS] age_gate: stint starts 1953, birth 1913 (age 40)
- [PASS] colony: 4 placed event(s) resolve to 'British Honduras'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1953-1954
- [FAIL] position_sim: best 50 vs bar 60: 'contrlr' ~ 'Controller of Imports'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
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

