<!-- {"case_id": "case_lyons_trevor-lennox_b1893", "bio_ids": ["lyons_trevor-lennox_b1893"], "stint_ids": ["Lyons, T. L___Jamaica___1937", "Lyons, T. L___Jamaica___1949"]} -->
# Dossier case_lyons_trevor-lennox_b1893

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 24 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `lyons_trevor-lennox_b1893`

- Printed name: **LYONS, Trevor Lennox**
- Birth year: 1893 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L34197.v` — printed in editions [1948, 1949, 1950, 1951]:**

> LYONS, Trevor Lennox.—b. 1893; ed. Jamaica Coll.; solr., sup. ct., J'ca., 1915; registr., sup. ct., 1933; edited rules and orders of the sup. ct., 1938 and mat. causes in J'ca., 1940.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1915 | solr., sup. ct. | Jamaica | [1948, 1949, 1950, 1951] |
| 1 | 1933 | registr., sup. ct. | — | [1948, 1949, 1950, 1951] |
| 2 | 1938 | — | — | [1948, 1949, 1950, 1951] |
| 3 | 1940 | — | Jamaica | [1948, 1949, 1950, 1951] |

## Candidate stint `Lyons, T. L___Jamaica___1937`

- Staff-list name: **Lyons, T. L** | colony: **Jamaica** | listed 1937–1940 | editions [1937, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1937 | T. L. Lyons | Registrar and Librarian of the Supreme Court of Judicature | Judicial and Legal | — | — |
| 1940 | T. L. Lyons | Registrar and Librarian of the Supreme Court of Judicature | Judicial and Legal | — | — |

### Deterministic checks: `lyons_trevor-lennox_b1893` vs `Lyons, T. L___Jamaica___1937`

- [PASS] surname_gate: bio 'LYONS' vs stint 'Lyons, T. L' (exact)
- [PASS] initials: bio ['T', 'L'] ~ stint ['T', 'L']
- [PASS] age_gate: stint starts 1937, birth 1893 (age 44)
- [PASS] colony: 2 placed event(s) resolve to 'Jamaica'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1937-1940
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Lyons, T. L___Jamaica___1949`

- Staff-list name: **Lyons, T. L** | colony: **Jamaica** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | T. L. Lyons | Registrar | JUDICIAL | — | — |
| 1950 | T. L. Lyons | Registrar | JUDICIAL | — | — |

### Deterministic checks: `lyons_trevor-lennox_b1893` vs `Lyons, T. L___Jamaica___1949`

- [PASS] surname_gate: bio 'LYONS' vs stint 'Lyons, T. L' (exact)
- [PASS] initials: bio ['T', 'L'] ~ stint ['T', 'L']
- [PASS] age_gate: stint starts 1949, birth 1893 (age 56)
- [PASS] colony: 2 placed event(s) resolve to 'Jamaica'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1950
- [FAIL] position_sim: no overlapping placed event to compare
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

