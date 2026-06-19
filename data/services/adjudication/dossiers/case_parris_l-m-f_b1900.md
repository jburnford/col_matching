<!-- {"case_id": "case_parris_l-m-f_b1900", "bio_ids": ["parris_l-m-f_b1900"], "stint_ids": ["Parris, L. M. F___Leeward Islands___1924", "Parris, L. M. F___Leeward Islands___1949"]} -->
# Dossier case_parris_l-m-f_b1900

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `parris_l-m-f_b1900`

- Printed name: **PARRIS, L. M. F**
- Birth year: 1900 (attested in editions [1953, 1954, 1955])
- Appears in editions: [1953, 1954, 1955]

### Verbatim printed entry text (OCR)

**Version `col1953-L18664.v` — printed in editions [1953, 1954, 1955]:**

> PARRIS, L. M. F.—b. 1900; ed. St. Paul's Sch., Nevis; rev. offr., 1928; registr's clk., 1930; senr. rev. offr., 1938; asst. marktg. offr., Nevis, 1942; marktg. offr., Antigua, 1944.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | rev. offr | — | [1953, 1954, 1955] |
| 1 | 1930 | registr's clk | — | [1953, 1954, 1955] |
| 2 | 1938 | senr. rev. offr | — | [1953, 1954, 1955] |
| 3 | 1942 | asst. marktg. offr. | Nevis | [1953, 1954, 1955] |
| 4 | 1944 | marktg. offr. | Antigua | [1953, 1954, 1955] |

## Candidate stint `Parris, L. M. F___Leeward Islands___1924`

- Staff-list name: **Parris, L. M. F** | colony: **Leeward Islands** | listed 1924–1925 | editions [1924, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1924 | L. M. F. Parris | Bailiff | Judicial and Legal | — | — |
| 1925 | L. M. F. Parris | Bailiff | Judicial and Legal | — | — |

### Deterministic checks: `parris_l-m-f_b1900` vs `Parris, L. M. F___Leeward Islands___1924`

- [PASS] surname_gate: bio 'PARRIS' vs stint 'Parris, L. M. F' (exact)
- [PASS] initials: bio ['L', 'M', 'F'] ~ stint ['L', 'M', 'F']
- [PASS] age_gate: stint starts 1924, birth 1900 (age 24)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1924-1925
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Parris, L. M. F___Leeward Islands___1949`

- Staff-list name: **Parris, L. M. F** | colony: **Leeward Islands** | listed 1949–1954 | editions [1949, 1950, 1951, 1953, 1954]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | L. M. F. Parris | Marketing Officer | Agriculture | — | — |
| 1950 | L. M. F. Parris | Marketing Officer | Agriculture | — | — |
| 1951 | L. M. F. Parris | Marketing Officer | Agriculture | — | — |
| 1953 | L. M. F. Parris | Marketing Officer | Civil Establishment | — | — |
| 1954 | L. M. F. Parris | Marketing Officer | Civil Establishment | — | — |

### Deterministic checks: `parris_l-m-f_b1900` vs `Parris, L. M. F___Leeward Islands___1949`

- [PASS] surname_gate: bio 'PARRIS' vs stint 'Parris, L. M. F' (exact)
- [PASS] initials: bio ['L', 'M', 'F'] ~ stint ['L', 'M', 'F']
- [PASS] age_gate: stint starts 1949, birth 1900 (age 49)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1954
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

