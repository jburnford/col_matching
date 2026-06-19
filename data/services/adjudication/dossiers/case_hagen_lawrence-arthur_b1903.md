<!-- {"case_id": "case_hagen_lawrence-arthur_b1903", "bio_ids": ["hagen_lawrence-arthur_b1903"], "stint_ids": ["Hagen, L. A___Gold Coast___1930"]} -->
# Dossier case_hagen_lawrence-arthur_b1903

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hagen_lawrence-arthur_b1903`

- Printed name: **HAGEN, Lawrence Arthur**
- Birth year: 1903 (attested in editions [1948, 1949, 1950, 1951])
- Honours: P.A.S.I
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L33076.v` — printed in editions [1948, 1949, 1950, 1951]:**

> HAGEN, Lawrence Arthur, P.A.S.I.—b. 1903; ed. Elstow, Bedford; chtrd survr., G.C., 1926; asst. supt.; police, 1932; supt., 1943.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | chtrd survr. | Gold Coast | [1948, 1949, 1950, 1951] |
| 1 | 1932 | police | Gold Coast *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 2 | 1943 | supt | Gold Coast *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Hagen, L. A___Gold Coast___1930`

- Staff-list name: **Hagen, L. A** | colony: **Gold Coast** | listed 1930–1936 | editions [1930, 1932, 1934, 1936]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1930 | L. A. Hagen | Quantity Surveyors | V. Architectural and Drawing Office Staff | — | — |
| 1932 | L. A. Hagen | Quantity Surveyors | Architectural and Drawing Office | — | — |
| 1934 | L. A. Hagen | Commissioners and Assistant Commissioners of Police | Police Department | — | — |
| 1936 | L. A. Hagen | Commissioners and Assistant Commissioners of Police | Police Department | — | — |

### Deterministic checks: `hagen_lawrence-arthur_b1903` vs `Hagen, L. A___Gold Coast___1930`

- [PASS] surname_gate: bio 'HAGEN' vs stint 'Hagen, L. A' (exact)
- [PASS] initials: bio ['L', 'A'] ~ stint ['L', 'A']
- [PASS] age_gate: stint starts 1930, birth 1903 (age 27)
- [PASS] colony: 3 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1930-1936
- [PASS] position_sim: best 100 vs bar 60: 'police' ~ 'Commissioners and Assistant Commissioners of Police'
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

