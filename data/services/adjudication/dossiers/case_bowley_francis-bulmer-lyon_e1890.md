<!-- {"case_id": "case_bowley_francis-bulmer-lyon_e1890", "bio_ids": ["bowley_francis-bulmer-lyon_e1890"], "stint_ids": ["Bowley, F. B. L___Hong Kong___1905"]} -->
# Dossier case_bowley_francis-bulmer-lyon_e1890

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bowley_francis-bulmer-lyon_e1890`

- Printed name: **BOWLEY, FRANCIS BULMER LYON**
- Birth year: not printed
- Appears in editions: [1906, 1907, 1908, 1909, 1910, 1911, 1912]

### Verbatim printed entry text (OCR)

**Version `col1906-L44380.v` — printed in editions [1906, 1907, 1908, 1909, 1910, 1911, 1912]:**

> BOWLEY, FRANCIS BULMER LYON—Sollr. of sup. ct., England, 1890; sollr. of sup. ct., Hong Kong, 1893; notary public, 1895; sec., librn. and curator of City Hall, 1899; ag. Crown sollr., May, 1899; Crown sollr. and Queen's Proctor, 1900.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1890 | Sollr. of sup. ct., England | — | [1906, 1907, 1908, 1909, 1910, 1911, 1912] |
| 1 | 1893 | sollr. of sup. ct. | Hong Kong | [1906, 1907, 1908, 1909, 1910, 1911, 1912] |
| 2 | 1895 | notary public | Hong Kong *(inherited from previous clause)* | [1906, 1907, 1908, 1909, 1910, 1911, 1912] |
| 3 | 1899 | sec., librn. and curator of City Hall | Hong Kong *(inherited from previous clause)* | [1906, 1907, 1908, 1909, 1910, 1911, 1912] |
| 4 | 1900 | Crown sollr. and Queen's Proctor | Hong Kong *(inherited from previous clause)* | [1906, 1907, 1908, 1909, 1910, 1911, 1912] |

## Candidate stint `Bowley, F. B. L___Hong Kong___1905`

- Staff-list name: **Bowley, F. B. L** | colony: **Hong Kong** | listed 1905–1910 | editions [1905, 1906, 1907, 1908, 1909, 1910]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1905 | F. Bowley | Crown Solicitor | Law Officers | — | — |
| 1906 | F. B. L. Bowley | Crown Solicitor | Law Officers | — | — |
| 1907 | F. B. L. Bowley | Crown Solicitor | Law Officers | — | — |
| 1908 | F. B. L. Bowley | Crown Solicitor | Law Officers | — | — |
| 1909 | F. B. L. Bowley | Crown Solicitor | Law Officers. | — | — |
| 1910 | F. B. L. Bowley | Crown Solicitor | Law Officers | — | — |

### Deterministic checks: `bowley_francis-bulmer-lyon_e1890` vs `Bowley, F. B. L___Hong Kong___1905`

- [PASS] surname_gate: bio 'BOWLEY' vs stint 'Bowley, F. B. L' (exact)
- [PASS] initials: bio ['F', 'B', 'L'] ~ stint ['F', 'B', 'L']
- [PASS] age_gate: stint starts 1905; no printed birth year — UNCHECKED
- [PASS] colony: 4 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1905-1910
- [FAIL] position_sim: best 50 vs bar 60: 'Crown sollr. and Queen's Proctor' ~ 'Crown Solicitor'
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

