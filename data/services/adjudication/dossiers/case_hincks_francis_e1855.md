<!-- {"case_id": "case_hincks_francis_e1855", "bio_ids": ["hincks_francis_e1855"], "stint_ids": ["Hincks, Francis___Canada___1877"]} -->
# Dossier case_hincks_francis_e1855

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['hincks_francis_e1855'] carry a single initial only — the namesake trap applies.

## Biography `hincks_francis_e1855`

- Printed name: **HINCKS, Francis**
- Birth year: not printed
- Honours: C.B. (1862), K.C.M.G. (1869)
- Terminal: resigned 1873 — “resigned Feb., 1873.”
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L28000.v` — printed in editions [1883]:**

> HINCKS, Sir Francis, K.C.M.G. (1869), C.B. (creat. 1862) — Was for several years a prominent member of the Canadian ministry, in which he held the office of inspector-general of accounts; appointed governor-in-chief of Barbados, and the Windward Islands, Oct. 1855; and governor and commander-in-chief, British Guiana, 1861, till commencement of 1869, when he retired on a pension; finance minister for Canada Nov. 1869; resigned Feb., 1873.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1855 | governor-in-chief | Barbados | [1883] |
| 1 | 1861–1869 | governor and commander-in-chief | British Guiana | [1883] |
| 2 | 1869 | finance minister | Canada | [1883] |
| 3 | ? | inspector-general of accounts | Canada | [1883] |

## Candidate stint `Hincks, Francis___Canada___1877`

- Staff-list name: **Hincks, Francis** | colony: **Canada** | listed 1877–1883 | editions [1877, 1878, 1880, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | Sir Francis Hincks | — | Civil Establishment | K.C.M.G., C.B. | — |
| 1878 | Francis Hincks | Privy Council Member | Civil Establishment | K.C.M.G., C.B. | — |
| 1880 | Sir Francis Hincks | — | Privy Council | K.C.M.G., C.B. | — |
| 1883 | Sir Francis Hincks | — | THE QUEEN'S PRIVY COUNCIL FOR CANADA | K.C.M.G., C.B. | — |

### Deterministic checks: `hincks_francis_e1855` vs `Hincks, Francis___Canada___1877`

- [PASS] surname_gate: bio 'HINCKS' vs stint 'Hincks, Francis' (exact)
- [PASS] initials: bio ['F'] ~ stint ['F']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1883
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: C.B., K.C.M.G.
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

