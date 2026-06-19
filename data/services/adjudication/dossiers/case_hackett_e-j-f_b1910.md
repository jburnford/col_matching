<!-- {"case_id": "case_hackett_e-j-f_b1910", "bio_ids": ["hackett_e-j-f_b1910"], "stint_ids": ["Hackett, E. J. F___Fiji___1960"]} -->
# Dossier case_hackett_e-j-f_b1910

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 12 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hackett_e-j-f_b1910`

- Printed name: **HACKETT, E. J. F**
- Birth year: 1910 (attested in editions [1966])
- Appears in editions: [1966]

### Verbatim printed entry text (OCR)

**Version `col1966-L15177.v` — printed in editions [1966]:**

> HACKETT, E. J. F.—b. 1910; ed. St. Mary's Sch., Morecambe and privately; mil. serv., 1942-46, R.N., lieut.; state inf. offr., Malaya, 1953; P.R.O., Fiji, 1957.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1953 | state inf. offr. | Malaya | [1966] |
| 1 | 1957 | P.R.O. | Fiji | [1966] |

## Candidate stint `Hackett, E. J. F___Fiji___1960`

- Staff-list name: **Hackett, E. J. F** | colony: **Fiji** | listed 1960–1966 | editions [1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1960 | E. J. F. Hackett | Public Relations Officer | Civil Establishment | — | — |
| 1961 | E. J. F. Hackett | Public Relations Officer | Law Officers | — | — |
| 1962 | E. J. F. Hackett | Public Relations Officer | Civil Establishment | — | — |
| 1963 | E. J. F. Hackett | Public Relations Officer | Civil Establishment | — | — |
| 1964 | E. J. F. Hackett | Public Relations Officer | Civil Establishment | — | — |
| 1965 | E. J. F. Hackett | Public Relations Officer | Civil Establishment | — | — |
| 1966 | E. J. F. Hackett | Public Relations Officer | Civil Establishment | — | — |

### Deterministic checks: `hackett_e-j-f_b1910` vs `Hackett, E. J. F___Fiji___1960`

- [PASS] surname_gate: bio 'HACKETT' vs stint 'Hackett, E. J. F' (exact)
- [PASS] initials: bio ['E', 'J', 'F'] ~ stint ['E', 'J', 'F']
- [PASS] age_gate: stint starts 1960, birth 1910 (age 50)
- [PASS] colony: 1 placed event(s) resolve to 'Fiji'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1960-1966
- [FAIL] position_sim: best 22 vs bar 60: 'P.R.O.' ~ 'Public Relations Officer'
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

