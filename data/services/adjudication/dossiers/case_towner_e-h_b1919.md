<!-- {"case_id": "case_towner_e-h_b1919", "bio_ids": ["towner_e-h_b1919"], "stint_ids": ["Towner, E. H___Grenada___1963"]} -->
# Dossier case_towner_e-h_b1919

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `towner_e-h_b1919`

- Printed name: **TOWNER, E. H**
- Birth year: 1919 (attested in editions [1964, 1965, 1966])
- Appears in editions: [1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1964-L22527.v` — printed in editions [1964, 1965, 1966]:**

> TOWNER, E. H.—b. 1919; ed. Judd Sch., Tonbridge; mil. serv., 1939–48, ch. petty offr., R.N.; N. Rhod., 1949; acctnt., 1952; estims. offr., 1955; senr. fin. offr., 1959; secon., Gren., as fin. sec., 1962–64; asst. sec., fin., 1964–65. (Zambia Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1949 | — | Northern Rhodesia | [1964, 1965, 1966] |
| 1 | 1952 | acctnt | Northern Rhodesia *(inherited from previous clause)* | [1964, 1965, 1966] |
| 2 | 1955 | estims. offr | Northern Rhodesia *(inherited from previous clause)* | [1964, 1965, 1966] |
| 3 | 1959 | senr. fin. offr | Northern Rhodesia *(inherited from previous clause)* | [1964, 1965, 1966] |
| 4 | 1962–1964 | secon., Gren., as fin. sec | Northern Rhodesia *(inherited from previous clause)* | [1964, 1965, 1966] |
| 5 | 1964–1965 | asst. sec., fin | Northern Rhodesia *(inherited from previous clause)* | [1964, 1965, 1966] |

## Candidate stint `Towner, E. H___Grenada___1963`

- Staff-list name: **Towner, E. H** | colony: **Grenada** | listed 1963–1964 | editions [1963, 1964]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1963 | E. H. Towner | Financial Secretary | Civil Establishment | — | — |
| 1964 | E. H. Towner | Financial Secretary | Civil Establishment | — | — |

### Deterministic checks: `towner_e-h_b1919` vs `Towner, E. H___Grenada___1963`

- [PASS] surname_gate: bio 'TOWNER' vs stint 'Towner, E. H' (exact)
- [PASS] initials: bio ['E', 'H'] ~ stint ['E', 'H']
- [PASS] age_gate: stint starts 1963, birth 1919 (age 44)
- [FAIL] colony: no placed event resolves to 'Grenada'
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

