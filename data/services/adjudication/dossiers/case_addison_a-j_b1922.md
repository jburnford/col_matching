<!-- {"case_id": "case_addison_a-j_b1922", "bio_ids": ["addison_a-j_b1922"], "stint_ids": ["Addison, A. J___Gold Coast___1949"]} -->
# Dossier case_addison_a-j_b1922

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 21 official(s) with this surname in the graph's staff lists; 10 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `addison_a-j_b1922`

- Printed name: **ADDISON, A. J**
- Birth year: 1922 (attested in editions [1956])
- Appears in editions: [1956]

### Verbatim printed entry text (OCR)

**Version `col1956-L19330.v` — printed in editions [1956]:**

> ADDISON, A. J.—b. 1922; ed. Msantsipim Sch., Achimota Coll. and Queen Mary Coll., London; prob. asst. engrnr., G.C., 1943; engrnr., 1948; regl. engrnr. (G.C. local service), 1955.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1943 | prob. asst. engrnr. | Gold Coast | [1956] |
| 1 | 1948 | engrnr | Gold Coast *(inherited from previous clause)* | [1956] |
| 2 | 1955 | regl. engrnr. (G.C. local service) | Gold Coast *(inherited from previous clause)* | [1956] |

## Candidate stint `Addison, A. J___Gold Coast___1949`

- Staff-list name: **Addison, A. J** | colony: **Gold Coast** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | A. J. Addison | Engineers | Posts and Telegraphs | — | — |
| 1951 | A. J. Addison | Engineers | Engineering Branch | — | — |

### Deterministic checks: `addison_a-j_b1922` vs `Addison, A. J___Gold Coast___1949`

- [PASS] surname_gate: bio 'ADDISON' vs stint 'Addison, A. J' (exact)
- [PASS] initials: bio ['A', 'J'] ~ stint ['A', 'J']
- [PASS] age_gate: stint starts 1949, birth 1922 (age 27)
- [PASS] colony: 3 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [PASS] position_sim: best 67 vs bar 60: 'engrnr' ~ 'Engineers'
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

