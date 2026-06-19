<!-- {"case_id": "case_eddie_a_e1891", "bio_ids": ["eddie_a_e1891"], "stint_ids": ["Eddie, L. A___Cape of Good Hope___1908"]} -->
# Dossier case_eddie_a_e1891

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['eddie_a_e1891'] carry a single initial only — the namesake trap applies.

## Biography `eddie_a_e1891`

- Printed name: **EDDIE, A**
- Birth year: not printed
- Appears in editions: [1911]

### Verbatim printed entry text (OCR)

**Version `col1911-L44484.v` — printed in editions [1911]:**

> EDDIE, HON. A.—M.L.A., New South Wales since 1891; sec. for mines, Oct., 1910.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1891 | M.L.A., New South Wales since | New South Wales | [1911] |
| 1 | 1910 | sec. for mines | New South Wales *(inherited from previous clause)* | [1911] |

## Candidate stint `Eddie, L. A___Cape of Good Hope___1908`

- Staff-list name: **Eddie, L. A** | colony: **Cape of Good Hope** | listed 1908–1909 | editions [1908, 1909]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1908 | L. A. Eddie | Clerk to Judge President | Eastern Districts Court | — | — |
| 1909 | L. A. Eddie | Clerk to Judge President | Eastern Districts Court | — | — |

### Deterministic checks: `eddie_a_e1891` vs `Eddie, L. A___Cape of Good Hope___1908`

- [PASS] surname_gate: bio 'EDDIE' vs stint 'Eddie, L. A' (exact)
- [PASS] initials: bio ['A'] ~ stint ['L', 'A']
- [PASS] age_gate: stint starts 1908; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1908-1909
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

