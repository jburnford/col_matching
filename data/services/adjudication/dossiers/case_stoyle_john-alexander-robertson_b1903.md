<!-- {"case_id": "case_stoyle_john-alexander-robertson_b1903", "bio_ids": ["stoyle_john-alexander-robertson_b1903"], "stint_ids": ["Stoyle, J. A. R___Nigeria___1952"]} -->
# Dossier case_stoyle_john-alexander-robertson_b1903

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `stoyle_john-alexander-robertson_b1903`

- Printed name: **STOYLE, John Alexander Robertson**
- Birth year: 1903 (attested in editions [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956])
- Honours: A.R.I.C
- Appears in editions: [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956]

### Verbatim printed entry text (OCR)

**Version `col1948-L36197.v` — printed in editions [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956]:**

> STOYLE, John Alexander Robertson, B.Sc. (hons.), A.R.I.C.—b. 1903; ed. Royal Belfast Acad. Inst. and Queen’s Univ., Belfast (schol.); on mil. serv. 1941-43, capt.; gov. analyst, Maur., 1934; asst. gov. chem., Nig., 1938; gov. chem., 1949.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1934 | gov. analyst | Mauritius | [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956] |
| 1 | 1938 | asst. gov. chem. | Nigeria | [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956] |
| 2 | 1949 | gov. chem | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956] |

## Candidate stint `Stoyle, J. A. R___Nigeria___1952`

- Staff-list name: **Stoyle, J. A. R** | colony: **Nigeria** | listed 1952–1956 | editions [1952, 1956]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1952 | J. A. R. Stoyle | Government Chemist | Civil Establishment | — | — |
| 1956 | J. A. R. Stoyle | Federal Government Chemist | Civil Establishment | — | — |

### Deterministic checks: `stoyle_john-alexander-robertson_b1903` vs `Stoyle, J. A. R___Nigeria___1952`

- [PASS] surname_gate: bio 'STOYLE' vs stint 'Stoyle, J. A. R' (exact)
- [PASS] initials: bio ['J', 'A', 'R'] ~ stint ['J', 'A', 'R']
- [PASS] age_gate: stint starts 1952, birth 1903 (age 49)
- [PASS] colony: 2 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1952-1956
- [PASS] position_sim: best 62 vs bar 60: 'gov. chem' ~ 'Government Chemist'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

