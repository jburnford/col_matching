<!-- {"case_id": "case_tingle_g-m_b1913", "bio_ids": ["tingle_g-m_b1913"], "stint_ids": ["Tingle, G. M___Hong Kong___1950"]} -->
# Dossier case_tingle_g-m_b1913

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `tingle_g-m_b1913`

- Printed name: **TINGLE, G. M**
- Birth year: 1913 (attested in editions [1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1960-L28788.v` — printed in editions [1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> TINGLE, G. M.—b. 1913; ed. King Edward VII Sch., Sheffield, and Queens' Coll., Camb.; cadet offr., cl. II, H.K., 1949; admin. offr., staff gr. C, 1959; asst. estab. offr., 1960; asst. dir., urban services, 1961; dir., urban services, 1963; def. sec., 1963-64; admin. offr., st. gr. B, 1964; prin. col. sec. (spec. duties), 1965.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1949 | cadet offr., cl. II | Hong Kong | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1959 | admin. offr., staff gr. C | Hong Kong *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1960 | asst. estab. offr | Hong Kong *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1961 | asst. dir., urban services | Hong Kong *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 4 | 1963 | dir., urban services | Hong Kong *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 5 | 1964 | admin. offr., st. gr. B | Hong Kong *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 6 | 1965 | prin. col. sec. (spec. duties) | Hong Kong *(inherited from previous clause)* | [1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Tingle, G. M___Hong Kong___1950`

- Staff-list name: **Tingle, G. M** | colony: **Hong Kong** | listed 1950–1953 | editions [1950, 1951, 1953]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | G. M. Tingle | Administrative Officer | Administrative Officers | — | — |
| 1950 | G. M. Tingle | Assistant Secretary | Secretariat | — | — |
| 1951 | G. M. Tingle | Assistant Secretaries | Administration | — | — |
| 1951 | G. M. Tingle | Administrative Officer | Administrative Officers | — | — |
| 1953 | G. M. Tingle | Commissioner, Essential Services Corps | Civil Establishment | — | — |

### Deterministic checks: `tingle_g-m_b1913` vs `Tingle, G. M___Hong Kong___1950`

- [PASS] surname_gate: bio 'TINGLE' vs stint 'Tingle, G. M' (exact)
- [PASS] initials: bio ['G', 'M'] ~ stint ['G', 'M']
- [PASS] age_gate: stint starts 1950, birth 1913 (age 37)
- [PASS] colony: 7 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1950-1953
- [FAIL] position_sim: best 47 vs bar 60: 'cadet offr., cl. II' ~ 'Administrative Officer'
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

