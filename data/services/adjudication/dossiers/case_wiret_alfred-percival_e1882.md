<!-- {"case_id": "case_wiret_alfred-percival_e1882", "bio_ids": ["wiret_alfred-percival_e1882"], "stint_ids": ["Viret, A. P___Sierra Leone___1900", "Viret, A. P___Sierra Leone___1919"]} -->
# Dossier case_wiret_alfred-percival_e1882

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Viret, A. P___Sierra Leone___1900` is also gate-compatible with biography(ies) outside this case: ['viret_alfred-percival_b1865'] (already linked elsewhere or filtered).
- NOTE: stint `Viret, A. P___Sierra Leone___1919` is also gate-compatible with biography(ies) outside this case: ['viret_alfred-percival_b1865'] (already linked elsewhere or filtered).

## Biography `wiret_alfred-percival_e1882`

- Printed name: **WIRET, Alfred Percival**
- Birth year: not printed
- Appears in editions: [1898]

### Verbatim printed entry text (OCR)

**Version `col1898-L36381.v` — printed in editions [1898]:**

> WIRET, Alfred Percival.—Revenue officer, Dominica, May, 1882; second-class medical officer, quarantine, Aug., 1884; second-class medical officer, local committee, India, and Colombo Exhibition, 1886; confidant clerk to presiding and clerk to executive council, May, 1886; government officer, quarantine, and quarantine officer, June, 1891.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1882 | Revenue officer | Dominica | [1898] |
| 1 | 1884 | second-class medical officer, quarantine | Dominica *(inherited from previous clause)* | [1898] |
| 2 | 1886 | second-class medical officer, local committee, India, and Colombo Exhibition | Dominica *(inherited from previous clause)* | [1898] |
| 3 | 1891 | government officer, quarantine, and quarantine officer | Dominica *(inherited from previous clause)* | [1898] |

## Candidate stint `Viret, A. P___Sierra Leone___1900`

- Staff-list name: **Viret, A. P** | colony: **Sierra Leone** | listed 1900–1915 | editions [1900, 1905, 1906, 1907, 1908, 1909, 1910, 1912, 1913, 1914, 1915]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1900 | A. P. Viret | Assistant Colonial Treasurer | Treasury Department | — | — |
| 1905 | A. P. Viret | Collector | Customs Department | — | — |
| 1906 | A. P. Viret | Collector | Customs Department | — | — |
| 1907 | A. P. Viret | Collector of Customs | Customs Department | — | — |
| 1908 | A. P. Viret | Collector of Customs | Customs Department | — | — |
| 1909 | A. P. Viret | Collector of Customs | Customs Department | — | — |
| 1910 | A. P. Viret | Collector of Customs | Customs Department | — | — |
| 1912 | A. P. Viret | Collector of Customs | Customs Department | — | — |
| 1913 | A. P. Viret | Comptroller of Customs | Customs Department | — | — |
| 1914 | A. P. Viret | Comptroller of Customs | Customs | — | — |
| 1915 | A. P. Viret | Comptroller of Customs | Customs Department | — | — |

### Deterministic checks: `wiret_alfred-percival_e1882` vs `Viret, A. P___Sierra Leone___1900`

- [PASS] surname_gate: bio 'WIRET' vs stint 'Viret, A. P' (fuzzy:1)
- [PASS] initials: bio ['A', 'P'] ~ stint ['A', 'P']
- [PASS] age_gate: stint starts 1900; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Sierra Leone'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1900-1915
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Viret, A. P___Sierra Leone___1919`

- Staff-list name: **Viret, A. P** | colony: **Sierra Leone** | listed 1919–1922 | editions [1919, 1920, 1921, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1919 | A. P. Viret | Comptroller of Customs | Customs Department | — | — |
| 1920 | A. P. Viret | Comptroller of Customs | Customs Department | — | — |
| 1921 | A. P. Viret | Comptroller of Customs | Customs Department | — | — |
| 1922 | A. P. Viret | Comptroller of Customs | Customs Department | — | — |

### Deterministic checks: `wiret_alfred-percival_e1882` vs `Viret, A. P___Sierra Leone___1919`

- [PASS] surname_gate: bio 'WIRET' vs stint 'Viret, A. P' (fuzzy:1)
- [PASS] initials: bio ['A', 'P'] ~ stint ['A', 'P']
- [PASS] age_gate: stint starts 1919; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Sierra Leone'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1919-1922
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

