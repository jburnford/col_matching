<!-- {"case_id": "case_denton-thompson_a-g_b1920", "bio_ids": ["denton-thompson_a-g_b1920"], "stint_ids": ["Denton-Thompson, A. G___Falkland Islands___1955"]} -->
# Dossier case_denton-thompson_a-g_b1920

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `denton-thompson_a-g_b1920`

- Printed name: **DENTON-THOMPSON, A. G**
- Birth year: 1920 (attested in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963])
- Honours: O.B.E (1958)
- Appears in editions: [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1956-L20800.v` — printed in editions [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963]:**

> DENTON-THOMPSON, A. G., O.B.E. (1958), M.C.—b. 1920; ed. Malvern; cadet, Basuto., 1944; admin. offr., Tang., 1947; secon. C.O., 1948-50; col. sec., Falklands, 1955; admin. offr., cl. IIB, Tang., 1960; dep. perm. sec., 1960-62.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1944 | cadet | Basutoland | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 1 | 1947 | admin. offr. | Tanganyika | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 2 | 1948–1950 | secon. C.O | Tanganyika *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 3 | 1955 | col. sec., Falklands | Tanganyika *(inherited from previous clause)* | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 4 | 1960 | admin. offr., cl. IIB | Tanganyika | [1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |

## Candidate stint `Denton-Thompson, A. G___Falkland Islands___1955`

- Staff-list name: **Denton-Thompson, A. G** | colony: **Falkland Islands** | listed 1955–1960 | editions [1955, 1956, 1957, 1958, 1959, 1960]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1955 | A. G. Denton-Thompson | Colonial Secretary | Civil Establishment | — | — |
| 1956 | A. G. Denton-Thompson | Colonial Secretary | Civil Establishment | — | — |
| 1957 | A. G. Denton-Thompson | Colonial Secretary | Civil Establishment | — | — |
| 1958 | A. G. Denton-Thompson | Colonial Secretary | Civil Establishment | — | — |
| 1959 | A. G. Denton-Thompson | Colonial Secretary | Civil Establishment | — | — |
| 1960 | A. G. Denton-Thompson | Colonial Secretary | Civil Establishment | — | — |

### Deterministic checks: `denton-thompson_a-g_b1920` vs `Denton-Thompson, A. G___Falkland Islands___1955`

- [PASS] surname_gate: bio 'DENTON-THOMPSON' vs stint 'Denton-Thompson, A. G' (exact)
- [PASS] initials: bio ['A', 'G'] ~ stint ['A', 'G']
- [PASS] age_gate: stint starts 1955, birth 1920 (age 35)
- [FAIL] colony: no placed event resolves to 'Falkland Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1955-1960
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

