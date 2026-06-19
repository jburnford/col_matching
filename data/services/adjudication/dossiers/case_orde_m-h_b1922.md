<!-- {"case_id": "case_orde_m-h_b1922", "bio_ids": ["orde_m-h_b1922"], "stint_ids": ["Orde, M. H___Gambia___1960"]} -->
# Dossier case_orde_m-h_b1922

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `orde_m-h_b1922`

- Printed name: **ORDE, M. H**
- Birth year: 1922 (attested in editions [1959, 1960, 1961, 1962, 1963, 1964, 1965])
- Honours: O.B.E (1963)
- Appears in editions: [1959, 1960, 1961, 1962, 1963, 1964, 1965]

### Verbatim printed entry text (OCR)

**Version `col1959-L26547.v` — printed in editions [1959, 1960, 1961, 1962, 1963, 1964, 1965]:**

> ORDE, M. H., O.B.E. (1963).—b. 1922; ed. Leighton Pk. Sch., and Christ Church, Oxford; mil. serv., 1942–47, capt.; admin. offr., cl. IV, N. Nig., 1947; cl. III, 1952; comsnr. for local govt., Gam., 1959–64.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947 | admin. offr., cl. IV | Northern Nigeria | [1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 1 | 1952 | cl. III | Northern Nigeria *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 2 | 1959–1964 | comsnr. for local govt., Gam | Northern Nigeria *(inherited from previous clause)* | [1959, 1960, 1961, 1962, 1963, 1964, 1965] |

## Candidate stint `Orde, M. H___Gambia___1960`

- Staff-list name: **Orde, M. H** | colony: **Gambia** | listed 1960–1964 | editions [1960, 1961, 1962, 1963, 1964]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1960 | M. H. Orde | Senior Commissioner | Civil Establishment | — | — |
| 1961 | M. H. Orde | Commissioner for Local Government | Civil Establishment | — | — |
| 1962 | M. H. Orde | Commissioner for Local Government | Civil Establishment | — | — |
| 1963 | M. H. Orde | Secretary to Ministry and Commissioner for Local Government | Ministry for Local Government and Lands | — | — |
| 1964 | M. H. Orde | Secretary | Ministry of Local Government, Lands and Labour | — | — |

### Deterministic checks: `orde_m-h_b1922` vs `Orde, M. H___Gambia___1960`

- [PASS] surname_gate: bio 'ORDE' vs stint 'Orde, M. H' (exact)
- [PASS] initials: bio ['M', 'H'] ~ stint ['M', 'H']
- [PASS] age_gate: stint starts 1960, birth 1922 (age 38)
- [FAIL] colony: no placed event resolves to 'Gambia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1960-1964
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

