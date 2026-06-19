<!-- {"case_id": "case_kennyon_vernon-cecil-wordsworth_b1905", "bio_ids": ["kennyon_vernon-cecil-wordsworth_b1905"], "stint_ids": ["Kenyon, V. C. W___Aden___1961"]} -->
# Dossier case_kennyon_vernon-cecil-wordsworth_b1905

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 5 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Kenyon, V. C. W___Aden___1961` is also gate-compatible with biography(ies) outside this case: ['kenyon_v-c-w_b1905'] (already linked elsewhere or filtered).

## Biography `kennyon_vernon-cecil-wordsworth_b1905`

- Printed name: **KENNYON, Vernon Cecil Wordsworth**
- Birth year: 1905 (attested in editions [1948])
- Appears in editions: [1948]

### Verbatim printed entry text (OCR)

**Version `col1948-L33795.v` — printed in editions [1948]:**

> KENNYON, Vernon Cecil Wordsworth.—b. 1905; apptd. draughtsmen, gr. IV., dept. of surveys, Pal., 1926; gr. I., 1932; offr., asst., H.Q., 1936; settlement offr., 1937; regional offr., 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | apptd. draughtsmen, gr. IV., dept. of surveys | Palestine | [1948] |
| 1 | 1932 | gr. I | Palestine *(inherited from previous clause)* | [1948] |
| 2 | 1936 | offr., asst., H.Q | Palestine *(inherited from previous clause)* | [1948] |
| 3 | 1937 | settlement offr | Palestine *(inherited from previous clause)* | [1948] |
| 4 | 1946 | regional offr | Palestine *(inherited from previous clause)* | [1948] |

## Candidate stint `Kenyon, V. C. W___Aden___1961`

- Staff-list name: **Kenyon, V. C. W** | colony: **Aden** | listed 1961–1965 | editions [1961, 1962, 1963, 1964, 1965]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1961 | V. C. W. Kenyon | Commissioner of Lands | Civil Establishment | — | — |
| 1962 | V. C. W. Kenyon | Commissioner of Lands | Civil Establishment | — | — |
| 1963 | V. C. W. Kenyon | Commissioner of Lands | Civil Establishment | — | — |
| 1964 | V. C. W. Kenyon | Commissioner of Lands | CIVIL ESTABLISHMENT | — | — |
| 1965 | V. C. W. Kenyon | Secretary and Commissioner of Lands | Civil Establishment | — | — |

### Deterministic checks: `kennyon_vernon-cecil-wordsworth_b1905` vs `Kenyon, V. C. W___Aden___1961`

- [PASS] surname_gate: bio 'KENNYON' vs stint 'Kenyon, V. C. W' (fuzzy:1)
- [PASS] initials: bio ['V', 'C', 'W'] ~ stint ['V', 'C', 'W']
- [PASS] age_gate: stint starts 1961, birth 1905 (age 56)
- [FAIL] colony: no placed event resolves to 'Aden'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1961-1965
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

