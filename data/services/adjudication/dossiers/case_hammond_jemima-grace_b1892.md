<!-- {"case_id": "case_hammond_jemima-grace_b1892", "bio_ids": ["hammond_jemima-grace_b1892"], "stint_ids": ["Hammond___Leeward Islands___1920"]} -->
# Dossier case_hammond_jemima-grace_b1892

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 29 official(s) with this surname in the graph's staff lists; 11 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Hammond___Leeward Islands___1920` is also gate-compatible with biography(ies) outside this case: ['hammond_e-j_e1876', 'hammond_h-t_e1881', 'hammond_stanley-alfred-andrew_b1898'] (already linked elsewhere or filtered).

## Biography `hammond_jemima-grace_b1892`

- Printed name: **HAMMOND, Jemima Grace**
- Birth year: 1892 (attested in editions [1949])
- Appears in editions: [1949]

### Verbatim printed entry text (OCR)

**Version `col1949-L32635.v` — printed in editions [1949]:**

> HAMMOND, Jemima Grace.—b. 1892; ed. Ashly Church Sch., Mkt. Harborough Gram. Sch. and Northampton High Sch., J.C.; nursing sister, 1930; senr., N. Rhod., 1944.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1930 | nursing sister | — | [1949] |
| 1 | 1944 | senr. | Northern Rhodesia | [1949] |

## Candidate stint `Hammond___Leeward Islands___1920`

- Staff-list name: **Hammond** | colony: **Leeward Islands** | listed 1920–1923 | editions [1920, 1922, 1923]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1920 | Hammond | Assistant Matron, Hospital | Hospital and Poor House | — | — |
| 1922 | Miss Hammond | Assistant Matron, Hospital | Hospital and Poor House | — | — |
| 1923 | Miss Hammond | Assistant Matron, Hospital | Hospital and Poor House | — | — |

### Deterministic checks: `hammond_jemima-grace_b1892` vs `Hammond___Leeward Islands___1920`

- [PASS] surname_gate: bio 'HAMMOND' vs stint 'Hammond' (exact)
- [PASS] initials: bio ['J', 'G'] ~ stint ['?']
- [PASS] age_gate: stint starts 1920, birth 1892 (age 28)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1920-1923
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

