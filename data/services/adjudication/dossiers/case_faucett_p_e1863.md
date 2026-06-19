<!-- {"case_id": "case_faucett_p_e1863", "bio_ids": ["faucett_p_e1863"], "stint_ids": ["Faucett, Peter___New South Wales___1877"]} -->
# Dossier case_faucett_p_e1863

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['faucett_p_e1863'] carry a single initial only — the namesake trap applies.

## Biography `faucett_p_e1863`

- Printed name: **FAUCETT, P.**
- Birth year: not printed
- Terminal: retired 1889 — “retd., 1889.”
- Appears in editions: [1886, 1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1886-L33321.v` — printed in editions [1886, 1888, 1889]:**

> FAUCETT, P.—Solicitor-general New South Wales, 16th Oct., 1863, to 2nd Feb., 1865; puisne judge, 4th Oct., 1876.

**Version `col1890-L33910.v` — printed in editions [1890]:**

> FAUCETT, P.—Solicitor-general New South Wales, 1863 to 1865; puisne judge, 1876; retd., 1889.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1863–1865 | Solicitor-general | New South Wales | [1886, 1888, 1889, 1890] |
| 1 | 1876 | puisne judge | — | [1886, 1888, 1889, 1890] |

## Candidate stint `Faucett, Peter___New South Wales___1877`

- Staff-list name: **Faucett, Peter** | colony: **New South Wales** | listed 1877–1888 | editions [1877, 1878, 1879, 1880, 1886, 1888]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | Peter Faucett | Puisne Judges | Judicial and Legal Departments | — | — |
| 1878 | Peter Faucett | Second puisne Judge | Judicial and Legal Departments | — | — |
| 1879 | Peter Faucett | Second Puisne Judge | Judicial and Legal Departments | — | — |
| 1880 | Peter Faucett | Second Puisne Judge | Judicial and Legal Departments | — | — |
| 1886 | Peter Faucett | 1st Private Judge | Judicial and Legal Departments | — | — |
| 1888 | Peter Faucett | 1st Puisne Judge | Judicial and Legal Departments | — | — |

### Deterministic checks: `faucett_p_e1863` vs `Faucett, Peter___New South Wales___1877`

- [PASS] surname_gate: bio 'FAUCETT' vs stint 'Faucett, Peter' (exact)
- [PASS] initials: bio ['P'] ~ stint ['P']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'New South Wales'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1888
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

