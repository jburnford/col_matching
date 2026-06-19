<!-- {"case_id": "case_hughes_n_b1910", "bio_ids": ["hughes_n_b1910"], "stint_ids": ["Hughes, N. E___North Borneo___1930"]} -->
# Dossier case_hughes_n_b1910

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 122 official(s) with this surname in the graph's staff lists; 39 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['hughes_n_b1910'] carry a single initial only — the namesake trap applies.

## Biography `hughes_n_b1910`

- Printed name: **HUGHES, N**
- Birth year: 1910 (attested in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964])
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1957-L24290.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]:**

> HUGHES, N.—b. 1910; ed. Barlows Sch., Macclesfield, and Stockport Coll.; acctnt., treasy., Nig., 1945; P.W.D., 1945; senr. acctnt., 1949; chief acctnt., 1952; fin. offr., min. of works, N. Nig., 1958. (Nig. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1945 | acctnt., treasy. | Nigeria | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1949 | senr. acctnt | Nigeria *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 2 | 1952 | chief acctnt | Nigeria *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 3 | 1958 | fin. offr., min. of works | Northern Nigeria | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |

## Candidate stint `Hughes, N. E___North Borneo___1930`

- Staff-list name: **Hughes, N. E** | colony: **North Borneo** | listed 1930–1932 | editions [1930, 1932]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1930 | N. E. Hughes | Cadet | Civil Establishment | — | — |
| 1932 | N. E. Hughes | Cadet | Civil Establishment | — | — |

### Deterministic checks: `hughes_n_b1910` vs `Hughes, N. E___North Borneo___1930`

- [PASS] surname_gate: bio 'HUGHES' vs stint 'Hughes, N. E' (exact)
- [PASS] initials: bio ['N'] ~ stint ['N', 'E']
- [PASS] age_gate: stint starts 1930, birth 1910 (age 20)
- [FAIL] colony: no placed event resolves to 'North Borneo'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1930-1932
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

