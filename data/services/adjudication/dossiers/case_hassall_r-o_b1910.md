<!-- {"case_id": "case_hassall_r-o_b1910", "bio_ids": ["hassall_r-o_b1910"], "stint_ids": ["Hassall, R. O___Fiji___1955"]} -->
# Dossier case_hassall_r-o_b1910

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hassall_r-o_b1910`

- Printed name: **HASSALL, R. O**
- Birth year: 1910 (attested in editions [1954])
- Appears in editions: [1954]

### Verbatim printed entry text (OCR)

**Version `col1954-L20725.v` — printed in editions [1954]:**

> HASSALL, R. O.—b. 1910; Swaz. police 1929; supt., 1943; Bech. Prot., 1952; dep. comsnr., 1953.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | Swaz. police | — | [1954] |
| 1 | 1943 | supt | — | [1954] |
| 2 | 1952 | supt | Bechuanaland | [1954] |
| 3 | 1953 | dep. comsnr | Bechuanaland *(inherited from previous clause)* | [1954] |

## Candidate stint `Hassall, R. O___Fiji___1955`

- Staff-list name: **Hassall, R. O** | colony: **Fiji** | listed 1955–1959 | editions [1955, 1956, 1957, 1958, 1959]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1955 | R. O. Hassall | Deputy Commissioner | Civil Establishment | — | — |
| 1956 | R. O. Hassall | Deputy Commissioner | Civil Establishment | — | — |
| 1957 | R. O. Hassall | Deputy Commissioner | Civil Establishment | — | — |
| 1958 | R. O. Hassall | Deputy Commissioner | Civil Establishment | — | — |
| 1959 | R. O. Hassall | Deputy Commissioner | Civil Establishment | — | — |

### Deterministic checks: `hassall_r-o_b1910` vs `Hassall, R. O___Fiji___1955`

- [PASS] surname_gate: bio 'HASSALL' vs stint 'Hassall, R. O' (exact)
- [PASS] initials: bio ['R', 'O'] ~ stint ['R', 'O']
- [PASS] age_gate: stint starts 1955, birth 1910 (age 45)
- [FAIL] colony: no placed event resolves to 'Fiji'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1955-1959
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

