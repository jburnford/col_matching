<!-- {"case_id": "case_champion_j-s_b1921", "bio_ids": ["champion_j-s_b1921"], "stint_ids": ["Champion, J. S___Uganda___1949", "Champion, J. S___Uganda___1960"]} -->
# Dossier case_champion_j-s_b1921

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 12 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `champion_j-s_b1921`

- Printed name: **CHAMPION, J. S**
- Birth year: 1921 (attested in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964])
- Honours: O.B.E (1963)
- Terminal: retired 1963 — “retd., 1963”
- Appears in editions: [1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1958-L21292.v` — printed in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964]:**

> CHAMPION, J. S., O.B.E. (1963).—b. 1921; ed. Shrewsbury Sch., and Balliol Coll., Oxford; mil. serv., 1941-46, lieut.; admin. cadet, Uga., 1946; D.O., 1948; clk., coun., 1951; p.s. to gov., 1952; asst. fin. sec., 1956; dep. sec. (admin.), min. of health, 1959; perm. sec., 1960; perm. sec., min. sec. and ext. rels., 1961; perm. sec., min. internal affairs; retd., 1963. (Uga. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | admin. cadet | Uganda | [1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1948 | admin. cadet | Dominions Office | [1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 2 | 1951 | clk., coun | Dominions Office *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 3 | 1952 | p.s. to gov | Dominions Office *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 4 | 1956 | asst. fin. sec | Dominions Office *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 5 | 1959 | dep. sec. (admin.), min. of health | Dominions Office *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 6 | 1960 | perm. sec | Dominions Office *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 7 | 1961 | perm. sec., min. sec. and ext. rels | Dominions Office *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Champion, J. S___Uganda___1949`

- Staff-list name: **Champion, J. S** | colony: **Uganda** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | J. S. Champion | District Officers and Assistant District Officers | Provincial Administration | — | — |
| 1951 | J. S. Champion | District Officers and Assistant District Officers | Provincial Administration | — | — |
| 1951 | J. S. Champion | Secretaries (Seconded from the Provincial Administration) | Secretariat | — | — |

### Deterministic checks: `champion_j-s_b1921` vs `Champion, J. S___Uganda___1949`

- [PASS] surname_gate: bio 'CHAMPION' vs stint 'Champion, J. S' (exact)
- [PASS] initials: bio ['J', 'S'] ~ stint ['J', 'S']
- [PASS] age_gate: stint starts 1949, birth 1921 (age 28)
- [PASS] colony: 1 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 33 vs bar 60: 'admin. cadet' ~ 'District Officers and Assistant District Officers'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Champion, J. S___Uganda___1960`

- Staff-list name: **Champion, J. S** | colony: **Uganda** | listed 1960–1962 | editions [1960, 1961, 1962]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1960 | J. S. Champion | Deputy Secretary to the Ministry of Health | Civil Establishment | — | — |
| 1961 | J. S. Champion | Permanent Secretary for Security and External Relations | Civil Establishment | — | — |
| 1962 | J. S. Champion | Permanent Secretary for Security and External Relations | Civil Establishment | — | — |

### Deterministic checks: `champion_j-s_b1921` vs `Champion, J. S___Uganda___1960`

- [PASS] surname_gate: bio 'CHAMPION' vs stint 'Champion, J. S' (exact)
- [PASS] initials: bio ['J', 'S'] ~ stint ['J', 'S']
- [PASS] age_gate: stint starts 1960, birth 1921 (age 39)
- [PASS] colony: 1 placed event(s) resolve to 'Uganda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1960-1962
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

