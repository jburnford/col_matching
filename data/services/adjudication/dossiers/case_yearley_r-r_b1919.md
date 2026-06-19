<!-- {"case_id": "case_yearley_r-r_b1919", "bio_ids": ["yearley_r-r_b1919"], "stint_ids": ["Yearley, R. R___Gold Coast___1949"]} -->
# Dossier case_yearley_r-r_b1919

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `yearley_r-r_b1919`

- Printed name: **YEARLEY, R. R**
- Birth year: 1919 (attested in editions [1957])
- Appears in editions: [1956, 1957]

### Verbatim printed entry text (OCR)

**Version `col1957-L28645.v` — printed in editions [1957]:**

> YEARLEY, R. R.—b. 1919; ed. Sir Geo. Monoux Gram. Sch.; mil. serv., 1940-46; Br. P.O., 1936; acctnt., posts and tels., G.C., 1948; contrlr., savings bk., 1955; (Ghana civ. serv.).

**Version `col1956-L25182.v` — printed in editions [1956]:**

> YEARLEY, R. R.—b. 1919; ed. Sir Geo. Monoux Gram. Sch.; mil. serv., 1940–46; Br. P.O., 1936; acctnt., posts and tels., G.C., 1948.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1936 | Br. P.O | — | [1956, 1957] |
| 1 | 1948 | acctnt., posts and tels. | Gold Coast | [1956, 1957] |
| 2 | 1955 | contrlr., savings bk | Gold Coast *(inherited from previous clause)* | [1957] |

## Candidate stint `Yearley, R. R___Gold Coast___1949`

- Staff-list name: **Yearley, R. R** | colony: **Gold Coast** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | R. R. Yearley | Accountants | Posts and Telegraphs | — | — |
| 1951 | R. R. Yearley | Accountants | Accounts Branch | — | — |

### Deterministic checks: `yearley_r-r_b1919` vs `Yearley, R. R___Gold Coast___1949`

- [PASS] surname_gate: bio 'YEARLEY' vs stint 'Yearley, R. R' (exact)
- [PASS] initials: bio ['R', 'R'] ~ stint ['R', 'R']
- [PASS] age_gate: stint starts 1949, birth 1919 (age 30)
- [PASS] colony: 2 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 56 vs bar 60: 'acctnt., posts and tels.' ~ 'Accountants'
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

