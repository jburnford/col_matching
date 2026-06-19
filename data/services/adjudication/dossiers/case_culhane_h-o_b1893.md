<!-- {"case_id": "case_culhane_h-o_b1893", "bio_ids": ["culhane_h-o_b1893"], "stint_ids": ["Culhane, H. O___Trinidad and Tobago___1952"]} -->
# Dossier case_culhane_h-o_b1893

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `culhane_h-o_b1893`

- Printed name: **CULHANE, H. O**
- Birth year: 1893 (attested in editions [1953, 1954])
- Appears in editions: [1953, 1954]

### Verbatim printed entry text (OCR)

**Version `col1953-L17049.v` — printed in editions [1953, 1954]:**

> CULHANE, H. O.—b. 1893; ed. Borlase Sch., Marlow-on-Thames.; mil. serv., 1914-18, capt., 1940-45, major; dep. wharf contrlr. and dep. wharf supt., Trin., 1943; wharf supt., 1945; dep. gen. man., port servs., 1949; gen. man., 1949.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1943 | dep. wharf contrlr. and dep. wharf supt. | Trinidad | [1953, 1954] |
| 1 | 1945 | wharf supt | Trinidad *(inherited from previous clause)* | [1953, 1954] |
| 2 | 1949 | dep. gen. man., port servs | Trinidad *(inherited from previous clause)* | [1953, 1954] |

## Candidate stint `Culhane, H. O___Trinidad and Tobago___1952`

- Staff-list name: **Culhane, H. O** | colony: **Trinidad and Tobago** | listed 1952–1954 | editions [1952, 1953, 1954]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1952 | H. O. Culhane | General Manager, Port Services | Civil Establishment | — | — |
| 1953 | H. O. Culhane | General Manager, Port Services | Civil Establishment | — | — |
| 1954 | H. O. Culhane | General Manager, Port Services | Civil Establishment | — | — |

### Deterministic checks: `culhane_h-o_b1893` vs `Culhane, H. O___Trinidad and Tobago___1952`

- [PASS] surname_gate: bio 'CULHANE' vs stint 'Culhane, H. O' (exact)
- [PASS] initials: bio ['H', 'O'] ~ stint ['H', 'O']
- [PASS] age_gate: stint starts 1952, birth 1893 (age 59)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1952-1954
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

