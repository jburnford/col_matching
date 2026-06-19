<!-- {"case_id": "case_bristow_g-w_b1903", "bio_ids": ["bristow_g-w_b1903"], "stint_ids": ["Bristow, G___Western Pacific___1951"]} -->
# Dossier case_bristow_g-w_b1903

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 6 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `bristow_g-w_b1903`

- Printed name: **BRISTOW, G. W**
- Birth year: 1903 (attested in editions [1957])
- Appears in editions: [1957]

### Verbatim printed entry text (OCR)

**Version `col1957-L21430.v` — printed in editions [1957]:**

> BRISTOW, G. W.—b. 1903; ed. Christ's Hosp. and London Univ.; mil. serv., 1942-45; prob. engrn., F.M.S., 1929; engrn., posts and tels., 1931; asst. contrlr., telecoms., 1941; contrlr., gr. II, 1949; gr. I, 1953.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1929 | prob. engrn. | Federated Malay States | [1957] |
| 1 | 1931 | engrn., posts and tels | Federated Malay States *(inherited from previous clause)* | [1957] |
| 2 | 1941 | asst. contrlr., telecoms | Federated Malay States *(inherited from previous clause)* | [1957] |
| 3 | 1949 | contrlr., gr. II | Federated Malay States *(inherited from previous clause)* | [1957] |
| 4 | 1953 | gr. I | Federated Malay States *(inherited from previous clause)* | [1957] |

## Candidate stint `Bristow, G___Western Pacific___1951`

- Staff-list name: **Bristow, G** | colony: **Western Pacific** | listed 1951–1966 | editions [1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1951 | G. Bristow | Cadet Officers | District Administration | — | — |
| 1953 | G. Bristow | Administration Officer | British National Administration | — | — |
| 1954 | G. Bristow | Administration Officer | British National Administration | — | — |
| 1955 | G. Bristow | Administration Officer | British National Administration | — | — |
| 1956 | G. Bristow | Administration Officer | British National Administration | — | — |
| 1957 | G. Bristow | Administration Officer | British National Administration | — | — |
| 1958 | G. Bristow | Administrative Officers | Civil Establishment | — | — |
| 1959 | G. Bristow | Administrative Officer – Class B | Civil Establishment | — | — |
| 1960 | G. Bristow | Administrative Officer | Civil Establishment | — | — |
| 1961 | G. Bristow | Administrative Officer – Class B | Civil Establishment | — | — |
| 1962 | G. Bristow | Administrative Officer (Class B) | Civil Establishment | — | — |
| 1964 | G. Bristow | Administrative Officer | Civil Establishment | — | — |
| 1965 | G. Bristow | Administrative Officer | Civil Establishment | — | — |
| 1966 | G. Bristow | Clerk | Executive Council | — | — |

### Deterministic checks: `bristow_g-w_b1903` vs `Bristow, G___Western Pacific___1951`

- [PASS] surname_gate: bio 'BRISTOW' vs stint 'Bristow, G' (exact)
- [PASS] initials: bio ['G', 'W'] ~ stint ['G']
- [PASS] age_gate: stint starts 1951, birth 1903 (age 48)
- [FAIL] colony: no placed event resolves to 'Western Pacific'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1951-1966
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

