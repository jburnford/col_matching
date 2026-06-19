<!-- {"case_id": "case_harding_annie-kathleen_b1902", "bio_ids": ["harding_annie-kathleen_b1902"], "stint_ids": ["Harding, A. K___Kenya___1937", "Harding, K___Bahamas___1954"]} -->
# Dossier case_harding_annie-kathleen_b1902

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 39 official(s) with this surname in the graph's staff lists; 18 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `harding_annie-kathleen_b1902`

- Printed name: **HARDING, Annie Kathleen**
- Birth year: 1902 (attested in editions [1949, 1950, 1951])
- Appears in editions: [1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1949-L32660.v` — printed in editions [1949, 1950, 1951]:**

> HARDING, Annie Kathleen, B.Sc. (hons. bot.), sec. teach. dip.—b. 1902; ed. Hanley High Sch., Stoke-on-Trent, and Manchester Univ.; sci. mist., High Sch., Ken., 1935.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1935 | sci. mist., High Sch. | Kenya | [1949, 1950, 1951] |

## Candidate stint `Harding, A. K___Kenya___1937`

- Staff-list name: **Harding, A. K** | colony: **Kenya** | listed 1937–1940 | editions [1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1937 | A. K. Harding | Education Officer—European Education | Education | — | — |
| 1939 | Miss A. K. Harding | Education Officer, European Education | Education | — | — |
| 1940 | Miss A. K. Harding | Education Officers—European Education | Education | — | — |

### Deterministic checks: `harding_annie-kathleen_b1902` vs `Harding, A. K___Kenya___1937`

- [PASS] surname_gate: bio 'HARDING' vs stint 'Harding, A. K' (exact)
- [PASS] initials: bio ['A', 'K'] ~ stint ['A', 'K']
- [PASS] age_gate: stint starts 1937, birth 1902 (age 35)
- [PASS] colony: 1 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1937-1940
- [FAIL] position_sim: best 23 vs bar 60: 'sci. mist., High Sch.' ~ 'Education Officers—European Education'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Harding, K___Bahamas___1954`

- Staff-list name: **Harding, K** | colony: **Bahamas** | listed 1954–1957 | editions [1954, 1955, 1956, 1957]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1954 | Major K. Harding | Private Secretary and Clerk to Executive Council | Civil Establishment | — | Major |
| 1955 | Major K. Harding. | Private Secretary and Clerk to Executive Council | Civil Establishment | — | Major |
| 1956 | K. Harding | Private Secretary and Clerk to Executive Council | Civil Establishment | — | Major |
| 1957 | Major K. Harding | Private Secretary | Civil Establishment | — | Major |

### Deterministic checks: `harding_annie-kathleen_b1902` vs `Harding, K___Bahamas___1954`

- [PASS] surname_gate: bio 'HARDING' vs stint 'Harding, K' (exact)
- [PASS] initials: bio ['A', 'K'] ~ stint ['K']
- [PASS] age_gate: stint starts 1954, birth 1902 (age 52)
- [FAIL] colony: no placed event resolves to 'Bahamas'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1954-1957
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

