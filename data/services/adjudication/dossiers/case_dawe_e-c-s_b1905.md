<!-- {"case_id": "case_dawe_e-c-s_b1905", "bio_ids": ["dawe_e-c-s_b1905"], "stint_ids": ["Dawe, E. C. S___Tanganyika___1953"]} -->
# Dossier case_dawe_e-c-s_b1905

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Dawe, E. C. S___Tanganyika___1953` is also gate-compatible with biography(ies) outside this case: ['dawe_eli_b1843'] (already linked elsewhere or filtered).

## Biography `dawe_e-c-s_b1905`

- Printed name: **DAWE, E. C. S**
- Birth year: 1905 (attested in editions [1953, 1954, 1955, 1956, 1957])
- Appears in editions: [1953, 1954, 1955, 1956, 1957]

### Verbatim printed entry text (OCR)

**Version `col1953-L17108.v` — printed in editions [1953, 1954, 1955, 1956, 1957]:**

> DAWE, E. C. S.—b. 1905 ; ed. Bedford Sch., Royal (Dick) Vet. Coll., Edin., and Royal Vet. Coll., Lond. ; vet. offr., Bech., 1933 ; prin. vet. offr., 1946 ; D.V.S., 1948 ; D.D.V.S., Tang., 1951.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1933 | vet. offr. | Bechuanaland | [1953, 1954, 1955, 1956, 1957] |
| 1 | 1946 | prin. vet. offr | Bechuanaland *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957] |
| 2 | 1948 | D.V.S | Bechuanaland *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957] |
| 3 | 1951 | D.D.V.S. | Tanganyika | [1953, 1954, 1955, 1956, 1957] |

## Candidate stint `Dawe, E. C. S___Tanganyika___1953`

- Staff-list name: **Dawe, E. C. S** | colony: **Tanganyika** | listed 1953–1957 | editions [1953, 1954, 1956, 1957]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1953 | E. C. S. Dawe | Deputy Director | Civil Establishment | — | — |
| 1954 | E. C. S. Dawe | Director of Veterinary Services | Civil Establishment | — | — |
| 1956 | E. C. S. Dawe | Director of Veterinary Services | Civil Establishment | — | — |
| 1957 | E. C. S. Dawe | Director of Veterinary Services | Civil Establishment | — | — |

### Deterministic checks: `dawe_e-c-s_b1905` vs `Dawe, E. C. S___Tanganyika___1953`

- [PASS] surname_gate: bio 'DAWE' vs stint 'Dawe, E. C. S' (exact)
- [PASS] initials: bio ['E', 'C', 'S'] ~ stint ['E', 'C', 'S']
- [PASS] age_gate: stint starts 1953, birth 1905 (age 48)
- [PASS] colony: 1 placed event(s) resolve to 'Tanganyika'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1953-1957
- [FAIL] position_sim: best 21 vs bar 60: 'D.D.V.S.' ~ 'Deputy Director'
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

