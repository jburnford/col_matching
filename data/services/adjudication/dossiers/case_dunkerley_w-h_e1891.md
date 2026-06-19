<!-- {"case_id": "case_dunkerley_w-h_e1891", "bio_ids": ["dunkerley_w-h_e1891"], "stint_ids": ["Dunkerley, W. H. C___Straits Settlements___1894", "Dunkerley, W. H. C___Straits Settlements___1900"]} -->
# Dossier case_dunkerley_w-h_e1891

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `dunkerley_w-h_e1891`

- Printed name: **DUNKERLEY, W. H**
- Birth year: not printed
- Appears in editions: [1894, 1896, 1897, 1898, 1900, 1905]

### Verbatim printed entry text (OCR)

**Version `col1897-L31792.v` — printed in editions [1897, 1898, 1900, 1905]:**

> DUNKERLEY, REV. W. H., M.A.—Ed. Pembroke Coll., Oxon.; col. chaplain, Malacca, 1891; ag. col. chaplain, Singapore, May to Oct., 1892, and May, 1896; col. chaplain, Penang, July, 1897; do. Singapore, April, 1901; archdeacon, Dec., 1902.

**Version `col1894-L31334.v` — printed in editions [1894, 1896]:**

> DUNKERLEY, REV. W. H., M.A.—Educated Pembroke Coll., Oxon.; col. chaplain, Malacca, 1891.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1891 | col. chaplain, Malacca | — | [1894, 1896, 1897, 1898, 1900, 1905] |
| 1 | 1892 | ag. col. chaplain | Singapore | [1897, 1898, 1900, 1905] |
| 2 | 1896 | ag. col. chaplain | Singapore *(inherited from previous clause)* | [1897, 1898, 1900, 1905] |
| 3 | 1897 | col. chaplain, Penang | Singapore *(inherited from previous clause)* | [1897, 1898, 1900, 1905] |
| 4 | 1901 | do. Singapore | Dominions Office | [1897, 1898, 1900, 1905] |
| 5 | 1902 | archdeacon | Dominions Office *(inherited from previous clause)* | [1897, 1898, 1900, 1905] |

## Candidate stint `Dunkerley, W. H. C___Straits Settlements___1894`

- Staff-list name: **Dunkerley, W. H. C** | colony: **Straits Settlements** | listed 1894–1897 | editions [1894, 1897]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | W. H. C. Dunkerley | Colonial Chaplain | Malacca | — | — |
| 1897 | Rev. W. H. C. Dunkerley | Colonial Chaplain | Malacca | — | — |

### Deterministic checks: `dunkerley_w-h_e1891` vs `Dunkerley, W. H. C___Straits Settlements___1894`

- [PASS] surname_gate: bio 'DUNKERLEY' vs stint 'Dunkerley, W. H. C' (exact)
- [PASS] initials: bio ['W', 'H'] ~ stint ['W', 'H', 'C']
- [PASS] age_gate: stint starts 1894; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1894-1897
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Dunkerley, W. H. C___Straits Settlements___1900`

- Staff-list name: **Dunkerley, W. H. C** | colony: **Straits Settlements** | listed 1900–1905 | editions [1900, 1905]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1900 | W. H. C. Dunkerley | Chaplain | Penang | — | — |
| 1905 | W. H. C. Dunkerley | Colonial Chaplain | Ecclesiastical | — | — |

### Deterministic checks: `dunkerley_w-h_e1891` vs `Dunkerley, W. H. C___Straits Settlements___1900`

- [PASS] surname_gate: bio 'DUNKERLEY' vs stint 'Dunkerley, W. H. C' (exact)
- [PASS] initials: bio ['W', 'H'] ~ stint ['W', 'H', 'C']
- [PASS] age_gate: stint starts 1900; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1900-1905
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

