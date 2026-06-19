<!-- {"case_id": "case_winslow_edward-charles_e1938", "bio_ids": ["winslow_edward-charles_e1938"], "stint_ids": ["Winslow, E. C___Singapore___1949", "Winslow, E___Canada___1886"]} -->
# Dossier case_winslow_edward-charles_e1938

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `winslow_edward-charles_e1938`

- Printed name: **WINSLOW, Edward Charles**
- Birth year: not printed
- Appears in editions: [1951]

### Verbatim printed entry text (OCR)

**Version `col1951-L43966.v` — printed in editions [1951]:**

> WINSLOW, Edward Charles, L.M.S. (S'pore.); ed. King Edward VII Coll of Med., S'pore.; asst. hse. surg., S'pore., 1938; med. offr., gr. III, 1939; gr. II, 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1938 | asst. hse. surg. | Singapore | [1951] |
| 1 | 1939 | med. offr., gr. III | — | [1951] |
| 2 | 1946 | gr. II | — | [1951] |

## Candidate stint `Winslow, E. C___Singapore___1949`

- Staff-list name: **Winslow, E. C** | colony: **Singapore** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | E. C. Winslow | Medical Officer | Mental Hospital | — | — |
| 1951 | E. C. Winslow | Medical Officer | Mental Hospital | — | — |

### Deterministic checks: `winslow_edward-charles_e1938` vs `Winslow, E. C___Singapore___1949`

- [PASS] surname_gate: bio 'WINSLOW' vs stint 'Winslow, E. C' (exact)
- [PASS] initials: bio ['E', 'C'] ~ stint ['E', 'C']
- [PASS] age_gate: stint starts 1949; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Singapore'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Winslow, E___Canada___1886`

- Staff-list name: **Winslow, E** | colony: **Canada** | listed 1886–1890 | editions [1886, 1888, 1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1886 | E. Winslow | Lieutenant-Governor | Lieutenant-Governors | — | — |
| 1888 | E. Winslow | Lieutenant-Governor | — | — | — |
| 1889 | E. Winslow | Lieutenant-Governor | — | — | — |
| 1890 | E. Winslow | Lieutenant-Governor | Lieutenant-Governors | — | — |

### Deterministic checks: `winslow_edward-charles_e1938` vs `Winslow, E___Canada___1886`

- [PASS] surname_gate: bio 'WINSLOW' vs stint 'Winslow, E' (exact)
- [PASS] initials: bio ['E', 'C'] ~ stint ['E']
- [PASS] age_gate: stint starts 1886; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1886-1890
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

