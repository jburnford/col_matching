<!-- {"case_id": "case_lempierie_victor-frederick_b1899", "bio_ids": ["lempierie_victor-frederick_b1899"], "stint_ids": ["Lempiere, V. F___Mauritius___1931"]} -->
# Dossier case_lempierie_victor-frederick_b1899

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `lempierie_victor-frederick_b1899`

- Printed name: **LEMPIERIE, Victor Frederick**
- Birth year: 1899 (attested in editions [1948])
- Appears in editions: [1948, 1949]

### Verbatim printed entry text (OCR)

**Version `col1948-L33994.v` — printed in editions [1948]:**

> LEMPIERIE, Victor Frederick.—b. 1899; ed. Victoria Coll., Jersey, Exeter Coll., Oxford, B.A. (hons. Oxon.); mstr., Royal Coll., Maur., 1927.

**Version `col1949-L33599.v` — printed in editions [1949]:**

> LEMPRIERE, Victor Frederick.—b. 1899; ed. Victoria Coll., Jersey, and Exeter Coll., Oxford, B.A. (hons. Oxon.); mstr., Royal Coll., Maur., 1927.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | mstr., Royal Coll. | Mauritius | [1948, 1949] |

## Candidate stint `Lempiere, V. F___Mauritius___1931`

- Staff-list name: **Lempiere, V. F** | colony: **Mauritius** | listed 1931–1939 | editions [1931, 1936, 1937, 1939]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | V. F. Lempiere | Masters | Education | — | — |
| 1936 | V. F. Lempiere | Teacher | Education | — | — |
| 1937 | V. F. Lempiere | Masters | Education | — | — |
| 1939 | V. F. Lempiere | Masters | Education | — | — |

### Deterministic checks: `lempierie_victor-frederick_b1899` vs `Lempiere, V. F___Mauritius___1931`

- [PASS] surname_gate: bio 'LEMPIERIE' vs stint 'Lempiere, V. F' (fuzzy:1)
- [PASS] initials: bio ['V', 'F'] ~ stint ['V', 'F']
- [PASS] age_gate: stint starts 1931, birth 1899 (age 32)
- [PASS] colony: 1 placed event(s) resolve to 'Mauritius'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1931-1939
- [FAIL] position_sim: best 36 vs bar 60: 'mstr., Royal Coll.' ~ 'Masters'
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

