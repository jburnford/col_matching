<!-- {"case_id": "case_temper_frederic-gordon_e1872", "bio_ids": ["temper_frederic-gordon_e1872"], "stint_ids": ["Kemper, G___Bermuda___1932"]} -->
# Dossier case_temper_frederic-gordon_e1872

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `temper_frederic-gordon_e1872`

- Printed name: **TEMPER, FREDERIC GORDON**
- Birth year: not printed
- Appears in editions: [1899, 1900]

### Verbatim printed entry text (OCR)

**Version `col1899-L37608.v` — printed in editions [1899, 1900]:**

> TEMPER, FREDERIC GORDON.—Ed. at Harrow and at Trin. Coll., Camb.; called to the bar, Inn. Tem., Nov., 1872; went the W. circuit; apptd. dist. judge, Kyrenia, Cyprus, 1882; ag. puisne judge, sup. ct., May to Oct., 1888; Nov., 1888, to Feb., 1889; Jan. to March, 1890; and May to Sept., 1891; dist. judge, Larnaka, 1891; Queen’s advoc., Cyprus, 1893; county ct. judge, York, 1898.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1872–1872 | called to the bar | — | [1899, 1900] |
| 1 | 1882–1882 | dist. judge | Cyprus | [1899, 1900] |
| 2 | 1888–1888 | ag. puisne judge, sup. ct. | — | [1899, 1900] |
| 3 | 1890–1890 | ag. puisne judge, sup. ct. | — | [1899, 1900] |
| 4 | 1891–1891 | ag. puisne judge, sup. ct. | — | [1899, 1900] |
| 5 | 1891–1891 | dist. judge | — | [1899, 1900] |
| 6 | 1893–1893 | Queen’s advoc. | Cyprus | [1899, 1900] |
| 7 | 1898–1898 | county ct. judge | — | [1899, 1900] |

## Candidate stint `Kemper, G___Bermuda___1932`

- Staff-list name: **Kemper, G** | colony: **Bermuda** | listed 1932–1934 | editions [1932, 1933, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1932 | G. Kemper | Consul | Foreign Consuls. | — | — |
| 1933 | G. Kemper | Consul | Foreign Consuls | — | — |
| 1934 | G. Kemper | Consul | Foreign Consuls | — | — |

### Deterministic checks: `temper_frederic-gordon_e1872` vs `Kemper, G___Bermuda___1932`

- [PASS] surname_gate: bio 'TEMPER' vs stint 'Kemper, G' (fuzzy:1)
- [PASS] initials: bio ['F', 'G'] ~ stint ['G']
- [PASS] age_gate: stint starts 1932; no printed birth year — UNCHECKED
- [FAIL] colony: no placed event resolves to 'Bermuda'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1932-1934
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

