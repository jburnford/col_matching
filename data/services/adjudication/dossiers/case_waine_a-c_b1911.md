<!-- {"case_id": "case_waine_a-c_b1911", "bio_ids": ["waine_a-c_b1911"], "stint_ids": ["Waine, A. C___Sarawak___1949"]} -->
# Dossier case_waine_a-c_b1911

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `waine_a-c_b1911`

- Printed name: **WAINE, A. C**
- Birth year: 1911 (attested in editions [1956, 1957, 1958, 1959, 1961, 1962, 1963, 1964])
- Honours: M.B.E
- Appears in editions: [1956, 1957, 1958, 1959, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1956-L24772.v` — printed in editions [1956, 1957, 1958, 1959, 1961, 1962, 1963, 1964]:**

> WAINE, A. C., M.B.E.—b. 1911; mil. serv., 1939–46, maj.; cadet, S'wak., 1946; secon., Ken., 1953; asst. sec. and ag. sec. for local govt., health and housing, 1954; senr. asst. sec., 1954; under sec., min. of local govt., health and housing, 1957.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | cadet, S'wak | — | [1956, 1957, 1958, 1959, 1961, 1962, 1963, 1964] |
| 1 | 1953 | secon. | Kenya | [1956, 1957, 1958, 1959, 1961, 1962, 1963, 1964] |
| 2 | 1954 | asst. sec. and ag. sec. for local govt., health and housing | Kenya *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1961, 1962, 1963, 1964] |
| 3 | 1957 | under sec., min. of local govt., health and housing | Kenya *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1961, 1962, 1963, 1964] |

## Candidate stint `Waine, A. C___Sarawak___1949`

- Staff-list name: **Waine, A. C** | colony: **Sarawak** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | A. C. Waine | District Officer / Assistant District Officer / Cadet | Administrative Service | — | — |
| 1951 | A. C. Waine | District Officers, Assistant District Officers and Cadets | Administrative Service | — | — |

### Deterministic checks: `waine_a-c_b1911` vs `Waine, A. C___Sarawak___1949`

- [PASS] surname_gate: bio 'WAINE' vs stint 'Waine, A. C' (exact)
- [PASS] initials: bio ['A', 'C'] ~ stint ['A', 'C']
- [PASS] age_gate: stint starts 1949, birth 1911 (age 38)
- [FAIL] colony: no placed event resolves to 'Sarawak'
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

