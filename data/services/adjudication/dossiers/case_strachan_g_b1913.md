<!-- {"case_id": "case_strachan_g_b1913", "bio_ids": ["strachan_g_b1913"], "stint_ids": ["Strachan, G. B___Bahamas___1932"]} -->
# Dossier case_strachan_g_b1913

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 20 official(s) with this surname in the graph's staff lists; 7 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['strachan_g_b1913'] carry a single initial only — the namesake trap applies.

## Biography `strachan_g_b1913`

- Printed name: **STRACHAN, G**
- Birth year: 1913 (attested in editions [1963, 1964, 1965, 1966])
- Appears in editions: [1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1963-L25308.v` — printed in editions [1963, 1964, 1965, 1966]:**

> STRACHAN, G.—b. 1913; ed. Christian Bros. Coll., Kimberley and Cape Town Univ.; mil. serv., 1939–45; water engnr., N. Rhod., 1952; senr. water engnr., 1964. (Zambia Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1952 | water engnr. | Northern Rhodesia | [1963, 1964, 1965, 1966] |
| 1 | 1964 | senr. water engnr | Northern Rhodesia *(inherited from previous clause)* | [1963, 1964, 1965, 1966] |

## Candidate stint `Strachan, G. B___Bahamas___1932`

- Staff-list name: **Strachan, G. B** | colony: **Bahamas** | listed 1932–1940 | editions [1932, 1933, 1934, 1936, 1937, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1932 | G. B. Strachan | Dispenser | Medical Department | — | — |
| 1933 | G. B. Strachan | Dispenser | Medical Department | — | — |
| 1934 | G. B. Strachan | Dispenser | Medical Department | — | — |
| 1936 | G. B. Strachan | Dispenser | Medical Department | — | — |
| 1937 | G. B. Strachan | Dispenser | Medical Department | — | — |
| 1939 | G. B. Strachan | Dispenser | Medical Department | — | — |
| 1940 | G. B. Strachan | Dispenser | Medical Department | — | — |

### Deterministic checks: `strachan_g_b1913` vs `Strachan, G. B___Bahamas___1932`

- [PASS] surname_gate: bio 'STRACHAN' vs stint 'Strachan, G. B' (exact)
- [PASS] initials: bio ['G'] ~ stint ['G', 'B']
- [PASS] age_gate: stint starts 1932, birth 1913 (age 19)
- [FAIL] colony: no placed event resolves to 'Bahamas'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1932-1940
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

