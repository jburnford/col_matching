<!-- {"case_id": "case_eustace_j-t_e1879", "bio_ids": ["eustace_j-t_e1879"], "stint_ids": ["Eustace, J. T___Cape of Good Hope___1890"]} -->
# Dossier case_eustace_j-t_e1879

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `eustace_j-t_e1879`

- Printed name: **EUSTACE, J. T**
- Birth year: not printed
- Appears in editions: [1886, 1888, 1889, 1890, 1894, 1896, 1897]

### Verbatim printed entry text (OCR)

**Version `col1886-L33272.v` — printed in editions [1886, 1888, 1889, 1890, 1894, 1896, 1897]:**

> EUSTACE, J. T.—Civil commissioner and resident magistrate, Namaqualand division, Cape of Good Hope, 1st July, 1879.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1879 | Civil commissioner and resident magistrate, Namaqualand division | Cape of Good Hope | [1886, 1888, 1889, 1890, 1894, 1896, 1897] |

## Candidate stint `Eustace, J. T___Cape of Good Hope___1890`

- Staff-list name: **Eustace, J. T** | colony: **Cape of Good Hope** | listed 1890–1896 | editions [1890, 1896]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1890 | J. T. Eustace | C.C. and R.M. | Division of Namaqualand | — | — |
| 1896 | J. T. Eustace | R.M. | DIVISION OF MOSSEL BAY | — | — |

### Deterministic checks: `eustace_j-t_e1879` vs `Eustace, J. T___Cape of Good Hope___1890`

- [PASS] surname_gate: bio 'EUSTACE' vs stint 'Eustace, J. T' (exact)
- [PASS] initials: bio ['J', 'T'] ~ stint ['J', 'T']
- [PASS] age_gate: stint starts 1890; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Cape of Good Hope'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1890-1896
- [FAIL] position_sim: best 50 vs bar 60: 'Civil commissioner and resident magistrate, Namaqualand division' ~ 'C.C. and R.M.'
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

