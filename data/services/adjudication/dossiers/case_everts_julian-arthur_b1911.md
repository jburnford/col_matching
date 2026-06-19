<!-- {"case_id": "case_everts_julian-arthur_b1911", "bio_ids": ["everts_julian-arthur_b1911"], "stint_ids": ["Evetts, J. A___Northern Rhodesia___1949"]} -->
# Dossier case_everts_julian-arthur_b1911

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `everts_julian-arthur_b1911`

- Printed name: **EVERTS, Julian Arthur**
- Birth year: 1911 (attested in editions [1948])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L32490.v` — printed in editions [1948]:**

> EVERTS, Julian Arthur.—b. 1911; ed. Westminster Sch., B.N.C., Oxford, B.A. (Oxon); cadet, N. Rhod., 1935; dist. offr., 1937.

**Version `col1949-L31925.v` — printed in editions [1949, 1950, 1951]:**

> EVETTS, Julian Arthur.—b. 1911; ed. Westminster Sch., and Brasenose Coll., Oxford, B.A. (Oxon); cadet, N. Rhod., 1935; dist. offr., 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1935 | cadet | Northern Rhodesia | [1948, 1949, 1950, 1951] |
| 1 | 1937 | dist. offr | Northern Rhodesia *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Evetts, J. A___Northern Rhodesia___1949`

- Staff-list name: **Evetts, J. A** | colony: **Northern Rhodesia** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | J. A. Evetts | Assistant Chief Secretaries | Secretariat | — | — |
| 1951 | J. A. Evetts | Assistant Chief Secretaries | Secretariat | — | — |

### Deterministic checks: `everts_julian-arthur_b1911` vs `Evetts, J. A___Northern Rhodesia___1949`

- [PASS] surname_gate: bio 'EVERTS' vs stint 'Evetts, J. A' (fuzzy:1)
- [PASS] initials: bio ['J', 'A'] ~ stint ['J', 'A']
- [PASS] age_gate: stint starts 1949, birth 1911 (age 38)
- [PASS] colony: 2 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 33 vs bar 60: 'dist. offr' ~ 'Assistant Chief Secretaries'
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

