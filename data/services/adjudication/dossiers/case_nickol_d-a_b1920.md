<!-- {"case_id": "case_nickol_d-a_b1920", "bio_ids": ["nickol_d-a_b1920"], "stint_ids": ["Nicol, A___Hong Kong___1939", "Nicol, A___Hong Kong___1949"]} -->
# Dossier case_nickol_d-a_b1920

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 24 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Nicol, A___Hong Kong___1939` is also gate-compatible with biography(ies) outside this case: ['nicol_alexander-kennedy-forest_b1911', 'nicol_andrew_b1898'] (already linked elsewhere or filtered).
- NOTE: stint `Nicol, A___Hong Kong___1949` is also gate-compatible with biography(ies) outside this case: ['nicol_alexander-kennedy-forest_b1911', 'nicol_andrew_b1898'] (already linked elsewhere or filtered).

## Biography `nickol_d-a_b1920`

- Printed name: **NICKOL, D. A**
- Birth year: 1920 (attested in editions [1958, 1959, 1960, 1961])
- Honours: M.B.E (1959)
- Appears in editions: [1958, 1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1958-L25618.v` — printed in editions [1958, 1959, 1960, 1961]:**

> NICKOL, D. A., M.B.E. (1959)—b. 1920; ed. Felsted; mil. serv., 1939-46, capt.; admin. cadet, Tang., 1946; dist. offr., 1948; publ. *Bena Wattle Scheme* (Ag. Jour.).

**Version `col1962-L24890.v` — printed in editions [1962]:**

> NICKOL, D. A., M.B.E. (1959)—b. 1920; ed. Felsted; mil. serv., 1939-46, capt.; admin. cadet, Tang., 1946; D.O., 1948-61.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | admin. cadet | Tanganyika | [1958, 1959, 1960, 1961, 1962] |
| 1 | 1948 | dist. offr | Tanganyika *(inherited from previous clause)* | [1958, 1959, 1960, 1961] |
| 2 | 1948–1961 | admin. cadet | Dominions Office | [1962] |

## Candidate stint `Nicol, A___Hong Kong___1939`

- Staff-list name: **Nicol, A** | colony: **Hong Kong** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | A. Nicol | Executive Engineer | Public Works Department | — | — |
| 1940 | A. Nicol | Executive Engineers | Public Works Department | — | — |

### Deterministic checks: `nickol_d-a_b1920` vs `Nicol, A___Hong Kong___1939`

- [PASS] surname_gate: bio 'NICKOL' vs stint 'Nicol, A' (fuzzy:1)
- [PASS] initials: bio ['D', 'A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1939, birth 1920 (age 19)
- [FAIL] colony: no placed event resolves to 'Hong Kong'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1939-1940
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Nicol, A___Hong Kong___1949`

- Staff-list name: **Nicol, A** | colony: **Hong Kong** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | A. Nicol | Executive Engineer | Public Works | — | — |
| 1950 | A. Nicol | Deputy Director of Public Works | Public Works | — | — |

### Deterministic checks: `nickol_d-a_b1920` vs `Nicol, A___Hong Kong___1949`

- [PASS] surname_gate: bio 'NICKOL' vs stint 'Nicol, A' (fuzzy:1)
- [PASS] initials: bio ['D', 'A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1949, birth 1920 (age 29)
- [FAIL] colony: no placed event resolves to 'Hong Kong'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1950
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

