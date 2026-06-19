<!-- {"case_id": "case_simpkins_alick-louis_b1901", "bio_ids": ["simpkins_alick-louis_b1901"], "stint_ids": ["Simpkins, A. L___Northern Rhodesia___1948"]} -->
# Dossier case_simpkins_alick-louis_b1901

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `simpkins_alick-louis_b1901`

- Printed name: **SIMPKINS, ALICK LOUIS**
- Birth year: 1901 (attested in editions [1939, 1940])
- Honours: A.C.G.I, A.C.I.E, M.I.C.E
- Appears in editions: [1939, 1940, 1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1939-L70616.v` — printed in editions [1939, 1940]:**

> SIMPKINS, ALICK LOUIS, A.C.I.E., A.M.Inst.C.E., A.M.Inst.M.E.—B. 1901; ed. Eastbourne Coll. and City and Guilds Engng. Coll.; astt. engnr., P.W.D., Nigeria, 1926; exec. engnr., 1933; superintending engnr., P.W.D., Cyprus, June, 1937; D.P.W., 1937.

**Version `col1948-L35903.v` — printed in editions [1948, 1949, 1950, 1951]:**

> SIMPKINS, Alick Louis, A.C.G.I., M.I.C.E., A.M.I.Mech.E.—b. 1901; ed. Eastbourne Coll., City and Guilds (Eng.) Coll.; asst. engr., P.W.D., Nig., 1926; D.P.W., Cyp., 1937; D.P.W., N. Rhod., 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | astt. engnr., P.W.D. | Nigeria | [1939, 1940, 1948, 1949, 1950, 1951] |
| 1 | 1933 | exec. engnr | Nigeria *(inherited from previous clause)* | [1939, 1940] |
| 2 | 1937 | superintending engnr., P.W.D. | Cyprus | [1939, 1940, 1948, 1949, 1950, 1951] |
| 3 | 1946 | D.P.W. | Northern Rhodesia | [1948, 1949, 1950, 1951] |

## Candidate stint `Simpkins, A. L___Northern Rhodesia___1948`

- Staff-list name: **Simpkins, A. L** | colony: **Northern Rhodesia** | listed 1948–1951 | editions [1948, 1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1948 | A. L. Simpkins | Nominated Official Member | LEGISLATIVE COUNCIL | — | — |
| 1949 | A. L. Simpkins | Director | PUBLIC WORKS | — | — |
| 1951 | A. L. Simpkins | Director | Public Works | — | — |

### Deterministic checks: `simpkins_alick-louis_b1901` vs `Simpkins, A. L___Northern Rhodesia___1948`

- [PASS] surname_gate: bio 'SIMPKINS' vs stint 'Simpkins, A. L' (exact)
- [PASS] initials: bio ['A', 'L'] ~ stint ['A', 'L']
- [PASS] age_gate: stint starts 1948, birth 1901 (age 47)
- [PASS] colony: 1 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1948-1951
- [FAIL] position_sim: best 18 vs bar 60: 'D.P.W.' ~ 'Director'
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

