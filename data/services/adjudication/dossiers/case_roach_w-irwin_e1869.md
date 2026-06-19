<!-- {"case_id": "case_roach_w-irwin_e1869", "bio_ids": ["roach_w-irwin_e1869"], "stint_ids": ["Roach, W. Irwin___Labuan___1878"]} -->
# Dossier case_roach_w-irwin_e1869

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 11 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `roach_w-irwin_e1869`

- Printed name: **ROACH, W. IRWIN**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L29262.v` — printed in editions [1883]:**

> ROACH, W. IRWIN.—Educated at Marlborough College; articled pupil first to Messrs. J. and J. Simpson, Grosvenor engine works, London, then to A. M. Rendel, C.E., Westminster; assistant to superintendent public works, Trinidad, October, 1869; associate instit. C.E., December, 1869; colonial engineer, Grenada, February, 1872; surveyor-general and superintendent of convicts, Labuan, March, 1875; member of legislative council, acting treasurer (in conjunction with his own office), June, 1876.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1869 | assistant to superintendent public works | Trinidad | [1883] |
| 1 | 1872 | colonial engineer | Grenada | [1883] |
| 2 | 1875 | surveyor-general and superintendent of convicts | Labuan | [1883] |
| 3 | 1876 | member of legislative council, acting treasurer (in conjunction with his own office) | Labuan *(inherited from previous clause)* | [1883] |

## Candidate stint `Roach, W. Irwin___Labuan___1878`

- Staff-list name: **Roach, W. Irwin** | colony: **Labuan** | listed 1878–1880 | editions [1878, 1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1878 | W. I. Roach | Judge of the General Court and Justice of the Peace | Civil Establishment | — | — |
| 1878 | W. Irwin Roach | Surveyor-General and Superintendent of Convicts | Civil Establishment | — | — |
| 1879 | W. Irwin Roach | Surveyor-General and Superintendent of Convicts | Civil Establishment | — | — |
| 1879 | W. I. Roach | Judge of the General Court and Justice of the Peace | Civil Establishment | — | — |
| 1880 | W. I. Roach | Judge of the General Court and Justice of the Peace | Civil Establishment | — | — |

### Deterministic checks: `roach_w-irwin_e1869` vs `Roach, W. Irwin___Labuan___1878`

- [PASS] surname_gate: bio 'ROACH' vs stint 'Roach, W. Irwin' (exact)
- [PASS] initials: bio ['W', 'I'] ~ stint ['W', 'I']
- [PASS] age_gate: stint starts 1878; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Labuan'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1878-1880
- [FAIL] position_sim: best 43 vs bar 60: 'member of legislative council, acting treasurer (in conjunction with his own office)' ~ 'Judge of the General Court and Justice of the Peace'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

