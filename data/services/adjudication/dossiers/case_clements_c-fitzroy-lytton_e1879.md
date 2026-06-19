<!-- {"case_id": "case_clements_c-fitzroy-lytton_e1879", "bio_ids": ["clements_c-fitzroy-lytton_e1879"], "stint_ids": ["Clements, C. F___St Vincent___1888"]} -->
# Dossier case_clements_c-fitzroy-lytton_e1879

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 12 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `clements_c-fitzroy-lytton_e1879`

- Printed name: **CLEMENTS, C. Fitzroy Lytton**
- Birth year: not printed
- Appears in editions: [1886, 1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1886-L32700.v` — printed in editions [1886, 1888, 1889, 1890]:**

> CLEMENTS, C. Fitzroy Lytton.—Entered audit office, Barbados, June, 1879; chief clerk and accountant, treasury, St. Lucia, April, 1881; chief clerk in the government office and clerk to the executive and legislative councils, St. Vincent, Oct., 1882; deputy treasurer, June, 1883; private secretary to the lieutenant governor, August, 1883; J.P. for the colony.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1879 | Entered audit office | Barbados | [1886, 1888, 1889, 1890] |
| 1 | 1881 | chief clerk and accountant, treasury | St. Lucia | [1886, 1888, 1889, 1890] |
| 2 | 1882 | chief clerk in the government office and clerk to the executive and legislative councils | St. Vincent | [1886, 1888, 1889, 1890] |
| 3 | 1883 | deputy treasurer | St. Vincent *(inherited from previous clause)* | [1886, 1888, 1889, 1890] |

## Candidate stint `Clements, C. F___St Vincent___1888`

- Staff-list name: **Clements, C. F** | colony: **St Vincent** | listed 1888–1890 | editions [1888, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | C. F. Clements | Chief Clerk | Civil Establishment | — | — |
| 1890 | C. F. Clements | Chief Clerk | Civil Establishment | — | — |

### Deterministic checks: `clements_c-fitzroy-lytton_e1879` vs `Clements, C. F___St Vincent___1888`

- [PASS] surname_gate: bio 'CLEMENTS' vs stint 'Clements, C. F' (exact)
- [PASS] initials: bio ['C', 'F', 'L'] ~ stint ['C', 'F']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'St Vincent'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1888-1890
- [FAIL] position_sim: best 30 vs bar 60: 'deputy treasurer' ~ 'Chief Clerk'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

