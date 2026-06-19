<!-- {"case_id": "case_tallack_r-j-k_b1913", "bio_ids": ["tallack_r-j-k_b1913"], "stint_ids": ["Tallack, R. J___Zanzibar___1950"]} -->
# Dossier case_tallack_r-j-k_b1913

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `tallack_r-j-k_b1913`

- Printed name: **TALLACK, R. J. K**
- Birth year: 1913 (attested in editions [1957, 1958, 1959])
- Appears in editions: [1957, 1958, 1959]

### Verbatim printed entry text (OCR)

**Version `col1957-L27680.v` — printed in editions [1957, 1958, 1959]:**

> TALLACK, R. J. K.—b. 1913; ed. Clifton Coll., Bristol; mil. serv., 1939-46, lt.-col. R.A.M.C.; M.O., Zanz., 1946; S.M.O., Ken., 1956-58.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | M.O. | Zanzibar | [1957, 1958, 1959] |
| 1 | 1956–1958 | S.M.O. | Kenya | [1957, 1958, 1959] |

## Candidate stint `Tallack, R. J___Zanzibar___1950`

- Staff-list name: **Tallack, R. J** | colony: **Zanzibar** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | R. J. Tallack | Medical Officers | Health | — | — |
| 1951 | R. J. Tallack | Medical Officer | Health | — | — |

### Deterministic checks: `tallack_r-j-k_b1913` vs `Tallack, R. J___Zanzibar___1950`

- [PASS] surname_gate: bio 'TALLACK' vs stint 'Tallack, R. J' (exact)
- [PASS] initials: bio ['R', 'J', 'K'] ~ stint ['R', 'J']
- [PASS] age_gate: stint starts 1950, birth 1913 (age 37)
- [PASS] colony: 1 placed event(s) resolve to 'Zanzibar'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1950-1951
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

