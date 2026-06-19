<!-- {"case_id": "case_wace_j-e_e1882", "bio_ids": ["wace_j-e_e1882"], "stint_ids": ["Wace, J. E___Natal___1883"]} -->
# Dossier case_wace_j-e_e1882

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `wace_j-e_e1882`

- Printed name: **WACE, J. E**
- Birth year: not printed
- Appears in editions: [1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1888-L36535.v` — printed in editions [1888, 1889, 1890]:**

> WACE, J. E.—Clerk, civil service salary commission, Natal, 1883; sessional clerk, legislative council, 1882; usher, Sept., 1882; sergeant-at-arms, 1889.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1882 | sessional clerk, legislative council | Natal *(inherited from previous clause)* | [1888, 1889, 1890] |
| 1 | 1883 | Clerk, civil service salary commission | Natal | [1888, 1889, 1890] |
| 2 | 1889 | sergeant-at-arms | Natal *(inherited from previous clause)* | [1888, 1889, 1890] |

## Candidate stint `Wace, J. E___Natal___1883`

- Staff-list name: **Wace, J. E** | colony: **Natal** | listed 1883–1889 | editions [1883, 1886, 1888, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1883 | J. E. Wace | Usher | Legislative Council Office | — | — |
| 1886 | J. E. Wace | Usher | Legislative Council Office | — | — |
| 1888 | J. E. Wace | Usher | Legislative Council Office | — | — |
| 1889 | J. E. Wace | Usher | Legislative Council Office | — | — |

### Deterministic checks: `wace_j-e_e1882` vs `Wace, J. E___Natal___1883`

- [PASS] surname_gate: bio 'WACE' vs stint 'Wace, J. E' (exact)
- [PASS] initials: bio ['J', 'E'] ~ stint ['J', 'E']
- [PASS] age_gate: stint starts 1883; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'Natal'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1883-1889
- [FAIL] position_sim: best 32 vs bar 60: 'sergeant-at-arms' ~ 'Usher'
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

