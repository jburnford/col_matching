<!-- {"case_id": "case_lilly_r-r-w_e1858", "bio_ids": ["lilly_r-r-w_e1858"], "stint_ids": ["Lilly, R. R. W___Newfoundland___1877"]} -->
# Dossier case_lilly_r-r-w_e1858

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `lilly_r-r-w_e1858`

- Printed name: **LILLY, R. R. W**
- Birth year: not printed
- Appears in editions: [1886, 1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1886-L34501.v` — printed in editions [1886, 1888, 1889, 1890]:**

> LILLY, R. R. W.—Clerk of central district Court, Newfoundland, 1858; registrar of vice-admiralty court, 1871.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1858 | Clerk of central district Court | Newfoundland | [1886, 1888, 1889, 1890] |
| 1 | 1871 | registrar of vice-admiralty court | Newfoundland *(inherited from previous clause)* | [1886, 1888, 1889, 1890] |

## Candidate stint `Lilly, R. R. W___Newfoundland___1877`

- Staff-list name: **Lilly, R. R. W** | colony: **Newfoundland** | listed 1877–1894 | editions [1877, 1878, 1879, 1880, 1883, 1886, 1888, 1889, 1894]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | R. R. W. Lilly | Registrar of the Vice-Admiralty Court | Judicial Establishment | — | — |
| 1878 | R. R. W. Lilly | Registrar of the Vice-Admiralty Court | Judicial Establishment | — | — |
| 1878 | R. R. W. Lilly | Clerk of the Peace at St. John's | Magistrates | — | — |
| 1879 | R. R. W. Lilly | Registrar of the Vice-Admiralty Court | Judicial Establishment | — | — |
| 1880 | R. R. W. Lilly | Registrar of the Vice-Admiralty Court | Judicial Establishment | — | — |
| 1883 | R. R. W. Lilly | Registrar of the Vice-Admiralty Court | Judicial Establishment | — | — |
| 1886 | R. R. W. Lilly | Registrar of the Vice-Admiralty Court | Judicial Establishment | — | — |
| 1888 | R. R. W. Lilly | Registrar of the Vice-Admiralty Court | Judicial Establishment | — | — |
| 1889 | R. R. W. Lilly | Registrar of the Vice-Admiralty Court | Judicial Establishment | — | — |
| 1894 | R. R. W. Lilly | Clerk of the Peace at St. John's, and Clerk of Central District Court | Judicial Establishment | — | — |

### Deterministic checks: `lilly_r-r-w_e1858` vs `Lilly, R. R. W___Newfoundland___1877`

- [PASS] surname_gate: bio 'LILLY' vs stint 'Lilly, R. R. W' (exact)
- [PASS] initials: bio ['R', 'R', 'W'] ~ stint ['R', 'R', 'W']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Newfoundland'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1894
- [PASS] position_sim: best 100 vs bar 60: 'registrar of vice-admiralty court' ~ 'Registrar of the Vice-Admiralty Court'
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

