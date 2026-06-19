<!-- {"case_id": "case_vetch_campbell-foster_b1886", "bio_ids": ["vetch_campbell-foster_b1886"], "stint_ids": ["Vetch, C. F___Nigeria___1921"]} -->
# Dossier case_vetch_campbell-foster_b1886

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `vetch_campbell-foster_b1886`

- Printed name: **VETCH, CAMPBELL FOSTER**
- Birth year: 1886 (attested in editions [1931, 1932, 1933])
- Appears in editions: [1931, 1932, 1933]

### Verbatim printed entry text (OCR)

**Version `col1931-L69014.v` — printed in editions [1931, 1932, 1933]:**

> VETCH, CAMPBELL FOSTER.—B. 1886; ed. Bedford and South Eastern Agrl. Coll., Wye; asst. conserv., forests, S. Nigeria, 1911; conserv., 1915; senr. conserv., 1928.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1911 | asst. conserv., forests | Southern Nigeria | [1931, 1932, 1933] |
| 1 | 1915 | conserv | Southern Nigeria *(inherited from previous clause)* | [1931, 1932, 1933] |
| 2 | 1928 | senr. conserv | Southern Nigeria *(inherited from previous clause)* | [1931, 1932, 1933] |

## Candidate stint `Vetch, C. F___Nigeria___1921`

- Staff-list name: **Vetch, C. F** | colony: **Nigeria** | listed 1921–1925 | editions [1921, 1922, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | C. F. Vetch | Conservator | Forestry | — | — |
| 1922 | C. F. Vetch | Conservator | Forestry | — | — |
| 1925 | C. F. Vetch | Conservator | Forestry | — | — |

### Deterministic checks: `vetch_campbell-foster_b1886` vs `Vetch, C. F___Nigeria___1921`

- [PASS] surname_gate: bio 'VETCH' vs stint 'Vetch, C. F' (exact)
- [PASS] initials: bio ['C', 'F'] ~ stint ['C', 'F']
- [PASS] age_gate: stint starts 1921, birth 1886 (age 35)
- [PASS] colony: 3 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1921-1925
- [PASS] position_sim: best 78 vs bar 60: 'conserv' ~ 'Conservator'
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

