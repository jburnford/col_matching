<!-- {"case_id": "case_aziz_ahmed_b1899", "bio_ids": ["aziz_ahmed_b1899"], "stint_ids": ["Aziz, A___Cyprus___1951"]} -->
# Dossier case_aziz_ahmed_b1899

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['aziz_ahmed_b1899'] carry a single initial only — the namesake trap applies.

## Biography `aziz_ahmed_b1899`

- Printed name: **AZIZ, Ahmed**
- Birth year: 1899 (attested in editions [1951, 1953, 1954])
- Appears in editions: [1951, 1953, 1954]

### Verbatim printed entry text (OCR)

**Version `col1951-L35837.v` — printed in editions [1951, 1953, 1954]:**

> AZIZ, Ahmed.—b. 1899; ed. Turkish Sch. and English Sch., Nicosia; student clk., gen. cler. staff, Cyp., 1918; ast. P.M.G., 1947; P.M.G., 1950.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1918 | student clk., gen. cler. staff | Cyprus | [1951, 1953, 1954] |
| 1 | 1947 | ast. P.M.G | Cyprus *(inherited from previous clause)* | [1951, 1953, 1954] |
| 2 | 1950 | P.M.G | Cyprus *(inherited from previous clause)* | [1951, 1953, 1954] |

## Candidate stint `Aziz, A___Cyprus___1951`

- Staff-list name: **Aziz, A** | colony: **Cyprus** | listed 1951–1954 | editions [1951, 1952, 1953, 1954]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1951 | A. Aziz | Postmaster-General | Posts | — | — |
| 1952 | A. Aziz | Postmaster-General | Civil Establishment | — | — |
| 1953 | A. Aziz | Postmaster-General | Civil Establishment | — | — |
| 1954 | A. Aziz | Postmaster-General | Civil Establishment | — | — |

### Deterministic checks: `aziz_ahmed_b1899` vs `Aziz, A___Cyprus___1951`

- [PASS] surname_gate: bio 'AZIZ' vs stint 'Aziz, A' (exact)
- [PASS] initials: bio ['A'] ~ stint ['A']
- [PASS] age_gate: stint starts 1951, birth 1899 (age 52)
- [PASS] colony: 3 placed event(s) resolve to 'Cyprus'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1951-1954
- [FAIL] position_sim: best 33 vs bar 60: 'ast. P.M.G' ~ 'Postmaster-General'
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

