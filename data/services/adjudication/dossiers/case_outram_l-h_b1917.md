<!-- {"case_id": "case_outram_l-h_b1917", "bio_ids": ["outram_l-h_b1917"], "stint_ids": ["Outram, L. H___British Honduras___1954"]} -->
# Dossier case_outram_l-h_b1917

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `outram_l-h_b1917`

- Printed name: **OUTRAM, L. H**
- Birth year: 1917 (attested in editions [1963, 1964, 1965, 1966])
- Honours: C.P.M (1952), O. St. J (1954)
- Appears in editions: [1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1963-L23488.v` — printed in editions [1963, 1964, 1965, 1966]:**

> OUTRAM, L. H., C.P.M. (1952), O. St. J. (1954).—b. 1917; ed. Elizabeth Coll., Guernsey; mil. serv., 1939-41; astt. supt. of pol., B. Guiana, 1941; Trin. and Tob., 1947; supt., 1951; chief of pol., B. Hond., 1954; senr. supt., Ken., 1956; astt. comsnr., 1961. (Ken. Govt. service.)

**Version `col1962-L25080.v` — printed in editions [1962]:**

> OUTRAM, L. H.—b. 1917; ed. Elizabeth Coll. Guernsey; asst. supt. of pol., B. Guiana, 1951; chief of pol., B. Hond. 1954; senr. supt., Ken., 1956; asst. comsnr., 1961.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1941 | astt. supt. of pol., B. Guiana | — | [1963, 1964, 1965, 1966] |
| 1 | 1947 | Trin. and Tob | Trinidad | [1963, 1964, 1965, 1966] |
| 2 | 1951 | supt | Trinidad *(inherited from previous clause)* | [1962, 1963, 1964, 1965, 1966] |
| 3 | 1954 | chief of pol. | British Honduras | [1962, 1963, 1964, 1965, 1966] |
| 4 | 1956 | senr. supt. | Kenya | [1962, 1963, 1964, 1965, 1966] |
| 5 | 1961 | astt. comsnr | Kenya *(inherited from previous clause)* | [1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Outram, L. H___British Honduras___1954`

- Staff-list name: **Outram, L. H** | colony: **British Honduras** | listed 1954–1956 | editions [1954, 1955, 1956]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1954 | L. H. Outram | Superintendent of Police | Civil Establishment | — | — |
| 1955 | L. H. Outram | Superintendent of Police | Civil Establishment | — | — |
| 1956 | L. H. Outram | Superintendent of Police | Civil Establishment | — | — |

### Deterministic checks: `outram_l-h_b1917` vs `Outram, L. H___British Honduras___1954`

- [PASS] surname_gate: bio 'OUTRAM' vs stint 'Outram, L. H' (exact)
- [PASS] initials: bio ['L', 'H'] ~ stint ['L', 'H']
- [PASS] age_gate: stint starts 1954, birth 1917 (age 37)
- [PASS] colony: 1 placed event(s) resolve to 'British Honduras'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1954-1956
- [FAIL] position_sim: best 39 vs bar 60: 'chief of pol.' ~ 'Superintendent of Police'
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

