<!-- {"case_id": "case_heisch_r-b_b1910", "bio_ids": ["heisch_r-b_b1910"], "stint_ids": ["Hersch, R. B___Kenya___1949"]} -->
# Dossier case_heisch_r-b_b1910

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `heisch_r-b_b1910`

- Printed name: **HEISCH, R. B**
- Birth year: 1910 (attested in editions [1957, 1958, 1959, 1960, 1961])
- Honours: O.B.E (1961)
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]

### Verbatim printed entry text (OCR)

**Version `col1957-L23993.v` — printed in editions [1957, 1958, 1959, 1960, 1961]:**

> HEISCH, R. B., O.B.E. (1961).—b. 1910; ed. Bradfield Coll. and Camb. Univ.; M.O., Ken., 1939; senr. parasitol., 1947; senr. specialist, 1956; pubns. Presence of Intracellular granules in lice infected with S. duttoni (Trans. R. Soc. Trop. Med. Hyg.); The Vector of an outbreak of Kala-Azar in Kenya (Nature); The Zoonesos as a study in Ecology, with special reference to Plague, Relapsing Fever and Leishmaniasis, etc.

**Version `col1962-L22165.v` — printed in editions [1962, 1963, 1964, 1965]:**

> HEISCH, R. B., O.B.E. (1961).—b. 1910; ed. Bradfield Coll. and Camb. Univ.; M.O., Ken., 1939; senr. parasitol., 1947; senr. specialist, 1956-64. (Ken. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1939 | M.O. | Kenya | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 1 | 1947 | senr. parasitol | Kenya *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 2 | 1956 | senr. specialist | Kenya *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |

## Candidate stint `Hersch, R. B___Kenya___1949`

- Staff-list name: **Hersch, R. B** | colony: **Kenya** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | R. B. Hersch | Parasitologist | Medical | — | — |
| 1950 | R. B. Hersch | Parasitologist | Medical | — | — |

### Deterministic checks: `heisch_r-b_b1910` vs `Hersch, R. B___Kenya___1949`

- [PASS] surname_gate: bio 'HEISCH' vs stint 'Hersch, R. B' (fuzzy:1)
- [PASS] initials: bio ['R', 'B'] ~ stint ['R', 'B']
- [PASS] age_gate: stint starts 1949, birth 1910 (age 39)
- [PASS] colony: 3 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1950
- [PASS] position_sim: best 71 vs bar 60: 'senr. parasitol' ~ 'Parasitologist'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

