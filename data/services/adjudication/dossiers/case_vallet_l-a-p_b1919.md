<!-- {"case_id": "case_vallet_l-a-p_b1919", "bio_ids": ["vallet_l-a-p_b1919"], "stint_ids": ["Vallet, L. A. P___Mauritius___1949"]} -->
# Dossier case_vallet_l-a-p_b1919

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `vallet_l-a-p_b1919`

- Printed name: **VALLET, L. A. P**
- Birth year: 1919 (attested in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1957-L27995.v` — printed in editions [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> VALLET, L. A. P.—b. 1919; ed. Royal Coll., Maur., and Oxford Univ.; o'seer., P.W.D., Maur., 1939; asst. tracer, 1940; tracer, 1941; o'seer., gr. II, 1941; gr. I, 1941; exec. engrnr., 1946; senr. engr., 1961.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1939 | o'seer., P.W.D. | Mauritius | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1940 | asst. tracer | Mauritius *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1941 | tracer | Mauritius *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1946 | exec. engrnr | Mauritius *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 4 | 1961 | senr. engr | Mauritius *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Vallet, L. A. P___Mauritius___1949`

- Staff-list name: **Vallet, L. A. P** | colony: **Mauritius** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | L. A. P. Vallet | Executive Engineer | Public Works and Surveys | — | — |
| 1950 | L. A. P. Vallet | Executive Engineers | PUBLIC WORKS AND SURVEYS | — | — |

### Deterministic checks: `vallet_l-a-p_b1919` vs `Vallet, L. A. P___Mauritius___1949`

- [PASS] surname_gate: bio 'VALLET' vs stint 'Vallet, L. A. P' (exact)
- [PASS] initials: bio ['L', 'A', 'P'] ~ stint ['L', 'A', 'P']
- [PASS] age_gate: stint starts 1949, birth 1919 (age 30)
- [PASS] colony: 5 placed event(s) resolve to 'Mauritius'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1950
- [PASS] position_sim: best 69 vs bar 60: 'exec. engrnr' ~ 'Executive Engineer'
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

