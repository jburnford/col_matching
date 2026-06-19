<!-- {"case_id": "case_sharp_commbr-george-arthur-coxall_b1891", "bio_ids": ["sharp_commbr-george-arthur-coxall_b1891"], "stint_ids": ["Sharp, A___Ceylon___1919"]} -->
# Dossier case_sharp_commbr-george-arthur-coxall_b1891

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 28 official(s) with this surname in the graph's staff lists; 13 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `sharp_commbr-george-arthur-coxall_b1891`

- Printed name: **SHARP, COMMBR. GEORGE ARTHUR COXALL**
- Birth year: 1891 (attested in editions [1937, 1939, 1940])
- Honours: D.S.C
- Appears in editions: [1937, 1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1937-L64590.v` — printed in editions [1937, 1939, 1940]:**

> SHARP, COMMBR. GEORGE ARTHUR COXALL, D.S.C., R.N. (ret.).—B. 1891; ed. R. Naval Colls., Osborne and Dartmouth; war serv., 1914-18; ret., 1920; marine offr., Tanganyika, 1927; marine supt., Takoradi, Gold Coast, 1936.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1920 | ret | — | [1937, 1939, 1940] |
| 1 | 1927 | marine offr. | Tanganyika | [1937, 1939, 1940] |
| 2 | 1936 | marine supt., Takoradi | Gold Coast | [1937, 1939, 1940] |

## Candidate stint `Sharp, A___Ceylon___1919`

- Staff-list name: **Sharp, A** | colony: **Ceylon** | listed 1919–1923 | editions [1919, 1920, 1921, 1923]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1919 | A. Sharp | Consul | Foreign Consuls | — | — |
| 1920 | A. Sharp | Consul | Foreign Consuls | — | — |
| 1921 | A. Sharp | Consul | Foreign Consuls | — | — |
| 1923 | A. Sharp | Consul, Portugal | Foreign Consuls | — | — |

### Deterministic checks: `sharp_commbr-george-arthur-coxall_b1891` vs `Sharp, A___Ceylon___1919`

- [PASS] surname_gate: bio 'SHARP' vs stint 'Sharp, A' (exact)
- [PASS] initials: bio ['C', 'G', 'A', 'C'] ~ stint ['A']
- [PASS] age_gate: stint starts 1919, birth 1891 (age 28)
- [FAIL] colony: no placed event resolves to 'Ceylon'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1919-1923
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

