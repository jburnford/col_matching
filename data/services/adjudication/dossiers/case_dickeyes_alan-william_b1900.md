<!-- {"case_id": "case_dickeyes_alan-william_b1900", "bio_ids": ["dickeyes_alan-william_b1900"], "stint_ids": ["Dickens, A. W___Western Pacific___1930"]} -->
# Dossier case_dickeyes_alan-william_b1900

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `dickeyes_alan-william_b1900`

- Printed name: **DICKEYES, Alan William**
- Birth year: 1900 (attested in editions [1948])
- Appears in editions: [1948]

### Verbatim printed entry text (OCR)

**Version `col1948-L32234.v` — printed in editions [1948]:**

> DICKEYES, Alan William.—b. 1900; ed. City of London Sch.; on mil. serv. 1941-45, maj.; clk., Br. Sol. Is. Prot., 1925; post-mstr., 1927; 1st clk. and customs offr., treas., 1928; asst. treas. and colictr. of customs, G. & E. Is. Prot., 1939; senr. acctnt., Nig., 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1925 | clk., Br. Sol. Is. Prot | — | [1948] |
| 1 | 1927 | post-mstr | — | [1948] |
| 2 | 1928 | 1st clk. and customs offr., treas | — | [1948] |
| 3 | 1939 | asst. treas. and colictr. of customs, G. & E. Is. Prot | — | [1948] |
| 4 | 1946 | senr. acctnt. | Nigeria | [1948] |

## Candidate stint `Dickens, A. W___Western Pacific___1930`

- Staff-list name: **Dickens, A. W** | colony: **Western Pacific** | listed 1930–1939 | editions [1930, 1933, 1936, 1937, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1930 | A. W. Dickens | First Clerk, and Boarding Officer | Civil Establishment | — | — |
| 1930 | A. W. Dickens | First Clerk and Boarding Officer | General | — | — |
| 1933 | A. W. Dickens | First Clerk and Boarding Officer | Treasury, Customs and Postal Department | — | — |
| 1936 | A. W. Dickens | First Clerk and Boarding Officer | Treasury, Customs and Postal Department | — | — |
| 1937 | A. W. Dickens | First Clerk and Boarding Officer | Treasury, Customs and Postal Department | — | — |
| 1939 | A. W. Dickens | First Clerk and Boarding Officer | Treasury, Customs and Postal Department | — | — |

### Deterministic checks: `dickeyes_alan-william_b1900` vs `Dickens, A. W___Western Pacific___1930`

- [PASS] surname_gate: bio 'DICKEYES' vs stint 'Dickens, A. W' (fuzzy:2)
- [PASS] initials: bio ['A', 'W'] ~ stint ['A', 'W']
- [PASS] age_gate: stint starts 1930, birth 1900 (age 30)
- [FAIL] colony: no placed event resolves to 'Western Pacific'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1930-1939
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

