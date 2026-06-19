<!-- {"case_id": "case_collyer_w-r_e1882", "bio_ids": ["collyer_w-r_e1882"], "stint_ids": ["Collyer, W. R___Straits Settlements___1894"]} -->
# Dossier case_collyer_w-r_e1882

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Collyer, W. R___Straits Settlements___1894` is also gate-compatible with biography(ies) outside this case: ['collyer_w-r_b1842'] (already linked elsewhere or filtered).

## Biography `collyer_w-r_e1882`

- Printed name: **COLLYER, W. R**
- Birth year: not printed
- Appears in editions: [1883, 1886]

### Verbatim printed entry text (OCR)

**Version `col1883-L26931.v` — printed in editions [1883, 1886]:**

> COLLYER, W. R.—Queen's advocate, Cyprus, 1882.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1882 | Queen's advocate | Cyprus | [1883, 1886] |

## Candidate stint `Collyer, W. R___Straits Settlements___1894`

- Staff-list name: **Collyer, W. R** | colony: **Straits Settlements** | listed 1894–1905 | editions [1894, 1896, 1897, 1898, 1899, 1905]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | W. R. Collyer | Attorney-General | Judicial Department | — | — |
| 1896 | W. R. Collyer | Attorney-General | Judicial Department | — | — |
| 1897 | W. R. Collyer | Attorney-General | Judicial Department | — | — |
| 1898 | W. R. Collyer | Attorney-General | Judicial Department | — | — |
| 1899 | W. R. Collyer | Attorney-General | Judicial Department | — | — |
| 1905 | W. R. Collyer | Attorney-General | Judicial Department | — | — |

### Deterministic checks: `collyer_w-r_e1882` vs `Collyer, W. R___Straits Settlements___1894`

- [PASS] surname_gate: bio 'COLLYER' vs stint 'Collyer, W. R' (exact)
- [PASS] initials: bio ['W', 'R'] ~ stint ['W', 'R']
- [PASS] age_gate: stint starts 1894; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1894-1905
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

