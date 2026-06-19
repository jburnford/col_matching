<!-- {"case_id": "case_carr_frederick-bernard_b1893-2", "bio_ids": ["carr_frederick-bernard_b1893-2"], "stint_ids": ["Carr, F. B___Nigeria___1925", "Carr, F. B___Nigeria___1946"]} -->
# Dossier case_carr_frederick-bernard_b1893-2

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 22 official(s) with this surname in the graph's staff lists; 13 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Carr, F. B___Nigeria___1925` is also gate-compatible with biography(ies) outside this case: ['carr_frederick-bernard_b1893'] (already linked elsewhere or filtered).
- NOTE: stint `Carr, F. B___Nigeria___1946` is also gate-compatible with biography(ies) outside this case: ['carr_frederick-bernard_b1893'] (already linked elsewhere or filtered).

## Biography `carr_frederick-bernard_b1893-2`

- Printed name: **CARR, Frederick Bernard**
- Birth year: 1893 (attested in editions [1948, 1949, 1950, 1951])
- Honours: C.M.G (1944), Kt. Bach (1946)
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L31647.v` — printed in editions [1948, 1949, 1950, 1951]:**

> CARR, Sir Frederick Bernard, Kt. Bach. (1946), C.M.G. (1944).—b. 1893; ed. Whitgift; on mil. serv., 1914–19; cadet, Nig., 1919; dep. res., 1933; res., 1935; staff grade, 1939; ch. comsnt., 1943; retd., 1949; sec., Aba comsnt. of enquiry, 1930; chmn., comittee of rev. of the salaries of native admin. employees, E. prov., 1942.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1919 | cadet | Nigeria | [1948, 1949, 1950, 1951] |
| 1 | 1930 | sec., Aba comsnt. of enquiry | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 2 | 1933 | dep. res | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 3 | 1935 | res | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 4 | 1939 | staff grade | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 5 | 1942 | chmn., comittee of rev. of the salaries of native admin. employees, E. prov | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 6 | 1943 | ch. comsnt | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 7 | 1949 | retd | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Carr, F. B___Nigeria___1925`

- Staff-list name: **Carr, F. B** | colony: **Nigeria** | listed 1925–1927 | editions [1925, 1927]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | Lieut. F. B. Carr | 294 District Officers | Political | M.C. | — |
| 1927 | F. B. Carr | Assistant Secretary | Secretariat, Southern Provinces and Colony | — | — |

### Deterministic checks: `carr_frederick-bernard_b1893-2` vs `Carr, F. B___Nigeria___1925`

- [PASS] surname_gate: bio 'CARR' vs stint 'Carr, F. B' (exact)
- [PASS] initials: bio ['F', 'B'] ~ stint ['F', 'B']
- [PASS] age_gate: stint starts 1925, birth 1893 (age 32)
- [PASS] colony: 8 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1925-1927
- [FAIL] position_sim: best 25 vs bar 60: 'cadet' ~ 'Assistant Secretary'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Carr, F. B___Nigeria___1946`

- Staff-list name: **Carr, F. B** | colony: **Nigeria** | listed 1946–1948 | editions [1946, 1948]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1946 | Sir F. B. Carr | Chief Commissioner, Eastern Provinces | Ex-officio Members | C.M.G. | — |
| 1948 | F. B. Carr | Chief Commissioner, Eastern Provinces | Ex-officio Members | C.M.G. | — |

### Deterministic checks: `carr_frederick-bernard_b1893-2` vs `Carr, F. B___Nigeria___1946`

- [PASS] surname_gate: bio 'CARR' vs stint 'Carr, F. B' (exact)
- [PASS] initials: bio ['F', 'B'] ~ stint ['F', 'B']
- [PASS] age_gate: stint starts 1946, birth 1893 (age 53)
- [PASS] colony: 8 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1946-1948
- [FAIL] position_sim: best 40 vs bar 60: 'ch. comsnt' ~ 'Chief Commissioner, Eastern Provinces'
- [PASS] honour: shared: C.M.G
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

