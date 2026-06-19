<!-- {"case_id": "case_bradford_m-g_e1895", "bio_ids": ["bradford_m-g_e1895"], "stint_ids": ["Bradford, M. G___North Borneo___1905", "Bradford, M. G___Sarawak___1908"]} -->
# Dossier case_bradford_m-g_e1895

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bradford_m-g_e1895`

- Printed name: **BRADFORD, M. G**
- Birth year: not printed
- Appears in editions: [1905, 1906, 1907, 1908, 1909, 1910]

### Verbatim printed entry text (OCR)

**Version `col1905-L42174.v` — printed in editions [1905, 1906, 1907, 1908, 1910]:**

> BRADFORD, M. G.—Asst., P.W.D., Sarawak, May, 1895; supt., July, 1901; ag. comntr., May, 1902.

**Version `col1909-L44063.v` — printed in editions [1909]:**

> BRADFORD, M. G.—ASST., P.W.D., SARAWAK, MAY, 1895; SUPT., JULY, 1901; AG. COMSR., MAY, 1902.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1895 | Asst., P.W.D. | Sarawak | [1905, 1906, 1907, 1908, 1909, 1910] |
| 1 | 1901 | supt | Sarawak *(inherited from previous clause)* | [1905, 1906, 1907, 1908, 1909, 1910] |
| 2 | 1902 | ag. comntr | Sarawak *(inherited from previous clause)* | [1905, 1906, 1907, 1908, 1910] |
| 3 | 1902 | AG. COMSR., MAY | — | [1909] |

## Candidate stint `Bradford, M. G___North Borneo___1905`

- Staff-list name: **Bradford, M. G** | colony: **North Borneo** | listed 1905–1907 | editions [1905, 1906, 1907]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | M. G. Bradford | Superintendent, P.W.D. | Civil Establishment | — | — |
| 1906 | M. G. Bradford | Superintendent, P. W.D. | Civil Establishment | — | — |
| 1907 | M. G. Bradford | Superintendent, P.W.D. | Chief Officers | — | — |

### Deterministic checks: `bradford_m-g_e1895` vs `Bradford, M. G___North Borneo___1905`

- [PASS] surname_gate: bio 'BRADFORD' vs stint 'Bradford, M. G' (exact)
- [PASS] initials: bio ['M', 'G'] ~ stint ['M', 'G']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'North Borneo'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1907
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Bradford, M. G___Sarawak___1908`

- Staff-list name: **Bradford, M. G** | colony: **Sarawak** | listed 1908–1910 | editions [1908, 1910]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1908 | M. G. Bradford | Superintendent, P.W.D. | Chief Officers | — | — |
| 1910 | M. G. Bradford | Municipal Officer | Civil Establishment | — | — |

### Deterministic checks: `bradford_m-g_e1895` vs `Bradford, M. G___Sarawak___1908`

- [PASS] surname_gate: bio 'BRADFORD' vs stint 'Bradford, M. G' (exact)
- [PASS] initials: bio ['M', 'G'] ~ stint ['M', 'G']
- [PASS] age_gate: stint starts 1908; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'Sarawak'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1908-1910
- [FAIL] position_sim: best 31 vs bar 60: 'ag. comntr' ~ 'Municipal Officer'
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

