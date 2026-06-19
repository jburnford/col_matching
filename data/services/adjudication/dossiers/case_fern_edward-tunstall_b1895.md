<!-- {"case_id": "case_fern_edward-tunstall_b1895", "bio_ids": ["fern_edward-tunstall_b1895"], "stint_ids": ["Fern, E. T___Falkland Islands___1955", "Fern, E. T___Northern Rhodesia___1927"]} -->
# Dossier case_fern_edward-tunstall_b1895

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `fern_edward-tunstall_b1895`

- Printed name: **FERN, Edward Tunstall**
- Birth year: 1895 (attested in editions [1948])
- Honours: M.R.C.V.S
- Appears in editions: [1948]

### Verbatim printed entry text (OCR)

**Version `col1948-L32566.v` — printed in editions [1948]:**

> FERN, Edward Tunstall, M.R.C.V.S.—b. 1895; ed. S.A. Coll. Sch., Royal (Dick) Vet. Coll., Edinburgh Univ.; on mil. serv. 1914-19; vet. offr., Union of S.A., 1922; N. Rhod., 1926; D.D.V.S., 1943.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1922 | vet. offr., Union of S.A | — | [1948] |
| 1 | 1926 | vet. offr., Union of S.A | Northern Rhodesia | [1948] |
| 2 | 1943 | D.D.V.S | Northern Rhodesia *(inherited from previous clause)* | [1948] |

## Candidate stint `Fern, E. T___Falkland Islands___1955`

- Staff-list name: **Fern, E. T** | colony: **Falkland Islands** | listed 1955–1957 | editions [1955, 1956, 1957]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1955 | E. T. Fern | Veterinary Officer | Civil Establishment | — | — |
| 1956 | E. T. Fern | Veterinary Officer | Civil Establishment | — | — |
| 1957 | E. T. Fern | Veterinary Officer | Civil Establishment | — | — |

### Deterministic checks: `fern_edward-tunstall_b1895` vs `Fern, E. T___Falkland Islands___1955`

- [PASS] surname_gate: bio 'FERN' vs stint 'Fern, E. T' (exact)
- [PASS] initials: bio ['E', 'T'] ~ stint ['E', 'T']
- [PASS] age_gate: stint starts 1955, birth 1895 (age 60)
- [FAIL] colony: no placed event resolves to 'Falkland Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1955-1957
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Fern, E. T___Northern Rhodesia___1927`

- Staff-list name: **Fern, E. T** | colony: **Northern Rhodesia** | listed 1927–1940 | editions [1927, 1929, 1930, 1931, 1933, 1936, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1927 | E. T. Fern | Veterinary Officers | Veterinary | — | — |
| 1929 | E. T. Fern | Veterinary Officer | Veterinary | — | — |
| 1930 | E. T. Fern | Veterinary Officers | Veterinary | — | — |
| 1931 | E. T. Fern | Veterinary Officers | Animal Health | — | — |
| 1933 | E. T. Fern | Veterinary Officer | Animal Health | — | — |
| 1936 | E. T. Fern | Veterinary Officer | Veterinary | — | — |
| 1937 | E. T. Fern | Veterinary Officer | Veterinary | — | — |
| 1939 | E. T. Fern | Veterinary Officer | Veterinary | — | — |
| 1940 | E. T. Fern | Veterinary Officers | Veterinary | — | — |

### Deterministic checks: `fern_edward-tunstall_b1895` vs `Fern, E. T___Northern Rhodesia___1927`

- [PASS] surname_gate: bio 'FERN' vs stint 'Fern, E. T' (exact)
- [PASS] initials: bio ['E', 'T'] ~ stint ['E', 'T']
- [PASS] age_gate: stint starts 1927, birth 1895 (age 32)
- [PASS] colony: 2 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1927-1940
- [FAIL] position_sim: best 46 vs bar 60: 'vet. offr., Union of S.A' ~ 'Veterinary Officers'
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

