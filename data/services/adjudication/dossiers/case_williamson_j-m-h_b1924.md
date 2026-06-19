<!-- {"case_id": "case_williamson_j-m-h_b1924", "bio_ids": ["williamson_j-m-h_b1924"], "stint_ids": ["Williamson, H___Bermuda___1939"]} -->
# Dossier case_williamson_j-m-h_b1924

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 17 official(s) with this surname in the graph's staff lists; 14 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Williamson, H___Bermuda___1939` is also gate-compatible with biography(ies) outside this case: ['williamson_harry-norman_b1905'] (already linked elsewhere or filtered).

## Biography `williamson_j-m-h_b1924`

- Printed name: **WILLIAMSON, J. M. H**
- Birth year: 1924 (attested in editions [1966])
- Appears in editions: [1966]

### Verbatim printed entry text (OCR)

**Version `col1966-L19012.v` — printed in editions [1966]:**

> WILLIAMSON, J. M. H.—b. 1924; ed. Caterham Sch. and Leeds Univ.; mil. serv., 1943-46, R.N.; asst. inspr., police, N. Rhod., 1949; sec. offr., ch. sec., 1951; senr. sec. offr., 1961; prin., 1965. (Zambia Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1949 | asst. inspr., police | Northern Rhodesia | [1966] |
| 1 | 1951 | sec. offr., ch. sec | Northern Rhodesia *(inherited from previous clause)* | [1966] |
| 2 | 1961 | senr. sec. offr | Northern Rhodesia *(inherited from previous clause)* | [1966] |
| 3 | 1965 | prin | Northern Rhodesia *(inherited from previous clause)* | [1966] |

## Candidate stint `Williamson, H___Bermuda___1939`

- Staff-list name: **Williamson, H** | colony: **Bermuda** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | H. Williamson | Consul | Foreign Consuls | — | — |
| 1940 | H. Williamson | Consul | Foreign Consuls | — | — |

### Deterministic checks: `williamson_j-m-h_b1924` vs `Williamson, H___Bermuda___1939`

- [PASS] surname_gate: bio 'WILLIAMSON' vs stint 'Williamson, H' (exact)
- [PASS] initials: bio ['J', 'M', 'H'] ~ stint ['H']
- [PASS] age_gate: stint starts 1939, birth 1924 (age 15)
- [FAIL] colony: no placed event resolves to 'Bermuda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1939-1940
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

