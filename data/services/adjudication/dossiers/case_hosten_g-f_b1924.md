<!-- {"case_id": "case_hosten_g-f_b1924", "bio_ids": ["hosten_g-f_b1924"], "stint_ids": ["Hosten, G. F___Grenada___1963"]} -->
# Dossier case_hosten_g-f_b1924

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hosten_g-f_b1924`

- Printed name: **HOSTEN, G. F**
- Birth year: 1924 (attested in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1958-L23775.v` — printed in editions [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> HOSTEN, G. F.—b. 1924; ed. Grenada Boys' Secondary Sch. and London Univ.; cler. appts., Grenada, 1943-49; clk., leg. co., 1950; prin. asst. sec., min. of trade and production, 1957; perm. sec., 1963.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1943–1949 | cler. appts. | Grenada | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1950 | clk., leg. co | Grenada *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1957 | prin. asst. sec., min. of trade and production | Grenada *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 3 | 1963 | perm. sec | Grenada *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Hosten, G. F___Grenada___1963`

- Staff-list name: **Hosten, G. F** | colony: **Grenada** | listed 1963–1964 | editions [1963, 1964]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1963 | G. F. Hosten | Ministry of Production and Labour | Civil Establishment | — | — |
| 1964 | G. F. Hosten | Ministry of Production and Labour | Civil Establishment | — | — |

### Deterministic checks: `hosten_g-f_b1924` vs `Hosten, G. F___Grenada___1963`

- [PASS] surname_gate: bio 'HOSTEN' vs stint 'Hosten, G. F' (exact)
- [PASS] initials: bio ['G', 'F'] ~ stint ['G', 'F']
- [PASS] age_gate: stint starts 1963, birth 1924 (age 39)
- [PASS] colony: 4 placed event(s) resolve to 'Grenada'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1963-1964
- [PASS] position_sim: best 73 vs bar 60: 'prin. asst. sec., min. of trade and production' ~ 'Ministry of Production and Labour'
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

