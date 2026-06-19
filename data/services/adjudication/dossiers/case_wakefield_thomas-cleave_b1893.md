<!-- {"case_id": "case_wakefield_thomas-cleave_b1893", "bio_ids": ["wakefield_thomas-cleave_b1893"], "stint_ids": ["Wakefield, T. C___Straits Settlements___1931"]} -->
# Dossier case_wakefield_thomas-cleave_b1893

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `wakefield_thomas-cleave_b1893`

- Printed name: **WAKEFIELD, THOMAS CLEAVE**
- Birth year: 1893 (attested in editions [1939, 1940])
- Honours: L.M, M.B
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L71488.v` — printed in editions [1939, 1940]:**

> WAKEFIELD, THOMAS CLEAVE, M.B., Ch.B. (Edin.), L.M., Rotunda Hosp., Dublin, grad., London S.T.M. (with distinc.).—B. 1893; med. offr., F.M.S., Aug., 1926; med. offr., European hosps., K. Lumpur, Feb., 1929; med. offr. in ch., Tan Toek Seng Hosp., S'pore, Oct., 1935; med. offr., Batu Gajah, Feb., 1936.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | med. offr. | Federated Malay States | [1939, 1940] |
| 1 | 1929 | med. offr., European hosps., K. Lumpur | Federated Malay States *(inherited from previous clause)* | [1939, 1940] |
| 2 | 1935 | med. offr. in ch., Tan Toek Seng Hosp., S'pore | Federated Malay States *(inherited from previous clause)* | [1939, 1940] |
| 3 | 1936 | med. offr., Batu Gajah | Federated Malay States *(inherited from previous clause)* | [1939, 1940] |

## Candidate stint `Wakefield, T. C___Straits Settlements___1931`

- Staff-list name: **Wakefield, T. C** | colony: **Straits Settlements** | listed 1931–1936 | editions [1931, 1932, 1933, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | T. C. Wakefield | Medical Officer | Medical | — | — |
| 1932 | T. C. Wakefield | Medical Officer | Medical | — | — |
| 1933 | T. C. Wakefield | Medical Officer | Medical | — | — |
| 1936 | T. C. Wakefield | Medical and Health Officer | Medical | — | — |

### Deterministic checks: `wakefield_thomas-cleave_b1893` vs `Wakefield, T. C___Straits Settlements___1931`

- [PASS] surname_gate: bio 'WAKEFIELD' vs stint 'Wakefield, T. C' (exact)
- [PASS] initials: bio ['T', 'C'] ~ stint ['T', 'C']
- [PASS] age_gate: stint starts 1931, birth 1893 (age 38)
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

