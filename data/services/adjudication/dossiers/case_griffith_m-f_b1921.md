<!-- {"case_id": "case_griffith_m-f_b1921", "bio_ids": ["griffith_m-f_b1921"], "stint_ids": ["Griffith, M. F. H___Leeward Islands___1949"]} -->
# Dossier case_griffith_m-f_b1921

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 51 official(s) with this surname in the graph's staff lists; 26 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `griffith_m-f_b1921`

- Printed name: **GRIFFITH, M.F.**
- Birth year: 1921 (attested in editions [1964, 1965, 1966])
- Appears in editions: [1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1964-L17616.v` — printed in editions [1964, 1965, 1966]:**

> GRIFFITH, M.F.—b. 1921; ed. Bryanston, Hastings Sch. of Art, Bromley Coll. of Art and Brighton Coll. of Art; mil. serv., 1940-46, R.N., It.; educ. offr., H.K., 1952.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1940–1946 | mil. serv., R.N., It. | — | [1964, 1965, 1966] |
| 1 | 1952 | educ. offr. | Hong Kong | [1964, 1965, 1966] |

## Candidate stint `Griffith, M. F. H___Leeward Islands___1949`

- Staff-list name: **Griffith, M. F. H** | colony: **Leeward Islands** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | M. F. H. Griffith | Medical Officer, District 7 | Health | — | — |
| 1950 | M. F. H. Griffith | Medical Officer, District 4 | HEALTH | — | — |
| 1951 | M. F. H. Griffith | Medical Officer, District 4 | HEALTH | — | — |

### Deterministic checks: `griffith_m-f_b1921` vs `Griffith, M. F. H___Leeward Islands___1949`

- [PASS] surname_gate: bio 'GRIFFITH' vs stint 'Griffith, M. F. H' (exact)
- [PASS] initials: bio ['M', 'F'] ~ stint ['M', 'F', 'H']
- [PASS] age_gate: stint starts 1949, birth 1921 (age 28)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
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

