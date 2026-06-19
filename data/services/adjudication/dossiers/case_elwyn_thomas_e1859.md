<!-- {"case_id": "case_elwyn_thomas_e1859", "bio_ids": ["elwyn_thomas_e1859"], "stint_ids": ["Elwyn, T___Canada___1883"]} -->
# Dossier case_elwyn_thomas_e1859

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['elwyn_thomas_e1859'] carry a single initial only — the namesake trap applies.

## Biography `elwyn_thomas_e1859`

- Printed name: **ELWYN, Thomas**
- Birth year: not printed
- Appears in editions: [1883, 1886, 1888, 1889, 1890]

### Verbatim printed entry text (OCR)

**Version `col1883-L27353.v` — printed in editions [1883, 1886, 1888, 1889, 1890]:**

> ELWYN, Thomas.—Formerly in the army; assistant gold commissioner and stipendiary magistrate British Columbia, June, 1859 to April, 1863; second in command of gold escort, June, 1863, deputy provincial secretary, British Columbia, Nov., 1877.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1859–1863 | assistant gold commissioner and stipendiary magistrate | British Columbia | [1883, 1886, 1888, 1889, 1890] |
| 1 | 1863 | second in command of gold escort | — | [1883, 1886, 1888, 1889, 1890] |
| 2 | 1877 | deputy provincial secretary | British Columbia | [1883, 1886, 1888, 1889, 1890] |

## Candidate stint `Elwyn, T___Canada___1883`

- Staff-list name: **Elwyn, T** | colony: **Canada** | listed 1883–1888 | editions [1883, 1886, 1888]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1883 | T. Elwyn | Deputy Provincial Secretary | Provincial Secretary's Office | — | — |
| 1886 | T. Elwyn | Deputy Provincial Secretary | Provincial Secretary's Office | — | — |
| 1888 | T. Elwyn | Deputy Provincial Secretary | Provincial Secretary's Office | — | — |

### Deterministic checks: `elwyn_thomas_e1859` vs `Elwyn, T___Canada___1883`

- [PASS] surname_gate: bio 'ELWYN' vs stint 'Elwyn, T' (exact)
- [PASS] initials: bio ['T'] ~ stint ['T']
- [PASS] age_gate: stint starts 1883; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Canada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1883-1888
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

