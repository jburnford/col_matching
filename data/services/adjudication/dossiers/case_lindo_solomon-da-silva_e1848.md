<!-- {"case_id": "case_lindo_solomon-da-silva_e1848", "bio_ids": ["lindo_solomon-da-silva_e1848"], "stint_ids": ["Lindo, S. D___Jamaica___1877"]} -->
# Dossier case_lindo_solomon-da-silva_e1848

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Lindo, S. D___Jamaica___1877` is also gate-compatible with biography(ies) outside this case: ['lindo_s-d_e1875'] (already linked elsewhere or filtered).

## Biography `lindo_solomon-da-silva_e1848`

- Printed name: **LINDO, SOLOMON DA SILVA**
- Birth year: not printed
- Appears in editions: [1888, 1889, 1890, 1894, 1896, 1898]

### Verbatim printed entry text (OCR)

**Version `col1888-L34527.v` — printed in editions [1888, 1889, 1890, 1894, 1896, 1898]:**

> LINDO, SOLOMON DA SILVA.—Admitted attorney supreme court, Jamaica, 1848; clerk of the peace for the parish of St. Mary, 1854; resigned on pension, 1868; advocate of the supreme court, 1870, and assistant to the attorney-general, Feb., 1872.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1848 | Admitted attorney supreme court | Jamaica | [1888, 1889, 1890, 1894, 1896, 1898] |
| 1 | 1854 | clerk of the peace for the parish of St | Jamaica *(inherited from previous clause)* | [1888, 1889, 1890, 1894, 1896, 1898] |
| 2 | 1868 | resigned on pension | Jamaica *(inherited from previous clause)* | [1888, 1889, 1890, 1894, 1896, 1898] |
| 3 | 1870 | advocate of the supreme court | Jamaica *(inherited from previous clause)* | [1888, 1889, 1890, 1894, 1896, 1898] |
| 4 | 1872 | assistant to the attorney-general | Jamaica *(inherited from previous clause)* | [1888, 1889, 1890, 1894, 1896, 1898] |

## Candidate stint `Lindo, S. D___Jamaica___1877`

- Staff-list name: **Lindo, S. D** | colony: **Jamaica** | listed 1877–1897 | editions [1877, 1878, 1879, 1880, 1883, 1886, 1888, 1889, 1890, 1894, 1896, 1897]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | S. D. Lindo | Assistant to the Attorney-General | Judicial Establishment | — | — |
| 1878 | S. D. Lindo | Assistant to the Attorney-General | Judicial Establishment | — | — |
| 1879 | S. D. Lindo | Assistant to the Attorney-General | Judicial Establishment | — | — |
| 1880 | S. D. Lindo | Assistant to the Attorney-General | Judicial Establishment | — | — |
| 1883 | S. D. Lindo | Assistant to the Attorney-General | Judicial Establishment | — | — |
| 1886 | S. D. Lindo | Assistant to the Attorney-General | Judicial Establishment | — | — |
| 1888 | S. D. Lindo | Assistant to the Attorney-General | Judicial Establishment | — | — |
| 1889 | S. D. Lindo | Assistants to the Attorney-General | Judicial Establishment | — | — |
| 1890 | S. D. Lindo | Assistant to the Attorney-General | Judicial Establishment | — | — |
| 1894 | S. D. Lindo | Assistant to the Attorney-General | Judicial Establishment | — | — |
| 1896 | S. D. Lindo | Assistant to the Attorney-General | Judicial Establishment | — | — |
| 1897 | S. D. Lindo | Assistant to the Attorney-General | Judicial Establishment | — | — |

### Deterministic checks: `lindo_solomon-da-silva_e1848` vs `Lindo, S. D___Jamaica___1877`

- [PASS] surname_gate: bio 'LINDO' vs stint 'Lindo, S. D' (exact)
- [PASS] initials: bio ['S', 'D', 'S'] ~ stint ['S', 'D']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 5 placed event(s) resolve to 'Jamaica'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1897
- [PASS] position_sim: best 100 vs bar 60: 'assistant to the attorney-general' ~ 'Assistant to the Attorney-General'
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

