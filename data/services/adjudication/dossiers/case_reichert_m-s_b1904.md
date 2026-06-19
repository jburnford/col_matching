<!-- {"case_id": "case_reichert_m-s_b1904", "bio_ids": ["reichert_m-s_b1904"], "stint_ids": ["Reichert, M. S___High Commission Territories___1959"]} -->
# Dossier case_reichert_m-s_b1904

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `reichert_m-s_b1904`

- Printed name: **REICHERT, M. S**
- Birth year: 1904 (attested in editions [1958, 1959, 1960, 1961, 1962])
- Honours: M.B.E (1959)
- Appears in editions: [1958, 1959, 1960, 1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1958-L26319.v` — printed in editions [1958, 1959, 1960, 1961, 1962]:**

> REICHERT, M. S., M.B.E. (1959)—b. 1904; ed. Vet. Medicine Academy, Poland, and Edin. Univ.; mil. serv., Polish Army, capt.; vet. offr., Bech. Prot., 1947; senr. vet. offr., 1957; D.D.V.S., 1957-61.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1947 | vet. offr. | Bechuanaland | [1958, 1959, 1960, 1961, 1962] |
| 1 | 1957 | senr. vet. offr | Bechuanaland *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962] |

## Candidate stint `Reichert, M. S___High Commission Territories___1959`

- Staff-list name: **Reichert, M. S** | colony: **High Commission Territories** | listed 1959–1960 | editions [1959, 1960]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1959 | M. S. Reichert | Deputy Director, Veterinary Services | BECHUANALAND PROTECTORATE | M.B.E. | — |
| 1960 | M. S. Reichert | Deputy Director, Veterinary Services | BECHUANALAND PROTECTORATE | M.B.E. | — |

### Deterministic checks: `reichert_m-s_b1904` vs `Reichert, M. S___High Commission Territories___1959`

- [PASS] surname_gate: bio 'REICHERT' vs stint 'Reichert, M. S' (exact)
- [PASS] initials: bio ['M', 'S'] ~ stint ['M', 'S']
- [PASS] age_gate: stint starts 1959, birth 1904 (age 55)
- [FAIL] colony: no placed event resolves to 'High Commission Territories'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1959-1960
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: M.B.E
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

