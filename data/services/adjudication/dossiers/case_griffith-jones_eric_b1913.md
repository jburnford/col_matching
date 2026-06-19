<!-- {"case_id": "case_griffith-jones_eric_b1913", "bio_ids": ["griffith-jones_eric_b1913"], "stint_ids": ["Griffith-Jones, E. N___Kenya___1953"]} -->
# Dossier case_griffith-jones_eric_b1913

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['griffith-jones_eric_b1913'] carry a single initial only — the namesake trap applies.

## Biography `griffith-jones_eric_b1913`

- Printed name: **GRIFFITH-JONES, Eric**
- Birth year: 1913 (attested in editions [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1964])
- Honours: C.M.G (1957), K.B.E (1962)
- Appears in editions: [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1964]

### Verbatim printed entry text (OCR)

**Version `col1953-L17542.v` — printed in editions [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1964]:**

> GRIFFITH-JONES, Sir Eric, K.B.E. (1962), C.M.G. (1957), Q.C.—b. 1913; ed. Cheltenham Coll.; barrister-at-law, Gray's Inn; mag., S.S., 1939; mil. serv., 1941-46; cr. coun., Mal., 1946; senr. fed. coun., 1948; solr.-gen., Ken., 1952; min. for legal affrs. and atty.-gen., 1955; dep. gov., 1962.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1939 | mag. | Straits Settlements | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1964] |
| 1 | 1946 | cr. coun. | Malaya | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1964] |
| 2 | 1948 | senr. fed. coun | Malaya *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1964] |
| 3 | 1952 | solr.-gen. | Kenya | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1964] |
| 4 | 1955 | min. for legal affrs. and atty.-gen | Kenya *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1964] |
| 5 | 1962 | dep. gov | Kenya *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1964] |

## Candidate stint `Griffith-Jones, E. N___Kenya___1953`

- Staff-list name: **Griffith-Jones, E. N** | colony: **Kenya** | listed 1953–1954 | editions [1953, 1954]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1953 | E. N. Griffith-Jones | Solicitor General | Civil Establishment | — | — |
| 1954 | E. N. Griffith-Jones | Solicitor General | Civil Establishment | — | — |

### Deterministic checks: `griffith-jones_eric_b1913` vs `Griffith-Jones, E. N___Kenya___1953`

- [PASS] surname_gate: bio 'GRIFFITH-JONES' vs stint 'Griffith-Jones, E. N' (exact)
- [PASS] initials: bio ['E'] ~ stint ['E', 'N']
- [PASS] age_gate: stint starts 1953, birth 1913 (age 40)
- [PASS] colony: 3 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1953-1954
- [FAIL] position_sim: best 33 vs bar 60: 'solr.-gen.' ~ 'Solicitor General'
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

