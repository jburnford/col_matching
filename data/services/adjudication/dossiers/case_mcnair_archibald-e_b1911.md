<!-- {"case_id": "case_mcnair_archibald-e_b1911", "bio_ids": ["mcnair_archibald-e_b1911"], "stint_ids": ["McNair, A. E___British Honduras___1951", "McNair, A. E___Jamaica___1954"]} -->
# Dossier case_mcnair_archibald-e_b1911

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mcnair_archibald-e_b1911`

- Printed name: **McNAIR, Archibald E**
- Birth year: 1911 (attested in editions [1955, 1956, 1957, 1959, 1960, 1961, 1962, 1963, 1964])
- Appears in editions: [1951, 1953, 1954, 1955, 1956, 1957, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1955-L21806.v` — printed in editions [1955, 1956, 1957, 1959, 1960, 1961, 1962, 1963, 1964]:**

> McNAIR, A. E.—b. 1911; ed. Barrow-in-Furness Gram. Sch., Didsbury Coll. and Manchester Univ.; Methodist missionary wk. in J'ca; soc. dev. offr. and registr. of co-op. soc. and credit unions, B. Hond., 1950; prin. asst. sec., min. of educ. and soc. welf., J'ca, 1953; sec., comsnr. of eng. into juvenile delinquency, B. Hond., 1953.

**Version `col1951-L40534.v` — printed in editions [1951, 1953, 1954]:**

> McNAIR, Archibald E.—b. 1911; ed. Coat Bridge Sch., Scotland, Barrow-in-Furness Gram. Sch. (N. Univ. cert.), Didsbury Coll., and Manchester Univ.; Methodist missionary wk. in Jca.; soc. dev. offr. and regisr. of co-op. soc., and credit unions, B. Hond., 1950; author of Studies in Poultry Rearing for Egg Production for Cooperative Groups.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1950 | soc. dev. offr. and registr. of co-op. soc. and credit unions | British Honduras | [1951, 1953, 1954, 1955, 1956, 1957, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1953 | prin. asst. sec., min. of educ. and soc. welf. | Jamaica | [1955, 1956, 1957, 1959, 1960, 1961, 1962, 1963, 1964] |
| 2 | 1953 | sec., comsnr. of eng. into juvenile delinquency | British Honduras | [1955, 1956, 1957, 1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `McNair, A. E___British Honduras___1951`

- Staff-list name: **McNair, A. E** | colony: **British Honduras** | listed 1951–1953 | editions [1951, 1952, 1953]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1951 | A. E. McNair | — | Social Development | — | — |
| 1952 | A. E. McNair | Social Development Officer | Civil Establishment | — | — |
| 1953 | A. E. McNair | Social Development Officer | Civil Establishment | — | — |

### Deterministic checks: `mcnair_archibald-e_b1911` vs `McNair, A. E___British Honduras___1951`

- [PASS] surname_gate: bio 'McNAIR' vs stint 'McNair, A. E' (exact)
- [PASS] initials: bio ['A', 'E'] ~ stint ['A', 'E']
- [PASS] age_gate: stint starts 1951, birth 1911 (age 40)
- [PASS] colony: 2 placed event(s) resolve to 'British Honduras'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1951-1953
- [FAIL] position_sim: best 44 vs bar 60: 'soc. dev. offr. and registr. of co-op. soc. and credit unions' ~ 'Social Development Officer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `McNair, A. E___Jamaica___1954`

- Staff-list name: **McNair, A. E** | colony: **Jamaica** | listed 1954–1956 | editions [1954, 1955, 1956]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1954 | A. E. McNair | Principal Assistant Secretary | Civil Establishment | — | — |
| 1955 | A. E. McNair | Principal Assistant Secretary | Civil Establishment | — | — |
| 1956 | A. E. McNair | Principal Assistant Secretary | Civil Establishment | — | — |

### Deterministic checks: `mcnair_archibald-e_b1911` vs `McNair, A. E___Jamaica___1954`

- [PASS] surname_gate: bio 'McNAIR' vs stint 'McNair, A. E' (exact)
- [PASS] initials: bio ['A', 'E'] ~ stint ['A', 'E']
- [PASS] age_gate: stint starts 1954, birth 1911 (age 43)
- [PASS] colony: 1 placed event(s) resolve to 'Jamaica'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1954-1956
- [FAIL] position_sim: best 45 vs bar 60: 'prin. asst. sec., min. of educ. and soc. welf.' ~ 'Principal Assistant Secretary'
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

