<!-- {"case_id": "case_fleming_valentine_e1838", "bio_ids": ["fleming_valentine_e1838"], "stint_ids": ["Fleming, M. H. V___Cyprus___1939"]} -->
# Dossier case_fleming_valentine_e1838

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 46 official(s) with this surname in the graph's staff lists; 19 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['fleming_valentine_e1838'] carry a single initial only — the namesake trap applies.

## Biography `fleming_valentine_e1838`

- Printed name: **FLEMING, VALENTINE**
- Birth year: not printed
- Honours: K.N.T. BACHEL. (1856)
- Terminal: retired 1870 — “Retired 1870.”
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L27478.v` — printed in editions [1883]:**

> FLEMING, SIR VALENTINE, K.N.T. BACHEL. (Created 1856).—Educated at Trinity College, Dublin, where he graduated B.A. 1834, and took honours; was called to the bar at Gray's Inn, 1838; appointed commissioner of the insolvent court for Hobart Town, 1841; solicitor-general of Tasmania, 1844; attorney-general, Jan. 1848; chief justice of the supreme court there, Aug. 1854, and knighted by patent, 1866. Retired 1870.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1838–1838 | called to the bar | — | [1883] |
| 1 | 1841–1841 | commissioner of the insolvent court | Hobart Town | [1883] |
| 2 | 1844–1844 | solicitor-general | Tasmania | [1883] |
| 3 | 1848–1848 | attorney-general | — | [1883] |
| 4 | 1854–1866 | chief justice of the supreme court | — | [1883] |

## Candidate stint `Fleming, M. H. V___Cyprus___1939`

- Staff-list name: **Fleming, M. H. V** | colony: **Cyprus** | listed 1939–1949 | editions [1939, 1949]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | M. H. V. Fleming | Chief Inspector of Schools | Education Department | — | — |
| 1949 | M. H. V. Fleming | Chief Inspector of Schools | Education | — | — |

### Deterministic checks: `fleming_valentine_e1838` vs `Fleming, M. H. V___Cyprus___1939`

- [PASS] surname_gate: bio 'FLEMING' vs stint 'Fleming, M. H. V' (exact)
- [PASS] initials: bio ['V'] ~ stint ['M', 'H', 'V']
- [PASS] age_gate: stint starts 1939; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Cyprus'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1939-1949
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

