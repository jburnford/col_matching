<!-- {"case_id": "case_schofield_f_b1910", "bio_ids": ["schofield_f_b1910"], "stint_ids": ["Schofield, I. F. W___Nigeria___1956"]} -->
# Dossier case_schofield_f_b1910

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 9 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['schofield_f_b1910'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Schofield, I. F. W___Nigeria___1956` is also gate-compatible with biography(ies) outside this case: ['schofield_i-f-w_b1904', 'schofield_walter_b1888'] (already linked elsewhere or filtered).

## Biography `schofield_f_b1910`

- Printed name: **SCHOFIELD, F.**
- Birth year: 1910 (attested in editions [1965, 1966])
- Appears in editions: [1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1965-L18947.v` — printed in editions [1965, 1966]:**

> SCHOFIELD, Miss F.—b. 1910; ed. Girls' High Sch., Pontefract and Univ. of Leeds; educ. offr. (woman), H.K., 1954.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1954 | educ. offr. (woman) | Hong Kong | [1965, 1966] |

## Candidate stint `Schofield, I. F. W___Nigeria___1956`

- Staff-list name: **Schofield, I. F. W** | colony: **Nigeria** | listed 1956–1960 | editions [1956, 1958, 1960]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1956 | I. F. W. Schofield | Administrative Officer (Staff Grade) | Civil Establishment | — | — |
| 1958 | I. F. W. Schofield | Permanent Secretaries and Administrative Officers (Staff Grade) | Civil Establishment | C.M.G. | — |
| 1960 | I. F. W. Schofield | Commissioner of Inland Revenue | Civil Establishment, Western Region | C.M.G. | — |

### Deterministic checks: `schofield_f_b1910` vs `Schofield, I. F. W___Nigeria___1956`

- [PASS] surname_gate: bio 'SCHOFIELD' vs stint 'Schofield, I. F. W' (exact)
- [PASS] initials: bio ['F'] ~ stint ['I', 'F', 'W']
- [PASS] age_gate: stint starts 1956, birth 1910 (age 46)
- [FAIL] colony: no placed event resolves to 'Nigeria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1956-1960
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

