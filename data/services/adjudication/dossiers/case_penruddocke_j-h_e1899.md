<!-- {"case_id": "case_penruddocke_j-h_e1899", "bio_ids": ["penruddocke_j-h_e1899", "pernuddocke_j-h_e1899"], "stint_ids": ["Penruddocke, J. H___Kenya___1909"]} -->
# Dossier case_penruddocke_j-h_e1899

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Penruddocke, J. H___Kenya___1909'] have more than one claimant biography in this case.

## Biography `penruddocke_j-h_e1899`

- Printed name: **PENRUDDOCKE, J. H**
- Birth year: not printed
- Appears in editions: [1910, 1912, 1913, 1914, 1915]

### Verbatim printed entry text (OCR)

**Version `col1910-L48043.v` — printed in editions [1910, 1912, 1913, 1914, 1915]:**

> PENRUDDOCKE, J. H.—Asst. loco., supt., Uganda rlyw., July, 1899.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1899 | Asst. loco., supt., Uganda rlyw | Uganda | [1910, 1912, 1913, 1914, 1915] |

## Biography `pernuddocke_j-h_e1899`

- Printed name: **PERNUDDOCKE, J. H**
- Birth year: not printed
- Appears in editions: [1911]

### Verbatim printed entry text (OCR)

**Version `col1911-L47253.v` — printed in editions [1911]:**

> PERNUDDOCKE, J. H.—Asst. loco., Uganda rlyw., July, 1899.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1899 | Asst. loco., Uganda rlyw | Uganda | [1911] |

## Candidate stint `Penruddocke, J. H___Kenya___1909`

- Staff-list name: **Penruddocke, J. H** | colony: **Kenya** | listed 1909–1911 | editions [1909, 1910, 1911]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1909 | J. H. Penruddocke | Locomotive, Carriage and Wagon Department | Railway | — | — |
| 1910 | J. H. Penruddocke | Locomotive, Carriage and Wagon Department | Locomotive, Carriage and Wagon Department | — | — |
| 1911 | J. H. Penruddocke | Locomotive, Carriage and Wagon Department | Accounts | — | — |

### Deterministic checks: `penruddocke_j-h_e1899` vs `Penruddocke, J. H___Kenya___1909`

- [PASS] surname_gate: bio 'PENRUDDOCKE' vs stint 'Penruddocke, J. H' (exact)
- [PASS] initials: bio ['J', 'H'] ~ stint ['J', 'H']
- [PASS] age_gate: stint starts 1909; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1909-1911
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `pernuddocke_j-h_e1899` vs `Penruddocke, J. H___Kenya___1909`

- [PASS] surname_gate: bio 'PERNUDDOCKE' vs stint 'Penruddocke, J. H' (fuzzy:2)
- [PASS] initials: bio ['J', 'H'] ~ stint ['J', 'H']
- [PASS] age_gate: stint starts 1909; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1909-1911
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

