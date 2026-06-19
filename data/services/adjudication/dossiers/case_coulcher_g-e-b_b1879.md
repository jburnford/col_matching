<!-- {"case_id": "case_coulcher_g-e-b_b1879", "bio_ids": ["coulcher_g-e-b_b1879"], "stint_ids": ["Coulcher, G. E. B___Nigeria___1928"]} -->
# Dossier case_coulcher_g-e-b_b1879

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `coulcher_g-e-b_b1879`

- Printed name: **COULCHER, G. E. B**
- Birth year: 1879 (attested in editions [1932])
- Honours: M.C. M.I.C.E
- Appears in editions: [1932]

### Verbatim printed entry text (OCR)

**Version `col1932-L59349.v` — printed in editions [1932]:**

> COULCHER, G. E. B., M.C. M.I.C.E., M.I. Struc. E., M.Am. Soc. C.E.—B.1879; mily. serv., France, four years with R.E.; dep. res. engrn., Lagos harbr. wks., 1922; dep. port engnr., harbr. dept., Lagos, Nov., 1927.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1922 | dep. res. engrn., Lagos harbr. wks | Lagos | [1932] |
| 1 | 1927 | dep. port engnr., harbr. dept. | Lagos | [1932] |

## Candidate stint `Coulcher, G. E. B___Nigeria___1928`

- Staff-list name: **Coulcher, G. E. B** | colony: **Nigeria** | listed 1928–1929 | editions [1928, 1929]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1928 | G. E. B. Coulcher | Deputy Port Engineer | Harbour Works, Lagos | — | — |
| 1929 | G. E. B. Coulcher | Deputy Port Engineer | Marine | M.C. | — |

### Deterministic checks: `coulcher_g-e-b_b1879` vs `Coulcher, G. E. B___Nigeria___1928`

- [PASS] surname_gate: bio 'COULCHER' vs stint 'Coulcher, G. E. B' (exact)
- [PASS] initials: bio ['G', 'E', 'B'] ~ stint ['G', 'E', 'B']
- [PASS] age_gate: stint starts 1928, birth 1879 (age 49)
- [FAIL] colony: no placed event resolves to 'Nigeria'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1928-1929
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

