<!-- {"case_id": "case_broome_stephen-bernard_e1877", "bio_ids": ["broome_stephen-bernard_e1877"], "stint_ids": ["Broome, S. B___Leeward Islands___1878"]} -->
# Dossier case_broome_stephen-bernard_e1877

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `broome_stephen-bernard_e1877`

- Printed name: **BROOME, STEPHEN BERNARD**
- Birth year: not printed
- Appears in editions: [1883, 1886]

### Verbatim printed entry text (OCR)

**Version `col1883-L26591.v` — printed in editions [1883, 1886]:**

> BROOME, STEPHEN BERNARD.—Medical officer, Antigua, 1877.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1877 | Medical officer | Antigua | [1883, 1886] |

## Candidate stint `Broome, S. B___Leeward Islands___1878`

- Staff-list name: **Broome, S. B** | colony: **Leeward Islands** | listed 1878–1886 | editions [1878, 1879, 1880, 1883, 1886]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1878 | S. B. Broome | — | Medical | — | — |
| 1879 | S. B. Broome | — | Medical | — | — |
| 1879 | S. B. Broome | Health Officer | Civil Establishment | — | — |
| 1880 | S. B. Broome | Health Officer | Civil Establishment | — | — |
| 1880 | S. B. Broome | — | Medical | — | — |
| 1883 | S. B. Broome | Health Officer | Civil Establishment | — | — |
| 1883 | S. B. Broome | — | Medical | — | — |
| 1886 | S. B. Broome | Medical, District No. 1 and Public Institutions | Medical | — | — |
| 1886 | S. B. Broome | Health Officer | Civil Establishment | — | — |

### Deterministic checks: `broome_stephen-bernard_e1877` vs `Broome, S. B___Leeward Islands___1878`

- [PASS] surname_gate: bio 'BROOME' vs stint 'Broome, S. B' (exact)
- [PASS] initials: bio ['S', 'B'] ~ stint ['S', 'B']
- [PASS] age_gate: stint starts 1878; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1878-1886
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

