<!-- {"case_id": "case_madar_a-r_e1867-2", "bio_ids": ["madar_a-r_e1867-2"], "stint_ids": ["Madar, A. R___Hong Kong___1877"]} -->
# Dossier case_madar_a-r_e1867-2

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Madar, A. R___Hong Kong___1877` is also gate-compatible with biography(ies) outside this case: ['madar_a-r_e1867'] (already linked elsewhere or filtered).

## Biography `madar_a-r_e1867-2`

- Printed name: **MADAR, A. R**
- Birth year: not printed
- Appears in editions: [1886, 1888]

### Verbatim printed entry text (OCR)

**Version `col1886-L34680.v` — printed in editions [1886, 1888]:**

> MADAR, A. R.—Clerk in the treasury, Hong Kong, 1867; 3rd clerk, 1 Jan., 1868.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1867 | Clerk in the treasury | Hong Kong | [1886, 1888] |
| 1 | 1868 | 3rd clerk | Hong Kong *(inherited from previous clause)* | [1886, 1888] |

## Candidate stint `Madar, A. R___Hong Kong___1877`

- Staff-list name: **Madar, A. R** | colony: **Hong Kong** | listed 1877–1897 | editions [1877, 1878, 1880, 1883, 1886, 1889, 1890, 1894, 1896, 1897]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | A. Madar | 3rd Clerk | Treasurer's Department | — | — |
| 1878 | A. Madar | 3rd Clerk | Treasurer's Department | — | — |
| 1880 | A. Madar | 3rd Clerk | Treasurer's Department | — | — |
| 1883 | A. Madar | 3rd Clerk | Treasurer's Department | — | — |
| 1886 | A. Madar | 3rd Clerk and Cashier | Treasurer's Department | — | — |
| 1889 | A. Madar | 3rd Clerk and Accountant | Treasurer's Department | — | — |
| 1890 | A. Madar | Clerk and Cashier | Treasurer's Department | — | — |
| 1894 | A. R. Madar | 2nd Clerk | Registrar-General's Department | — | — |
| 1896 | A. R. Madar | 2nd Clerk | Registrar-General's Department | — | — |
| 1897 | A. R. Madar | 2nd Clerk | Registrar-General's Department | — | — |

### Deterministic checks: `madar_a-r_e1867-2` vs `Madar, A. R___Hong Kong___1877`

- [PASS] surname_gate: bio 'MADAR' vs stint 'Madar, A. R' (exact)
- [PASS] initials: bio ['A', 'R'] ~ stint ['A', 'R']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1897
- [PASS] position_sim: best 100 vs bar 60: '3rd clerk' ~ '3rd Clerk'
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

