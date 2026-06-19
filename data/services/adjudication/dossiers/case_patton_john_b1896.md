<!-- {"case_id": "case_patton_john_b1896", "bio_ids": ["patton_john_b1896"], "stint_ids": ["Patton, M. J___Canada___1912"]} -->
# Dossier case_patton_john_b1896

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['patton_john_b1896'] carry a single initial only — the namesake trap applies.

## Biography `patton_john_b1896`

- Printed name: **PATTON, JOHN**
- Birth year: 1896 (attested in editions [1939, 1940])
- Honours: D.P.H, M.B
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L69659.v` — printed in editions [1939, 1940]:**

> PATTON, JOHN, M.B., Ch.B., B.A.O. (Belf.), D.P.H.—B. 1896; temp. med. offr., Basutoland, 1936; med. offr., 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1936 | temp. med. offr. | Basutoland | [1939, 1940] |
| 1 | 1937 | med. offr | Basutoland *(inherited from previous clause)* | [1939, 1940] |

## Candidate stint `Patton, M. J___Canada___1912`

- Staff-list name: **Patton, M. J** | colony: **Canada** | listed 1912–1913 | editions [1912, 1913]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1912 | M. J. Patton | Assistant Secretary and Editor | Conservation Commission | — | — |
| 1913 | M. J. Patton | Assistant Secretary and Editor | Conservation Commission | — | — |

### Deterministic checks: `patton_john_b1896` vs `Patton, M. J___Canada___1912`

- [PASS] surname_gate: bio 'PATTON' vs stint 'Patton, M. J' (exact)
- [PASS] initials: bio ['J'] ~ stint ['M', 'J']
- [PASS] age_gate: stint starts 1912, birth 1896 (age 16)
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1912-1913
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

