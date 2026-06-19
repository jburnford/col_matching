<!-- {"case_id": "case_rolleston_christopher_e1843", "bio_ids": ["rolleston_christopher_e1843"], "stint_ids": ["Rolleston, C___New South Wales___1877"]} -->
# Dossier case_rolleston_christopher_e1843

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['rolleston_christopher_e1843'] carry a single initial only — the namesake trap applies.

## Biography `rolleston_christopher_e1843`

- Printed name: **ROLLESTON, CHRISTOPHER**
- Birth year: not printed
- Honours: C.M.G. (1879)
- Terminal: retired 1883 — “retired 1883”
- Appears in editions: [1883, 1886, 1888]

### Verbatim printed entry text (OCR)

**Version `col1883-L29305.v` — printed in editions [1883, 1886, 1888]:**

> ROLLESTON, CHRISTOPHER, C.M.G. (1879).—Entered the public service in New South Wales on Jan. 1, 1843, as commissioner of crown lands for the district of Darling Downs; obtained leave of absence to visit England in Jan. 1853; returned to the colony at the end of 1854; private secretary to Sir William Thomas Denison, governor-general, in Jan. 1855; and registrar-general of the colony, Jan. 1, 1856; auditor-general, 1864; retired 1883.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1843 | commissioner of crown lands for the district of Darling Downs | New South Wales | [1883, 1886, 1888] |
| 1 | 1853 | — | England | [1883, 1886, 1888] |
| 2 | 1854 | — | — | [1883, 1886, 1888] |
| 3 | 1855 | private secretary to Sir William Thomas Denison, governor-general | — | [1883, 1886, 1888] |
| 4 | 1856 | registrar-general | — | [1883, 1886, 1888] |
| 5 | 1864 | auditor-general | — | [1883, 1886, 1888] |

## Candidate stint `Rolleston, C___New South Wales___1877`

- Staff-list name: **Rolleston, C** | colony: **New South Wales** | listed 1877–1880 | editions [1877, 1878, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | C. Rolleston | Auditor-General | Auditor-General's Department | — | — |
| 1878 | C. Rolleston | Auditor-General | Auditor-General's Department | — | — |
| 1879 | C. Rolleston | Auditor-General | Auditor-General's Department | — | — |
| 1880 | C. Rolleston | Auditor-General | Auditor-General's Department | — | — |

### Deterministic checks: `rolleston_christopher_e1843` vs `Rolleston, C___New South Wales___1877`

- [PASS] surname_gate: bio 'ROLLESTON' vs stint 'Rolleston, C' (exact)
- [PASS] initials: bio ['C'] ~ stint ['C']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'New South Wales'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1880
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

