<!-- {"case_id": "case_redhead_george-anthony_b1898", "bio_ids": ["redhead_george-anthony_b1898"], "stint_ids": ["Redhead, G. A___Grenada___1963", "Redhead, G. A___Windward Islands___1939"]} -->
# Dossier case_redhead_george-anthony_b1898

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 12 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `redhead_george-anthony_b1898`

- Printed name: **REDHEAD, George Anthony**
- Birth year: 1898 (attested in editions [1949, 1950, 1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1961])
- Appears in editions: [1949, 1950, 1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961]

### Verbatim printed entry text (OCR)

**Version `col1949-L35162.v` — printed in editions [1949, 1950, 1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1961]:**

> REDHEAD, George Anthony.—b. 1898; ed. Grenada Boys Sec. Sch.; solr., sup. ct., Windward and Leeward Is.; dist. offr., Northern Dist. and mag., Dominica, 1944.

**Version `col1960-L27253.v` — printed in editions [1960]:**

> REDEHEAD, G. A.—b. 1898; ed. Grenada Boys’ Sec. Sch.; solr., sup. ct., Wind. and Leeward Is.; dist. offr., N. dist., and mag., Dominica, 1944–59.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1944 | dist. offr., Northern Dist. and mag. | Dominica | [1949, 1950, 1951, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961] |

## Candidate stint `Redhead, G. A___Grenada___1963`

- Staff-list name: **Redhead, G. A** | colony: **Grenada** | listed 1963–1964 | editions [1963, 1964]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1963 | G. A. Redhead | Magistrate (Northern and Western) | Civil Establishment | — | — |
| 1964 | G. A. Redhead | Magistrate, Eastern | Civil Establishment | — | — |

### Deterministic checks: `redhead_george-anthony_b1898` vs `Redhead, G. A___Grenada___1963`

- [PASS] surname_gate: bio 'REDHEAD' vs stint 'Redhead, G. A' (exact)
- [PASS] initials: bio ['G', 'A'] ~ stint ['G', 'A']
- [PASS] age_gate: stint starts 1963, birth 1898 (age 65)
- [FAIL] colony: no placed event resolves to 'Grenada'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1963-1964
- [FAIL] position_sim: no overlapping placed event to compare
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: no supporting events

## Candidate stint `Redhead, G. A___Windward Islands___1939`

- Staff-list name: **Redhead, G. A** | colony: **Windward Islands** | listed 1939–1950 | editions [1939, 1950]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | G. A. Redhead | — | Legislative Council | — | — |
| 1950 | G. A. Redhead | Magistrate, District “G” (see District Officer, Northern District) | JUDICIAL | — | — |

### Deterministic checks: `redhead_george-anthony_b1898` vs `Redhead, G. A___Windward Islands___1939`

- [PASS] surname_gate: bio 'REDHEAD' vs stint 'Redhead, G. A' (exact)
- [PASS] initials: bio ['G', 'A'] ~ stint ['G', 'A']
- [PASS] age_gate: stint starts 1939, birth 1898 (age 41)
- [FAIL] colony: no placed event resolves to 'Windward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1939-1950
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

