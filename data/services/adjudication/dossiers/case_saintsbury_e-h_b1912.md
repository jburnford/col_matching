<!-- {"case_id": "case_saintsbury_e-h_b1912", "bio_ids": ["saintsbury_e-h_b1912"], "stint_ids": ["Sainsbury, E. H___Hong Kong___1949"]} -->
# Dossier case_saintsbury_e-h_b1912

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `saintsbury_e-h_b1912`

- Printed name: **SAINTSBURY, E. H**
- Birth year: 1912 (attested in editions [1958, 1960, 1965])
- Appears in editions: [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965]

### Verbatim printed entry text (OCR)

**Version `col1958-L26622.v` — printed in editions [1958, 1960, 1965]:**

> SAINTSBURY, E. H., T.D.—b. 1912; ed. Cardiff High Sch. and Univ. of S. Wales and Mon. Law Sch.; barrister-at-law; mil. serv., 1938-45, maj.; asst. solr., H.K., 1946; legal dfstmn., Nig., 1954; prin. legal dfstmn., Fed. of Nig., 1958; judge, Lagos and S. Cams., 1960. (Nig. Govt. service.)

**Version `col1959-L27549.v` — printed in editions [1959, 1961, 1962, 1963, 1964]:**

> SAINSBURY, E. H., T.D.—b. 1912; ed. Cardiff High Sch. and Univ. of S. Wales and Mon. Law Sch.; barrister-at-law; mil. serv., 1938–45, maj. asst. solr., H.K., 1946; legal dfstmn., Nig., 1954; prin. legal dfstmn., Fed. of Nig., 1958; judge, Lagos and S. Cams., 1960. (Nig. Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1946 | asst. solr. | Hong Kong | [1958, 1960, 1965] |
| 1 | 1954 | legal dfstmn. | Nigeria | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 2 | 1958 | prin. legal dfstmn., Fed. of Nig | Nigeria *(inherited from previous clause)* | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |
| 3 | 1960 | judge, Lagos and S. Cams | Lagos | [1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965] |

## Candidate stint `Sainsbury, E. H___Hong Kong___1949`

- Staff-list name: **Sainsbury, E. H** | colony: **Hong Kong** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | E. H. Sainsbury | Assistant Crown Solicitor | Legal | — | — |
| 1950 | E. H. Sainsbury | Legal Officer | Legal | — | — |
| 1951 | E. H. Sainsbury | Legal Officer | Legal | — | — |

### Deterministic checks: `saintsbury_e-h_b1912` vs `Sainsbury, E. H___Hong Kong___1949`

- [PASS] surname_gate: bio 'SAINTSBURY' vs stint 'Sainsbury, E. H' (fuzzy:1)
- [PASS] initials: bio ['E', 'H'] ~ stint ['E', 'H']
- [PASS] age_gate: stint starts 1949, birth 1912 (age 37)
- [PASS] colony: 1 placed event(s) resolve to 'Hong Kong'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 53 vs bar 60: 'asst. solr.' ~ 'Assistant Crown Solicitor'
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

