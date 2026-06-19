<!-- {"case_id": "case_forster_arthur-frost_e1908", "bio_ids": ["forster_arthur-frost_e1908"], "stint_ids": ["Forster, A___New South Wales___1900"]} -->
# Dossier case_forster_arthur-frost_e1908

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 26 official(s) with this surname in the graph's staff lists; 12 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `forster_arthur-frost_e1908`

- Printed name: **FORSTER, ARTHUR FROST**
- Birth year: not printed
- Appears in editions: [1910]

### Verbatim printed entry text (OCR)

**Version `col1910-L45781.v` — printed in editions [1910]:**

> FORSTER, ARTHUR FROST, M.R.C.S. (Eng.), L.R.C.P. (Lond.)—Med. offr., Uganda Prot., 1908; transf. to Nyassaland Prot., 1909.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1908 | Med. offr. | Uganda | [1910] |
| 1 | 1909 | transf. to Nyassaland Prot | Uganda *(inherited from previous clause)* | [1910] |

## Candidate stint `Forster, A___New South Wales___1900`

- Staff-list name: **Forster, A** | colony: **New South Wales** | listed 1900–1917 | editions [1900, 1905, 1906, 1917]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1900 | A. Forster | Registrar | Board of Pharmacy | — | — |
| 1905 | A. Forster | Registrar | Board of Pharmacy. | — | — |
| 1906 | A. Forster | Registrar | Board of Pharmacy | — | — |
| 1917 | A. Forster | Registrar | Board of Pharmacy | — | — |

### Deterministic checks: `forster_arthur-frost_e1908` vs `Forster, A___New South Wales___1900`

- [PASS] surname_gate: bio 'FORSTER' vs stint 'Forster, A' (exact)
- [PASS] initials: bio ['A', 'F'] ~ stint ['A']
- [PASS] age_gate: stint starts 1900; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'New South Wales'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1900-1917
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

