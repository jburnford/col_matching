<!-- {"case_id": "case_mundy_john-cloudesley_b1900", "bio_ids": ["mundy_john-cloudesley_b1900"], "stint_ids": ["Mundy, J. C___Kenya___1939"]} -->
# Dossier case_mundy_john-cloudesley_b1900

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `mundy_john-cloudesley_b1900`

- Printed name: **MUNDY, John Cloudesley**
- Birth year: 1900 (attested in editions [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956, 1957])
- Honours: C.M.G. (1947)
- Appears in editions: [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956, 1957]

### Verbatim printed entry text (OCR)

**Version `col1948-L34831.v` — printed in editions [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956, 1957]:**

> MUNDY, John Cloudesley, C.M.G. (1947).—b. 1900; ed. Varndean, Brighton; on mil. serv. 1918 (R.A.F.); asst. instr. taxes, U.K., 1920; instr. taxes, 1922; comsnt., inland rev., Ken., 1937; comsnt., income tax, E.A., 1940; introduced income tax, Ken., 1937 and T.T., Uga. and Zanz., 1940; fin. mem., E.A.H.C., 1948.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1918–1918 | mil. serv. | — | [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956, 1957] |
| 1 | 1920–1920 | asst. instr. taxes | United Kingdom | [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956, 1957] |
| 2 | 1922–1922 | instr. taxes | — | [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956, 1957] |
| 3 | 1937–1937 | comsnt., inland rev. | Kenya | [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956, 1957] |
| 4 | 1937–1940 | — | Kenya, Tanganyika Territory, Uganda and Zanzibar | [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956, 1957] |
| 5 | 1940–1940 | comsnt., income tax | East Africa | [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956, 1957] |
| 6 | 1948–1948 | fin. mem. | East Africa High Commission | [1948, 1949, 1950, 1951, 1953, 1954, 1955, 1956, 1957] |

## Candidate stint `Mundy, J. C___Kenya___1939`

- Staff-list name: **Mundy, J. C** | colony: **Kenya** | listed 1939–1948 | editions [1939, 1940, 1946, 1948]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | J. C. Mundy | Commissioner | Inland Revenue | — | — |
| 1940 | J. C. Mundy | Commissioner | Inland Revenue | — | — |
| 1946 | J. C. Mundy | Commissioner of Inland Revenue | Nominated Official Members | — | — |
| 1948 | J. C. Mundy | Commissioner for Inland Revenue | Legislative Council | C.M.G. | — |

### Deterministic checks: `mundy_john-cloudesley_b1900` vs `Mundy, J. C___Kenya___1939`

- [PASS] surname_gate: bio 'MUNDY' vs stint 'Mundy, J. C' (exact)
- [PASS] initials: bio ['J', 'C'] ~ stint ['J', 'C']
- [PASS] age_gate: stint starts 1939, birth 1900 (age 39)
- [PASS] colony: 1 placed event(s) resolve to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1939-1948
- [FAIL] position_sim: no overlapping placed event to compare
- [PASS] honour: shared: C.M.G.
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

