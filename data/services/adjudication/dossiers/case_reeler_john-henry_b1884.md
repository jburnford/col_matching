<!-- {"case_id": "case_reeler_john-henry_b1884", "bio_ids": ["reeler_john-henry_b1884"], "stint_ids": ["Reeler, J. H___Cape of Good Hope___1907"]} -->
# Dossier case_reeler_john-henry_b1884

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `reeler_john-henry_b1884`

- Printed name: **REELER, JOHN HENRY**
- Birth year: 1884 (attested in editions [1939, 1940])
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L70079.v` — printed in editions [1939, 1940]:**

> REELER, JOHN HENRY.—B. 1884; ed. Sea Point High Schl., Cape Town; Cape col. pub. serv., 1899; Cape Prov. adminstr., 1910; prov. acct., 1922.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1899 | Cape col. pub. serv | Cape of Good Hope | [1939, 1940] |
| 1 | 1910 | Cape Prov. adminstr | Cape of Good Hope | [1939, 1940] |
| 2 | 1922 | prov. acct | Cape of Good Hope *(inherited from previous clause)* | [1939, 1940] |

## Candidate stint `Reeler, J. H___Cape of Good Hope___1907`

- Staff-list name: **Reeler, J. H** | colony: **Cape of Good Hope** | listed 1907–1908 | editions [1907, 1908]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1907 | J. H. Reeler | Clerks | Accounting Branch | — | — |
| 1908 | J. H. Reeler | Clerks | Accounting Branch | — | — |

### Deterministic checks: `reeler_john-henry_b1884` vs `Reeler, J. H___Cape of Good Hope___1907`

- [PASS] surname_gate: bio 'REELER' vs stint 'Reeler, J. H' (exact)
- [PASS] initials: bio ['J', 'H'] ~ stint ['J', 'H']
- [PASS] age_gate: stint starts 1907, birth 1884 (age 23)
- [PASS] colony: 3 placed event(s) resolve to 'Cape of Good Hope'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1907-1908
- [FAIL] position_sim: best 35 vs bar 60: 'Cape col. pub. serv' ~ 'Clerks'
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

