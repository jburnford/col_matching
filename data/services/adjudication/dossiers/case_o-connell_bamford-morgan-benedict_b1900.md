<!-- {"case_id": "case_o-connell_bamford-morgan-benedict_b1900", "bio_ids": ["o-connell_bamford-morgan-benedict_b1900"], "stint_ids": ["O'Connell, M___Cyprus___1920"]} -->
# Dossier case_o-connell_bamford-morgan-benedict_b1900

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `o-connell_bamford-morgan-benedict_b1900`

- Printed name: **O'CONNELL, BAMFORD MORGAN BENEDICT**
- Birth year: 1900 (attested in editions [1939, 1940])
- Honours: R.N.C
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L69500.v` — printed in editions [1939, 1940]:**

> O'CONNELL, BAMFORD MORGAN BENEDICT, LIEUT. R.N. (Ret.), R.N.C.—B. 1900; ed. Corpus Christi Coll., Cambridge; pol. prob., F.M.S., Dec., 1920; crim. regtay., S.S. & F.M.S., ag. ast. commr., pol., Jan., 1923; ast. commr., pol., F.M.S., May, 1925; adjt., fedl. headqrs., Sept., 1930; dep. commr., pol., F.M.S., Oct., 1935; ag. commr., pol. and aliens immigrn. offr., Kedah, Feb., 1936; ch. pol. offr., Penang, Dec., 1938.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920 | pol. prob. | Federated Malay States | [1939, 1940] |
| 1 | 1923 | crim. regtay., S.S. & F.M.S., ag. ast. commr., pol | Federated Malay States *(inherited from previous clause)* | [1939, 1940] |
| 2 | 1925 | ast. commr., pol. | Federated Malay States | [1939, 1940] |
| 3 | 1930 | adjt., fedl. headqrs | Federated Malay States *(inherited from previous clause)* | [1939, 1940] |
| 4 | 1935 | dep. commr., pol. | Federated Malay States | [1939, 1940] |
| 5 | 1936 | ag. commr., pol. and aliens immigrn. offr. | Kedah | [1939, 1940] |
| 6 | 1938 | ch. pol. offr., Penang | Kedah *(inherited from previous clause)* | [1939, 1940] |

## Candidate stint `O'Connell, M___Cyprus___1920`

- Staff-list name: **O'Connell, M** | colony: **Cyprus** | listed 1920–1922 | editions [1920, 1921, 1922]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1920 | Miss M. O'Connell | Nursing Sister | Medical Department | — | — |
| 1921 | Miss M. O'Connell | Nursing Sister, Central Hospital | Medical Department | — | — |
| 1922 | M. O'Connell | Nursing Sister, Central Hospital | Medical Department | — | — |

### Deterministic checks: `o-connell_bamford-morgan-benedict_b1900` vs `O'Connell, M___Cyprus___1920`

- [PASS] surname_gate: bio 'O'CONNELL' vs stint 'O'Connell, M' (exact)
- [PASS] initials: bio ['B', 'M', 'B'] ~ stint ['M']
- [PASS] age_gate: stint starts 1920, birth 1900 (age 20)
- [FAIL] colony: no placed event resolves to 'Cyprus'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1920-1922
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

