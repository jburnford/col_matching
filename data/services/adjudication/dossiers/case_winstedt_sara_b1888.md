<!-- {"case_id": "case_winstedt_sara_b1888", "bio_ids": ["winstedt_sara_b1888"], "stint_ids": ["Winstedt, S___Straits Settlements___1922"]} -->
# Dossier case_winstedt_sara_b1888

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['winstedt_sara_b1888'] carry a single initial only — the namesake trap applies.

## Biography `winstedt_sara_b1888`

- Printed name: **WINSTEDT, SARA**
- Birth year: 1888 (attested in editions [1932, 1933])
- Honours: M.B
- Appears in editions: [1932, 1933]

### Verbatim printed entry text (OCR)

**Version `col1932-L65166.v` — printed in editions [1932, 1933]:**

> WINSTEDT, SARA, M.B., Ch. B. (Edin.).—B. 1888; med. offr., gen. hosp., Kuala Lumpur, 1913; Singapore, 1921.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1913 | med. offr., gen. hosp., Kuala Lumpur | — | [1932, 1933] |
| 1 | 1921 | med. offr., gen. hosp., Kuala Lumpur | Singapore | [1932, 1933] |

## Candidate stint `Winstedt, S___Straits Settlements___1922`

- Staff-list name: **Winstedt, S** | colony: **Straits Settlements** | listed 1922–1933 | editions [1922, 1923, 1925, 1931, 1933]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1922 | S. Winstedt | Medical Officer and Health Officer | Medical | — | — |
| 1923 | S. Winstedt | Medical Officers and Health Officers | Medical | — | — |
| 1925 | S. Winstedt | Lady Medical Officer | SINGAPORE | — | — |
| 1931 | S. Winstedt | Medical and Health Officer | Medical | — | — |
| 1933 | S. Winstedt | Medical and Health Officer | Medical | — | — |

### Deterministic checks: `winstedt_sara_b1888` vs `Winstedt, S___Straits Settlements___1922`

- [PASS] surname_gate: bio 'WINSTEDT' vs stint 'Winstedt, S' (exact)
- [PASS] initials: bio ['S'] ~ stint ['S']
- [PASS] age_gate: stint starts 1922, birth 1888 (age 34)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1922-1933
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

