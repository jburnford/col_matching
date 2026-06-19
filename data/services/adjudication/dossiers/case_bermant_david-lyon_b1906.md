<!-- {"case_id": "case_bermant_david-lyon_b1906", "bio_ids": ["bermant_david-lyon_b1906"], "stint_ids": ["Bermant, D. L___Northern Rhodesia___1949"]} -->
# Dossier case_bermant_david-lyon_b1906

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bermant_david-lyon_b1906`

- Printed name: **BERMANT, David Lyon**
- Birth year: 1906 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L31147.v` — printed in editions [1948, 1949, 1950, 1951]:**

> BERMANT, David Lyon.—b. 1906; ed. Jeppie High Sch., Johannesburg; clk., N. Rhod., 1930; collctr. of customs, grade II, 1945; grade I, 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1930 | clk. | Northern Rhodesia | [1948, 1949, 1950, 1951] |
| 1 | 1945 | collctr. of customs, grade II | Northern Rhodesia *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 2 | 1947 | grade I | Northern Rhodesia *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Bermant, D. L___Northern Rhodesia___1949`

- Staff-list name: **Bermant, D. L** | colony: **Northern Rhodesia** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | D. L. Bermant | Collector | CUSTOMS | — | — |
| 1951 | D. L. Bermant | Collector | CUSTOMS | — | — |

### Deterministic checks: `bermant_david-lyon_b1906` vs `Bermant, D. L___Northern Rhodesia___1949`

- [PASS] surname_gate: bio 'BERMANT' vs stint 'Bermant, D. L' (exact)
- [PASS] initials: bio ['D', 'L'] ~ stint ['D', 'L']
- [PASS] age_gate: stint starts 1949, birth 1906 (age 43)
- [PASS] colony: 3 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 12 vs bar 60: 'grade I' ~ 'Collector'
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

