<!-- {"case_id": "case_lowesley_lionel-dewe_e1902", "bio_ids": ["lowesley_lionel-dewe_e1902", "lowsley_lionel-dewe_e1902"], "stint_ids": ["Lowsley, L. D___Kenya___1913"]} -->
# Dossier case_lowesley_lionel-dewe_e1902

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Lowsley, L. D___Kenya___1913'] have more than one claimant biography in this case.
- NOTE: stint `Lowsley, L. D___Kenya___1913` is also gate-compatible with biography(ies) outside this case: ['lowsley_lionel-dewe_e1902-2'] (already linked elsewhere or filtered).
- NOTE: stint `Lowsley, L. D___Kenya___1913` is also gate-compatible with biography(ies) outside this case: ['lowsley_lionel-dewe_e1902-2'] (already linked elsewhere or filtered).

## Biography `lowesley_lionel-dewe_e1902`

- Printed name: **LOWESLEY, LIONEL DEWE**
- Birth year: not printed
- Appears in editions: [1909, 1911]

### Verbatim printed entry text (OCR)

**Version `col1909-L47997.v` — printed in editions [1909, 1911]:**

> LOWESLEY, LIONEL DEWE.—Med. offr., Uganda Prot., 1st Mar., 1902.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1902 | Med. offr. | Uganda | [1909, 1911] |

## Biography `lowsley_lionel-dewe_e1902`

- Printed name: **LOWSLEY, LIONEL DEWE**
- Birth year: not printed
- Appears in editions: [1910]

### Verbatim printed entry text (OCR)

**Version `col1910-L47188.v` — printed in editions [1910]:**

> LOWSLEY, LIONEL DEWE.—Med. offr., Uganda Prot., 1st Mar., 1902.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1902 | Med. offr. | Uganda | [1910] |

## Candidate stint `Lowsley, L. D___Kenya___1913`

- Staff-list name: **Lowsley, L. D** | colony: **Kenya** | listed 1913–1915 | editions [1913, 1914, 1915]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1913 | L. D. Lowsley | Medical Officer | Medical | — | — |
| 1914 | L. D. Lowsley | Senior Medical Officer | Medical (East Africa and Uganda) | — | — |
| 1915 | L. D. Lowsley | Senior Medical Officer | Medical (East Africa and Uganda) | — | — |

### Deterministic checks: `lowesley_lionel-dewe_e1902` vs `Lowsley, L. D___Kenya___1913`

- [PASS] surname_gate: bio 'LOWESLEY' vs stint 'Lowsley, L. D' (fuzzy:1)
- [PASS] initials: bio ['L', 'D'] ~ stint ['L', 'D']
- [PASS] age_gate: stint starts 1913; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1913-1915
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `lowsley_lionel-dewe_e1902` vs `Lowsley, L. D___Kenya___1913`

- [PASS] surname_gate: bio 'LOWSLEY' vs stint 'Lowsley, L. D' (exact)
- [PASS] initials: bio ['L', 'D'] ~ stint ['L', 'D']
- [PASS] age_gate: stint starts 1913; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1913-1915
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

