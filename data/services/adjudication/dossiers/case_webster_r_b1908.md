<!-- {"case_id": "case_webster_r_b1908", "bio_ids": ["webster_r_b1908"], "stint_ids": ["Webster, R___High Commission Territories___1963"]} -->
# Dossier case_webster_r_b1908

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 44 official(s) with this surname in the graph's staff lists; 21 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['webster_r_b1908'] carry a single initial only — the namesake trap applies.

## Biography `webster_r_b1908`

- Printed name: **WEBSTER, R**
- Birth year: 1908 (attested in editions [1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1962-L27741.v` — printed in editions [1962, 1963, 1964, 1965, 1966]:**

> WEBSTER, R.—b. 1908; ed. Mafeking and Kimberley High Schs.; publ. serv. S.A., 1925; postal offr., Basuto., 1955; senr. postm./inspector, 1959; contrl. posts and tels., 1961.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1925 | publ. serv. S.A | — | [1962, 1963, 1964, 1965, 1966] |
| 1 | 1955 | postal offr. | Basutoland | [1962, 1963, 1964, 1965, 1966] |
| 2 | 1959 | senr. postm./inspector | Basutoland *(inherited from previous clause)* | [1962, 1963, 1964, 1965, 1966] |
| 3 | 1961 | contrl. posts and tels | Basutoland *(inherited from previous clause)* | [1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Webster, R___High Commission Territories___1963`

- Staff-list name: **Webster, R** | colony: **High Commission Territories** | listed 1963–1964 | editions [1963, 1964]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1963 | R. Webster | Controller of Posts & Telegraphs | Law Officers | — | — |
| 1964 | R. Webster | Controller of Posts & Telegraphs | Secretariat | — | — |

### Deterministic checks: `webster_r_b1908` vs `Webster, R___High Commission Territories___1963`

- [PASS] surname_gate: bio 'WEBSTER' vs stint 'Webster, R' (exact)
- [PASS] initials: bio ['R'] ~ stint ['R']
- [PASS] age_gate: stint starts 1963, birth 1908 (age 55)
- [FAIL] colony: no placed event resolves to 'High Commission Territories'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1963-1964
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

