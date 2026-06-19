<!-- {"case_id": "case_bascom_henry-sabsbiefeld_e1887", "bio_ids": ["bascom_henry-sabsbiefeld_e1887"], "stint_ids": ["Bascom, H. S___Gambia___1894", "Bascom, H. S___Gold Coast___1889"]} -->
# Dossier case_bascom_henry-sabsbiefeld_e1887

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Bascom, H. S___Gambia___1894` is also gate-compatible with biography(ies) outside this case: ['bascom_henry-sarsfield_e1887'] (already linked elsewhere or filtered).
- NOTE: stint `Bascom, H. S___Gold Coast___1889` is also gate-compatible with biography(ies) outside this case: ['bascom_henry-sarsfield_e1887'] (already linked elsewhere or filtered).

## Biography `bascom_henry-sabsbiefeld_e1887`

- Printed name: **BASCOM, HENRY SABSBIEFELD**
- Birth year: not printed
- Appears in editions: [1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1888-L31986.v` — printed in editions [1888, 1889, 1890]:**

> BASCOM, HENRY SABSBIEFELD.—Educated at Harrow; supervisor of customs, Gold Coast, Jan., 1887; chief clerk, colonial secretary's office, Aug., 1887.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1887 | supervisor of customs | Gold Coast | [1888, 1889, 1890] |

## Candidate stint `Bascom, H. S___Gambia___1894`

- Staff-list name: **Bascom, H. S** | colony: **Gambia** | listed 1894–1896 | editions [1894, 1896]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | H. S. Bascom | Collector of Customs | Civil Establishment | — | — |
| 1896 | H. S. Bascom | Collector of Customs | Civil Establishment | — | — |

### Deterministic checks: `bascom_henry-sabsbiefeld_e1887` vs `Bascom, H. S___Gambia___1894`

- [PASS] surname_gate: bio 'BASCOM' vs stint 'Bascom, H. S' (exact)
- [PASS] initials: bio ['H', 'S'] ~ stint ['H', 'S']
- [PASS] age_gate: stint starts 1894; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Gambia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1894-1896
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Bascom, H. S___Gold Coast___1889`

- Staff-list name: **Bascom, H. S** | colony: **Gold Coast** | listed 1889–1890 | editions [1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1889 | H. S. Bascom | Chief Clerk | Colonial Secretary's Office | — | — |
| 1890 | H. S. Bascom | Chief Clerk | Colonial Secretary's Office | — | — |

### Deterministic checks: `bascom_henry-sabsbiefeld_e1887` vs `Bascom, H. S___Gold Coast___1889`

- [PASS] surname_gate: bio 'BASCOM' vs stint 'Bascom, H. S' (exact)
- [PASS] initials: bio ['H', 'S'] ~ stint ['H', 'S']
- [PASS] age_gate: stint starts 1889; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1889-1890
- [FAIL] position_sim: best 31 vs bar 60: 'supervisor of customs' ~ 'Chief Clerk'
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

