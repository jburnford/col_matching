<!-- {"case_id": "case_moosai-maharaj_s_b1909", "bio_ids": ["moosai-maharaj_s_b1909"], "stint_ids": ["Moosai-Maharaj, S___West Indies Federation___1961"]} -->
# Dossier case_moosai-maharaj_s_b1909

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['moosai-maharaj_s_b1909'] carry a single initial only — the namesake trap applies.

## Biography `moosai-maharaj_s_b1909`

- Printed name: **MOOSAI-MAHARAJ, S**
- Birth year: 1909 (attested in editions [1960, 1961, 1962, 1963])
- Appears in editions: [1960, 1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1960-L26198.v` — printed in editions [1960, 1961, 1962, 1963]:**

> MOOSAI-MAHARAJ, S.—b. 1909; ed. Naparima Coll., Trin., Mt. Allison Univ., Canada, and Lincoln Coll., Oxford; health educ. offr., Trin., 1943; asst. sec., 1956; senr. asst. sec., T.W.I., 1958-62.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1943 | health educ. offr. | Trinidad | [1960, 1961, 1962, 1963] |
| 1 | 1956 | asst. sec | Trinidad *(inherited from previous clause)* | [1960, 1961, 1962, 1963] |
| 2 | 1958–1962 | senr. asst. sec., T.W.I | Trinidad *(inherited from previous clause)* | [1960, 1961, 1962, 1963] |

## Candidate stint `Moosai-Maharaj, S___West Indies Federation___1961`

- Staff-list name: **Moosai-Maharaj, S** | colony: **West Indies Federation** | listed 1961–1962 | editions [1961, 1962]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1961 | S. Moosai-Maharaj | Ministry of Labour and Social Affairs | Civil Establishment | — | — |
| 1962 | S. Moosai-Maharaj | Ministry of Labour and Social Affairs | Civil Establishment | — | — |

### Deterministic checks: `moosai-maharaj_s_b1909` vs `Moosai-Maharaj, S___West Indies Federation___1961`

- [PASS] surname_gate: bio 'MOOSAI-MAHARAJ' vs stint 'Moosai-Maharaj, S' (exact)
- [PASS] initials: bio ['S'] ~ stint ['S']
- [PASS] age_gate: stint starts 1961, birth 1909 (age 52)
- [FAIL] colony: no placed event resolves to 'West Indies Federation'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1961-1962
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

