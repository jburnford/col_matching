<!-- {"case_id": "case_jourbert_m-j-a_b1882", "bio_ids": ["jourbert_m-j-a_b1882"], "stint_ids": ["Joubert, M. J. A___South Africa___1914"]} -->
# Dossier case_jourbert_m-j-a_b1882

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 8 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `jourbert_m-j-a_b1882`

- Printed name: **JOURBERT, M. J. A**
- Birth year: 1882 (attested in editions [1932, 1939])
- Appears in editions: [1932, 1933, 1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1932-L61598.v` — printed in editions [1932, 1939]:**

> JOURBERT, M. J. A., B.S.A. (Toronto).—B. 1882; pupil teacher, O.F.S., 1897; asst. to govt. agronomist, O.F.S., 1906; itinerant instr., agr., 1910; offr., u.ch. and prin., Glen schl. of agr., 1913; prin., schl. of agr., Glen., 1917; prin., Grootfontein schl. of agr. (Cape), 1924; asst. ch. dir., plant industry, dept., agr., Pretoria, 1929; ch., dir., of agr. educn. and extension, Pretoria, 1932; under-sec., agr., 1933.

**Version `col1933-L61157.v` — printed in editions [1933, 1937, 1940]:**

> JOUBERT, M. J. A., B.S.A. (Toronto).—B. 1882; pupil teacher, O.F.S., 1897; asst. to govt. agronomist, O.F.S., 1905; itinerant instr., agr., 1910; offr., u.ch. and prin., Glen schl. of agr., 1913; prin., scl. of agr., Glen., 1917; prin., Grootfontein schl. of agr. (Cape), 1924; asst. ch. dir., plant industry, dept., agr., Pretoria, 1929; ch., divn. of agr. educn. and extension, Pretoria, 1932; under-sec., agr., 1933.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1897 | pupil teacher | Orange Free State | [1932, 1933, 1937, 1939, 1940] |
| 1 | 1905 | asst. to govt. agronomist | Orange Free State | [1933, 1937, 1940] |
| 2 | 1906 | asst. to govt. agronomist | Orange Free State | [1932, 1939] |
| 3 | 1910 | itinerant instr., agr | Orange Free State *(inherited from previous clause)* | [1932, 1933, 1937, 1939, 1940] |
| 4 | 1913 | offr., u.ch. and prin., Glen schl. of agr | Orange Free State *(inherited from previous clause)* | [1932, 1933, 1937, 1939, 1940] |
| 5 | 1917 | prin., schl. of agr., Glen | Orange Free State *(inherited from previous clause)* | [1932, 1933, 1937, 1939, 1940] |
| 6 | 1924 | prin., Grootfontein schl. of agr. (Cape) | Orange Free State *(inherited from previous clause)* | [1932, 1933, 1937, 1939, 1940] |
| 7 | 1929 | asst. ch. dir., plant industry, dept., agr., Pretoria | Orange Free State *(inherited from previous clause)* | [1932, 1933, 1937, 1939, 1940] |
| 8 | 1932 | ch., dir., of agr. educn. and extension, Pretoria | Orange Free State *(inherited from previous clause)* | [1932, 1933, 1937, 1939, 1940] |
| 9 | 1933 | under-sec., agr | Orange Free State *(inherited from previous clause)* | [1932, 1933, 1937, 1939, 1940] |

## Candidate stint `Joubert, M. J. A___South Africa___1914`

- Staff-list name: **Joubert, M. J. A** | colony: **South Africa** | listed 1914–1918 | editions [1914, 1918]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1914 | M. J. Joubert | — | Agricultural Schools, Stud Farms and Experimental Stations | — | — |
| 1918 | M. J. A. Joubert | Officer-in-Charge | Agricultural Schools and Experiment Farms | — | — |

### Deterministic checks: `jourbert_m-j-a_b1882` vs `Joubert, M. J. A___South Africa___1914`

- [PASS] surname_gate: bio 'JOURBERT' vs stint 'Joubert, M. J. A' (fuzzy:1)
- [PASS] initials: bio ['M', 'J', 'A'] ~ stint ['M', 'J', 'A']
- [PASS] age_gate: stint starts 1914, birth 1882 (age 32)
- [FAIL] colony: no placed event resolves to 'South Africa'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1914-1918
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

