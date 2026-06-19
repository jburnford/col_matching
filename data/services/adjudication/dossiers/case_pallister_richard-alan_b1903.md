<!-- {"case_id": "case_pallister_richard-alan_b1903", "bio_ids": ["pallister_richard-alan_b1903"], "stint_ids": ["Pallister, R. A___Straits Settlements___1931"]} -->
# Dossier case_pallister_richard-alan_b1903

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `pallister_richard-alan_b1903`

- Printed name: **PALLISTER, RICHARD ALAN**
- Birth year: 1903 (attested in editions [1956, 1957])
- Honours: M.D, M.R.C.P, O.B.E (1946)
- Appears in editions: [1939, 1940, 1956, 1957]

### Verbatim printed entry text (OCR)

**Version `col1956-L23379.v` — printed in editions [1956, 1957]:**

> PALLISTER, R. A., O.B.E. (1946).—b. 1903; ed. Rutherford Coll., Newcastle, and Durham Univ.; interned, 1942-45; M.O., F.M.S., 1927; Penang, 1938; physician, S'pore, 1946; Johore, 1947; Penang, 1948; specialist physician, Fed. of Mal., 1950.

**Version `col1939-L69585.v` — printed in editions [1939, 1940]:**

> PALLISTER, RICHARD ALAN, M.D., B.S. (Durham), M.R.C.P., D.T.M. & H. (Lond.)—B. 1903; ed. Rutherford Coll., Univ. of Durham Coll. of Med.; M.O., Malaya, Aug., 1927; asst. prof. of med., Coll. of Med., S'pore, Sept., 1935; ag. assoc., do., June, 1937; ag. prof. of med., July, 1937.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | M.O. | Federated Malay States | [1939, 1940, 1956, 1957] |
| 1 | 1935 | asst. prof. of med., Coll. of Med., S'pore | Malaya *(inherited from previous clause)* | [1939, 1940] |
| 2 | 1937 | ag. assoc. | Dominions Office | [1939, 1940] |
| 3 | 1938 | Penang | Federated Malay States *(inherited from previous clause)* | [1956, 1957] |
| 4 | 1942–1945 | interned | — | [1956, 1957] |
| 5 | 1946 | physician, S'pore | Federated Malay States *(inherited from previous clause)* | [1956, 1957] |
| 6 | 1947 | physician, S'pore | Johore | [1956, 1957] |
| 7 | 1948 | Penang | Johore *(inherited from previous clause)* | [1956, 1957] |
| 8 | 1950 | specialist physician, Fed. of Mal | Johore *(inherited from previous clause)* | [1956, 1957] |

## Candidate stint `Pallister, R. A___Straits Settlements___1931`

- Staff-list name: **Pallister, R. A** | colony: **Straits Settlements** | listed 1931–1936 | editions [1931, 1932, 1933, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | R. A. Pallister | Medical Officer | Medical | — | — |
| 1932 | R. A. Pallister | Medical Officer | Medical | — | — |
| 1933 | R. A. Pallister | Medical Officer | Medical | — | — |
| 1936 | R. A. Pallister | Medical and Health Officer | Medical | — | — |

### Deterministic checks: `pallister_richard-alan_b1903` vs `Pallister, R. A___Straits Settlements___1931`

- [PASS] surname_gate: bio 'PALLISTER' vs stint 'Pallister, R. A' (exact)
- [PASS] initials: bio ['R', 'A'] ~ stint ['R', 'A']
- [PASS] age_gate: stint starts 1931, birth 1903 (age 28)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1936
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

