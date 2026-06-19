<!-- {"case_id": "case_pentlow_w_e1860", "bio_ids": ["pentlow_w_e1860"], "stint_ids": ["Pentelow, W. C. D___Ceylon___1928"]} -->
# Dossier case_pentlow_w_e1860

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['pentlow_w_e1860'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Pentelow, W. C. D___Ceylon___1928` is also gate-compatible with biography(ies) outside this case: ['pentelow_william-cyril-doughty_b1903'] (already linked elsewhere or filtered).

## Biography `pentlow_w_e1860`

- Printed name: **PENTLOW, W.**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L29079.v` — printed in editions [1883]:**

> PENTLOW, W.—Was clerk to Crown solicitor, Western Australia, from February, 1860, to April, 1878; clerk to attorney-general and Crown solicitor, 1873.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1860–1878 | clerk to Crown solicitor | Western Australia | [1883] |
| 1 | 1873–1873 | clerk to attorney-general and Crown solicitor | — | [1883] |

## Candidate stint `Pentelow, W. C. D___Ceylon___1928`

- Staff-list name: **Pentelow, W. C. D** | colony: **Ceylon** | listed 1928–1929 | editions [1928, 1929]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1928 | W. C. D. Pentelow | Office Assistant | — | — | — |
| 1929 | W. C. D. Pentelow | Assistant Collector and Landing Surveyor | Northern Province | — | — |

### Deterministic checks: `pentlow_w_e1860` vs `Pentelow, W. C. D___Ceylon___1928`

- [PASS] surname_gate: bio 'PENTLOW' vs stint 'Pentelow, W. C. D' (fuzzy:1)
- [PASS] initials: bio ['W'] ~ stint ['W', 'C', 'D']
- [PASS] age_gate: stint starts 1928; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1928-1929
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

