<!-- {"case_id": "case_musaid_a-a_b1929", "bio_ids": ["musaid_a-a_b1929"], "stint_ids": ["Musaid, A. A___Aden___1964"]} -->
# Dossier case_musaid_a-a_b1929

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `musaid_a-a_b1929`

- Printed name: **MUSAID, A. A**
- Birth year: 1929 (attested in editions [1966])
- Appears in editions: [1966]

### Verbatim printed entry text (OCR)

**Version `col1966-L16860.v` — printed in editions [1966]:**

> MUSAID, A. A.—b. 1929; ed. Bukit el Radha Inst., Sudan; teacher, Aden, 1949; asst. educ. offr. (Prot.), 1955; Prot. educ. offr., 1957; sec., supreme coun., 1962; admin. offr., cl. III, 1963.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1949 | teacher | Aden | [1966] |
| 1 | 1955 | asst. educ. offr. (Prot.) | Aden *(inherited from previous clause)* | [1966] |
| 2 | 1957 | Prot. educ. offr | Aden *(inherited from previous clause)* | [1966] |
| 3 | 1962 | sec., supreme coun | Aden *(inherited from previous clause)* | [1966] |
| 4 | 1963 | admin. offr., cl. III | Aden *(inherited from previous clause)* | [1966] |

## Candidate stint `Musaid, A. A___Aden___1964`

- Staff-list name: **Musaid, A. A** | colony: **Aden** | listed 1964–1966 | editions [1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1964 | A. A. Musaid | Secretary | FEDERAL COUNCIL | — | — |
| 1965 | A. A. Musaid | Secretary | Federal Council | — | — |
| 1966 | A. A. Musaid | Secretary | Federal Council | — | — |

### Deterministic checks: `musaid_a-a_b1929` vs `Musaid, A. A___Aden___1964`

- [PASS] surname_gate: bio 'MUSAID' vs stint 'Musaid, A. A' (exact)
- [PASS] initials: bio ['A', 'A'] ~ stint ['A', 'A']
- [PASS] age_gate: stint starts 1964, birth 1929 (age 35)
- [PASS] colony: 5 placed event(s) resolve to 'Aden'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1964-1966
- [FAIL] position_sim: best 40 vs bar 60: 'sec., supreme coun' ~ 'Secretary'
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

