<!-- {"case_id": "case_palmer_gerald-graham_e1901", "bio_ids": ["palmer_gerald-graham_e1901"], "stint_ids": ["Palmer, G. G___British Central Africa___1906"]} -->
# Dossier case_palmer_gerald-graham_e1901

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 61 official(s) with this surname in the graph's staff lists; 25 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `palmer_gerald-graham_e1901`

- Printed name: **PALMER, GERALD GRAHAM**
- Birth year: not printed
- Appears in editions: [1907, 1908, 1909, 1910, 1911]

### Verbatim printed entry text (OCR)

**Version `col1907-L46177.v` — printed in editions [1907, 1908, 1909, 1910, 1911]:**

> PALMER, GERALD GRAHAM.—Apptd. 3rd astt., B.C. Africa Prot., May, 1901; 2nd cls. dist. res., Apr., 1906.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1901 | Apptd. 3rd astt., B.C. Africa Prot | British Columbia | [1907, 1908, 1909, 1910, 1911] |
| 1 | 1906 | 2nd cls. dist. res | British Columbia *(inherited from previous clause)* | [1907, 1908, 1909, 1910, 1911] |

## Candidate stint `Palmer, G. G___British Central Africa___1906`

- Staff-list name: **Palmer, G. G** | colony: **British Central Africa** | listed 1906–1907 | editions [1906, 1907]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1906 | G. G. Palmer | 3rd class Assistant | Collectors | — | — |
| 1907 | G. G. Palmer | Twelve 2nd class | Residents | — | — |

### Deterministic checks: `palmer_gerald-graham_e1901` vs `Palmer, G. G___British Central Africa___1906`

- [PASS] surname_gate: bio 'PALMER' vs stint 'Palmer, G. G' (exact)
- [PASS] initials: bio ['G', 'G'] ~ stint ['G', 'G']
- [PASS] age_gate: stint starts 1906; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'British Central Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1906-1907
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

