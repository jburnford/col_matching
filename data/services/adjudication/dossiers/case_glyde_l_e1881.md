<!-- {"case_id": "case_glyde_l_e1881", "bio_ids": ["glyde_l_e1881"], "stint_ids": ["Glyde, Lavington___South Australia___1878", "Glyde, Lavington___South Australia___1888"]} -->
# Dossier case_glyde_l_e1881

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['glyde_l_e1881'] carry a single initial only — the namesake trap applies.

## Biography `glyde_l_e1881`

- Printed name: **GLYDE, L**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L27664.v` — printed in editions [1883]:**

> GLYDE, HON. L.—Treasurer, South Australia, 24 June, 1881.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1881 | Treasurer | South Australia | [1883] |

## Candidate stint `Glyde, Lavington___South Australia___1878`

- Staff-list name: **Glyde, Lavington** | colony: **South Australia** | listed 1878–1880 | editions [1878, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1878 | L. Glyde | Member | House of Assembly | — | — |
| 1878 | L. Glyde | Chairman | South Australian Institute - Board of Governors | — | — |
| 1880 | Hon. L. Glyde | Board of Governors | South Australian Institute | — | — |

### Deterministic checks: `glyde_l_e1881` vs `Glyde, Lavington___South Australia___1878`

- [PASS] surname_gate: bio 'GLYDE' vs stint 'Glyde, Lavington' (exact)
- [PASS] initials: bio ['L'] ~ stint ['L']
- [PASS] age_gate: stint starts 1878; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'South Australia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1878-1880
- [FAIL] position_sim: best 40 vs bar 60: 'Treasurer' ~ 'Member'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Glyde, Lavington___South Australia___1888`

- Staff-list name: **Glyde, Lavington** | colony: **South Australia** | listed 1888–1890 | editions [1888, 1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | Lavington Glyde | Accountant | Magistrates and Local Courts | — | — |
| 1889 | Lavington Glyde | Accountant | Magistrates and Local Courts | — | — |
| 1890 | Lavington Glyde | Accountant | Magistrates and Local Courts | — | — |

### Deterministic checks: `glyde_l_e1881` vs `Glyde, Lavington___South Australia___1888`

- [PASS] surname_gate: bio 'GLYDE' vs stint 'Glyde, Lavington' (exact)
- [PASS] initials: bio ['L'] ~ stint ['L']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'South Australia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1888-1890
- [FAIL] position_sim: best 21 vs bar 60: 'Treasurer' ~ 'Accountant'
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

