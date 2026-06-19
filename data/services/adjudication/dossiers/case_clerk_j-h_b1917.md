<!-- {"case_id": "case_clerk_j-h_b1917", "bio_ids": ["clerk_j-h_b1917"], "stint_ids": ["Clerk, J. H___Jamaica___1954"]} -->
# Dossier case_clerk_j-h_b1917

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `clerk_j-h_b1917`

- Printed name: **CLERK, J. H**
- Birth year: 1917 (attested in editions [1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964])
- Appears in editions: [1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1954-L19940.v` — printed in editions [1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]:**

> CLERK, J. H.—b. 1917; ed. J'ca Coll.; apptd. J'ca, 1936; H.M. Legation, Panama (sec'on.), 1941-44; C.O., 1948-51; prin. asst. sec., 1953; perm. sec., 1956.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1936 | apptd. J'ca | — | [1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1941–1944 | H.M. Legation, Panama (sec'on.) | — | [1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 2 | 1948–1951 | H.M. Legation, Panama (sec'on.) | Colonial Office | [1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 3 | 1953 | prin. asst. sec | Colonial Office *(inherited from previous clause)* | [1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 4 | 1956 | perm. sec | Colonial Office *(inherited from previous clause)* | [1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Clerk, J. H___Jamaica___1954`

- Staff-list name: **Clerk, J. H** | colony: **Jamaica** | listed 1954–1956 | editions [1954, 1955, 1956]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1954 | J. H. Clerk | Principal Assistant Secretary | Civil Establishment | — | — |
| 1955 | J. H. Clerk | Principal Assistant Secretary | Civil Establishment | — | — |
| 1956 | J. H. Clerk | Principal Assistant Secretary | Civil Establishment | — | — |

### Deterministic checks: `clerk_j-h_b1917` vs `Clerk, J. H___Jamaica___1954`

- [PASS] surname_gate: bio 'CLERK' vs stint 'Clerk, J. H' (exact)
- [PASS] initials: bio ['J', 'H'] ~ stint ['J', 'H']
- [PASS] age_gate: stint starts 1954, birth 1917 (age 37)
- [FAIL] colony: no placed event resolves to 'Jamaica'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1954-1956
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

