<!-- {"case_id": "case_shaw_g-d_b1917", "bio_ids": ["shaw_g-d_b1917"], "stint_ids": ["Shaw, G. D___Northern Rhodesia___1949"]} -->
# Dossier case_shaw_g-d_b1917

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 83 official(s) with this surname in the graph's staff lists; 29 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `shaw_g-d_b1917`

- Printed name: **SHAW, G. D**
- Birth year: 1917 (attested in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1957-L27117.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> SHAW, G. D.—b. 1917; ed. Kingswood Coll., Grahamstown, S.A., and Liverpool Univ.; vet. offr., S. Rhod., 1941; N. Rhod., 1944; chief vet. research offr., 1952; dir., vet. and tsetse contrl. services, 1965. (Zambia Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1941 | vet. offr. | Southern Rhodesia | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1944 | vet. offr. | Northern Rhodesia | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1952 | chief vet. research offr | Northern Rhodesia *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1965 | dir., vet. and tsetse contrl. services | Northern Rhodesia *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Shaw, G. D___Northern Rhodesia___1949`

- Staff-list name: **Shaw, G. D** | colony: **Northern Rhodesia** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | G. D. Shaw | Veterinary Officers | Veterinary | — | — |
| 1951 | G. D. Shaw | Veterinary Officers | VETERINARY | — | — |

### Deterministic checks: `shaw_g-d_b1917` vs `Shaw, G. D___Northern Rhodesia___1949`

- [PASS] surname_gate: bio 'SHAW' vs stint 'Shaw, G. D' (exact)
- [PASS] initials: bio ['G', 'D'] ~ stint ['G', 'D']
- [PASS] age_gate: stint starts 1949, birth 1917 (age 32)
- [PASS] colony: 3 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 59 vs bar 60: 'vet. offr.' ~ 'Veterinary Officers'
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

