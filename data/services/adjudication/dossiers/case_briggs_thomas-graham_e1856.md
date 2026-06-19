<!-- {"case_id": "case_briggs_thomas-graham_e1856", "bio_ids": ["briggs_thomas-graham_e1856"], "stint_ids": ["Briggs, T. G___Leeward Islands___1877"]} -->
# Dossier case_briggs_thomas-graham_e1856

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 21 official(s) with this surname in the graph's staff lists; 10 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `briggs_thomas-graham_e1856`

- Printed name: **BRIGGS, THOMAS GRAHAM**
- Birth year: not printed
- Appears in editions: [1883, 1886]

### Verbatim printed entry text (OCR)

**Version `col1883-L26574.v` — printed in editions [1883, 1886]:**

> BRIGGS, SIR THOMAS GRAHAM, 1st BART. (created 1871).—Educated at Codrington College, and Trinity College, Cambridge; B.A. 1856; M.A. 1862; J.P. Nevis and Barbados; member of the executive council of the Island of Barbados; appointed member of the executive council of Nevis, 1872; is also a member of the general council of the Leeward Islands; member of the legislative assembly, Nevis, 1878; was president of the legislative council, Barbados, June, 1876.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1856 | B.A | — | [1883, 1886] |
| 1 | 1862 | M.A | — | [1883, 1886] |
| 2 | 1872 | appointed member of the executive council of Nevis | — | [1883, 1886] |
| 3 | 1876 | was president of the legislative council | Barbados | [1883, 1886] |
| 4 | 1878 | member of the legislative assembly | Nevis | [1883, 1886] |

## Candidate stint `Briggs, T. G___Leeward Islands___1877`

- Staff-list name: **Briggs, T. G** | colony: **Leeward Islands** | listed 1877–1886 | editions [1877, 1878, 1879, 1880, 1883, 1886]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | T. G. Briggs | Justice of the Peace | Justices of the Peace | — | — |
| 1878 | T. G. Briggs | Justice of the Peace | Judicial Establishment | — | — |
| 1879 | T. G. Briggs | Justice of the Peace | Justices of the Peace | — | — |
| 1880 | T. G. Briggs | Justice of the Peace | Justices of the Peace | — | — |
| 1883 | Sir T. G. Briggs, Bart. | Justice of the Peace | Justices of the Peace | — | — |
| 1886 | T. G. Briggs | Justice of the Peace | Justices of the Peace (Nevis) | — | — |

### Deterministic checks: `briggs_thomas-graham_e1856` vs `Briggs, T. G___Leeward Islands___1877`

- [PASS] surname_gate: bio 'BRIGGS' vs stint 'Briggs, T. G' (exact)
- [PASS] initials: bio ['T', 'G'] ~ stint ['T', 'G']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1877-1886
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

