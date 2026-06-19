<!-- {"case_id": "case_chilton_noel_b1900", "bio_ids": ["chilton_noel_b1900"], "stint_ids": ["Chilton, N___Tanganyika___1940"]} -->
# Dossier case_chilton_noel_b1900

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['chilton_noel_b1900'] carry a single initial only — the namesake trap applies.

## Biography `chilton_noel_b1900`

- Printed name: **CHILTON, Noel**
- Birth year: 1900 (attested in editions [1956])
- Honours: B.A, B.M
- Appears in editions: [1933, 1935, 1936, 1948, 1949, 1950, 1951, 1956]

### Verbatim printed entry text (OCR)

**Version `col1956-L20372.v` — printed in editions [1956]:**

> CHILTON, N.—b. 1900; ed. Marlborough Coll., Brasenose Coll., Oxford and St. Bart's Hosp.; mil. serv., 1940-44, surg. lt.-cmdr.; M.O., Tang., 1929; tutorial M.O., 1936; S.M.O., 1947; regl. asst. D.M.S., 1950; author of Swahili Textbook on Parasitic Diseases.

**Version `col1950-L34372.v` — printed in editions [1950, 1951]:**

> CHILTON, Noel, B.A., D.M. (Oxon), D.T.M. & H. (Eng.).—b. 1900; ed. Marlborough Coll. and Brasenose Coll., Oxford; on mil. serv., 1940-44; med. offr., T.T., 1929; S.M.O., 1946; reg. assr. D.M.S., 1950; author of Swahili Text Book on Parasitic Diseases.

**Version `col1948-L31753.v` — printed in editions [1948, 1949]:**

> CHILTON, Noel, B.A., B.M., B.Ch. (Oxon), D.T.M. & H. (Lond.)—b. 1900; ed. Marlborough Coll, Brasenose Coll., Oxford, and St. Bart's Hosp.; med. offr., T.T., 1929; S.M.O., 1947.

**Version `col1933-L58611.v` — printed in editions [1933, 1935, 1936]:**

> CHILTON, N., B.A. (Hons.), B.M., B.Ch. (Orf.), D.T.M. & H. (Lond.).—B. 1900; med. offr., Tanganyika Territory, Mar., 1929.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | M.O. | Tanganyika | [1933, 1935, 1936, 1956] |
| 1 | 1929 | med. offr., T.T | — | [1948, 1949, 1950, 1951] |
| 2 | 1936 | tutorial M.O | Tanganyika *(inherited from previous clause)* | [1956] |
| 3 | 1946 | S.M.O | — | [1950, 1951] |
| 4 | 1947 | S.M.O | Tanganyika *(inherited from previous clause)* | [1948, 1949, 1956] |
| 5 | 1950 | regl. asst. D.M.S | Tanganyika *(inherited from previous clause)* | [1950, 1951, 1956] |

## Candidate stint `Chilton, N___Tanganyika___1940`

- Staff-list name: **Chilton, N** | colony: **Tanganyika** | listed 1940–1949 | editions [1940, 1949]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1940 | N. Chilton | Medical Officer | Medical Department | — | — |
| 1949 | N. Chilton | Senior Medical Officer | Medical and Sanitation | — | — |

### Deterministic checks: `chilton_noel_b1900` vs `Chilton, N___Tanganyika___1940`

- [PASS] surname_gate: bio 'CHILTON' vs stint 'Chilton, N' (exact)
- [PASS] initials: bio ['N'] ~ stint ['N']
- [PASS] age_gate: stint starts 1940, birth 1900 (age 40)
- [PASS] colony: 4 placed event(s) resolve to 'Tanganyika'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1940-1949
- [FAIL] position_sim: best 31 vs bar 60: 'tutorial M.O' ~ 'Medical Officer'
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

