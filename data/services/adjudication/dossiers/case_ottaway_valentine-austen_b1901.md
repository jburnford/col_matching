<!-- {"case_id": "case_ottaway_valentine-austen_b1901", "bio_ids": ["ottaway_valentine-austen_b1901"], "stint_ids": ["Ottoway, V. A___Kenya___1937"]} -->
# Dossier case_ottaway_valentine-austen_b1901

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `ottaway_valentine-austen_b1901`

- Printed name: **OTTAWAY, Valentine Austen**
- Birth year: 1901 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L35060.v` — printed in editions [1948, 1949, 1950, 1951]:**

> OTTAWAY, Valentine Austen.—b. 1901; ed. City of London Sch. and Merton Coll., Oxford, M.A. (hons.) (Oxon) ; asst. mstr., Ken., 1930; senr. educ. offr., 1943.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1930 | asst. mstr. | Kenya | [1948, 1949, 1950, 1951] |
| 1 | 1943 | senr. educ. offr | Kenya *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Ottoway, V. A___Kenya___1937`

- Staff-list name: **Ottoway, V. A** | colony: **Kenya** | listed 1937–1940 | editions [1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1937 | V. A. Ottoway | Education Officer—African Education | Education | — | — |
| 1939 | V. A. Ottoway | Education Officer, African Education | Education | — | — |
| 1940 | V. A. Ottoway | Education Officers—African Education | Education | — | — |

### Deterministic checks: `ottaway_valentine-austen_b1901` vs `Ottoway, V. A___Kenya___1937`

- [PASS] surname_gate: bio 'OTTAWAY' vs stint 'Ottoway, V. A' (fuzzy:1)
- [PASS] initials: bio ['V', 'A'] ~ stint ['V', 'A']
- [PASS] age_gate: stint starts 1937, birth 1901 (age 36)
- [PASS] colony: 2 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1937-1940
- [FAIL] position_sim: best 29 vs bar 60: 'asst. mstr.' ~ 'Education Officers—African Education'
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

