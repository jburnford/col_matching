<!-- {"case_id": "case_paikaudeau_e-a_e1876", "bio_ids": ["paikaudeau_e-a_e1876"], "stint_ids": ["Pairandeau, E. A___British Guiana___1888"]} -->
# Dossier case_paikaudeau_e-a_e1876

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `paikaudeau_e-a_e1876`

- Printed name: **PAIKAUDEAU, E. A**
- Birth year: not printed
- Appears in editions: [1897]

### Verbatim printed entry text (OCR)

**Version `col1897-L33715.v` — printed in editions [1897]:**

> PAIKAUDEAU, E. A.—2nd clerk, crown lids. dept., Br. Guiana, Nov., 1876; 1st ditto and draughtsman, Sept., 1879; 3rd asst. crown surveyor, Sept., 1884; 2nd govt. surveyor, Jan., 1887.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1876 | 2nd clerk, crown lids. dept. | British Guiana | [1897] |
| 1 | 1879 | 1st ditto and draughtsman | British Guiana *(inherited from previous clause)* | [1897] |
| 2 | 1884 | 3rd asst. crown surveyor | British Guiana *(inherited from previous clause)* | [1897] |
| 3 | 1887 | 2nd govt. surveyor | British Guiana *(inherited from previous clause)* | [1897] |

## Candidate stint `Pairandeau, E. A___British Guiana___1888`

- Staff-list name: **Pairandeau, E. A** | colony: **British Guiana** | listed 1888–1890 | editions [1888, 1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | E. A. Pairandeau | Government Surveyor | Government Land Department | — | — |
| 1889 | E. A. Pairandeau | Government Surveyor | Government Land Department | — | — |
| 1890 | E. A. Pairandeau | Government Surveyors | Government Land Department | — | — |

### Deterministic checks: `paikaudeau_e-a_e1876` vs `Pairandeau, E. A___British Guiana___1888`

- [PASS] surname_gate: bio 'PAIKAUDEAU' vs stint 'Pairandeau, E. A' (fuzzy:2)
- [PASS] initials: bio ['E', 'A'] ~ stint ['E', 'A']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [PASS] colony: 4 placed event(s) resolve to 'British Guiana'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1888-1890
- [PASS] position_sim: best 72 vs bar 60: '2nd govt. surveyor' ~ 'Government Surveyor'
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

