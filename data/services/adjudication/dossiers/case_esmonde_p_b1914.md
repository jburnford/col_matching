<!-- {"case_id": "case_esmonde_p_b1914", "bio_ids": ["esmonde_p_b1914"], "stint_ids": ["Esmonde, P___Hong Kong___1949"]} -->
# Dossier case_esmonde_p_b1914

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['esmonde_p_b1914'] carry a single initial only — the namesake trap applies.

## Biography `esmonde_p_b1914`

- Printed name: **ESMONDE, P**
- Birth year: 1914 (attested in editions [1958, 1959, 1960, 1961, 1962])
- Appears in editions: [1958, 1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1958-L22344.v` — printed in editions [1958, 1959, 1960, 1961, 1962]:**

> ESMONDE, P., M.C.—b. 1914; ed. Wimbledon Coll., Stonyhurst Coll., and Royal Coll. of Surgeons, Ireland; mil. serv., 1941-45, major, R.A.M.C.; M.O., H.K., 1945; Uga., 1955; prin. M.O., Buganda, 1957-58; S.M.O., 1958-61.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1945 | M.O. | Hong Kong | [1958, 1959, 1960, 1961, 1962] |
| 1 | 1955 | M.O. | Uganda | [1958, 1959, 1960, 1961, 1962] |
| 2 | 1957–1958 | prin. M.O., Buganda | Uganda *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962] |
| 3 | 1958–1961 | S.M.O | Uganda *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962] |

## Candidate stint `Esmonde, P___Hong Kong___1949`

- Staff-list name: **Esmonde, P** | colony: **Hong Kong** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | P. Esmonde | Medical Officer | Medical | — | — |
| 1950 | P. Esmonde | Medical and Health Officer | MEDICAL | — | — |

### Deterministic checks: `esmonde_p_b1914` vs `Esmonde, P___Hong Kong___1949`

- [PASS] surname_gate: bio 'ESMONDE' vs stint 'Esmonde, P' (exact)
- [PASS] initials: bio ['P'] ~ stint ['P']
- [PASS] age_gate: stint starts 1949, birth 1914 (age 35)
- [PASS] colony: 1 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1950
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

