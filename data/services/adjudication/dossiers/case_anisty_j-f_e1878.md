<!-- {"case_id": "case_anisty_j-f_e1878", "bio_ids": ["anisty_j-f_e1878", "manisty_j-f_e1878-2"], "stint_ids": ["Manisty, J. F___Natal___1883"]} -->
# Dossier case_anisty_j-f_e1878

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Manisty, J. F___Natal___1883'] have more than one claimant biography in this case.
- NOTE: stint `Manisty, J. F___Natal___1883` is also gate-compatible with biography(ies) outside this case: ['manisty_j-f_e1878'] (already linked elsewhere or filtered).
- NOTE: stint `Manisty, J. F___Natal___1883` is also gate-compatible with biography(ies) outside this case: ['manisty_j-f_e1878'] (already linked elsewhere or filtered).

## Biography `anisty_j-f_e1878`

- Printed name: **ANISTY, J. F**
- Birth year: not printed
- Appears in editions: [1897]

### Verbatim printed entry text (OCR)

**Version `col1897-L33264.v` — printed in editions [1897]:**

> ANISTY, J. F.—Traffic superintendent, Natal government railways, 1878; dep. prot. of Indian grants, 1892.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1878 | Traffic superintendent, Natal government railways | Natal | [1897] |
| 1 | 1892 | dep. prot. of Indian grants | Natal *(inherited from previous clause)* | [1897] |

## Biography `manisty_j-f_e1878-2`

- Printed name: **MANISTY, J. F**
- Birth year: not printed
- Appears in editions: [1896, 1898, 1899, 1900]

### Verbatim printed entry text (OCR)

**Version `col1896-L40245.v` — printed in editions [1896, 1898, 1899, 1900]:**

> MANISTY, J. F.—Traffic superintendent, Natal government railways, 1878; dep. prot. of Indian immigrants, 1892.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1878 | Traffic superintendent, Natal government railways | Natal | [1896, 1898, 1899, 1900] |
| 1 | 1892 | dep. prot. of Indian immigrants | Natal *(inherited from previous clause)* | [1896, 1898, 1899, 1900] |

## Candidate stint `Manisty, J. F___Natal___1883`

- Staff-list name: **Manisty, J. F** | colony: **Natal** | listed 1883–1890 | editions [1883, 1886, 1888, 1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1883 | J. F. Manisty | Superintendent of Indian and Native Labour Department | Natal Government Railways | — | — |
| 1886 | J. F. Manisty | Superintendent of Indian and Native Labour Department | Natal Government Railways | — | — |
| 1888 | J. F. Manisty | Superintendent of Indian and Native Labour Department | Natal Government Railways | — | — |
| 1889 | J. F. Manisty | Superintendent of Indian and Native Labour Department | Natal Government Railways | — | — |
| 1890 | J. F. Manisty | Superintendent of Indian and Native Labour Department | Natal Government Railways | — | — |

### Deterministic checks: `anisty_j-f_e1878` vs `Manisty, J. F___Natal___1883`

- [PASS] surname_gate: bio 'ANISTY' vs stint 'Manisty, J. F' (fuzzy:1)
- [PASS] initials: bio ['J', 'F'] ~ stint ['J', 'F']
- [PASS] age_gate: stint starts 1883; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Natal'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1883-1890
- [FAIL] position_sim: best 59 vs bar 60: 'Traffic superintendent, Natal government railways' ~ 'Superintendent of Indian and Native Labour Department'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

### Deterministic checks: `manisty_j-f_e1878-2` vs `Manisty, J. F___Natal___1883`

- [PASS] surname_gate: bio 'MANISTY' vs stint 'Manisty, J. F' (exact)
- [PASS] initials: bio ['J', 'F'] ~ stint ['J', 'F']
- [PASS] age_gate: stint starts 1883; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Natal'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1883-1890
- [FAIL] position_sim: best 59 vs bar 60: 'Traffic superintendent, Natal government railways' ~ 'Superintendent of Indian and Native Labour Department'
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

