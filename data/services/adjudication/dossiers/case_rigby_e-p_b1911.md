<!-- {"case_id": "case_rigby_e-p_b1911", "bio_ids": ["rigby_e-p_b1911"], "stint_ids": ["Rigby, E. P___Kenya___1949"]} -->
# Dossier case_rigby_e-p_b1911

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 15 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `rigby_e-p_b1911`

- Printed name: **RIGBY, E. P**
- Birth year: 1911 (attested in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963])
- Honours: M.B.E
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1957-L26726.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963]:**

> RIGBY, E. P., M.B.E.—b. 1911; ed. Rossall Sch. and London Univ.; mil. serv., 1940-45, maj.; M.O., Ken., 1939; S.M.O., 1952; asst. D.M.S., 1955; D.D.M.S., 1957; C.M.O., 1961-62.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1939 | M.O. | Kenya | [1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 1 | 1952 | S.M.O | Kenya *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 2 | 1955 | asst. D.M.S | Kenya *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 3 | 1957 | D.D.M.S | Kenya *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 4 | 1961–1962 | C.M.O | Kenya *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963] |

## Candidate stint `Rigby, E. P___Kenya___1949`

- Staff-list name: **Rigby, E. P** | colony: **Kenya** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | E. P. Rigby | Medical Officer | Medical | — | — |
| 1950 | E. P. Rigby | Medical Officer | Medical | — | — |
| 1951 | E. P. Rigby | Medical Officer | Medical | — | — |

### Deterministic checks: `rigby_e-p_b1911` vs `Rigby, E. P___Kenya___1949`

- [PASS] surname_gate: bio 'RIGBY' vs stint 'Rigby, E. P' (exact)
- [PASS] initials: bio ['E', 'P'] ~ stint ['E', 'P']
- [PASS] age_gate: stint starts 1949, birth 1911 (age 38)
- [PASS] colony: 5 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 24 vs bar 60: 'M.O.' ~ 'Medical Officer'
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

