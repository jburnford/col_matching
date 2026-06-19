<!-- {"case_id": "case_lovelace_lovelace-harte_b1858", "bio_ids": ["lovelace_lovelace-harte_b1858"], "stint_ids": ["Lovelace, L. F. E. R. Hart___Trinidad and Tobago___1905"]} -->
# Dossier case_lovelace_lovelace-harte_b1858

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `lovelace_lovelace-harte_b1858`

- Printed name: **LOVELACE, Lovelace Harte**
- Birth year: 1858 (attested in editions [1912, 1913, 1914, 1915])
- Appears in editions: [1912, 1913, 1914, 1915]

### Verbatim printed entry text (OCR)

**Version `col1912-L45743.v` — printed in editions [1912, 1913, 1914, 1915]:**

> LOVELACE, Lovelace Harte.—B. 1858; clk. of the peace, Trinidad, 1876; clk. of cust., 1877; audit offr., 1878; prim. clk., sup. ct., 1887; also commr. of oaths; ag. dep. registr., 1890-7-8, 1900, 1903, 1906 and 1907; dep. registr., 12th Dec., 1910.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1876–1876 | clk. of the peace | Trinidad | [1912, 1913, 1914, 1915] |
| 1 | 1877–1877 | clk. of cust. | — | [1912, 1913, 1914, 1915] |
| 2 | 1878–1878 | audit offr. | — | [1912, 1913, 1914, 1915] |
| 3 | 1887–1887 | prim. clk., sup. ct. | — | [1912, 1913, 1914, 1915] |
| 4 | 1890–1907 | ag. dep. registr. | — | [1912, 1913, 1914, 1915] |
| 5 | 1910–1910 | dep. registr. | — | [1912, 1913, 1914, 1915] |

## Candidate stint `Lovelace, L. F. E. R. Hart___Trinidad and Tobago___1905`

- Staff-list name: **Lovelace, L. F. E. R. Hart** | colony: **Trinidad and Tobago** | listed 1905–1912 | editions [1905, 1907, 1912]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | L. F. E. R. Hart Lovelace | 2nd Clerk | Registrar of the Courts, Registrar in Bankruptcy, and Marshal | — | — |
| 1907 | L. F. E. R. Hart Lovelace | 2nd Clerk | Judicial Department | — | — |
| 1912 | L. F. E. R. Hart Lovelace | Chief Clerk and Deputy Registrar | Judicial Department | — | — |

### Deterministic checks: `lovelace_lovelace-harte_b1858` vs `Lovelace, L. F. E. R. Hart___Trinidad and Tobago___1905`

- [PASS] surname_gate: bio 'LOVELACE' vs stint 'Lovelace, L. F. E. R. Hart' (exact)
- [PASS] initials: bio ['L', 'H'] ~ stint ['L', 'F', 'E', 'R', 'H']
- [PASS] age_gate: stint starts 1905, birth 1858 (age 47)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1905-1912
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

