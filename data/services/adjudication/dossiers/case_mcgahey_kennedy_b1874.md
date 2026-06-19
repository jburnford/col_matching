<!-- {"case_id": "case_mcgahey_kennedy_b1874", "bio_ids": ["mcgahey_kennedy_b1874"], "stint_ids": ["McGahey, K___Northern Nigeria___1907"]} -->
# Dossier case_mcgahey_kennedy_b1874

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['mcgahey_kennedy_b1874'] carry a single initial only — the namesake trap applies.

## Biography `mcgahey_kennedy_b1874`

- Printed name: **MCGAHEY, KENNEDY**
- Birth year: 1874 (attested in editions [1920, 1921])
- Appears in editions: [1920, 1921]

### Verbatim printed entry text (OCR)

**Version `col1920-L55399.v` — printed in editions [1920, 1921]:**

> MCGAHEY, KENNEDY.—B. 1874; D.P.H., L.R.C.S.P., Edin.; L.F.P., Glasgow; senr. sanitary offr., Ceylon, Nov., 1913.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1913 | senr. sanitary offr. | Ceylon | [1920, 1921] |

## Candidate stint `McGahey, K___Northern Nigeria___1907`

- Staff-list name: **McGahey, K** | colony: **Northern Nigeria** | listed 1907–1913 | editions [1907, 1908, 1909, 1910, 1911, 1912, 1913]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1907 | K. McGahey | Medical Officer | Medical | — | — |
| 1908 | K. McGahey | Thirty-Two Medical Officers | Medical | — | — |
| 1909 | K. McGahey | Medical Officer | Medical | — | — |
| 1910 | K. McGahey | Medical Officer | Medical | — | — |
| 1911 | K. McGahey | Medical Officer | Medical | — | — |
| 1912 | K. McGahey | Medical Officer | Medical | — | — |
| 1913 | K. McGahey | Medical Officer | Medical | — | — |

### Deterministic checks: `mcgahey_kennedy_b1874` vs `McGahey, K___Northern Nigeria___1907`

- [PASS] surname_gate: bio 'MCGAHEY' vs stint 'McGahey, K' (exact)
- [PASS] initials: bio ['K'] ~ stint ['K']
- [PASS] age_gate: stint starts 1907, birth 1874 (age 33)
- [FAIL] colony: no placed event resolves to 'Northern Nigeria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1907-1913
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

