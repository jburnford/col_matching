<!-- {"case_id": "case_stylianakis_n_b1902", "bio_ids": ["stylianakis_n_b1902"], "stint_ids": ["Stylianakis, N___Cyprus___1934"]} -->
# Dossier case_stylianakis_n_b1902

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['stylianakis_n_b1902'] carry a single initial only — the namesake trap applies.

## Biography `stylianakis_n_b1902`

- Printed name: **STYLIANAKIS, N**
- Birth year: 1902 (attested in editions [1959, 1960])
- Honours: M.B.E
- Appears in editions: [1959, 1960]

### Verbatim printed entry text (OCR)

**Version `col1959-L28362.v` — printed in editions [1959, 1960]:**

> STYLIANAKIS, N., M.B.E.—b. 1902; ed. English Sch., Nicosia; student clk., Cyp., 1917; 3rd div. clk., col. sec.'s office, 1927; Greek interpreter, leg. co., 1927-30; asst. registr., sup. court, 1930; registr. and interpreter, dist. court, 1930; asst. sec., 1944; admin. sec., medical dept., 1946; chief registr., sup. court, 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1917 | student clk. | Cyprus | [1959, 1960] |
| 1 | 1927 | 3rd div. clk., col. sec.'s office | Cyprus *(inherited from previous clause)* | [1959, 1960] |
| 2 | 1930 | asst. registr., sup. court | Cyprus *(inherited from previous clause)* | [1959, 1960] |
| 3 | 1944 | asst. sec | Cyprus *(inherited from previous clause)* | [1959, 1960] |
| 4 | 1946 | admin. sec., medical dept | Cyprus *(inherited from previous clause)* | [1959, 1960] |
| 5 | 1947 | chief registr., sup. court | Cyprus *(inherited from previous clause)* | [1959, 1960] |

## Candidate stint `Stylianakis, N___Cyprus___1934`

- Staff-list name: **Stylianakis, N** | colony: **Cyprus** | listed 1934–1936 | editions [1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1934 | N. Stylianakis | Registrar and Interpreter | Judicial Departments | — | — |
| 1936 | N. Stylianakis | Registrar and Interpreter | Judicial Department | — | — |

### Deterministic checks: `stylianakis_n_b1902` vs `Stylianakis, N___Cyprus___1934`

- [PASS] surname_gate: bio 'STYLIANAKIS' vs stint 'Stylianakis, N' (exact)
- [PASS] initials: bio ['N'] ~ stint ['N']
- [PASS] age_gate: stint starts 1934, birth 1902 (age 32)
- [PASS] colony: 6 placed event(s) resolve to 'Cyprus'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1934-1936
- [FAIL] position_sim: best 51 vs bar 60: 'asst. registr., sup. court' ~ 'Registrar and Interpreter'
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

