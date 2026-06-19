<!-- {"case_id": "case_philip_m-m_e1854", "bio_ids": ["philip_m-m_e1854"], "stint_ids": ["Philip, M. M___Trinidad___1877"]} -->
# Dossier case_philip_m-m_e1854

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 14 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `philip_m-m_e1854`

- Printed name: **PHILIP, M. M.**
- Birth year: not printed
- Appears in editions: [1886, 1888]

### Verbatim printed entry text (OCR)

**Version `col1886-L35269.v` — printed in editions [1886]:**

> PHILIP, M. M.—Solicitor-general, Trinidad, March, 1871; acted as attorney-general, June, 1873, to July, 1874; was called to the bar by the honourable society of the Middle Temple, 1854.

**Version `col1888-L35523.v` — printed in editions [1888]:**

> PHILIP, M. M.—Called to the bar, Middle Temple, 1854; acting inspector of schools, Trinidad, 1856 and 1865; solicitor-general, Mar., 1871; has frequently acted as attorney-general.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1854 | called to the bar | — | [1886, 1888] |
| 1 | 1856–1865 | acting inspector of schools | Trinidad | [1888] |
| 2 | 1871 | Solicitor-general | Trinidad | [1886, 1888] |
| 3 | 1873–1874 | acted as attorney-general | — | [1886] |

## Candidate stint `Philip, M. M___Trinidad___1877`

- Staff-list name: **Philip, M. M** | colony: **Trinidad** | listed 1877–1888 | editions [1877, 1878, 1879, 1883, 1886, 1888]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | M. M. Philip | Solicitor-General | Judicial Department | — | — |
| 1878 | M. M. Philip | Solicitor-General | Judicial Department | — | — |
| 1879 | M. M. Philip | Solicitor-General | Judicial Department | — | — |
| 1883 | M. M. Philip | Solicitor-General | Judicial Department | — | — |
| 1886 | M. M. Philip | Solicitor-General | Judicial Department | — | — |
| 1888 | M. M. Philip | Solicitor-General | Clerks to the Attorney-General | — | — |

### Deterministic checks: `philip_m-m_e1854` vs `Philip, M. M___Trinidad___1877`

- [PASS] surname_gate: bio 'PHILIP' vs stint 'Philip, M. M' (exact)
- [PASS] initials: bio ['M', 'M'] ~ stint ['M', 'M']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 2 placed event(s) resolve to 'Trinidad'
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

