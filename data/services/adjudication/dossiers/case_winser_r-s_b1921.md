<!-- {"case_id": "case_winser_r-s_b1921", "bio_ids": ["winser_r-s_b1921"], "stint_ids": ["Winser, R. S___Kenya___1950"]} -->
# Dossier case_winser_r-s_b1921

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `winser_r-s_b1921`

- Printed name: **WINSER, R. S**
- Birth year: 1921 (attested in editions [1962, 1963, 1964])
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1962-L28029.v` — printed in editions [1962, 1963, 1964]:**

> WINSER, R. S.—b. 1921; ed. Bradfield Coll. and Corpus Christi Coll., Oxford; D.O., Ken., 1942; munic. African affrs. offr., 1954; D.O., 1958; senr. dist. comsnr., 1961; higher superscale, 1962–63. (Ken. Govt. service.)

**Version `col1957-L28519.v` — printed in editions [1957, 1958, 1959, 1960, 1961]:**

> WINSER, R. S.—b. 1921; ed. Bradfield Coll. and Corpus Christi African Coll., Oxford; dist. offr., Ken., 1942; munic. affrs. offr., 1948.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1942 | D.O. | Kenya | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1948 | munic. affrs. offr | Kenya *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961] |
| 2 | 1954 | munic. African affrs. offr | Kenya *(inherited from previous clause)* | [1962, 1963, 1964] |
| 3 | 1958 | munic. African affrs. offr | Dominions Office | [1962, 1963, 1964] |
| 4 | 1961 | senr. dist. comsnr | Dominions Office *(inherited from previous clause)* | [1962, 1963, 1964] |
| 5 | 1962–1963 | higher superscale | Dominions Office *(inherited from previous clause)* | [1962, 1963, 1964] |

## Candidate stint `Winser, R. S___Kenya___1950`

- Staff-list name: **Winser, R. S** | colony: **Kenya** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | R. S. Winser | Assistant Secretary | Secretariat | — | — |
| 1951 | R. S. Winser | Assistant Secretary | Secretariat | — | — |

### Deterministic checks: `winser_r-s_b1921` vs `Winser, R. S___Kenya___1950`

- [PASS] surname_gate: bio 'WINSER' vs stint 'Winser, R. S' (exact)
- [PASS] initials: bio ['R', 'S'] ~ stint ['R', 'S']
- [PASS] age_gate: stint starts 1950, birth 1921 (age 29)
- [PASS] colony: 3 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1950-1951
- [FAIL] position_sim: best 29 vs bar 60: 'munic. affrs. offr' ~ 'Assistant Secretary'
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

