<!-- {"case_id": "case_beadon_e-h-f_b1907", "bio_ids": ["beadon_e-h-f_b1907"], "stint_ids": ["Beadon, E. H. F___Trinidad and Tobago___1952"]} -->
# Dossier case_beadon_e-h-f_b1907

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `beadon_e-h-f_b1907`

- Printed name: **BEADON, E. H. F**
- Birth year: 1907 (attested in editions [1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963])
- Appears in editions: [1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963]

### Verbatim printed entry text (OCR)

**Version `col1951-L36038.v` — printed in editions [1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963]:**

> BEADON, E. H. F., O.B.E. (mil.), Burma police medal.—b. 1907; mil. serv., 1945, lt.-col.; asst. supt. police, I.P.S. (Burma), 1926; supt., 1935; asst. dir., intell. bureau, India, 1942; supt. police, Burma, 1945; comsnr., Trin., 1949–62. (T'dad Govt. service.)

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1926 | asst. supt. police, I.P.S. (Burma) | — | [1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 1 | 1935 | supt | — | [1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 2 | 1942 | asst. dir., intell. bureau, India | — | [1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 3 | 1945 | supt. police, Burma | — | [1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |
| 4 | 1949–1962 | comsnr. | Trinidad | [1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963] |

## Candidate stint `Beadon, E. H. F___Trinidad and Tobago___1952`

- Staff-list name: **Beadon, E. H. F** | colony: **Trinidad and Tobago** | listed 1952–1962 | editions [1952, 1953, 1954, 1962]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1952 | E. H. F. Beadon | Commissioner of Police | Civil Establishment | — | Colonel |
| 1953 | E. H. F. Beadon | Commissioner of Police | Civil Establishment | — | — |
| 1954 | E. H. F. Beadon | Commissioner of Police | Civil Establishment | O.B.E. | — |
| 1962 | E. H. F. Beadon | Commissioner of Police | Civil Establishment | — | — |

### Deterministic checks: `beadon_e-h-f_b1907` vs `Beadon, E. H. F___Trinidad and Tobago___1952`

- [PASS] surname_gate: bio 'BEADON' vs stint 'Beadon, E. H. F' (exact)
- [PASS] initials: bio ['E', 'H', 'F'] ~ stint ['E', 'H', 'F']
- [PASS] age_gate: stint starts 1952, birth 1907 (age 45)
- [FAIL] colony: no placed event resolves to 'Trinidad and Tobago'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1952-1962
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

