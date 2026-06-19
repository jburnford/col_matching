<!-- {"case_id": "case_oliver_george-richard_b1905", "bio_ids": ["oliver_george-richard_b1905"], "stint_ids": ["Oliver, G___Uganda___1949"]} -->
# Dossier case_oliver_george-richard_b1905

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 32 official(s) with this surname in the graph's staff lists; 14 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `oliver_george-richard_b1905`

- Printed name: **OLIVER, George Richard**
- Birth year: 1905 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L35015.v` — printed in editions [1948, 1949, 1950, 1951]:**

> OLIVER, George Richard.—b. 1905; ed. Eastbourne Coll., Trinity Coll., Cambridge, M.A. (Cantab.); cadet, N. Rhod., 1927; dist. offr., 1929.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | cadet | Northern Rhodesia | [1948, 1949, 1950, 1951] |
| 1 | 1929 | dist. offr | Northern Rhodesia *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Oliver, G___Uganda___1949`

- Staff-list name: **Oliver, G** | colony: **Uganda** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | G. Oliver | European Agricultural Assistant | Agricultural | — | — |
| 1951 | G. Oliver | European Agricultural Assistants | Agricultural | — | — |
| 1951 | G. Oliver | Aide-de-Camp | Governor and Personal Staff | — | Captain |

### Deterministic checks: `oliver_george-richard_b1905` vs `Oliver, G___Uganda___1949`

- [PASS] surname_gate: bio 'OLIVER' vs stint 'Oliver, G' (exact)
- [PASS] initials: bio ['G', 'R'] ~ stint ['G']
- [PASS] age_gate: stint starts 1949, birth 1905 (age 44)
- [FAIL] colony: no placed event resolves to 'Uganda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
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

