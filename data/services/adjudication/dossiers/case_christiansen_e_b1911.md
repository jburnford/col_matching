<!-- {"case_id": "case_christiansen_e_b1911", "bio_ids": ["christiansen_e_b1911"], "stint_ids": ["Christianson, E___Seychelles___1949"]} -->
# Dossier case_christiansen_e_b1911

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['christiansen_e_b1911'] carry a single initial only — the namesake trap applies.
- NOTE: stint `Christianson, E___Seychelles___1949` is also gate-compatible with biography(ies) outside this case: ['christianson_edward_b1911'] (already linked elsewhere or filtered).

## Biography `christiansen_e_b1911`

- Printed name: **CHRISTIANSEN, E**
- Birth year: 1911 (attested in editions [1962, 1963, 1964])
- Appears in editions: [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1962-L19699.v` — printed in editions [1962, 1963, 1964]:**

> CHRISTIANSEN, E.—b. 1911; ed. Bloxham Sch., Banbury, and Camb. and Edin. Univs.; M.O., Sey., 1938; N. Borneo, 1951; P.M.O. 1962-63.

**Version `col1956-L20378.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961]:**

> CHRISTIANSEN, E.—b. 1911; ed. Bloxham Sch., Banbury, and Camb. and Edin. Unis.; M.O., Sey., 1938; N. Borneo, 1951; author Sarcoma of the Thyroid; Albinism in Sey. Native Families; Medical Life and Work in Sey., etc.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1938 | M.O. | Seychelles | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1951 | M.O. | North Borneo | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 2 | 1962–1963 | P.M.O | North Borneo *(inherited from previous clause)* | [1962, 1963, 1964] |

## Candidate stint `Christianson, E___Seychelles___1949`

- Staff-list name: **Christianson, E** | colony: **Seychelles** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | E. Christianson | Medical Officers | Medical | — | — |
| 1950 | E. Christianson | Medical Officer | MEDICAL | — | — |
| 1951 | E. Christianson | Medical Officer | MEDICAL | — | — |

### Deterministic checks: `christiansen_e_b1911` vs `Christianson, E___Seychelles___1949`

- [PASS] surname_gate: bio 'CHRISTIANSEN' vs stint 'Christianson, E' (fuzzy:1)
- [PASS] initials: bio ['E'] ~ stint ['E']
- [PASS] age_gate: stint starts 1949, birth 1911 (age 38)
- [PASS] colony: 1 placed event(s) resolve to 'Seychelles'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 24 vs bar 60: 'M.O.' ~ 'Medical Officer'
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

