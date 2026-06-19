<!-- {"case_id": "case_rice_cuthbert-llewellyn_b1903", "bio_ids": ["rice_cuthbert-llewellyn_b1903"], "stint_ids": ["Rice, C. Ll___Sierra Leone___1949"]} -->
# Dossier case_rice_cuthbert-llewellyn_b1903

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 26 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `rice_cuthbert-llewellyn_b1903`

- Printed name: **RICE, Cuthbert Llewellyn**
- Birth year: 1903 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L35486.v` — printed in editions [1948, 1949, 1950, 1951]:**

> RICE, Cuthbert Llewellyn.—b. 1903; ed. Taunton Sch. and London Univ., B.A. (hons.) (Lond.); on mil. serv. 1939-40, lieut.; supt. of educ., Nig., 1929; title changed to educ. offr.; educ. offr., S.L., 1944 (on secondment).

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | supt. of educ. | Nigeria | [1948, 1949, 1950, 1951] |

## Candidate stint `Rice, C. Ll___Sierra Leone___1949`

- Staff-list name: **Rice, C. Ll** | colony: **Sierra Leone** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | C. L. Rice | Education Officer | Education | — | — |
| 1950 | C. Ll. Rice | Education Officers | Education | — | — |
| 1951 | C. Ll. Rice | Education Officer | EDUCATION | — | — |

### Deterministic checks: `rice_cuthbert-llewellyn_b1903` vs `Rice, C. Ll___Sierra Leone___1949`

- [PASS] surname_gate: bio 'RICE' vs stint 'Rice, C. Ll' (exact)
- [PASS] initials: bio ['C', 'L'] ~ stint ['C', 'L']
- [PASS] age_gate: stint starts 1949, birth 1903 (age 46)
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

