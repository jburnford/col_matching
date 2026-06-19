<!-- {"case_id": "case_subrahmanyan_chinniah_b1899", "bio_ids": ["subrahmanyan_chinniah_b1899"], "stint_ids": ["Subrahmanyam, C___Singapore___1949"]} -->
# Dossier case_subrahmanyan_chinniah_b1899

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['subrahmanyan_chinniah_b1899'] carry a single initial only — the namesake trap applies.

## Biography `subrahmanyan_chinniah_b1899`

- Printed name: **SUBRAHMANYAN, Chinniah**
- Birth year: 1899 (attested in editions [1951])
- Honours: L.M.S
- Appears in editions: [1951]

### Verbatim printed entry text (OCR)

**Version `col1951-L42912.v` — printed in editions [1951]:**

> SUBRAHMANYAN, Chinniah, L.M.S., S'pore.—b. 1899; ed. King Edward VII Coll. of Med., S'pore.; asst. in pathology, S'pore., 1923; asst. surg., S.S., 1924; asst. pathologist, 1930; gr. II, 1937; med. offr., Mal., med. serv., 1939; senr. pathologist, S'pore., 1949.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1923 | asst. in pathology, S'pore | — | [1951] |
| 1 | 1924 | asst. surg. | Straits Settlements | [1951] |
| 2 | 1930 | asst. pathologist | Straits Settlements *(inherited from previous clause)* | [1951] |
| 3 | 1937 | gr. II | Straits Settlements *(inherited from previous clause)* | [1951] |
| 4 | 1939 | med. offr., Mal., med. serv | Straits Settlements *(inherited from previous clause)* | [1951] |
| 5 | 1949 | senr. pathologist, S'pore | Straits Settlements *(inherited from previous clause)* | [1951] |

## Candidate stint `Subrahmanyam, C___Singapore___1949`

- Staff-list name: **Subrahmanyam, C** | colony: **Singapore** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | Dr. C. Subrahmanyam | Assistant Pathologists | Pathological Branch | — | — |
| 1951 | C. Subrahmanyam | Senior Pathologist | Pathological Branch | — | — |

### Deterministic checks: `subrahmanyan_chinniah_b1899` vs `Subrahmanyam, C___Singapore___1949`

- [PASS] surname_gate: bio 'SUBRAHMANYAN' vs stint 'Subrahmanyam, C' (fuzzy:1)
- [PASS] initials: bio ['C'] ~ stint ['C']
- [PASS] age_gate: stint starts 1949, birth 1899 (age 50)
- [FAIL] colony: no placed event resolves to 'Singapore'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
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

