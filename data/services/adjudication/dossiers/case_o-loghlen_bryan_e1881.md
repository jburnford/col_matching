<!-- {"case_id": "case_o-loghlen_bryan_e1881", "bio_ids": ["o-loghlen_bryan_e1881"], "stint_ids": ["O'Loughlen, B___Victoria___1879"]} -->
# Dossier case_o-loghlen_bryan_e1881

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['o-loghlen_bryan_e1881'] carry a single initial only — the namesake trap applies.
- NOTE: stint `O'Loughlen, B___Victoria___1879` is also gate-compatible with biography(ies) outside this case: ['o-loghlen_bryan_e1881-2'] (already linked elsewhere or filtered).

## Biography `o-loghlen_bryan_e1881`

- Printed name: **O'LOGHLEN, BRYAN**
- Birth year: not printed
- Terminal: retired 1883 — “retired, 1883.”
- Appears in editions: [1883, 1886, 1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1883-L28929.v` — printed in editions [1883, 1886, 1888, 1889, 1890]:**

> O'LOGHLEN, SIR BRYAN, BART.—Attorney-general, treasurer and premier of Victoria, Australia, 9th July, 1881; retired, 1883.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1881 | Attorney-general, treasurer and premier of Victoria | Australia | [1883, 1886, 1888, 1889, 1890] |

## Candidate stint `O'Loughlen, B___Victoria___1879`

- Staff-list name: **O'Loughlen, B** | colony: **Victoria** | listed 1879–1880 | editions [1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1879 | Sir B. O'Loughlen | Attorney-General | Crown Law Offices | — | — |
| 1880 | B. O'Loughlen | Attorney-General | Crown Law Offices | — | — |

### Deterministic checks: `o-loghlen_bryan_e1881` vs `O'Loughlen, B___Victoria___1879`

- [PASS] surname_gate: bio 'O'LOGHLEN' vs stint 'O'Loughlen, B' (fuzzy:1)
- [PASS] initials: bio ['B'] ~ stint ['B']
- [PASS] age_gate: stint starts 1879; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Victoria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1879-1880
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

