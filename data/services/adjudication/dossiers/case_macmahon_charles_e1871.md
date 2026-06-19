<!-- {"case_id": "case_macmahon_charles_e1871", "bio_ids": ["macmahon_charles_e1871"], "stint_ids": ["MacMahon, N. C. M___Uganda___1911"]} -->
# Dossier case_macmahon_charles_e1871

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['macmahon_charles_e1871'] carry a single initial only — the namesake trap applies.
- NOTE: stint `MacMahon, N. C. M___Uganda___1911` is also gate-compatible with biography(ies) outside this case: ['macmahon_neil-cullagh-milfred_e1907'] (already linked elsewhere or filtered).

## Biography `macmahon_charles_e1871`

- Printed name: **MACMAHON, CHARLES**
- Birth year: not printed
- Honours: KNT. BACH. (1875)
- Appears in editions: [1886]

### Verbatim printed entry text (OCR)

**Version `col1886-L34668.v` — printed in editions [1886]:**

> MACMAHON, SIR CHARLES, KNT. BACH. (1875).—Speaker of the legislative assembly, Victoria, 1871-77 and 1880.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1871–1880 | Speaker of the legislative assembly | Victoria | [1886] |

## Candidate stint `MacMahon, N. C. M___Uganda___1911`

- Staff-list name: **MacMahon, N. C. M** | colony: **Uganda** | listed 1911–1913 | editions [1911, 1912, 1913]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1911 | N. C. MacMahon | Assistant District Commissioner | Administration | — | — |
| 1912 | N. C. MacMahon | Assistant District Commissioner | Administration | — | — |
| 1913 | N. C. M. MacMahon | Assistant District Commissioner | Administration | — | — |

### Deterministic checks: `macmahon_charles_e1871` vs `MacMahon, N. C. M___Uganda___1911`

- [PASS] surname_gate: bio 'MACMAHON' vs stint 'MacMahon, N. C. M' (exact)
- [PASS] initials: bio ['C'] ~ stint ['N', 'C', 'M']
- [PASS] age_gate: stint starts 1911; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Uganda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1911-1913
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

