<!-- {"case_id": "case_crichton_p_b1920", "bio_ids": ["crichton_p_b1920"], "stint_ids": ["Crichton, P. D. O'N___St Vincent___1961"]} -->
# Dossier case_crichton_p_b1920

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['crichton_p_b1920'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Crichton, P. D. O'N___St Vincent___1961` is also gate-compatible with biography(ies) outside this case: ['crichton_p-d-o_b1915'] (already linked elsewhere or filtered).

## Biography `crichton_p_b1920`

- Printed name: **CRICHTON, P**
- Birth year: 1920 (attested in editions [1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1960-L21998.v` — printed in editions [1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> CRICHTON, P.—b. 1920; ed. Bryanston Sch., and New Coll., Oxford; mil. serv., 1940-46, R.N.; D.O., Ken., 1947; asst. sec., 1959; asst. dir., personnel, 1963-65. (Ken. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947 | D.O. | Kenya | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1959 | asst. sec | Kenya *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1963–1965 | asst. dir., personnel | Kenya *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Crichton, P. D. O'N___St Vincent___1961`

- Staff-list name: **Crichton, P. D. O'N** | colony: **St Vincent** | listed 1961–1965 | editions [1961, 1964, 1965]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1961 | P. D. O. Crichton | Colonial Postmaster | Civil Establishment | — | — |
| 1964 | P. D. O'N. Crichton | Accountant General | Civil Establishment | — | — |
| 1965 | P. D. O'N. Crichton | Accountant General | Civil Establishment | — | — |

### Deterministic checks: `crichton_p_b1920` vs `Crichton, P. D. O'N___St Vincent___1961`

- [PASS] surname_gate: bio 'CRICHTON' vs stint 'Crichton, P. D. O'N' (exact)
- [PASS] initials: bio ['P'] ~ stint ['P', 'D', 'O']
- [PASS] age_gate: stint starts 1961, birth 1920 (age 41)
- [FAIL] colony: no placed event resolves to 'St Vincent'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1961-1965
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

