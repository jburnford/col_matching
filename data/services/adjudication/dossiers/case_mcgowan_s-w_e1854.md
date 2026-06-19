<!-- {"case_id": "case_mcgowan_s-w_e1854", "bio_ids": ["mcgowan_s-w_e1854"], "stint_ids": ["McGowan, S. W___Victoria___1877"]} -->
# Dossier case_mcgowan_s-w_e1854

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mcgowan_s-w_e1854`

- Printed name: **McGOWAN, S. W**
- Birth year: not printed
- Appears in editions: [1886]

### Verbatim printed entry text (OCR)

**Version `col1886-L34621.v` — printed in editions [1886]:**

> McGOWAN, S. W.—In charge of telegraphs, Victoria, 1854; chief inspector of postal and telegraph service, 1st March, 1869; now deputy postmaster-general.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1854 | In charge of telegraphs | Victoria | [1886] |
| 1 | 1869 | chief inspector of postal and telegraph service | Victoria *(inherited from previous clause)* | [1886] |

## Candidate stint `McGowan, S. W___Victoria___1877`

- Staff-list name: **McGowan, S. W** | colony: **Victoria** | listed 1877–1883 | editions [1877, 1878, 1880, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | S. W. McGowan | Inspector of Postal and Telegraph Service | Postmaster General's Division | — | — |
| 1878 | S. W. McGowan | Inspector of Postal and Telegraph Service | Postmaster General's Division | — | — |
| 1880 | S. W. McGowan | Inspector of Postal and Telegraph Service | Postmaster General's Division | — | — |
| 1883 | S. W. McGowan | Chief Inspector of Postal and Telegraph Service | Postmaster General's Division | — | — |

### Deterministic checks: `mcgowan_s-w_e1854` vs `McGowan, S. W___Victoria___1877`

- [PASS] surname_gate: bio 'McGOWAN' vs stint 'McGowan, S. W' (exact)
- [PASS] initials: bio ['S', 'W'] ~ stint ['S', 'W']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Victoria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1883
- [PASS] position_sim: best 100 vs bar 60: 'chief inspector of postal and telegraph service' ~ 'Inspector of Postal and Telegraph Service'
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

