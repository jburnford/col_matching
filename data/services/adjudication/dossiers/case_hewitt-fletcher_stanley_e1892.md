<!-- {"case_id": "case_hewitt-fletcher_stanley_e1892", "bio_ids": ["hewitt-fletcher_stanley_e1892"], "stint_ids": ["Hewitt-Fletcher, S___Nyasaland___1910"]} -->
# Dossier case_hewitt-fletcher_stanley_e1892

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['hewitt-fletcher_stanley_e1892'] carry a single initial only — the namesake trap applies.

## Biography `hewitt-fletcher_stanley_e1892`

- Printed name: **HEWITT-FLETCHER, STANLEY**
- Birth year: not printed
- Appears in editions: [1905]

### Verbatim printed entry text (OCR)

**Version `col1905-L43767.v` — printed in editions [1905]:**

> HEWITT-FLETCHER, STANLEY.—Passed exams. and admitted mem. of Institute of Chartered Actuaries, England and Wales, June, 1892; 2nd acctnt., B.C.A. prot., 1st June, 1893; ag. ch. acctnt., 12th Aug., 1894 to 31st Mar., 1896, 11th May, 1887 to 4th Jan., 1898, and 6th Sept., 1899 to 26th Mar., 1900; collr. and mag., Zomba, Apl., 1900; ag. British agent and vice-consul, Chinde, July, 1900 to 31st Dec., 1900; apptd. to that post, 1st Jan., 1901; ag. vice-consul, Quillimane, Apl., 1902 to 31st Dec., 1903; British agent and vice-consul, Chinde, 1904; has recd. the B.C.A. medal and clasp, 1894-8.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1892–1892 | mem. of Institute of Chartered Actuaries | — | [1905] |
| 1 | 1893–1893 | 2nd acctnt. | British Central Africa Protectorate | [1905] |
| 2 | 1894–1900 | ag. ch. acctnt. | — | [1905] |
| 3 | 1900–1900 | collr. and mag. | Zomba | [1905] |
| 4 | 1900–1900 | ag. British agent and vice-consul | Chinde | [1905] |
| 5 | 1901–1901 | — | — | [1905] |
| 6 | 1902–1903 | ag. vice-consul | Quillimane | [1905] |
| 7 | 1904–1904 | British agent and vice-consul | Chinde | [1905] |

## Candidate stint `Hewitt-Fletcher, S___Nyasaland___1910`

- Staff-list name: **Hewitt-Fletcher, S** | colony: **Nyasaland** | listed 1910–1918 | editions [1910, 1911, 1912, 1913, 1914, 1915, 1917, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1910 | S. Hewitt-Fletcher | Consul and Agent, Chinde | Residents | — | — |
| 1911 | S. Hewitt-Fletcher | Consul and Agent | H.M. Consul and Agent, Chinde | — | — |
| 1912 | S. Hewitt-Fletcher | H.B.M. Consul and Agent | — | — | — |
| 1913 | S. Hewitt-Fletcher | H.B.M. Consul and Agent | Residents | — | — |
| 1914 | S. Hewitt-Fletcher | H.B.M. Consul and Agent | Residents | — | — |
| 1915 | S. Hewitt-Fletcher | H.B.M. Consul and Agent | District Residents | — | — |
| 1917 | S. Hewitt-Fletcher | H.E.M. Consul and Agent, Chinde | District Residents | — | — |
| 1918 | S. Hewitt-Fletcher | H.B.M. Consul and Agent | District Residents | — | — |

### Deterministic checks: `hewitt-fletcher_stanley_e1892` vs `Hewitt-Fletcher, S___Nyasaland___1910`

- [PASS] surname_gate: bio 'HEWITT-FLETCHER' vs stint 'Hewitt-Fletcher, S' (exact)
- [PASS] initials: bio ['S'] ~ stint ['S']
- [PASS] age_gate: stint starts 1910; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Nyasaland'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1910-1918
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

