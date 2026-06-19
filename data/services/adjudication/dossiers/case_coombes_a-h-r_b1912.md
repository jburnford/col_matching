<!-- {"case_id": "case_coombes_a-h-r_b1912", "bio_ids": ["coombes_a-h-r_b1912"], "stint_ids": ["Coombes, A. H. R___Hong Kong___1965"]} -->
# Dossier case_coombes_a-h-r_b1912

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `coombes_a-h-r_b1912`

- Printed name: **COOMBES, A. H. R**
- Birth year: 1912 (attested in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965])
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1957-L22133.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]:**

> COOMBES, A. H. R., M.B.E. (Mil.)—b. 1912; ed. Douai Sch., Camb. Univ. and London Hosp.; mil. serv., 1939–46, capt.; M.O., H.K., 1946; senr. health offr., 1956; asst. D.M.S., 1959; redesig. asst. D.M. & H.S., 1959; D.D.M. & H.S., 1964.

**Version `col1966-L13973.v` — printed in editions [1966]:**

> COUMBES, A. H. R., M.B.E. (Mil.)—b. 1912; ed. Douai Sch., Camb. Univ. and London Hosp.; mil. serv., 1939-46, capt.; M.O., H.K., 1946; senr. health offr., 1956; asst. D.M.S., 1959; redesig. asst. D.M. & H.S., 1959; D.D.M. & H.S., 1964.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | M.O. | Hong Kong | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1956 | senr. health offr | Hong Kong *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1959 | asst. D.M.S | Hong Kong *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1964 | D.D.M. & H.S | Hong Kong *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Coombes, A. H. R___Hong Kong___1965`

- Staff-list name: **Coombes, A. H. R** | colony: **Hong Kong** | listed 1965–1966 | editions [1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1965 | A. H. R. Coombes | Deputy Director of Medical and Health Services | Civil Establishment | M.B.E. | — |
| 1966 | A. H. R. Coombes | Deputy Director of Medical and Health Services | Civil Establishment | — | — |

### Deterministic checks: `coombes_a-h-r_b1912` vs `Coombes, A. H. R___Hong Kong___1965`

- [PASS] surname_gate: bio 'COOMBES' vs stint 'Coombes, A. H. R' (exact)
- [PASS] initials: bio ['A', 'H', 'R'] ~ stint ['A', 'H', 'R']
- [PASS] age_gate: stint starts 1965, birth 1912 (age 53)
- [PASS] colony: 4 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1965-1966
- [FAIL] position_sim: best 22 vs bar 60: 'asst. D.M.S' ~ 'Deputy Director of Medical and Health Services'
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

