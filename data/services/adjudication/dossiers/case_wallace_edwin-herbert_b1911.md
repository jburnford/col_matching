<!-- {"case_id": "case_wallace_edwin-herbert_b1911", "bio_ids": ["wallace_edwin-herbert_b1911"], "stint_ids": ["Wallace, E. H___Brunei___1953", "Wallace, E. H___Sarawak___1949"]} -->
# Dossier case_wallace_edwin-herbert_b1911

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 58 official(s) with this surname in the graph's staff lists; 28 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `wallace_edwin-herbert_b1911`

- Printed name: **WALLACE, Edwin Herbert**
- Birth year: 1911 (attested in editions [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961])
- Honours: M.B
- Appears in editions: [1950, 1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961]

### Verbatim printed entry text (OCR)

**Version `col1953-L19424.v` — printed in editions [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961]:**

> WALLACE, E. H.—b. 1911; ed. Thetford Gram. Sch. and Glasgow Univ.; mil. serv. (p.o.w.), 1942-45; apptd. I.M.S., 1935; M.O. (on contract), Sarawak, 1948; secon., Brunei, 1952; spec. ophthal., 1958. (Deceased.)

**Version `col1950-L40455.v` — printed in editions [1950, 1951]:**

> WALLACE, Edwin Herbert, M.B., Ch.B. (Glas.).—b. 1911; ed. Thetford Gram. Sch., and Glasgow Univ.; on mil. serv. (p.o.w.), 1942–45; apptd. Indian med. serv., 1935; med. offr. (on contract), Sarawak, 1948.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1935 | apptd. I.M.S | — | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961] |
| 1 | 1935 | apptd. Indian med. serv | — | [1950, 1951] |
| 2 | 1948 | M.O. (on contract) | Sarawak | [1950, 1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961] |
| 3 | 1952 | secon. | Brunei | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961] |
| 4 | 1958 | spec. ophthal | Brunei *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961] |

## Candidate stint `Wallace, E. H___Brunei___1953`

- Staff-list name: **Wallace, E. H** | colony: **Brunei** | listed 1953–1954 | editions [1953, 1954]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1953 | E. H. Wallace | Medical Officer | Civil Establishment | — | — |
| 1954 | E. H. Wallace | Medical Officer | Civil Establishment | — | — |

### Deterministic checks: `wallace_edwin-herbert_b1911` vs `Wallace, E. H___Brunei___1953`

- [PASS] surname_gate: bio 'WALLACE' vs stint 'Wallace, E. H' (exact)
- [PASS] initials: bio ['E', 'H'] ~ stint ['E', 'H']
- [PASS] age_gate: stint starts 1953, birth 1911 (age 42)
- [PASS] colony: 2 placed event(s) resolve to 'Brunei'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1953-1954
- [FAIL] position_sim: best 30 vs bar 60: 'secon.' ~ 'Medical Officer'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Wallace, E. H___Sarawak___1949`

- Staff-list name: **Wallace, E. H** | colony: **Sarawak** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | E. H. Wallace | Medical Officer | Medical and Health | — | — |
| 1950 | E. H. Wallace | Medical Officers | MEDICAL AND HEALTH | — | — |
| 1951 | E. H. Wallace | Medical Officer | Medical and Health | — | — |

### Deterministic checks: `wallace_edwin-herbert_b1911` vs `Wallace, E. H___Sarawak___1949`

- [PASS] surname_gate: bio 'WALLACE' vs stint 'Wallace, E. H' (exact)
- [PASS] initials: bio ['E', 'H'] ~ stint ['E', 'H']
- [PASS] age_gate: stint starts 1949, birth 1911 (age 38)
- [PASS] colony: 1 placed event(s) resolve to 'Sarawak'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 28 vs bar 60: 'M.O. (on contract)' ~ 'Medical Officer'
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

