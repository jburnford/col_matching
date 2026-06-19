<!-- {"case_id": "case_brazao_alfred-casimiro_b1905", "bio_ids": ["brazao_alfred-casimiro_b1905"], "stint_ids": ["Brazao, A. C___British Guiana___1949"]} -->
# Dossier case_brazao_alfred-casimiro_b1905

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Brazao, A. C___British Guiana___1949` is also gate-compatible with biography(ies) outside this case: ['brazaq_alfred-casimir_b1905'] (already linked elsewhere or filtered).

## Biography `brazao_alfred-casimiro_b1905`

- Printed name: **BRAZAO, Alfred Casimiro**
- Birth year: 1905 (attested in editions [1939, 1940])
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L65070.v` — printed in editions [1939, 1940]:**

> BRAZAO, Alfred Casimiro.—B. 1905; called to bar, 1930; crown proscr., B. Guiana, 1934, 1935, 1936; ag. stip. mag., 1934, 1935, 1936; stip. mag., Nov., 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1930–1930 | called to bar | — | [1939, 1940] |
| 1 | 1934–1936 | crown proscr. | British Guiana | [1939, 1940] |
| 2 | 1934–1936 | ag. stip. mag. | — | [1939, 1940] |
| 3 | 1937 | stip. mag. | — | [1939, 1940] |

## Candidate stint `Brazao, A. C___British Guiana___1949`

- Staff-list name: **Brazao, A. C** | colony: **British Guiana** | listed 1949–1953 | editions [1949, 1950, 1953]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | A. C. Brazao | Legal Draftsman | LEGAL | — | — |
| 1950 | A. C. Brazao | Solicitor-General | LEGAL | — | — |
| 1953 | A. C. Brazao | Solicitor-General | Civil Establishment | — | — |

### Deterministic checks: `brazao_alfred-casimiro_b1905` vs `Brazao, A. C___British Guiana___1949`

- [PASS] surname_gate: bio 'BRAZAO' vs stint 'Brazao, A. C' (exact)
- [PASS] initials: bio ['A', 'C'] ~ stint ['A', 'C']
- [PASS] age_gate: stint starts 1949, birth 1905 (age 44)
- [PASS] colony: 1 placed event(s) resolve to 'British Guiana'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1953
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

