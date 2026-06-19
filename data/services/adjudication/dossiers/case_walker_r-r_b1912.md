<!-- {"case_id": "case_walker_r-r_b1912", "bio_ids": ["walker_r-r_b1912"], "stint_ids": ["Walker, R. R___Northern Rhodesia___1949"]} -->
# Dossier case_walker_r-r_b1912

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 124 official(s) with this surname in the graph's staff lists; 70 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Walker, R. R___Northern Rhodesia___1949` is also gate-compatible with biography(ies) outside this case: ['walker_richard_e1923', 'walker_robert_b1881'] (already linked elsewhere or filtered).

## Biography `walker_r-r_b1912`

- Printed name: **WALKER, R. R**
- Birth year: 1912 (attested in editions [1963, 1964, 1965, 1966])
- Appears in editions: [1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1963-L25976.v` — printed in editions [1963, 1964, 1965, 1966]:**

> WALKER, R. R.—b. 1912; ed. St. Joseph's Acad., Blackheath; mil. serv., 1939-45, maj., (desps.); dist. astt., N. Rhod., 1946; supvr., co-op. soc., 1948; senr. co-op. and marketg. offr., 1956; prin. co-op. and marketg. offr., 1962. (Zambia Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | dist. astt. | Northern Rhodesia | [1963, 1964, 1965, 1966] |
| 1 | 1948 | supvr., co-op. soc | Northern Rhodesia *(inherited from previous clause)* | [1963, 1964, 1965, 1966] |
| 2 | 1956 | senr. co-op. and marketg. offr | Northern Rhodesia *(inherited from previous clause)* | [1963, 1964, 1965, 1966] |
| 3 | 1962 | prin. co-op. and marketg. offr | Northern Rhodesia *(inherited from previous clause)* | [1963, 1964, 1965, 1966] |

## Candidate stint `Walker, R. R___Northern Rhodesia___1949`

- Staff-list name: **Walker, R. R** | colony: **Northern Rhodesia** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | R. R. Walker | Supervisors | CO-OPERATIVE SOCIETIES | — | — |
| 1951 | R. R. Walker | Supervisor | CO-OPERATIVE SOCIETIES | — | — |

### Deterministic checks: `walker_r-r_b1912` vs `Walker, R. R___Northern Rhodesia___1949`

- [PASS] surname_gate: bio 'WALKER' vs stint 'Walker, R. R' (exact)
- [PASS] initials: bio ['R', 'R'] ~ stint ['R', 'R']
- [PASS] age_gate: stint starts 1949, birth 1912 (age 37)
- [PASS] colony: 4 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 42 vs bar 60: 'supvr., co-op. soc' ~ 'Supervisor'
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

