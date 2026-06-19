<!-- {"case_id": "case_everingham_william_e1879", "bio_ids": ["everingham_william_e1879"], "stint_ids": ["Everingham, W___Straits Settlements___1888"]} -->
# Dossier case_everingham_william_e1879

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['everingham_william_e1879'] carry a single initial only — the namesake trap applies.

## Biography `everingham_william_e1879`

- Printed name: **EVERINGHAM, WILLIAM**
- Birth year: not printed
- Appears in editions: [1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1889-L32998.v` — printed in editions [1889, 1890]:**

> EVERINGHAM, REV. WILLIAM.—Lincoln Theological Coll., 1887; 1st class Camb. Theol. exam.; curate of Beeston, 1879; of Diss., 1880; acting military chaplain, assistant chaplain St. Andrew's Cathedral, and chaplain to merchant seamen, Hong Kong, 1881; acting colonial chaplain, Hong Kong, 1884; colonial chaplain, Malacca, 1885.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1879 | curate of Beeston | — | [1889, 1890] |
| 1 | 1880 | of Diss | — | [1889, 1890] |
| 2 | 1881 | acting military chaplain, assistant chaplain St. Andrew's Cathedral, and chaplain to merchant seamen | Hong Kong | [1889, 1890] |
| 3 | 1884 | acting colonial chaplain | Hong Kong | [1889, 1890] |
| 4 | 1885 | colonial chaplain, Malacca | Hong Kong *(inherited from previous clause)* | [1889, 1890] |
| 5 | 1887 | Lincoln Theological Coll | — | [1889, 1890] |

## Candidate stint `Everingham, W___Straits Settlements___1888`

- Staff-list name: **Everingham, W** | colony: **Straits Settlements** | listed 1888–1889 | editions [1888, 1889]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1888 | W. Everingham | Colonial Chaplain | Malacca | — | — |
| 1889 | W. Everingham | Official | Malacca | — | — |

### Deterministic checks: `everingham_william_e1879` vs `Everingham, W___Straits Settlements___1888`

- [PASS] surname_gate: bio 'EVERINGHAM' vs stint 'Everingham, W' (exact)
- [PASS] initials: bio ['W'] ~ stint ['W']
- [PASS] age_gate: stint starts 1888; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1888-1889
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

