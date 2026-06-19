<!-- {"case_id": "case_burkitt_d-p_b1911", "bio_ids": ["burkitt_d-p_b1911"], "stint_ids": ["Burkitt, D. P___Uganda___1949"]} -->
# Dossier case_burkitt_d-p_b1911

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `burkitt_d-p_b1911`

- Printed name: **BURKITT, D. P.**
- Birth year: 1911 (attested in editions [1958, 1959, 1960, 1961])
- Appears in editions: [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]

### Verbatim printed entry text (OCR)

**Version `col1958-L21028.v` — printed in editions [1958, 1959, 1960, 1961]:**

> BURKITT, D. P.—b. 1911; ed. Dean Close Sch., Cheltenham, and Trinity Coll., Dublin; mil. serv., 1941–46, major, R.A.M.C.; M.O., Uga., 1946; specialist surgeon, 1952; author Treatment of Hydrocoele Acute Abdomens—Europeans and Africans compared (Lancet, 1951) (E.A., Med. Jour. 1953).

**Version `col1962-L19310.v` — printed in editions [1962, 1963, 1964, 1965]:**

> BURKITT, D. P.—b. 1911; ed. Dean Close Sch., Cheltenham, and Trinity Coll., Dublin; mil. serv., 1941-46, major, R.A.M.C.; M.O., Uga., 1946; specialist surgeon, 1952; senr. specialist, 1961. (Uga. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1941–1946 | major, R.A.M.C. | — | [1958, 1959, 1960, 1961] |
| 1 | 1946 | M.O. | Uganda | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 2 | 1952 | specialist surgeon | Uganda *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 3 | 1961 | senr. specialist | Uganda *(inherited from previous clause)* | [1962, 1963, 1964, 1965] |

## Candidate stint `Burkitt, D. P___Uganda___1949`

- Staff-list name: **Burkitt, D. P** | colony: **Uganda** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | D. P. Burkitt | Medical Officers | Medical | — | — |
| 1951 | D. P. Burkitt | Medical Officers | MEDICAL | — | — |

### Deterministic checks: `burkitt_d-p_b1911` vs `Burkitt, D. P___Uganda___1949`

- [PASS] surname_gate: bio 'BURKITT' vs stint 'Burkitt, D. P' (exact)
- [PASS] initials: bio ['D', 'P'] ~ stint ['D', 'P']
- [PASS] age_gate: stint starts 1949, birth 1911 (age 38)
- [PASS] colony: 3 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 35 vs bar 60: 'specialist surgeon' ~ 'Medical Officers'
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

