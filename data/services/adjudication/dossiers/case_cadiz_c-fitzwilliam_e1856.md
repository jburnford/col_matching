<!-- {"case_id": "case_cadiz_c-fitzwilliam_e1856", "bio_ids": ["cadiz_c-fitzwilliam_e1856"], "stint_ids": ["Cadiz, C. F. C. V___Tanganyika___1956", "Cadiz, C. F___Natal___1879"]} -->
# Dossier case_cadiz_c-fitzwilliam_e1856

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Cadiz, C. F. C. V___Tanganyika___1956` is also gate-compatible with biography(ies) outside this case: ['cadiz_c-f-c-v_b1907'] (already linked elsewhere or filtered).

## Biography `cadiz_c-fitzwilliam_e1856`

- Printed name: **CADIZ, C. FITZWILLIAM**
- Birth year: not printed
- Honours: B.A.
- Appears in editions: [1883, 1886, 1888]

### Verbatim printed entry text (OCR)

**Version `col1883-L26701.v` — printed in editions [1883, 1886, 1888]:**

> CADIZ, C. FITZWILLIAM, B.A.—Of Pembroke College, Oxford, was called to the bar by the Honourable Society of Lincoln's Inn in 1856; appointed acting clerk of council, Trinidad, in 1858; member of privy council of Tobago; stipendiary magistrate in the said island, April, 1862; and coroner and visiting justice of the gaol; member of the executive committee, 1860; attorney-general, 1868; puisne judge, Natal, 1876; first puisne judge, 1879; compiled and edited an edition of the "Ordinances, Laws, and Proclamations of Natal, from 1843-78."

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1856–1856 | called to the bar | — | [1883, 1886, 1888] |
| 1 | 1858–1858 | acting clerk of council | Trinidad | [1883, 1886, 1888] |
| 2 | 1860–1860 | member of the executive committee | — | [1883, 1886, 1888] |
| 3 | 1862–1862 | stipendiary magistrate | Tobago | [1883, 1886, 1888] |
| 4 | 1868–1868 | attorney-general | — | [1883, 1886, 1888] |
| 5 | 1876–1876 | puisne judge | Natal | [1883, 1886, 1888] |
| 6 | 1879–1879 | first puisne judge | — | [1883, 1886, 1888] |

## Candidate stint `Cadiz, C. F. C. V___Tanganyika___1956`

- Staff-list name: **Cadiz, C. F. C. V** | colony: **Tanganyika** | listed 1956–1958 | editions [1956, 1957, 1958]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1956 | C. F. C. V. Cadiz | Provincial Commissioner | Civil Establishment | — | — |
| 1957 | C. F. C. V. Cadiz | Provincial Commissioners | Civil Establishment | — | — |
| 1958 | C. F. C. V. Cadiz | Provincial Commissioners | Civil Establishment | — | — |

### Deterministic checks: `cadiz_c-fitzwilliam_e1856` vs `Cadiz, C. F. C. V___Tanganyika___1956`

- [PASS] surname_gate: bio 'CADIZ' vs stint 'Cadiz, C. F. C. V' (exact)
- [PASS] initials: bio ['C', 'F'] ~ stint ['C', 'F', 'C', 'V']
- [PASS] age_gate: stint starts 1956; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Tanganyika'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1956-1958
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Cadiz, C. F___Natal___1879`

- Staff-list name: **Cadiz, C. F** | colony: **Natal** | listed 1879–1880 | editions [1879, 1880]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1879 | C. F. Cadiz | 2nd Puisne Judge | Judicial Department | — | — |
| 1880 | C. F. Cadiz | 2nd Puisne Judge | Judicial Department | — | — |

### Deterministic checks: `cadiz_c-fitzwilliam_e1856` vs `Cadiz, C. F___Natal___1879`

- [PASS] surname_gate: bio 'CADIZ' vs stint 'Cadiz, C. F' (exact)
- [PASS] initials: bio ['C', 'F'] ~ stint ['C', 'F']
- [PASS] age_gate: stint starts 1879; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Natal'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1879-1880
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

