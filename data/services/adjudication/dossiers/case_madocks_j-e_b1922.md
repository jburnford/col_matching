<!-- {"case_id": "case_madocks_j-e_b1922", "bio_ids": ["madocks_j-e_b1922"], "stint_ids": ["Madocks, J. E___Northern Rhodesia___1963"]} -->
# Dossier case_madocks_j-e_b1922

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `madocks_j-e_b1922`

- Printed name: **MADOCKS, J. E**
- Birth year: 1922 (attested in editions [1961, 1963, 1965, 1966])
- Honours: C.B.E (1965), M.B.E (1957)
- Appears in editions: [1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1961-L24971.v` — printed in editions [1961, 1963, 1965, 1966]:**

> MADOCKS, J. E., C.B.E. (1965), M.B.E. (1957).—b. 1922; ed. King Edward's Sch., Lichfield, and Birmingham Univ.; mil. serv., 1941-46, major; cadet, N. Rhod., 1946; dist. offr., 1948; senr. D.O. II, 1958; asst. sec., 1961; under-sec., 1962; perm. sec., 1964-65. (Zambia Govt. service.)

**Version `col1962-L24116.v` — printed in editions [1962, 1964]:**

> MADDOCKS, J. E., M.B.E. (1951).—b. 1922; ed. King Edward's Sch., Lichfield, and Birmingham Univ.; mil. serv., 1941-46, major; cadet, N. Rhod., 1946; dist. offr., 1948; senr. D.O. II, 1958; asst. sec., 1961; under-sec., 1962.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | cadet | Northern Rhodesia | [1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1948 | dist. offr | Northern Rhodesia *(inherited from previous clause)* | [1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1958 | senr. D.O. II | Dominions Office | [1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1961 | asst. sec | Dominions Office *(inherited from previous clause)* | [1961, 1962, 1963, 1964, 1965, 1966] |
| 4 | 1962 | under-sec | Dominions Office *(inherited from previous clause)* | [1961, 1962, 1963, 1964, 1965, 1966] |
| 5 | 1964–1965 | perm. sec | Dominions Office *(inherited from previous clause)* | [1961, 1963, 1965, 1966] |

## Candidate stint `Madocks, J. E___Northern Rhodesia___1963`

- Staff-list name: **Madocks, J. E** | colony: **Northern Rhodesia** | listed 1963–1964 | editions [1963, 1964]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1963 | J. E. Madocks | Under Secretary | Civil Establishment | — | — |
| 1964 | J. E. Madocks | Under Secretaries | Civil Establishment | — | — |

### Deterministic checks: `madocks_j-e_b1922` vs `Madocks, J. E___Northern Rhodesia___1963`

- [PASS] surname_gate: bio 'MADOCKS' vs stint 'Madocks, J. E' (exact)
- [PASS] initials: bio ['J', 'E'] ~ stint ['J', 'E']
- [PASS] age_gate: stint starts 1963, birth 1922 (age 41)
- [PASS] colony: 2 placed event(s) resolve to 'Northern Rhodesia'
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

