<!-- {"case_id": "case_skenn_g-j-a_e1869", "bio_ids": ["skenn_g-j-a_e1869"], "stint_ids": ["Skeen, G. J. A___Ceylon___1877"]} -->
# Dossier case_skenn_g-j-a_e1869

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Skeen, G. J. A___Ceylon___1877` is also gate-compatible with biography(ies) outside this case: ['skeen_g-j-a_e1869'] (already linked elsewhere or filtered).

## Biography `skenn_g-j-a_e1869`

- Printed name: **SKENN, G. J. A**
- Birth year: not printed
- Appears in editions: [1890]

### Verbatim printed entry text (OCR)

**Version `col1890-L36710.v` — printed in editions [1890]:**

> SKENN, G. J. A.—Extra asst. govt. printer, Ceylon, 1869; asst. govt. printer, 1872; acting govt. printer, 1875; govt. printer, 1881.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1869 | Extra asst. govt. printer | Ceylon | [1890] |
| 1 | 1872 | asst. govt. printer | Ceylon *(inherited from previous clause)* | [1890] |
| 2 | 1875 | acting govt. printer | Ceylon *(inherited from previous clause)* | [1890] |
| 3 | 1881 | govt. printer | Ceylon *(inherited from previous clause)* | [1890] |

## Candidate stint `Skeen, G. J. A___Ceylon___1877`

- Staff-list name: **Skeen, G. J. A** | colony: **Ceylon** | listed 1877–1906 | editions [1877, 1878, 1879, 1880, 1883, 1886, 1888, 1889, 1890, 1896, 1898, 1899, 1900, 1905, 1906]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | G. J. A. Skeen | Assistant Government Printer | Colonial Secretary's Office | — | — |
| 1878 | G. J. A. Skeen | Assistant Government Printer | Colonial Secretary's Office | — | — |
| 1879 | G. J. A. Skeen | Assistant Government Printer | Colonial Secretary's Office | — | — |
| 1880 | G. J. A. Skeen | Government Secretary | Colonial Secretary's Office | — | — |
| 1883 | G. J. A. Skeen | Government Printer | Colonial Secretary's Office | — | — |
| 1886 | G. J. A. Skeen | Government Printer | Colonial Secretary's Office | — | — |
| 1888 | G. J. A. Skeen | Government Printer | Civil Establishment | — | — |
| 1889 | G. J. A. Skeen | Government Printer | Civil Establishment | — | — |
| 1890 | G. J. A. Skeen | Government Printer | Civil Establishment | — | — |
| 1896 | G. J. A. Skeen | Government Printer | Civil Establishment | — | — |
| 1898 | G. J. A. Skeen | Government Printer | Civil Establishment | — | — |
| 1899 | G. J. A. Skeen | Government Printer | Civil Establishment | — | — |
| 1900 | G. J. A. Skeen | Government Printer | Civil Establishment | — | — |
| 1905 | G. J. A. Skeen | Government Printer | Civil Establishment | — | — |
| 1906 | G. J. A. Skeen | Government Printer | Civil Establishment | — | — |

### Deterministic checks: `skenn_g-j-a_e1869` vs `Skeen, G. J. A___Ceylon___1877`

- [PASS] surname_gate: bio 'SKENN' vs stint 'Skeen, G. J. A' (fuzzy:1)
- [PASS] initials: bio ['G', 'J', 'A'] ~ stint ['G', 'J', 'A']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 4 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1877-1906
- [PASS] position_sim: best 80 vs bar 60: 'govt. printer' ~ 'Government Printer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): 1 agreeing edition-year(s) [1890] pos~80 (bar: >=2)
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

