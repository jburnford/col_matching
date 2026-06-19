<!-- {"case_id": "case_hobrough_edward-cecil_b1901", "bio_ids": ["hobrough_edward-cecil_b1901"], "stint_ids": ["Hobrough, E. C___Northern Rhodesia___1936", "Hobrough, E. C___Northern Rhodesia___1949"]} -->
# Dossier case_hobrough_edward-cecil_b1901

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hobrough_edward-cecil_b1901`

- Printed name: **HOBROUGH, Edward Cecil**
- Birth year: 1901 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L33364.v` — printed in editions [1948, 1949, 1950, 1951]:**

> HOBROUGH, Edward Cecil.—b. 1901; ed. Brockley Sec. Sch. and King's Coll., London, B.A. (hons.), Latin), dip. in pedagogy; prin., dept. European educ., N. Rhod., 1931.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1931 | prin., dept. European educ. | Northern Rhodesia | [1948, 1949, 1950, 1951] |

## Candidate stint `Hobrough, E. C___Northern Rhodesia___1936`

- Staff-list name: **Hobrough, E. C** | colony: **Northern Rhodesia** | listed 1936–1940 | editions [1936, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | E. C. Hobrough | Headmasters | European Education | — | — |
| 1937 | E. C. Hobrough | Headmasters | European Education | — | — |
| 1939 | E. C. Hobrough | Head Master | European Education | — | — |
| 1940 | E. C. Hobrough | Head Master | European Education | — | — |

### Deterministic checks: `hobrough_edward-cecil_b1901` vs `Hobrough, E. C___Northern Rhodesia___1936`

- [PASS] surname_gate: bio 'HOBROUGH' vs stint 'Hobrough, E. C' (exact)
- [PASS] initials: bio ['E', 'C'] ~ stint ['E', 'C']
- [PASS] age_gate: stint starts 1936, birth 1901 (age 35)
- [PASS] colony: 1 placed event(s) resolve to 'Northern Rhodesia'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1936-1940
- [FAIL] position_sim: best 29 vs bar 60: 'prin., dept. European educ.' ~ 'Head Master'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Hobrough, E. C___Northern Rhodesia___1949`

- Staff-list name: **Hobrough, E. C** | colony: **Northern Rhodesia** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | E. C. Hobrough | Principal | Education | — | — |
| 1951 | E. C. Hobrough | Principal | Education | — | — |

### Deterministic checks: `hobrough_edward-cecil_b1901` vs `Hobrough, E. C___Northern Rhodesia___1949`

- [PASS] surname_gate: bio 'HOBROUGH' vs stint 'Hobrough, E. C' (exact)
- [PASS] initials: bio ['E', 'C'] ~ stint ['E', 'C']
- [PASS] age_gate: stint starts 1949, birth 1901 (age 48)
- [PASS] colony: 1 placed event(s) resolve to 'Northern Rhodesia'
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

