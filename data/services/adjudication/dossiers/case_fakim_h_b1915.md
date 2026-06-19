<!-- {"case_id": "case_fakim_h_b1915", "bio_ids": ["fakim_h_b1915"], "stint_ids": ["Fakim, H___Mauritius___1962"]} -->
# Dossier case_fakim_h_b1915

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['fakim_h_b1915'] carry a single initial only — the namesake trap applies.

## Biography `fakim_h_b1915`

- Printed name: **FAKIM, H**
- Birth year: 1915 (attested in editions [1963, 1964, 1965, 1966])
- Appears in editions: [1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1963-L19500.v` — printed in editions [1963, 1964, 1965, 1966]:**

> FAKIM, H.—b. 1915; ed. Royal Coll., Maur., Univs. Lond. and Wales; med. offr., Maur., 1949; T.B. specialist, 1952; P.M.O., 1963.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1949 | med. offr. | Mauritius | [1963, 1964, 1965, 1966] |
| 1 | 1952 | T.B. specialist | Mauritius *(inherited from previous clause)* | [1963, 1964, 1965, 1966] |
| 2 | 1963 | P.M.O | Mauritius *(inherited from previous clause)* | [1963, 1964, 1965, 1966] |

## Candidate stint `Fakim, H___Mauritius___1962`

- Staff-list name: **Fakim, H** | colony: **Mauritius** | listed 1962–1966 | editions [1962, 1963, 1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1962 | H. Fakim | Deputy Director of Medical Services | CIVIL ESTABLISHMENT | — | — |
| 1963 | H. Fakim | Principal Medical Officer | Civil Establishment | — | — |
| 1964 | H. Fakim | Principal Medical Officer | Civil Establishment | — | — |
| 1965 | H. Fakim | Principal Medical Officer | Civil Establishment | — | — |
| 1966 | H. Fakim | Principal Medical Officer | Civil Establishment | — | — |

### Deterministic checks: `fakim_h_b1915` vs `Fakim, H___Mauritius___1962`

- [PASS] surname_gate: bio 'FAKIM' vs stint 'Fakim, H' (exact)
- [PASS] initials: bio ['H'] ~ stint ['H']
- [PASS] age_gate: stint starts 1962, birth 1915 (age 47)
- [PASS] colony: 3 placed event(s) resolve to 'Mauritius'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1962-1966
- [FAIL] position_sim: best 33 vs bar 60: 'T.B. specialist' ~ 'Deputy Director of Medical Services'
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

