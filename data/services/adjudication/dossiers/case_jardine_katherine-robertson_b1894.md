<!-- {"case_id": "case_jardine_katherine-robertson_b1894", "bio_ids": ["jardine_katherine-robertson_b1894"], "stint_ids": ["Jardine, K. R___Kenya___1949"]} -->
# Dossier case_jardine_katherine-robertson_b1894

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 25 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `jardine_katherine-robertson_b1894`

- Printed name: **JARDINE, Katherine Robertson**
- Birth year: 1894 (attested in editions [1949, 1950, 1951])
- Appears in editions: [1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1949-L33209.v` — printed in editions [1949, 1950, 1951]:**

> JARDINE, Katherine Robertson.—b. 1894; ed. St. Joseph's Coll., W. Aust.; nursing sister, Ken., 1930; senr., 1944.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1930 | nursing sister | Kenya | [1949, 1950, 1951] |
| 1 | 1944 | senr | Kenya *(inherited from previous clause)* | [1949, 1950, 1951] |

## Candidate stint `Jardine, K. R___Kenya___1949`

- Staff-list name: **Jardine, K. R** | colony: **Kenya** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | K. R. Jardine | Matrons (2), Grade II | Medical | — | — |
| 1950 | K. R. Jardine | Matrons, Grade I | Medical | — | — |

### Deterministic checks: `jardine_katherine-robertson_b1894` vs `Jardine, K. R___Kenya___1949`

- [PASS] surname_gate: bio 'JARDINE' vs stint 'Jardine, K. R' (exact)
- [PASS] initials: bio ['K', 'R'] ~ stint ['K', 'R']
- [PASS] age_gate: stint starts 1949, birth 1894 (age 55)
- [PASS] colony: 2 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1950
- [FAIL] position_sim: best 21 vs bar 60: 'senr' ~ 'Matrons, Grade I'
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

