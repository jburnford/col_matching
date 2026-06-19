<!-- {"case_id": "case_culpin_g-e_b1919", "bio_ids": ["culpin_g-e_b1919"], "stint_ids": ["Culpin, G. E___Gold Coast___1949"]} -->
# Dossier case_culpin_g-e_b1919

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `culpin_g-e_b1919`

- Printed name: **CULPIN, G. E**
- Birth year: 1919 (attested in editions [1959, 1960])
- Appears in editions: [1956, 1959, 1960]

### Verbatim printed entry text (OCR)

**Version `col1959-L22133.v` — printed in editions [1959, 1960]:**

> CULPIN, G. E.—b. 1919; ed. Mexboro' Gram. Sch.; mil. serv., 1939-46; acctnt., G.C. rlyws. and harbours, 1947; senr. acctnt., 1954; asst. to gen. manager, 1956 (Ghana civil service).

**Version `col1956-L20657.v` — printed in editions [1956]:**

> CULPIN, G. E.—b. 1919; ed. Mexborough Gram. Sch. and Rotherham Coll. of Tech.; acctnt., G.C. rlys., 1947; senr. acctnt., 1954 (G.C. local service).

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947 | acctnt., G.C. rlyws. and harbours | Gold Coast | [1956, 1959, 1960] |
| 1 | 1954 | senr. acctnt | Gold Coast *(inherited from previous clause)* | [1956, 1959, 1960] |
| 2 | 1956 | asst. to gen. manager | Gold Coast *(inherited from previous clause)* | [1959, 1960] |

## Candidate stint `Culpin, G. E___Gold Coast___1949`

- Staff-list name: **Culpin, G. E** | colony: **Gold Coast** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | G. E. Culpin | Accountants | Railway and Takoradi Harbour | — | — |
| 1951 | G. E. Culpin | Accountants | Accounts Branch | — | — |

### Deterministic checks: `culpin_g-e_b1919` vs `Culpin, G. E___Gold Coast___1949`

- [PASS] surname_gate: bio 'CULPIN' vs stint 'Culpin, G. E' (exact)
- [PASS] initials: bio ['G', 'E'] ~ stint ['G', 'E']
- [PASS] age_gate: stint starts 1949, birth 1919 (age 30)
- [PASS] colony: 3 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 41 vs bar 60: 'acctnt., G.C. rlyws. and harbours' ~ 'Accountants'
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

