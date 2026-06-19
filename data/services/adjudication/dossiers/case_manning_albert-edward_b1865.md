<!-- {"case_id": "case_manning_albert-edward_b1865", "bio_ids": ["manning_albert-edward_b1865"], "stint_ids": ["Manning, A. E___British Guiana___1894"]} -->
# Dossier case_manning_albert-edward_b1865

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 39 official(s) with this surname in the graph's staff lists; 11 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `manning_albert-edward_b1865`

- Printed name: **MANNING, ALBERT EDWARD**
- Birth year: 1865 (attested in editions [1905, 1906, 1907, 1908, 1909, 1910, 1911])
- Appears in editions: [1905, 1906, 1907, 1908, 1909, 1910, 1911]

### Verbatim printed entry text (OCR)

**Version `col1905-L44722.v` — printed in editions [1905, 1906, 1907, 1908, 1909, 1910, 1911]:**

> MANNING, ALBERT EDWARD.—B. 1865; Copyist in registrar's office, Br. Guiana, 1882; asst. sworn clk., 1887; sworn clk. and notary public, 1898; comntr. to administer oaths to affidavits, 1900.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1882 | Copyist in registrar's office | British Guiana | [1905, 1906, 1907, 1908, 1909, 1910, 1911] |
| 1 | 1887 | asst. sworn clk | British Guiana *(inherited from previous clause)* | [1905, 1906, 1907, 1908, 1909, 1910, 1911] |
| 2 | 1898 | sworn clk. and notary public | British Guiana *(inherited from previous clause)* | [1905, 1906, 1907, 1908, 1909, 1910, 1911] |
| 3 | 1900 | comntr. to administer oaths to affidavits | British Guiana *(inherited from previous clause)* | [1905, 1906, 1907, 1908, 1909, 1910, 1911] |

## Candidate stint `Manning, A. E___British Guiana___1894`

- Staff-list name: **Manning, A. E** | colony: **British Guiana** | listed 1894–1911 | editions [1894, 1896, 1897, 1898, 1899, 1900, 1905, 1906, 1908, 1909, 1910, 1911]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1894 | A. E. Manning | Assistant Sworn Clerk | Judicial Establishment | — | — |
| 1896 | A. E. Manning | Assistant Sworn Clerks | Judicial Establishment | — | — |
| 1897 | A. E. Manning | Assistant Sworn Clerks | Judicial Establishment | — | — |
| 1898 | A. E. Manning | Assistant Serjeant Clerk | Judicial Establishment | — | — |
| 1899 | A. E. Manning | Sworn Clerks and Notaries Public | Judicial Establishment | — | — |
| 1900 | A. E. Manning | Sworn Clerks and Notaries Public | Judicial Establishment | — | — |
| 1905 | A. E. Manning | Sworn Clerks and Notaries Public | Judicial Establishment | — | — |
| 1906 | A. E. Manning | Sworn Clerks and Notaries Public | Judicial Establishment | — | — |
| 1908 | A. E. Manning | Sworn Clerk and Notary Public | Judicial Establishment | — | — |
| 1909 | A. E. Manning | Sworn Clerk and Notary Public | Judicial Establishment | — | — |
| 1910 | A. E. Manning | Sworn Clerks and Notaries Public | Judicial Establishment | — | — |
| 1911 | A. E. Manning | 1st Class Clerks and Sworn Clerks and Notaries Public | Judicial Establishment | — | — |

### Deterministic checks: `manning_albert-edward_b1865` vs `Manning, A. E___British Guiana___1894`

- [PASS] surname_gate: bio 'MANNING' vs stint 'Manning, A. E' (exact)
- [PASS] initials: bio ['A', 'E'] ~ stint ['A', 'E']
- [PASS] age_gate: stint starts 1894, birth 1865 (age 29)
- [PASS] colony: 4 placed event(s) resolve to 'British Guiana'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1894-1911
- [PASS] position_sim: best 96 vs bar 60: 'sworn clk. and notary public' ~ 'Sworn Clerk and Notary Public'
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

