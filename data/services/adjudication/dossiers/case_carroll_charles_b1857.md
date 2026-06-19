<!-- {"case_id": "case_carroll_charles_b1857", "bio_ids": ["carroll_charles_b1857"], "stint_ids": ["Carroll, C. J___Cape of Good Hope___1883"]} -->
# Dossier case_carroll_charles_b1857

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 18 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['carroll_charles_b1857'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Carroll, C. J___Cape of Good Hope___1883` is also gate-compatible with biography(ies) outside this case: ['carroll_james_b1857'] (already linked elsewhere or filtered).

## Biography `carroll_charles_b1857`

- Printed name: **CARROLL, CHARLES**
- Birth year: 1857 (attested in editions [1911])
- Appears in editions: [1911]

### Verbatim printed entry text (OCR)

**Version `col1911-L43710.v` — printed in editions [1911]:**

> CARROLL, HON. CHARLES.—B. 1857; nat. min. and comsnr. of stamp duties, New Zealand, 1900.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1900 | nat. min. and comsnr. of stamp duties | New Zealand | [1911] |

## Candidate stint `Carroll, C. J___Cape of Good Hope___1883`

- Staff-list name: **Carroll, C. J** | colony: **Cape of Good Hope** | listed 1883–1890 | editions [1883, 1888, 1889, 1890]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1883 | C. J. Carroll | Examiner of Accounts | Accounting Branch | — | — |
| 1888 | C. J. Carroll | Examiner of Accounts | Accounting Branch | — | — |
| 1889 | C. J. Carroll | Asst. Acctt. and Bookkeeper | Accounting Branch | — | — |
| 1890 | C. J. Carroll | Asst. Acctt. and Bookkeeper | Accounting Branch | — | — |

### Deterministic checks: `carroll_charles_b1857` vs `Carroll, C. J___Cape of Good Hope___1883`

- [PASS] surname_gate: bio 'CARROLL' vs stint 'Carroll, C. J' (exact)
- [PASS] initials: bio ['C'] ~ stint ['C', 'J']
- [PASS] age_gate: stint starts 1883, birth 1857 (age 26)
- [FAIL] colony: no placed event resolves to 'Cape of Good Hope'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1883-1890
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

