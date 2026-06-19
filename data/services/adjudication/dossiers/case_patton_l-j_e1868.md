<!-- {"case_id": "case_patton_l-j_e1868", "bio_ids": ["patton_l-j_e1868"], "stint_ids": ["Patton, John___Canada___1896"]} -->
# Dossier case_patton_l-j_e1868

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `patton_l-j_e1868`

- Printed name: **PATTON, L. J**
- Birth year: not printed
- Appears in editions: [1889]

### Verbatim printed entry text (OCR)

**Version `col1889-L35034.v` — printed in editions [1889]:**

> PATTON, L. J.—Chief clerk to auditor general, Barbados, 1868; has acted on several occasions as auditor; government auditor, Barbados railway, May, 1883.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1868 | Chief clerk to auditor general | Barbados | [1889] |
| 1 | 1883 | government auditor, Barbados railway | Barbados | [1889] |

## Candidate stint `Patton, John___Canada___1896`

- Staff-list name: **Patton, John** | colony: **Canada** | listed 1896–1898 | editions [1896, 1898]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1896 | John Patton | Consul | — | — | — |
| 1898 | John Patton | Consul | Vice and Deputy Consul, St. John, N.B., L. M. Jewett | — | — |

### Deterministic checks: `patton_l-j_e1868` vs `Patton, John___Canada___1896`

- [PASS] surname_gate: bio 'PATTON' vs stint 'Patton, John' (exact)
- [PASS] initials: bio ['L', 'J'] ~ stint ['J']
- [PASS] age_gate: stint starts 1896; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1896-1898
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

