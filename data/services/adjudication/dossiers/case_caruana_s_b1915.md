<!-- {"case_id": "case_caruana_s_b1915", "bio_ids": ["caruana_s_b1915"], "stint_ids": ["Caruana, S___Sierra Leone___1949"]} -->
# Dossier case_caruana_s_b1915

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 35 official(s) with this surname in the graph's staff lists; 5 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['caruana_s_b1915'] carry a single initial only — the namesake trap applies.

## Biography `caruana_s_b1915`

- Printed name: **CARUANA, S**
- Birth year: 1915 (attested in editions [1958, 1959, 1960, 1961])
- Appears in editions: [1958, 1959, 1960, 1961]

### Verbatim printed entry text (OCR)

**Version `col1958-L21241.v` — printed in editions [1958, 1959, 1960, 1961]:**

> CARUANA, S.—b. 1915; ed. Lyceum, and Royal Univ., Malta; asst. M.O., Malta, 1943; M.O., S. Leone, 1946; S.M.O.(H.), 1957-60.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1943 | asst. M.O. | Malta | [1958, 1959, 1960, 1961] |
| 1 | 1946 | M.O., S. Leone | Malta *(inherited from previous clause)* | [1958, 1959, 1960, 1961] |
| 2 | 1957–1960 | S.M.O.(H.) | Malta *(inherited from previous clause)* | [1958, 1959, 1960, 1961] |

## Candidate stint `Caruana, S___Sierra Leone___1949`

- Staff-list name: **Caruana, S** | colony: **Sierra Leone** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | S. Caruana | Medical Officer | Medical | — | — |
| 1950 | S. Caruana | Medical Officer | Medical | — | — |
| 1951 | S. Caruana | Medical Officer | Medical | — | — |

### Deterministic checks: `caruana_s_b1915` vs `Caruana, S___Sierra Leone___1949`

- [PASS] surname_gate: bio 'CARUANA' vs stint 'Caruana, S' (exact)
- [PASS] initials: bio ['S'] ~ stint ['S']
- [PASS] age_gate: stint starts 1949, birth 1915 (age 34)
- [FAIL] colony: no placed event resolves to 'Sierra Leone'
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

