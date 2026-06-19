<!-- {"case_id": "case_searl_theodore-nathaniel_b1893", "bio_ids": ["searl_theodore-nathaniel_b1893"], "stint_ids": ["Searl, T. N___Trinidad and Tobago___1925"]} -->
# Dossier case_searl_theodore-nathaniel_b1893

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `searl_theodore-nathaniel_b1893`

- Printed name: **SEARL, Theodore Nathaniel**
- Birth year: 1893 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L35776.v` — printed in editions [1948, 1949, 1950, 1951]:**

> SEARL, Theodore Nathaniel.—b. 1893; ed. Queen's Royal Coll., Trin.; clk., Trin., 1920; asst. warden, 1933; warden, 1947.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920 | clk. | Trinidad | [1948, 1949, 1950, 1951] |
| 1 | 1933 | asst. warden | Trinidad *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 2 | 1947 | warden | Trinidad *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Searl, T. N___Trinidad and Tobago___1925`

- Staff-list name: **Searl, T. N** | colony: **Trinidad and Tobago** | listed 1925–1939 | editions [1925, 1927, 1928, 1929, 1931, 1933, 1934, 1937, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | T. N. Searl | 4th Clerk | Auditor's Department | — | — |
| 1927 | T. N. Searl | 4th Clerk | Auditor's Department | — | — |
| 1928 | T. N. Searl | 4th Clerk | Auditor's Department | — | — |
| 1929 | T. N. Searl | 3rd Clerk | Auditor's Department | — | — |
| 1931 | T. N. Searl | Clerk | Audit Department | — | — |
| 1933 | T. N. Searl | Senior Clerk | Colonial Secretary's Department | — | — |
| 1934 | T. N. Searl | Asst. Warden, Toco | Wardens | — | — |
| 1937 | T. N. Searl | Assistant Warden, Eastern Counties (Toco) | District Administration | — | — |
| 1939 | T. N. Searl | Assistant Warden, Eastern Counties | District Administration | — | — |

### Deterministic checks: `searl_theodore-nathaniel_b1893` vs `Searl, T. N___Trinidad and Tobago___1925`

- [PASS] surname_gate: bio 'SEARL' vs stint 'Searl, T. N' (exact)
- [PASS] initials: bio ['T', 'N'] ~ stint ['T', 'N']
- [PASS] age_gate: stint starts 1925, birth 1893 (age 32)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1925-1939
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

