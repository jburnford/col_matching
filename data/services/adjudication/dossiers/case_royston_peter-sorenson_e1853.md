<!-- {"case_id": "case_royston_peter-sorenson_e1853", "bio_ids": ["royston_peter-sorenson_e1853"], "stint_ids": ["Royston, P. S___Mauritius___1879"]} -->
# Dossier case_royston_peter-sorenson_e1853

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `royston_peter-sorenson_e1853`

- Printed name: **Royston, Peter Sorenson**
- Birth year: not printed
- Appears in editions: [1883, 1886, 1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1883-L28628.v` — printed in editions [1883, 1886, 1888, 1889, 1890]:**

> MAURITIUS, 4th Bishop of, Peter Sorenson, Royston.—Trinity College, Cambridge, B.A. in classical and mathematical honours, 1853; M.A., 1860; D.D., 1872; resident tutor of Church Missionary College, 1853-55; corresponding secretary of South India mission, 1855-71, except from 1864-66, when incumbent of Plaines Wilhems, Mauritius; consecrated 1872.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1853–1855 | resident tutor of Church Missionary College | — | [1883, 1886, 1888, 1889, 1890] |
| 1 | 1855–1871 | corresponding secretary of South India mission | — | [1883, 1886, 1888, 1889, 1890] |
| 2 | 1864–1866 | incumbent of Plaines Wilhems | Mauritius | [1883, 1886, 1888, 1889, 1890] |
| 3 | 1872–1872 | — | — | [1883, 1886, 1888, 1889, 1890] |

## Candidate stint `Royston, P. S___Mauritius___1879`

- Staff-list name: **Royston, P. S** | colony: **Mauritius** | listed 1879–1890 | editions [1879, 1883, 1888, 1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1879 | P. S. Royston | Lord Bishop of Mauritius | Church of England | — | — |
| 1883 | Right Rev. P. S. Royston | Bishop of Mauritius | Church of England | — | — |
| 1888 | P. S. Royston | Bishop of Mauritius | Church of England | — | — |
| 1889 | P. S. Royston | Bishop of Mauritius | Church of England | — | — |
| 1890 | P. S. Royston | Bishop of Mauritius | Church of England | — | — |

### Deterministic checks: `royston_peter-sorenson_e1853` vs `Royston, P. S___Mauritius___1879`

- [PASS] surname_gate: bio 'Royston' vs stint 'Royston, P. S' (exact)
- [PASS] initials: bio ['P', 'S'] ~ stint ['P', 'S']
- [PASS] age_gate: stint starts 1879; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Mauritius'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1879-1890
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

