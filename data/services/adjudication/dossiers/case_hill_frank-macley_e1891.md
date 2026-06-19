<!-- {"case_id": "case_hill_frank-macley_e1891", "bio_ids": ["hill_frank-macley_e1891"], "stint_ids": ["Hill, F. M___Bechuanaland___1921"]} -->
# Dossier case_hill_frank-macley_e1891

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 111 official(s) with this surname in the graph's staff lists; 42 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hill_frank-macley_e1891`

- Printed name: **HILL, FRANK MACLEY**
- Birth year: not printed
- Appears in editions: [1924, 1925, 1927, 1928, 1929]

### Verbatim printed entry text (OCR)

**Version `col1924-L55095.v` — printed in editions [1924, 1925, 1927, 1928, 1929]:**

> HILL, FRANK MACLEY.—Graduated, Lond., 1891; gov't. vet. offr., Bechuana land Prot., 1919; J.P., 1920.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1891 | Graduated, Lond | — | [1924, 1925, 1927, 1928, 1929] |
| 1 | 1919 | gov't. vet. offr. | Bechuana land | [1924, 1925, 1927, 1928, 1929] |
| 2 | 1920 | J.P | Bechuana land *(inherited from previous clause)* | [1924, 1925, 1927, 1928, 1929] |

## Candidate stint `Hill, F. M___Bechuanaland___1921`

- Staff-list name: **Hill, F. M** | colony: **Bechuanaland** | listed 1921–1925 | editions [1921, 1922, 1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | F. M. Hill | Veterinary Surgeon | Establishment | — | — |
| 1922 | F. M. Hill | Veterinary Surgeon | Establishment | — | — |
| 1924 | F. M. Hill | Veterinary Surgeon | — | — | — |
| 1925 | F. M. Hill | Veterinary Surgeon | Civil Establishment | — | — |

### Deterministic checks: `hill_frank-macley_e1891` vs `Hill, F. M___Bechuanaland___1921`

- [PASS] surname_gate: bio 'HILL' vs stint 'Hill, F. M' (exact)
- [PASS] initials: bio ['F', 'M'] ~ stint ['F', 'M']
- [PASS] age_gate: stint starts 1921; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Bechuanaland'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1921-1925
- [FAIL] position_sim: best 39 vs bar 60: 'gov't. vet. offr.' ~ 'Veterinary Surgeon'
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

