<!-- {"case_id": "case_adapoe_cephas-kodjo-fianyehia_b1912", "bio_ids": ["adapoe_cephas-kodjo-fianyehia_b1912", "adapoe_cephas-kodjo-flanyehia_b1912"], "stint_ids": ["Adapoe, C. K. F___Gold Coast___1949"]} -->
# Dossier case_adapoe_cephas-kodjo-fianyehia_b1912

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Adapoe, C. K. F___Gold Coast___1949'] have more than one claimant biography in this case.

## Biography `adapoe_cephas-kodjo-fianyehia_b1912`

- Printed name: **ADAPOE, Cephas Kodjo Fianyehia**
- Birth year: 1912 (attested in editions [1951])
- Appears in editions: [1951]

### Verbatim printed entry text (OCR)

**Version `col1951-L35537.v` — printed in editions [1951]:**

> ADAPOE, Cephas Kodjo Fianyehia.—b. 1912; ed. Ewe Prep. Sch., Gov. Tech. Sch., City of Lond. Coll., and acctnt. gen. dept., G.P.O., Lond.; 2nd div. clk., G.C., 1930; acctnt., posts and tels. dept., G.C., 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1930 | 2nd div. clk. | Gold Coast | [1951] |
| 1 | 1947 | acctnt., posts and tels. dept. | Gold Coast | [1951] |

## Biography `adapoe_cephas-kodjo-flanyehia_b1912`

- Printed name: **ADAPOE, Cephas Kodjo Flanyehia**
- Birth year: 1912 (attested in editions [1950])
- Appears in editions: [1950]

### Verbatim printed entry text (OCR)

**Version `col1950-L33092.v` — printed in editions [1950]:**

> ADAPOE, Cephas Kodjo Flanyehia.—b. 1912; ed. Ewe Presb. Sch., City of Lond. Coll., and acctnt. gen. dept., Lond.; 2nd div. clk., G.C., 1930; acctnt., 1497.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1930 | 2nd div. clk. | Gold Coast | [1950] |

## Candidate stint `Adapoe, C. K. F___Gold Coast___1949`

- Staff-list name: **Adapoe, C. K. F** | colony: **Gold Coast** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | C. K. F. Adapoe | Accountants | Posts and Telegraphs | — | — |
| 1951 | C. K. F. Adapoe | Accountants | Accounts Branch | — | — |

### Deterministic checks: `adapoe_cephas-kodjo-fianyehia_b1912` vs `Adapoe, C. K. F___Gold Coast___1949`

- [PASS] surname_gate: bio 'ADAPOE' vs stint 'Adapoe, C. K. F' (exact)
- [PASS] initials: bio ['C', 'K', 'F'] ~ stint ['C', 'K', 'F']
- [PASS] age_gate: stint starts 1949, birth 1912 (age 37)
- [PASS] colony: 2 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 49 vs bar 60: 'acctnt., posts and tels. dept.' ~ 'Accountants'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `adapoe_cephas-kodjo-flanyehia_b1912` vs `Adapoe, C. K. F___Gold Coast___1949`

- [PASS] surname_gate: bio 'ADAPOE' vs stint 'Adapoe, C. K. F' (exact)
- [PASS] initials: bio ['C', 'K', 'F'] ~ stint ['C', 'K', 'F']
- [PASS] age_gate: stint starts 1949, birth 1912 (age 37)
- [PASS] colony: 1 placed event(s) resolve to 'Gold Coast'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
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

