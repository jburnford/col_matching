<!-- {"case_id": "case_sheen_a_b1909", "bio_ids": ["sheen_a_b1909"], "stint_ids": ["Sheen, A___High Commission Territories___1959"]} -->
# Dossier case_sheen_a_b1909

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['sheen_a_b1909'] carry a single initial only — the namesake trap applies.

## Biography `sheen_a_b1909`

- Printed name: **SHEEN, A**
- Birth year: 1909 (attested in editions [1960, 1961, 1962, 1963, 1964, 1965])
- Honours: M.B.E
- Appears in editions: [1960, 1961, 1962, 1963, 1964, 1965]

### Verbatim printed entry text (OCR)

**Version `col1960-L27934.v` — printed in editions [1960, 1961, 1962, 1963, 1964, 1965]:**

> SHEEN, A., M.B.E.—b. 1909; mil. serv., 1939–45, major; F.O., 1948–55; estab. offr., Basuto., 1956; asst. sec. (estab.), high comsnr's office, 1958; sec., Surridge salaries comsn., 1958–59.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1948–1955 | F.O | — | [1960, 1961, 1962, 1963, 1964, 1965] |
| 1 | 1956 | estab. offr. | Basutoland | [1960, 1961, 1962, 1963, 1964, 1965] |
| 2 | 1958 | asst. sec. (estab.), high comsnr's office | Basutoland *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964, 1965] |

## Candidate stint `Sheen, A___High Commission Territories___1959`

- Staff-list name: **Sheen, A** | colony: **High Commission Territories** | listed 1959–1962 | editions [1959, 1960, 1962]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1959 | A. Sheen | Assistant Secretaries | HIGH COMMISSIONER'S OFFICE | M.B.E. | — |
| 1960 | A. Sheen | Assistant Secretary (Establishments) | HIGH COMMISSIONER'S OFFICE | M.B.E. | — |
| 1962 | A. Sheen | Assistant Secretary (Establishment) | HIGH COMMISSIONER'S OFFICE | — | — |

### Deterministic checks: `sheen_a_b1909` vs `Sheen, A___High Commission Territories___1959`

- [PASS] surname_gate: bio 'SHEEN' vs stint 'Sheen, A' (exact)
- [PASS] initials: bio ['A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1959, birth 1909 (age 50)
- [FAIL] colony: no placed event resolves to 'High Commission Territories'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1959-1962
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: M.B.E
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

