<!-- {"case_id": "case_o-connor_michael-patrick_b1896", "bio_ids": ["o-connor_michael-patrick_b1896"], "stint_ids": ["O'Connor, M. P___Straits Settlements___1931"]} -->
# Dossier case_o-connor_michael-patrick_b1896

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 56 official(s) with this surname in the graph's staff lists; 30 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `o-connor_michael-patrick_b1896`

- Printed name: **O'CONNOR, MICHAEL PATRICK**
- Birth year: 1896 (attested in editions [1939, 1940])
- Honours: B.A.O, M.D
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L69513.v` — printed in editions [1939, 1940]:**

> O'CONNOR, MICHAEL PATRICK, M.D., Ch.B., B.A.O., Cert. L.S.T.M.—B. 1896; ed. St. Joseph's Coll., Ireland and Univ. Coll., Dublin; war serv., 1916-20; M.O., Malaya, Feb., 1927; demonstr. in pub. health, Coll. of Med., S'pore, Feb., 1935.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | M.O. | Malaya | [1939, 1940] |
| 1 | 1935 | demonstr. in pub. health, Coll. of Med., S'pore | Malaya *(inherited from previous clause)* | [1939, 1940] |

## Candidate stint `O'Connor, M. P___Straits Settlements___1931`

- Staff-list name: **O'Connor, M. P** | colony: **Straits Settlements** | listed 1931–1933 | editions [1931, 1932, 1933]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | M. P. O'Connor | Medical Officer | Medical | — | — |
| 1932 | M. P. O'Connor | Medical Officer | Medical | — | — |
| 1933 | M. P. O'Connor | Medical Officer | Medical | — | — |

### Deterministic checks: `o-connor_michael-patrick_b1896` vs `O'Connor, M. P___Straits Settlements___1931`

- [PASS] surname_gate: bio 'O'CONNOR' vs stint 'O'Connor, M. P' (exact)
- [PASS] initials: bio ['M', 'P'] ~ stint ['M', 'P']
- [PASS] age_gate: stint starts 1931, birth 1896 (age 35)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1933
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

