<!-- {"case_id": "case_cole_joseph-w_e1864", "bio_ids": ["cole_joseph-w_e1864"], "stint_ids": ["Cole, J. W___Sierra Leone___1878"]} -->
# Dossier case_cole_joseph-w_e1864

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 96 official(s) with this surname in the graph's staff lists; 31 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `cole_joseph-w_e1864`

- Printed name: **COLE, JOSEPH W.**
- Birth year: not printed
- Appears in editions: [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898]

### Verbatim printed entry text (OCR)

**Version `col1883-L26912.v` — printed in editions [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897]:**

> COLE, JOSEPH W.—Temporary clerk in the colonial secretary's office, Sierra Leone, Nov., 1864; was clerk to the queen's advocate from June, 1868, to July, 1869; transferred to the customs' department as second clerk and locker, in July, 1869.

**Version `col1898-L32728.v` — printed in editions [1898]:**

> COLE, JOSEPH W.—Temporary clk. in the col. sec.'s office, S. Leone, Nov., 1864; was clk. to the Queen's advoc. from June, 1868, to July, 1869; transf'd. to the customs dept. as 2nd clerk and locker in July, 1869.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1864–1864 | Temporary clerk in the colonial secretary's office | Sierra Leone | [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898] |
| 1 | 1868–1869 | clerk to the queen's advocate | — | [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898] |
| 2 | 1869–1869 | second clerk and locker | — | [1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897, 1898] |

## Candidate stint `Cole, J. W___Sierra Leone___1878`

- Staff-list name: **Cole, J. W** | colony: **Sierra Leone** | listed 1878–1899 | editions [1878, 1879, 1880, 1883, 1886, 1888, 1889, 1896, 1898, 1899]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1878 | J. Cole | Clerk to Registrar of Court of Summary Jurisdiction | Judicial Establishment | — | — |
| 1878 | J. W. Cole | 2nd Clerk and Locker | Customs Departments | — | — |
| 1879 | J. W. Cole | 2nd Clerk and Locker | Customs Department | — | — |
| 1880 | J. W. Cole | Clerk | Customs Department | — | — |
| 1883 | J. W. Cole | Clerk | In-door Officers | — | — |
| 1886 | J. W. Cole | Clerk | In-door Officers | — | — |
| 1888 | J. W. Cole | Clerk | Customs Department | — | — |
| 1889 | J. W. Cole | Clerk | Customs Department | — | — |
| 1896 | J. W. Cole | Chief Clerk | Customs Department | — | — |
| 1898 | J. W. Cole | Chief Clerk | Customs Department | — | — |
| 1899 | J. W. Cole | Chief Clerk | Customs Department | — | — |

### Deterministic checks: `cole_joseph-w_e1864` vs `Cole, J. W___Sierra Leone___1878`

- [PASS] surname_gate: bio 'COLE' vs stint 'Cole, J. W' (exact)
- [PASS] initials: bio ['J', 'W'] ~ stint ['J', 'W']
- [PASS] age_gate: stint starts 1878; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Sierra Leone'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1878-1899
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

