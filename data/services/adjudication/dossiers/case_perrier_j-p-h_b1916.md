<!-- {"case_id": "case_perrier_j-p-h_b1916", "bio_ids": ["perrier_j-p-h_b1916"], "stint_ids": ["Perrier, P___Mauritius___1949"]} -->
# Dossier case_perrier_j-p-h_b1916

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Perrier, P___Mauritius___1949` is also gate-compatible with biography(ies) outside this case: ['perrier_joseph-paul_b1912'] (already linked elsewhere or filtered).

## Biography `perrier_j-p-h_b1916`

- Printed name: **PERRIER, J. P. H**
- Birth year: 1916 (attested in editions [1963, 1964, 1965, 1966])
- Appears in editions: [1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1963-L23700.v` — printed in editions [1963, 1964, 1965, 1966]:**

> PERRIER, J. P. H.—b. 1916; ed. Stanislas Coll., Maur.; mil. serv., Jan./July, 1942, pl. sgt.; police const., Maur., 1935; inspr., 1949; asst., 1952; supt., 1959.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1935 | police const. | Mauritius | [1963, 1964, 1965, 1966] |
| 1 | 1949 | inspr | Mauritius *(inherited from previous clause)* | [1963, 1964, 1965, 1966] |
| 2 | 1952 | asst | Mauritius *(inherited from previous clause)* | [1963, 1964, 1965, 1966] |
| 3 | 1959 | supt | Mauritius *(inherited from previous clause)* | [1963, 1964, 1965, 1966] |

## Candidate stint `Perrier, P___Mauritius___1949`

- Staff-list name: **Perrier, P** | colony: **Mauritius** | listed 1949–1950 | editions [1949, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | P. Perrier | Assistant Superintendent | Police | — | — |
| 1950 | P. Perrier | Assistant Superintendent | Police | — | — |

### Deterministic checks: `perrier_j-p-h_b1916` vs `Perrier, P___Mauritius___1949`

- [PASS] surname_gate: bio 'PERRIER' vs stint 'Perrier, P' (exact)
- [PASS] initials: bio ['J', 'P', 'H'] ~ stint ['P']
- [PASS] age_gate: stint starts 1949, birth 1916 (age 33)
- [PASS] colony: 4 placed event(s) resolve to 'Mauritius'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1950
- [FAIL] position_sim: best 34 vs bar 60: 'inspr' ~ 'Assistant Superintendent'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

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

