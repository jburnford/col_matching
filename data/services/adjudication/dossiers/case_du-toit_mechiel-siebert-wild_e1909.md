<!-- {"case_id": "case_du-toit_mechiel-siebert-wild_e1909", "bio_ids": ["du-toit_mechiel-siebert-wild_e1909"], "stint_ids": ["du Toit, M. S. W___South Africa___1912"]} -->
# Dossier case_du-toit_mechiel-siebert-wild_e1909

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 15 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `du-toit_mechiel-siebert-wild_e1909`

- Printed name: **DU TOIT, MECHIEL SIEBERT WILD**
- Birth year: not printed
- Appears in editions: [1928]

### Verbatim printed entry text (OCR)

**Version `col1928-L65902.v` — printed in editions [1928]:**

> DU TOIT, MECHIEL SIEBERT WILD.—Comn., pol., Orange River Colony, 9th Feb., 1909; dep. comn., S. African pol., 1st Apr., 1913; dep. comn., S. African pol. hdqrs., 1st Jan., 1927.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1909 | Comn., pol. | Orange River Colony | [1928] |
| 1 | 1913 | dep. comn., S. African pol | Orange River Colony *(inherited from previous clause)* | [1928] |
| 2 | 1927 | dep. comn., S. African pol. hdqrs | Orange River Colony *(inherited from previous clause)* | [1928] |

## Candidate stint `du Toit, M. S. W___South Africa___1912`

- Staff-list name: **du Toit, M. S. W** | colony: **South Africa** | listed 1912–1918 | editions [1912, 1914, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | M. S. W. du Toit | Commissioner of Police, Orange Free State | Police | — | — |
| 1914 | M. S. W. du Toit | Deputy Commissioner, Orange Free State Division, Bloemfontein | Police | — | — |
| 1918 | M. S. W. du Toit | Deputy Commissioner, Cape Eastern Division | Police | — | — |

### Deterministic checks: `du-toit_mechiel-siebert-wild_e1909` vs `du Toit, M. S. W___South Africa___1912`

- [PASS] surname_gate: bio 'DU TOIT' vs stint 'du Toit, M. S. W' (exact)
- [PASS] initials: bio ['M', 'S', 'W'] ~ stint ['M', 'S', 'W']
- [PASS] age_gate: stint starts 1912; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1918
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

