<!-- {"case_id": "case_fadelle_fred-steens_e1871", "bio_ids": ["fadelle_fred-steens_e1871"], "stint_ids": ["Fadelle, F. S___Dominica___1886", "Fadelle, F. S___Leeward Islands___1899"]} -->
# Dossier case_fadelle_fred-steens_e1871

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Fadelle, F. S___Dominica___1886` is also gate-compatible with biography(ies) outside this case: ['fadelie_f-s_e1878', 'fadelle_fred-stewart_e1871'] (already linked elsewhere or filtered).
- NOTE: stint `Fadelle, F. S___Leeward Islands___1899` is also gate-compatible with biography(ies) outside this case: ['fadelie_f-s_e1878', 'fadelle_fred-stewart_e1871'] (already linked elsewhere or filtered).

## Biography `fadelle_fred-steens_e1871`

- Printed name: **FADELLE, FRED. STEENS**
- Birth year: not printed
- Appears in editions: [1886, 1888, 1889, 1890, 1894]

### Verbatim printed entry text (OCR)

**Version `col1886-L33286.v` — printed in editions [1886, 1888, 1889, 1890, 1894]:**

> FADELLE, FRED. STEENS.—French interpreter to the government, Dominica, 1871; excise officer, 1873; acted as inspector of schools, Jan. to July, 1882.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1871 | French interpreter to the government | Dominica | [1886, 1888, 1889, 1890, 1894] |
| 1 | 1873 | excise officer | Dominica *(inherited from previous clause)* | [1886, 1888, 1889, 1890, 1894] |
| 2 | 1882 | acted as inspector of schools | Dominica *(inherited from previous clause)* | [1886, 1888, 1889, 1890, 1894] |

## Candidate stint `Fadelle, F. S___Dominica___1886`

- Staff-list name: **Fadelle, F. S** | colony: **Dominica** | listed 1886–1898 | editions [1886, 1888, 1894, 1898]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1886 | F. S. Fadelle | Excise Officer | Civil Establishment | — | — |
| 1888 | F. S. Fadelle | Excise Officer | Excise Officers | — | — |
| 1894 | F. S. Fadelle | District Government Officer | Civil Establishment | — | — |
| 1898 | F. S. Fadelle | Postmaster | Post Office | — | — |

### Deterministic checks: `fadelle_fred-steens_e1871` vs `Fadelle, F. S___Dominica___1886`

- [PASS] surname_gate: bio 'FADELLE' vs stint 'Fadelle, F. S' (exact)
- [PASS] initials: bio ['F', 'S'] ~ stint ['F', 'S']
- [PASS] age_gate: stint starts 1886; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'Dominica'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1886-1898
- [FAIL] position_sim: best 39 vs bar 60: 'acted as inspector of schools' ~ 'District Government Officer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

## Candidate stint `Fadelle, F. S___Leeward Islands___1899`

- Staff-list name: **Fadelle, F. S** | colony: **Leeward Islands** | listed 1899–1900 | editions [1899, 1900]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1899 | F. S. Fadelle | Postmaster | Post Office | — | — |
| 1900 | F. S. Fadelle | Postmaster | Post Office | — | — |

### Deterministic checks: `fadelle_fred-steens_e1871` vs `Fadelle, F. S___Leeward Islands___1899`

- [PASS] surname_gate: bio 'FADELLE' vs stint 'Fadelle, F. S' (exact)
- [PASS] initials: bio ['F', 'S'] ~ stint ['F', 'S']
- [PASS] age_gate: stint starts 1899; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1899-1900
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

