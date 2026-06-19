<!-- {"case_id": "case_dansey_g-f_e1871", "bio_ids": ["dansey_g-f_e1871"], "stint_ids": ["Dansey, G. F___New South Wales___1894"]} -->
# Dossier case_dansey_g-f_e1871

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `dansey_g-f_e1871`

- Printed name: **DANSEY, G. F**
- Birth year: not printed
- Appears in editions: [1886, 1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1886-L32935.v` — printed in editions [1886, 1888, 1889, 1890]:**

> DANSEY, G. F.—Principal medical officer, New South Wales, 23rd June, 1871.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1871 | Principal medical officer | New South Wales | [1886, 1888, 1889, 1890] |

## Candidate stint `Dansey, G. F___New South Wales___1894`

- Staff-list name: **Dansey, G. F** | colony: **New South Wales** | listed 1894–1896 | editions [1894, 1896]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | G. F. Dansey | Commanding Surgeon-Major | Medical Staff Corps | — | — |
| 1896 | G. F. Dansey | Commanding Surgeon-Major | Medical Staff Corps | — | — |

### Deterministic checks: `dansey_g-f_e1871` vs `Dansey, G. F___New South Wales___1894`

- [PASS] surname_gate: bio 'DANSEY' vs stint 'Dansey, G. F' (exact)
- [PASS] initials: bio ['G', 'F'] ~ stint ['G', 'F']
- [PASS] age_gate: stint starts 1894; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'New South Wales'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1894-1896
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

