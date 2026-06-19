<!-- {"case_id": "case_bean_arnold_b1899", "bio_ids": ["bean_arnold_b1899"], "stint_ids": ["Bean, A___Straits Settlements___1931"]} -->
# Dossier case_bean_arnold_b1899

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['bean_arnold_b1899'] carry a single initial only — the namesake trap applies.

## Biography `bean_arnold_b1899`

- Printed name: **BEAN, Arnold**
- Birth year: 1899 (attested in editions [1948, 1949])
- Honours: A.C.S.M, A.I.M.M
- Appears in editions: [1948, 1949]

### Verbatim printed entry text (OCR)

**Version `col1948-L31050.v` — printed in editions [1948, 1949]:**

> BEAN, Arnold, A.C.S.M., A.I.M.M.—b. 1899; ed. Camborne Sch. of Mines, Cornwall; on mil. serv., 1941-46, lt.; apptd. col. serv., 1927; senr. inspr., mines, Mal., 1938; ch. inspr., mines, Mal., 1946; chmn., Chinese tin mines, loans bd.; mem., econ. dev. comtece.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | apptd. col. serv | — | [1948, 1949] |
| 1 | 1938 | senr. inspr., mines | Malaya | [1948, 1949] |
| 2 | 1946 | ch. inspr., mines | Malaya | [1948, 1949] |

## Candidate stint `Bean, A___Straits Settlements___1931`

- Staff-list name: **Bean, A** | colony: **Straits Settlements** | listed 1931–1933 | editions [1931, 1933]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | A. Bean | Inspectors of Mines | Mines | — | — |
| 1933 | A. Bean | Inspectors of Mines | Mines | — | — |

### Deterministic checks: `bean_arnold_b1899` vs `Bean, A___Straits Settlements___1931`

- [PASS] surname_gate: bio 'BEAN' vs stint 'Bean, A' (exact)
- [PASS] initials: bio ['A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1931, birth 1899 (age 32)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1933
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

