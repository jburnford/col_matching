<!-- {"case_id": "case_mcgregor_frank_b1883", "bio_ids": ["mcgregor_frank_b1883"], "stint_ids": ["McGregor, F___Northern Rhodesia___1925"]} -->
# Dossier case_mcgregor_frank_b1883

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 29 official(s) with this surname in the graph's staff lists; 16 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['mcgregor_frank_b1883'] carry a single initial only — the namesake trap applies.

## Biography `mcgregor_frank_b1883`

- Printed name: **McGREGOR, FRANK**
- Birth year: 1883 (attested in editions [1937, 1939])
- Appears in editions: [1937, 1939]

### Verbatim printed entry text (OCR)

**Version `col1937-L62887.v` — printed in editions [1937, 1939]:**

> McGREGOR, FRANK.—B. 1883; mines dept., Transvaal, July, 1902; astt. censor, dept. of defence, Johannesburg, 1914; transfd. to dept. of lab., 1924; chmn., workmen's compensation commn., 1930 and 1932; chmn., wage bd., Jan., 1936.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1902 | mines dept. | Transvaal | [1937, 1939] |
| 1 | 1914 | astt. censor, dept. of defence | Johannesburg | [1937, 1939] |
| 2 | 1924 | transfd. to dept. of lab. | — | [1937, 1939] |
| 3 | 1930–1932 | chmn., workmen's compensation commn. | — | [1937, 1939] |
| 4 | 1936 | chmn., wage bd. | — | [1937, 1939] |

## Candidate stint `McGregor, F___Northern Rhodesia___1925`

- Staff-list name: **McGregor, F** | colony: **Northern Rhodesia** | listed 1925–1931 | editions [1925, 1927, 1929, 1931]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | F. McGregor | Teacher | Education | — | — |
| 1927 | Mrs. F. McGregor | Teacher | Education | — | — |
| 1929 | Mrs. F. McGregor | Mistresses | European Education | — | — |
| 1931 | Mrs. F. McGregor | Missesses | European Education | — | — |

### Deterministic checks: `mcgregor_frank_b1883` vs `McGregor, F___Northern Rhodesia___1925`

- [PASS] surname_gate: bio 'McGREGOR' vs stint 'McGregor, F' (exact)
- [PASS] initials: bio ['F'] ~ stint ['F']
- [PASS] age_gate: stint starts 1925, birth 1883 (age 42)
- [FAIL] colony: no placed event resolves to 'Northern Rhodesia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1925-1931
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

