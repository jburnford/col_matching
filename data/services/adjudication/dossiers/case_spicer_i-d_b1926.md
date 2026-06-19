<!-- {"case_id": "case_spicer_i-d_b1926", "bio_ids": ["spicer_i-d_b1926"], "stint_ids": ["Spicer, I. D___Swaziland___1965"]} -->
# Dossier case_spicer_i-d_b1926

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 13 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `spicer_i-d_b1926`

- Printed name: **SPICER, I. D**
- Birth year: 1926 (attested in editions [1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1960-L28269.v` — printed in editions [1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> SPICER, I. D.—b. 1926; ed. Archbp. Tenison's and Southgate County Gram. Sch.; mil. serv., 1944–48, capt.; O.A.D., 1948; asst. audr., Nig., 1948; audr., 1952; senr. audr., Ken., 1954; prin. audr., E. Nig., 1959; dep. dir. aud., 1961; dir. audit, Swaz., 1964.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1948 | O.A.D | — | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1948 | asst. audr. | Nigeria | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1952 | audr | Nigeria *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1954 | senr. audr. | Kenya | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 4 | 1959 | prin. audr. | Eastern Nigeria | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 5 | 1961 | dep. dir. aud | Eastern Nigeria *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 6 | 1964 | dir. audit, Swaz | Eastern Nigeria *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Spicer, I. D___Swaziland___1965`

- Staff-list name: **Spicer, I. D** | colony: **Swaziland** | listed 1965–1966 | editions [1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1965 | I. D. Spicer | Director of Audit | Secretariat | — | — |
| 1966 | I. D. Spicer | Director of Audit | Civil Establishment | — | — |

### Deterministic checks: `spicer_i-d_b1926` vs `Spicer, I. D___Swaziland___1965`

- [PASS] surname_gate: bio 'SPICER' vs stint 'Spicer, I. D' (exact)
- [PASS] initials: bio ['I', 'D'] ~ stint ['I', 'D']
- [PASS] age_gate: stint starts 1965, birth 1926 (age 39)
- [FAIL] colony: no placed event resolves to 'Swaziland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1965-1966
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

