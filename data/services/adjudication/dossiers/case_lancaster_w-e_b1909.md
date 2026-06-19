<!-- {"case_id": "case_lancaster_w-e_b1909", "bio_ids": ["lancaster_w-e_b1909"], "stint_ids": ["Lancaster, W. E___Federation of Malaya___1951"]} -->
# Dossier case_lancaster_w-e_b1909

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `lancaster_w-e_b1909`

- Printed name: **LANCASTER, W. E**
- Birth year: 1909 (attested in editions [1953])
- Appears in editions: [1953, 1954, 1955, 1956, 1957]

### Verbatim printed entry text (OCR)

**Version `col1953-L18072.v` — printed in editions [1953]:**

> LANCASTER, W. E.—b. 1909; ed. Bedford Modern Sch., Royal (Dick) Vet. Coll. and Edin. and Camb. Univs.; mil. serv., p.o.w., 1942-45; vet. surg., S.S. and F.M.S., 1933; state vet. surg., 1935; vet. offr., Johore, 1941; D.D.V.S., 1946; D.V.S., Mal., 1950.

**Version `col1954-L21184.v` — printed in editions [1954, 1955, 1956, 1957]:**

> LANCASTER, W. E.—b. 1909 ; ed. Bedford Modern Sch., Royal (Dick) Vet. Coll., Edin. Univ. and Downing Coll., Camb.; mil. serv., p.o.w., 1942-45; vet. offr., S.S. and F.M.S., 1933; D.D.V.S., Mal., 1946; D.V.S., 1950.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1933 | vet. surg., S.S. and F.M.S | Straits Settlements | [1953, 1954, 1955, 1956, 1957] |
| 1 | 1935 | state vet. surg | Straits Settlements *(inherited from previous clause)* | [1953] |
| 2 | 1941 | vet. offr. | Johore | [1953] |
| 3 | 1946 | D.D.V.S | Malaya | [1953, 1954, 1955, 1956, 1957] |
| 4 | 1950 | D.V.S. | Malaya | [1953, 1954, 1955, 1956, 1957] |

## Candidate stint `Lancaster, W. E___Federation of Malaya___1951`

- Staff-list name: **Lancaster, W. E** | colony: **Federation of Malaya** | listed 1951–1952 | editions [1951, 1952]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1951 | W. E. Lancaster | Malayan Administrative Pool | Administrative Service | — | — |
| 1951 | W. E. Lancaster | Director of Veterinary Services | Veterinary | — | — |
| 1952 | W. E. Lancaster | Director of Veterinary Services | Civil Establishment | — | — |

### Deterministic checks: `lancaster_w-e_b1909` vs `Lancaster, W. E___Federation of Malaya___1951`

- [PASS] surname_gate: bio 'LANCASTER' vs stint 'Lancaster, W. E' (exact)
- [PASS] initials: bio ['W', 'E'] ~ stint ['W', 'E']
- [PASS] age_gate: stint starts 1951, birth 1909 (age 42)
- [PASS] colony: 3 placed event(s) resolve to 'Federation of Malaya'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1951-1952
- [FAIL] position_sim: best 18 vs bar 60: 'D.V.S.' ~ 'Director of Veterinary Services'
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

