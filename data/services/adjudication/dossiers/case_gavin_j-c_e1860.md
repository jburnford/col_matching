<!-- {"case_id": "case_gavin_j-c_e1860", "bio_ids": ["gavin_j-c_e1860"], "stint_ids": ["Gavin, J. C___New Zealand___1877"]} -->
# Dossier case_gavin_j-c_e1860

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Gavin, J. C___New Zealand___1877` is also gate-compatible with biography(ies) outside this case: ['gavin_j-c_e1860-2'] (already linked elsewhere or filtered).

## Biography `gavin_j-c_e1860`

- Printed name: **GAVIN, J. C**
- Birth year: not printed
- Appears in editions: [1886, 1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1886-L33664.v` — printed in editions [1886, 1888, 1889, 1890]:**

> GAVIN, J. C.—Secretary to treasury, receiver-general and paymaster-general, New Zealand, 1st March, 1860.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1860 | Secretary to treasury, receiver-general and paymaster-general | New Zealand | [1886, 1888, 1889, 1890] |

## Candidate stint `Gavin, J. C___New Zealand___1877`

- Staff-list name: **Gavin, J. C** | colony: **New Zealand** | listed 1877–1907 | editions [1877, 1878, 1879, 1880, 1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1907]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | J. C. Gavin | Chief Clerk and Accountant | TREASURY | — | — |
| 1878 | J. C. Gavin | Chief Clerk and Accountant | Treasury | — | — |
| 1879 | J. C. Gavin | Accountant | Treasury | — | — |
| 1880 | J. C. Gavin | Secretary to Treasury, Receiver-General and Paymaster-General | Treasury | — | — |
| 1883 | J. C. Gavin | Secretary to Treasury, Receiver-General and Paymaster-General | Treasury | — | — |
| 1886 | J. C. Gavin | Secretary to Treasury, Receiver-General and Paymaster-General | Treasury | — | — |
| 1888 | J. C. Gavin | Secretary to Treasury, Receiver-General and Paymaster-General | Treasury | — | — |
| 1889 | J. C. Gavin | Secretary to Treasury, Receiver-General and Paymaster-General | Treasury | — | — |
| 1890 | J. C. Gavin | Secretary to Treasury, Receiver-General and Paymaster-General | Treasury | — | — |
| 1894 | J. C. Gavin | Assistant Controller and Auditor-General | Audit Office | — | — |
| 1896 | J. C. Gavin | Assistant Controller and Auditor-General | Audit Office | — | — |
| 1897 | J. C. Gavin | Assistant duty | Audit Office | — | — |
| 1898 | J. C. Gavin | Assistant Comptroller and Auditor-General | Audit Office | — | — |
| 1899 | J. C. Gavin | Assistant Comptroller and Auditor-General | Audit Office | — | — |
| 1900 | J. C. Gavin | Assistant Comptroller and Auditor-General | Audit Office | — | — |
| 1905 | J. C. Gavin | Assistant Comptroller and Auditor-General | Audit Office | — | — |
| 1906 | J. C. Gavin | Assistant Comptroller and Auditor-General | Audit Office | — | — |
| 1907 | J. C. Gavin | Assistant Comptroller and Auditor-General | Audit Office | — | — |

### Deterministic checks: `gavin_j-c_e1860` vs `Gavin, J. C___New Zealand___1877`

- [PASS] surname_gate: bio 'GAVIN' vs stint 'Gavin, J. C' (exact)
- [PASS] initials: bio ['J', 'C'] ~ stint ['J', 'C']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'New Zealand'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1907
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

