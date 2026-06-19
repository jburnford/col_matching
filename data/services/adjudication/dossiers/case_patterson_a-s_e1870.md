<!-- {"case_id": "case_patterson_a-s_e1870", "bio_ids": ["patterson_a-s_e1870"], "stint_ids": ["Patterson, Andrew___Gibraltar___1886"]} -->
# Dossier case_patterson_a-s_e1870

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 41 official(s) with this surname in the graph's staff lists; 23 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Patterson, Andrew___Gibraltar___1886` is also gate-compatible with biography(ies) outside this case: ['patterson_andrew_e1851'] (already linked elsewhere or filtered).

## Biography `patterson_a-s_e1870`

- Printed name: **PATTERSON, A. S**
- Birth year: not printed
- Appears in editions: [1896]

### Verbatim printed entry text (OCR)

**Version `col1896-L40735.v` — printed in editions [1896]:**

> PATTERSON, A. S., M.D.—Colonial surgeon, South Australia, 1 Jan., 1870.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1870 | Colonial surgeon | South Australia | [1896] |

## Candidate stint `Patterson, Andrew___Gibraltar___1886`

- Staff-list name: **Patterson, Andrew** | colony: **Gibraltar** | listed 1886–1890 | editions [1886, 1888, 1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1886 | Andrew Patterson | Assistant Colonial Auditor | Port Office | — | — |
| 1888 | Andrew Patterson | Colonial Auditor | Audit | — | — |
| 1889 | Andrew Patterson | Colonial Auditor | Audit | — | — |
| 1890 | Andrew Patterson | Colonial Auditor | Audit | — | — |

### Deterministic checks: `patterson_a-s_e1870` vs `Patterson, Andrew___Gibraltar___1886`

- [PASS] surname_gate: bio 'PATTERSON' vs stint 'Patterson, Andrew' (exact)
- [PASS] initials: bio ['A', 'S'] ~ stint ['A']
- [PASS] age_gate: stint starts 1886; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Gibraltar'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1886-1890
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

