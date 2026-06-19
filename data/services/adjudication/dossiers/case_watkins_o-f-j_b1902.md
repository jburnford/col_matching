<!-- {"case_id": "case_watkins_o-f-j_b1902", "bio_ids": ["watkins_o-f-j_b1902", "watkins_o-f_e1908"], "stint_ids": ["Watkins, O. F___Kenya___1925"]} -->
# Dossier case_watkins_o-f-j_b1902

## Case context

- 2 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 25 official(s) with this surname in the graph's staff lists; 11 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- CONTESTED: stint(s) ['Watkins, O. F___Kenya___1925'] have more than one claimant biography in this case.
- NOTE: stint `Watkins, O. F___Kenya___1925` is also gate-compatible with biography(ies) outside this case: ['watkins_oscar-ferris_e1899'] (already linked elsewhere or filtered).
- NOTE: stint `Watkins, O. F___Kenya___1925` is also gate-compatible with biography(ies) outside this case: ['watkins_oscar-ferris_e1899'] (already linked elsewhere or filtered).

## Biography `watkins_o-f-j_b1902`

- Printed name: **WATKINS, O. F. J**
- Birth year: 1902 (attested in editions [1956, 1957])
- Appears in editions: [1956, 1957]

### Verbatim printed entry text (OCR)

**Version `col1956-L24870.v` — printed in editions [1956, 1957]:**

> WATKINS, O. F. J.—b. 1902; ed. Ellesmere Coll.; mil. serv., 1941-45; asst. signals and tel. engrnr., F.M.S., 1928; engrnr., posts and tels., 1933; asst. contrlr., telecoms., 1940; contrlr., telecoms., 1946; dir., telecoms., Fed. of Mal., 1951.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | asst. signals and tel. engrnr. | Federated Malay States | [1956, 1957] |
| 1 | 1933 | engrnr., posts and tels | Federated Malay States *(inherited from previous clause)* | [1956, 1957] |
| 2 | 1940 | asst. contrlr., telecoms | Federated Malay States *(inherited from previous clause)* | [1956, 1957] |
| 3 | 1946 | contrlr., telecoms | Federated Malay States *(inherited from previous clause)* | [1956, 1957] |
| 4 | 1951 | dir., telecoms., Fed. of Mal | Federated Malay States *(inherited from previous clause)* | [1956, 1957] |

## Biography `watkins_o-f_e1908`

- Printed name: **WATKINS, O. F**
- Birth year: not printed
- Appears in editions: [1910, 1911]

### Verbatim printed entry text (OCR)

**Version `col1910-L49353.v` — printed in editions [1910, 1911]:**

> WATKINS, O. F.—Asst. dist. comsnr., E.A.P., 16th Jan., 1908.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1908 | Asst. dist. comsnr. | East Africa Protectorate | [1910, 1911] |

## Candidate stint `Watkins, O. F___Kenya___1925`

- Staff-list name: **Watkins, O. F** | colony: **Kenya** | listed 1925–1930 | editions [1925, 1927, 1928, 1930]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | O. F. Watkins | Deputy Chief Native Commissioner | Native Affairs Department | D.S.O. | Lt.-Col. |
| 1927 | O. F. Watkins | Deputy Chief Native Commissioner | Native Affairs Department | D.S.O. | Lt.-Col. |
| 1928 | O. F. Watkins | Deputy Chief Native Commissioner | Native Affairs Department | D.S.O. | — |
| 1930 | Lieut.-Col. O. F. Watkins | Senior Commissioner, 1st Class | Provincial Administration | C.B.E., D.S.O. | Lieut.-Col. |

### Deterministic checks: `watkins_o-f-j_b1902` vs `Watkins, O. F___Kenya___1925`

- [PASS] surname_gate: bio 'WATKINS' vs stint 'Watkins, O. F' (exact)
- [PASS] initials: bio ['O', 'F', 'J'] ~ stint ['O', 'F']
- [PASS] age_gate: stint starts 1925, birth 1902 (age 23)
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1925-1930
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

### Deterministic checks: `watkins_o-f_e1908` vs `Watkins, O. F___Kenya___1925`

- [PASS] surname_gate: bio 'WATKINS' vs stint 'Watkins, O. F' (exact)
- [PASS] initials: bio ['O', 'F'] ~ stint ['O', 'F']
- [PASS] age_gate: stint starts 1925; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1925-1930
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

