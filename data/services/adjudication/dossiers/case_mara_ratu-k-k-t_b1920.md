<!-- {"case_id": "case_mara_ratu-k-k-t_b1920", "bio_ids": ["mara_ratu-k-k-t_b1920"], "stint_ids": ["Mara, Ratu K. K. T___Fiji___1965"]} -->
# Dossier case_mara_ratu-k-k-t_b1920

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mara_ratu-k-k-t_b1920`

- Printed name: **MARA, Ratu K. K. T**
- Birth year: 1920 (attested in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Honours: O.B.E (1961)
- Appears in editions: [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1958-L25096.v` — printed in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> MARA, Ratu K. K. T., O.B.E. (1961).—b. 1920; ed. Queen Victoria Sch., Fiji, Otago Univ., N.Z., and Wadham Coll., Oxford and L.S.E.; admin. offr., cl. II, Fiji, 1950; cl. IIA, 1962; cl. I, 1964; mem. for natural resources, 1964.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1950 | admin. offr., cl. II | Fiji | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1962 | cl. IIA | Fiji *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1964 | cl. I | Fiji *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Mara, Ratu K. K. T___Fiji___1965`

- Staff-list name: **Mara, Ratu K. K. T** | colony: **Fiji** | listed 1965–1966 | editions [1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1965 | Ratu K. K. T. Mara | Member for Natural Resources | Civil Establishment | — | — |
| 1966 | Ratu K. K. T. Mara | Member for Natural Resources | Civil Establishment | — | — |

### Deterministic checks: `mara_ratu-k-k-t_b1920` vs `Mara, Ratu K. K. T___Fiji___1965`

- [PASS] surname_gate: bio 'MARA' vs stint 'Mara, Ratu K. K. T' (exact)
- [PASS] initials: bio ['R', 'K', 'K', 'T'] ~ stint ['R', 'K', 'K', 'T']
- [PASS] age_gate: stint starts 1965, birth 1920 (age 45)
- [PASS] colony: 3 placed event(s) resolve to 'Fiji'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1965-1966
- [FAIL] position_sim: best 12 vs bar 60: 'cl. I' ~ 'Member for Natural Resources'
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

