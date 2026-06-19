<!-- {"case_id": "case_callanan_j-c-j_b1897", "bio_ids": ["callanan_j-c-j_b1897"], "stint_ids": ["Callanan, J. C. J___Kenya___1922", "Callanan, J. C. J___Kenya___1932"]} -->
# Dossier case_callanan_j-c-j_b1897

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `callanan_j-c-j_b1897`

- Printed name: **CALLANAN, J. C. J**
- Birth year: 1897 (attested in editions [1957])
- Honours: O.B.E
- Appears in editions: [1953, 1954, 1957]

### Verbatim printed entry text (OCR)

**Version `col1957-L21686.v` — printed in editions [1957]:**

> CALLANAN, J. C. J., O.B.E.—b. 1897; ed. Clongowes Wood Coll. and Trinity Coll., Dublin; mil. serv., 1919-20, lieut.; M.O., Ken., 1921; S.M.O., 1934; asst. D.M.S., 1939; D.M.S., Swaz., 1946; med. mem., Ken. war pension assess. bd.; sec. and mem., control bd. of health, Ken.; M.O.H., Nairobi dist. coun. area, 1935-45; chmn., High Comsn. Terrs. nursing coun.; publ. Sidelight on the production of Plasmodium tenue.

**Version `col1953-L16778.v` — printed in editions [1953, 1954]:**

> CALLANAN, J. C. J., O.B.E.—b. 1897; Kenya, 1921; D.M.S., Swaz., 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1921 | M.O. | Kenya | [1953, 1954, 1957] |
| 1 | 1934 | S.M.O | Kenya *(inherited from previous clause)* | [1957] |
| 2 | 1935–1945 | M.O.H., Nairobi dist. coun. area | Kenya *(inherited from previous clause)* | [1957] |
| 3 | 1939 | asst. D.M.S | Kenya *(inherited from previous clause)* | [1957] |
| 4 | 1946 | D.M.S., Swaz | Kenya *(inherited from previous clause)* | [1953, 1954, 1957] |

## Candidate stint `Callanan, J. C. J___Kenya___1922`

- Staff-list name: **Callanan, J. C. J** | colony: **Kenya** | listed 1922–1925 | editions [1922, 1923, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | J. C. J. Callanan | Medical Officer | Medical | — | — |
| 1923 | J. C. J. Callanan | Medical Officer | Medical | — | — |
| 1924 | J. C. J. Callanan | Medical Officer | Medical | — | — |
| 1925 | J. C. Callanan | Medical Officer | Medical Department | — | — |

### Deterministic checks: `callanan_j-c-j_b1897` vs `Callanan, J. C. J___Kenya___1922`

- [PASS] surname_gate: bio 'CALLANAN' vs stint 'Callanan, J. C. J' (exact)
- [PASS] initials: bio ['J', 'C', 'J'] ~ stint ['J', 'C', 'J']
- [PASS] age_gate: stint starts 1922, birth 1897 (age 25)
- [PASS] colony: 5 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1922-1925
- [FAIL] position_sim: best 24 vs bar 60: 'M.O.' ~ 'Medical Officer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Callanan, J. C. J___Kenya___1932`

- Staff-list name: **Callanan, J. C. J** | colony: **Kenya** | listed 1932–1936 | editions [1932, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1932 | J. C. J. Callanan | Medical Officers | Medical Department | — | — |
| 1936 | J. C. J. Callanan | Senior Medical Officer | Medical Department | — | — |

### Deterministic checks: `callanan_j-c-j_b1897` vs `Callanan, J. C. J___Kenya___1932`

- [PASS] surname_gate: bio 'CALLANAN' vs stint 'Callanan, J. C. J' (exact)
- [PASS] initials: bio ['J', 'C', 'J'] ~ stint ['J', 'C', 'J']
- [PASS] age_gate: stint starts 1932, birth 1897 (age 35)
- [PASS] colony: 5 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1932-1936
- [FAIL] position_sim: best 38 vs bar 60: 'M.O.H., Nairobi dist. coun. area' ~ 'Senior Medical Officer'
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

