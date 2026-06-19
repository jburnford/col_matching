<!-- {"case_id": "case_haralampides_m-k_b1904", "bio_ids": ["haralampides_m-k_b1904"], "stint_ids": ["Haralampides, M. K___Cyprus___1955"]} -->
# Dossier case_haralampides_m-k_b1904

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `haralampides_m-k_b1904`

- Printed name: **HARALAMPIDES, M. K**
- Birth year: 1904 (attested in editions [1955, 1956, 1957, 1958, 1959, 1960])
- Honours: O.B.E (1960)
- Appears in editions: [1955, 1956, 1957, 1958, 1959, 1960]

### Verbatim printed entry text (OCR)

**Version `col1955-L20982.v` — printed in editions [1955, 1956, 1957, 1958, 1959, 1960]:**

> HARALAMPIDES, M. K., O.B.E. (1960).—b. 1904; ed. Classical Greek Gymnasium and English Sch., Cyp.; land clk., Cyp., 1920; admin. asst., 1st gr., 1947; admin. offr., cl. III, 1952; P.M.G., 1954.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920 | land clk. | Cyprus | [1955, 1956, 1957, 1958, 1959, 1960] |
| 1 | 1947 | admin. asst., 1st gr | Cyprus *(inherited from previous clause)* | [1955, 1956, 1957, 1958, 1959, 1960] |
| 2 | 1952 | admin. offr., cl. III | Cyprus *(inherited from previous clause)* | [1955, 1956, 1957, 1958, 1959, 1960] |
| 3 | 1954 | P.M.G | Cyprus *(inherited from previous clause)* | [1955, 1956, 1957, 1958, 1959, 1960] |

## Candidate stint `Haralampides, M. K___Cyprus___1955`

- Staff-list name: **Haralampides, M. K** | colony: **Cyprus** | listed 1955–1959 | editions [1955, 1956, 1957, 1958, 1959]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1955 | M. K. Haralampides | Postmaster-General | Civil Establishment | — | — |
| 1956 | M. K. Haralampides | Postmaster-General | Civil Establishment | — | — |
| 1957 | M. K. Haralampides | Postmaster-General | Civil Establishment | — | — |
| 1958 | M. K. Haralampides | Postmaster-General | Civil Establishment | — | — |
| 1959 | M. K. Haralampides | Postmaster-General | Civil Establishment | — | — |

### Deterministic checks: `haralampides_m-k_b1904` vs `Haralampides, M. K___Cyprus___1955`

- [PASS] surname_gate: bio 'HARALAMPIDES' vs stint 'Haralampides, M. K' (exact)
- [PASS] initials: bio ['M', 'K'] ~ stint ['M', 'K']
- [PASS] age_gate: stint starts 1955, birth 1904 (age 51)
- [PASS] colony: 4 placed event(s) resolve to 'Cyprus'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1955-1959
- [FAIL] position_sim: best 30 vs bar 60: 'P.M.G' ~ 'Postmaster-General'
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

