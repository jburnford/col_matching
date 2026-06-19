<!-- {"case_id": "case_cruchley_i-h_b1902", "bio_ids": ["cruchley_i-h_b1902"], "stint_ids": ["Cruchley, I. H___Jamaica___1923"]} -->
# Dossier case_cruchley_i-h_b1902

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `cruchley_i-h_b1902`

- Printed name: **CRUCHLEY, I. H**
- Birth year: 1902 (attested in editions [1955, 1956, 1957, 1958, 1960, 1961, 1962, 1963, 1964, 1965, 1966])
- Appears in editions: [1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966]

### Verbatim printed entry text (OCR)

**Version `col1955-L20319.v` — printed in editions [1955, 1956, 1957, 1958, 1960, 1961, 1962, 1963, 1964, 1965, 1966]:**

> CRUCHLEY, I. H., Q.C.—b. 1902; ed. St. George's Coll., J'ca; barrister-at-law, Gray's Inn; res. mag., J'ca, 1950; solr.-gen., 1953; temp. legal asst., C.O., 1955; pub. Handbook on Bankruptcy Law and Practice.

**Version `col1959-L22119.v` — printed in editions [1959]:**

> CRUCHELEY, I. H., Q.C.—b. 1902; ed; St. George's Coll., J'ca; barrister-at-law, Gray's Inn; res. mag., J'ca, 1950; solr.-gen., 1953; temp. legal asst., C.O., 1955; pub. Handbook on Bankruptcy Law and Practice.

**Version `col1954-L20085.v` — printed in editions [1954]:**

> CRUCHEY, I. H., Q.C.—b. 1902; ed. St. George's Coll., J'ca; barrister-at-law, Gray's Inn; res. mag., J'ca, 1950; solr.-gen., 1953; pub. Handbook on Bankruptcy Law and Practice.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1950 | res. mag. | Jamaica | [1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 1 | 1953 | solr.-gen | Jamaica *(inherited from previous clause)* | [1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |
| 2 | 1955 | temp. legal asst. | Colonial Office | [1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966] |

## Candidate stint `Cruchley, I. H___Jamaica___1923`

- Staff-list name: **Cruchley, I. H** | colony: **Jamaica** | listed 1923–1925 | editions [1923, 1925]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1923 | I. Cruchley | Assistants | Post Office | — | — |
| 1925 | I. Cruchley | Assistants | Post Office | — | — |

### Deterministic checks: `cruchley_i-h_b1902` vs `Cruchley, I. H___Jamaica___1923`

- [PASS] surname_gate: bio 'CRUCHLEY' vs stint 'Cruchley, I. H' (exact)
- [PASS] initials: bio ['I', 'H'] ~ stint ['I', 'H']
- [PASS] age_gate: stint starts 1923, birth 1902 (age 21)
- [PASS] colony: 2 placed event(s) resolve to 'Jamaica'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1923-1925
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

