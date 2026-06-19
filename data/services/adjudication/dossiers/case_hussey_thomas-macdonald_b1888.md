<!-- {"case_id": "case_hussey_thomas-macdonald_b1888", "bio_ids": ["hussey_thomas-macdonald_b1888"], "stint_ids": ["Hussey, T. M___Straits Settlements___1921"]} -->
# Dossier case_hussey_thomas-macdonald_b1888

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 14 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hussey_thomas-macdonald_b1888`

- Printed name: **HUSSEY, Thomas Macdonald**
- Birth year: 1888 (attested in editions [1933])
- Appears in editions: [1933, 1934, 1935, 1936, 1937, 1939]

### Verbatim printed entry text (OCR)

**Version `col1933-L60897.v` — printed in editions [1933]:**

> HUSSEY, Thomas Macdonald.—B. 1888; offi. censor, cinematograph films, S.S., F.M.S. and Johore, Dec., 1919.

**Version `dol1935-L59653.v` — printed in editions [1935, 1936, 1937, 1939]:**

> HUSSEY, THOMAS MACDONALD.—B. 1888; ed. Long Ashton Coll., Somerset; offi. censor, cinematograph films, S.S., F.M.S. and Johore, Dec., 1919.

**Version `col1934-L60478.v` — printed in editions [1934]:**

> HUSSBY, THOMAS MACDONALD.—B. 1888; ed. Long Ashton Coll., Somerset; offl. censor, cinematograph films, S.S., F.M.S. and Johore, Dec., 1919.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1919 | offi. censor, cinematograph films, S.S., F.M.S. and Johore | Federated Malay States | [1933, 1934, 1935, 1936, 1937, 1939] |

## Candidate stint `Hussey, T. M___Straits Settlements___1921`

- Staff-list name: **Hussey, T. M** | colony: **Straits Settlements** | listed 1921–1936 | editions [1921, 1922, 1923, 1925, 1931, 1933, 1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1921 | Capt. T. M. Hussey | Official Censor of Cinematograph Films | Police | — | Captain |
| 1922 | T. M. Hussey | Official Censor of Cinematograph Films | Police | — | Captain |
| 1923 | T. M. Hussey | Official Censor of Cinematograph Films | Police | — | Captain |
| 1925 | T. M. Hussey | Official Censor of Cinematograph Films | Police | — | Captain |
| 1931 | T. M. Hussey | Official Censor of Cinematograph Films | Police | — | Captain |
| 1933 | T. M. Hussey | Official Censor of Cinematograph Films | Police | — | Captain |
| 1934 | T. M. Hussey | Official Censor of Cinematograph Films | Police | — | Captain |
| 1936 | T. M. Hussey | Official Censor of Cinematograph Films | Police | — | Captain |

### Deterministic checks: `hussey_thomas-macdonald_b1888` vs `Hussey, T. M___Straits Settlements___1921`

- [PASS] surname_gate: bio 'HUSSEY' vs stint 'Hussey, T. M' (exact)
- [PASS] initials: bio ['T', 'M'] ~ stint ['T', 'M']
- [PASS] age_gate: stint starts 1921, birth 1888 (age 33)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1921-1936
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

