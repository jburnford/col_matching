<!-- {"case_id": "case_littleton_william-francis_e1882", "bio_ids": ["littleton_william-francis_e1882"], "stint_ids": ["Littleton, W. F___Cape of Good Hope___1878"]} -->
# Dossier case_littleton_william-francis_e1882

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `littleton_william-francis_e1882`

- Printed name: **LITTLETON, WILLIAM FRANCIS**
- Birth year: not printed
- Honours: C.M.G (1880)
- Terminal: retired 1884 — “retired, 1884.”
- Appears in editions: [1883, 1886, 1888, 1889]

### Verbatim printed entry text (OCR)

**Version `col1883-L28399.v` — printed in editions [1883, 1886, 1888, 1889]:**

> LITTLETON, THE HON. WILLIAM FRANCIS, C.M.G. (1880).—Private secretary to the Right Hon. Sir Bartle Frere, Bart., when governor of the Cape of Good Hope; précis writer, Mauritius, 1882; retired, 1884.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1882 | précis writer | Mauritius | [1883, 1886, 1888, 1889] |

## Candidate stint `Littleton, W. F___Cape of Good Hope___1878`

- Staff-list name: **Littleton, W. F** | colony: **Cape of Good Hope** | listed 1878–1880 | editions [1878, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1878 | Hon. W. F. Littleton | Private Secretary | Civil Establishment | — | — |
| 1879 | Hon. W. F. Littleton | Private Secretary | Civil Establishment | — | — |
| 1880 | Hon. W. F. Littleton | Private Secretary | Governor's Establishment | — | — |

### Deterministic checks: `littleton_william-francis_e1882` vs `Littleton, W. F___Cape of Good Hope___1878`

- [PASS] surname_gate: bio 'LITTLETON' vs stint 'Littleton, W. F' (exact)
- [PASS] initials: bio ['W', 'F'] ~ stint ['W', 'F']
- [PASS] age_gate: stint starts 1878; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1878-1880
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

