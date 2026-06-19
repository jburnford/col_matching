<!-- {"case_id": "case_roe_h-s_b1901", "bio_ids": ["roe_h-s_b1901"], "stint_ids": ["Roe, H. S___Sarawak___1953"]} -->
# Dossier case_roe_h-s_b1901

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 16 official(s) with this surname in the graph's staff lists; 9 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `roe_h-s_b1901`

- Printed name: **ROE, H. S**
- Birth year: 1901 (attested in editions [1948, 1949, 1950, 1951, 1954, 1955, 1956, 1957, 1958, 1959])
- Appears in editions: [1948, 1949, 1950, 1951, 1954, 1955, 1956, 1957, 1958, 1959]

### Verbatim printed entry text (OCR)

**Version `col1948-L35599.v` — printed in editions [1948, 1949, 1950, 1951, 1954, 1955, 1956, 1957, 1958, 1959]:**

> ROE, H. S.—b. 1901; ed. Wellington Coll., Berks. and King's Coll., Lond.; asst. engnr., P.W.D., Tang., 1927; div. engnr., gr. II, 1942; div. engnr., gr. I, 1944; D.D.P.W., Fiji, 1947; Sarawak, 1952; D.P.W., 1955-58.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1927 | asst. engnr., P.W.D. | Tanganyika | [1948, 1949, 1950, 1951, 1954, 1955, 1956, 1957, 1958, 1959] |
| 1 | 1942 | div. engnr., gr. II | Tanganyika *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1954, 1955, 1956, 1957, 1958, 1959] |
| 2 | 1944 | div. engnr., gr. I | Tanganyika *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1954, 1955, 1956, 1957, 1958, 1959] |
| 3 | 1947 | D.D.P.W. | Fiji | [1948, 1949, 1950, 1951, 1954, 1955, 1956, 1957, 1958, 1959] |
| 4 | 1952 | D.D.P.W. | Sarawak | [1948, 1949, 1950, 1951, 1954, 1955, 1956, 1957, 1958, 1959] |
| 5 | 1955–1958 | D.P.W | Sarawak *(inherited from previous clause)* | [1948, 1949, 1950, 1951, 1954, 1955, 1956, 1957, 1958, 1959] |

## Candidate stint `Roe, H. S___Sarawak___1953`

- Staff-list name: **Roe, H. S** | colony: **Sarawak** | listed 1953–1957 | editions [1953, 1954, 1955, 1957]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1953 | H. S. Roe | Deputy Director of Public Works | Civil Establishment | — | — |
| 1954 | H. S. Roe | Deputy Director of Public Works | Civil Establishment | — | — |
| 1955 | H. S. Roe | Deputy Director of Public Works | Civil Establishment | — | — |
| 1957 | H. S. Roe | Director of Public Works | Civil Establishment | — | — |

### Deterministic checks: `roe_h-s_b1901` vs `Roe, H. S___Sarawak___1953`

- [PASS] surname_gate: bio 'ROE' vs stint 'Roe, H. S' (exact)
- [PASS] initials: bio ['H', 'S'] ~ stint ['H', 'S']
- [PASS] age_gate: stint starts 1953, birth 1901 (age 52)
- [PASS] colony: 2 placed event(s) resolve to 'Sarawak'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1953-1957
- [FAIL] position_sim: best 23 vs bar 60: 'D.D.P.W.' ~ 'Deputy Director of Public Works'
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

