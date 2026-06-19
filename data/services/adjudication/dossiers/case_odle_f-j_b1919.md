<!-- {"case_id": "case_odle_f-j_b1919", "bio_ids": ["odle_f-j_b1919"], "stint_ids": ["Odle, F___Leeward Islands___1954"]} -->
# Dossier case_odle_f-j_b1919

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `odle_f-j_b1919`

- Printed name: **ODLE, F. J**
- Birth year: 1919 (attested in editions [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Honours: M.B.E (1956)
- Appears in editions: [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1959-L26498.v` — printed in editions [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> ODLE, F. J., M.B.E. (1956).—b. 1919; ed. Harrison Coll.; clk., labr. dept., Barb., 1943; labr. offr., 1950; labr. comsnr., Antigua, 1953; Barb., 1957; perm. sec., 1960.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1943 | clk., labr. dept. | Barbados | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1950 | labr. offr | Barbados *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1953 | labr. comsnr. | Antigua | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1957 | labr. comsnr. | Barbados | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 4 | 1960 | perm. sec | Barbados *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Odle, F___Leeward Islands___1954`

- Staff-list name: **Odle, F** | colony: **Leeward Islands** | listed 1954–1957 | editions [1954, 1955, 1956, 1957]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1954 | F. Odle | Labour Officer | Civil Establishment | — | — |
| 1955 | F. Odle | Labour Commissioner | Civil Establishment | — | — |
| 1956 | F. Odle | Labour Commissioner | Civil Establishment | — | — |
| 1957 | F. Odle | Labour Commissioner | Civil Establishment | — | — |

### Deterministic checks: `odle_f-j_b1919` vs `Odle, F___Leeward Islands___1954`

- [PASS] surname_gate: bio 'ODLE' vs stint 'Odle, F' (exact)
- [PASS] initials: bio ['F', 'J'] ~ stint ['F']
- [PASS] age_gate: stint starts 1954, birth 1919 (age 35)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1954-1957
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

