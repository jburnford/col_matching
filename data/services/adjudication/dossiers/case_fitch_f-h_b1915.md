<!-- {"case_id": "case_fitch_f-h_b1915", "bio_ids": ["fitch_f-h_b1915"], "stint_ids": ["Fitch, F. H___Sarawak___1961"]} -->
# Dossier case_fitch_f-h_b1915

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `fitch_f-h_b1915`

- Printed name: **FITCH, F. H**
- Birth year: 1915 (attested in editions [1956, 1957, 1958, 1960, 1961])
- Honours: M.B.E (1964)
- Appears in editions: [1956, 1957, 1958, 1960, 1961, 1963, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1956-L21136.v` — printed in editions [1956, 1957, 1958, 1960, 1961]:**

> FITCH, F. H.—b. 1915; ed. Westminster City Sch. and Royal Coll. of Science (Imp. Coll. of Science and Tech.); mil. serv., 1941–45; geol., Mal., 1938; senr. geol., Br. Borneo terrs., 1949; dep. dir., geol. surv., (N.Borneo) 1952; dir., 1960; author The geology and mineral resources of the neighbourhood of Kuantan, Pahang; and The geology and mineral resources of part of the Segama Valley and Darvel Bay area. Colony of North Borneo.

**Version `col1963-L19643.v` — printed in editions [1963, 1965, 1966]:**

> FITCH, F. H., M.B.E. (1964).—b. 1915; ed. Westminster City Sch. and Royal Coll. of Science (Imp. Coll. of Science and Tech.); mil. serv., 1941-45; geol., Mal., 1938; senr. geol., Br. Borneo terrs., 1949; dep. dir., geol. surv. (N. Borneo), 1952; dir., 1960.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1938 | geol. | Malaya | [1956, 1957, 1958, 1960, 1961, 1963, 1965, 1966] |
| 1 | 1949 | senr. geol., Br. Borneo terrs | Malaya *(inherited from previous clause)* | [1956, 1957, 1958, 1960, 1961, 1963, 1965, 1966] |
| 2 | 1952 | dep. dir., geol. surv. | North Borneo | [1956, 1957, 1958, 1960, 1961, 1963, 1965, 1966] |
| 3 | 1960 | dir | North Borneo *(inherited from previous clause)* | [1956, 1957, 1958, 1960, 1961, 1963, 1965, 1966] |

## Candidate stint `Fitch, F. H___Sarawak___1961`

- Staff-list name: **Fitch, F. H** | colony: **Sarawak** | listed 1961–1963 | editions [1961, 1962, 1963]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1961 | F. H. Fitch | Director of Geological Surveys (Borneo Territories) | Civil Establishment | — | — |
| 1962 | F. H. Fitch | Director of Geological Surveys (Borneo Territories) | Civil Establishment | — | — |
| 1963 | F. H. Fitch | Director of Geological Surveys (Borneo Territories) | Civil Establishment | — | — |

### Deterministic checks: `fitch_f-h_b1915` vs `Fitch, F. H___Sarawak___1961`

- [PASS] surname_gate: bio 'FITCH' vs stint 'Fitch, F. H' (exact)
- [PASS] initials: bio ['F', 'H'] ~ stint ['F', 'H']
- [PASS] age_gate: stint starts 1961, birth 1915 (age 46)
- [FAIL] colony: no placed event resolves to 'Sarawak'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1961-1963
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

