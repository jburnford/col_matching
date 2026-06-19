<!-- {"case_id": "case_pasqual_james-robert-hylton_b1898", "bio_ids": ["pasqual_james-robert-hylton_b1898"], "stint_ids": ["Pasqual, J. R. H___North Borneo___1950"]} -->
# Dossier case_pasqual_james-robert-hylton_b1898

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `pasqual_james-robert-hylton_b1898`

- Printed name: **PASQUAL, James Robert Hylton**
- Birth year: 1898 (attested in editions [1949, 1950, 1951])
- Appears in editions: [1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1949-L34814.v` — printed in editions [1949, 1950, 1951]:**

> PASQUAL, James Robert Hylton, M.B., Ch.B. (Edin.), L.S.H.T.M. cert.—b. 1898; ed. Stonyhurst Coll. and Edin. Univ.; on naval serv., 1917-19, surg. sub-lieut.; med. offr., Nig., 1925; S.M.O., 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1917–1919 | surg. sub-lieut. | — | [1949, 1950, 1951] |
| 1 | 1925 | med. offr. | Nigeria | [1949, 1950, 1951] |
| 2 | 1937 | S.M.O. | — | [1949, 1950, 1951] |

## Candidate stint `Pasqual, J. R. H___North Borneo___1950`

- Staff-list name: **Pasqual, J. R. H** | colony: **North Borneo** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | J. R. H. Pasqual | Medical Officer | MEDICAL | — | — |
| 1951 | J. R. H. Pasqual | Medical Officer | MEDICAL | — | — |

### Deterministic checks: `pasqual_james-robert-hylton_b1898` vs `Pasqual, J. R. H___North Borneo___1950`

- [PASS] surname_gate: bio 'PASQUAL' vs stint 'Pasqual, J. R. H' (exact)
- [PASS] initials: bio ['J', 'R', 'H'] ~ stint ['J', 'R', 'H']
- [PASS] age_gate: stint starts 1950, birth 1898 (age 52)
- [FAIL] colony: no placed event resolves to 'North Borneo'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1950-1951
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

