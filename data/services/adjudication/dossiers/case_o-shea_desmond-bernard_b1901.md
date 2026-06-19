<!-- {"case_id": "case_o-shea_desmond-bernard_b1901", "bio_ids": ["o-shea_desmond-bernard_b1901"], "stint_ids": ["O'Shea, D. B___Nyasaland___1951"]} -->
# Dossier case_o-shea_desmond-bernard_b1901

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `o-shea_desmond-bernard_b1901`

- Printed name: **O'SHEA, Desmond Bernard**
- Birth year: 1901 (attested in editions [1953, 1954])
- Honours: M.I.C.E
- Appears in editions: [1949, 1950, 1951, 1953, 1954]

### Verbatim printed entry text (OCR)

**Version `col1953-L18625.v` — printed in editions [1953, 1954]:**

> O'SHEA, D. B.—b. 1901; ed. Stonyhurst Coll. and Pembroke Coll., Camb.; mil. serv., 1940–45, maj.; asst. engrn., Nig., 1926; Ken., 1938; exec. engrn., gr. I, 1946; D.D.P.W., N. Borneo, 1948; exec. engrn., P.W.D., Nyasa., 1949; D.D.P.W., 1951.

**Version `col1949-L34722.v` — printed in editions [1949, 1950, 1951]:**

> O'SHEA, Desmond Bernard, M.A. (Cantab.), M.I.C.E., M.I.Mun.E., A.M.I. Mech.E.—b. 1901; ed. Stonyhurst Coll. and Pembroke Coll., Lambeth; on mil. serv., 1940-45, maj.; asst. engnr., Nig., 1926; Ken., 1938; exec. engnr., gr. I, 1946; D.D.P.W., N. Borneo, 1948; exec. engnr., P.W.D., Nyasa., 1949.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | asst. engrn. | Nigeria | [1949, 1950, 1951, 1953, 1954] |
| 1 | 1938 | asst. engrn. | Kenya | [1949, 1950, 1951, 1953, 1954] |
| 2 | 1946 | exec. engrn., gr. I | Kenya *(inherited from previous clause)* | [1949, 1950, 1951, 1953, 1954] |
| 3 | 1948 | D.D.P.W. | North Borneo | [1949, 1950, 1951, 1953, 1954] |
| 4 | 1949 | exec. engrn., P.W.D. | Nyasaland | [1949, 1950, 1951, 1953, 1954] |
| 5 | 1951 | D.D.P.W | Nyasaland *(inherited from previous clause)* | [1953, 1954] |

## Candidate stint `O'Shea, D. B___Nyasaland___1951`

- Staff-list name: **O'Shea, D. B** | colony: **Nyasaland** | listed 1951–1954 | editions [1951, 1953, 1954]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1951 | D. B. O'Shea | Executive Engineer | Public Works | — | — |
| 1953 | D. B. O'Shea | Deputy Director of Public Works | Civil Establishment | — | — |
| 1954 | D. B. O'Shea | Deputy Director of Public Works | Civil Establishment | — | — |

### Deterministic checks: `o-shea_desmond-bernard_b1901` vs `O'Shea, D. B___Nyasaland___1951`

- [PASS] surname_gate: bio 'O'SHEA' vs stint 'O'Shea, D. B' (exact)
- [PASS] initials: bio ['D', 'B'] ~ stint ['D', 'B']
- [PASS] age_gate: stint starts 1951, birth 1901 (age 50)
- [PASS] colony: 2 placed event(s) resolve to 'Nyasaland'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1951-1954
- [FAIL] position_sim: best 56 vs bar 60: 'exec. engrn., P.W.D.' ~ 'Executive Engineer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

