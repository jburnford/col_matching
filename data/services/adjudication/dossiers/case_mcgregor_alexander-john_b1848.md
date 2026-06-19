<!-- {"case_id": "case_mcgregor_alexander-john_b1848", "bio_ids": ["mcgregor_alexander-john_b1848"], "stint_ids": ["McGregor, A. J___South Africa___1914"]} -->
# Dossier case_mcgregor_alexander-john_b1848

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 29 official(s) with this surname in the graph's staff lists; 16 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mcgregor_alexander-john_b1848`

- Printed name: **MCGREGOR, ALEXANDER JOHN**
- Birth year: 1848 (attested in editions [1921, 1922, 1923, 1927])
- Appears in editions: [1921, 1922, 1923, 1927]

### Verbatim printed entry text (OCR)

**Version `col1921-L58168.v` — printed in editions [1921, 1922, 1923, 1927]:**

> MCGREGOR, ALEXANDER JOHN, B.A. (Cape).—B. 1848; ed., Oriel Coll., Oxford; 1st cls. hons., mod. hist.; called to the bar (Inner Temple), 1889; admitted to Cape sup. ct. bar, 1882; puisne judge, Eastern dist. local divn., Grahamstown, 1st Aug., 1913; puisne judge, O.F.S. prov. divn., 15th July, 1915.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1882 | admitted to Cape sup. ct. bar | — | [1921, 1922, 1923, 1927] |
| 1 | 1889 | called to the bar (Inner Temple) | — | [1921, 1922, 1923, 1927] |
| 2 | 1913 | puisne judge, Eastern dist. local divn., Grahamstown | — | [1921, 1922, 1923, 1927] |
| 3 | 1915 | puisne judge, O.F.S. prov. divn | Orange Free State | [1921, 1922, 1923, 1927] |

## Candidate stint `McGregor, A. J___South Africa___1914`

- Staff-list name: **McGregor, A. J** | colony: **South Africa** | listed 1914–1918 | editions [1914, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1914 | A. J. McGregor | Puise Judge | Eastern Districts Local Division | — | — |
| 1918 | A. J. McGregor | Puisne Judges | Orange Free State Provincial Division | — | — |

### Deterministic checks: `mcgregor_alexander-john_b1848` vs `McGregor, A. J___South Africa___1914`

- [PASS] surname_gate: bio 'MCGREGOR' vs stint 'McGregor, A. J' (exact)
- [PASS] initials: bio ['A', 'J'] ~ stint ['A', 'J']
- [PASS] age_gate: stint starts 1914, birth 1848 (age 66)
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1914-1918
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

