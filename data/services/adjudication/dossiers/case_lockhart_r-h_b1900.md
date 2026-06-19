<!-- {"case_id": "case_lockhart_r-h_b1900", "bio_ids": ["lockhart_r-h_b1900"], "stint_ids": ["Lockhart, R. H___Leeward Islands___1950"]} -->
# Dossier case_lockhart_r-h_b1900

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 24 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `lockhart_r-h_b1900`

- Printed name: **LOCKHART, R. H**
- Birth year: 1900 (attested in editions [1953, 1954, 1955, 1956, 1957])
- Appears in editions: [1953, 1954, 1955, 1956, 1957]

### Verbatim printed entry text (OCR)

**Version `col1953-L18178.v` — printed in editions [1953, 1954, 1955, 1956, 1957]:**

> LOCKHART, R. H.—b. 1900; ed. Lycée Schoelcher, Martinique, and Xaverian Coll., Clapham; called to bar, Middle Temple; mag. and crown atty., Montserrat, 1949; cr. atty., Antigua, 1954.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1949 | mag. and crown atty. | Montserrat | [1953, 1954, 1955, 1956, 1957] |
| 1 | 1954 | cr. atty. | Antigua | [1953, 1954, 1955, 1956, 1957] |

## Candidate stint `Lockhart, R. H___Leeward Islands___1950`

- Staff-list name: **Lockhart, R. H** | colony: **Leeward Islands** | listed 1950–1957 | editions [1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | R. H. Lockhart | Crown Attorney-Magistrate | JUDICIAL | — | — |
| 1950 | R. H. Lockhart | Magistrate | Magistrates | — | — |
| 1951 | R. H. Lockhart | Crown Attorney-Magistrate | Judicial | — | — |
| 1951 | R. H. Lockhart | Magistrate | Legal | — | — |
| 1951 | R. H. Lockhart | Crown Attorney | Executive Council | — | — |
| 1952 | R. H. Lockhart | Crown Attorney-Magistrate | Civil Establishment | — | — |
| 1952 | R. H. Lockhart | Crown Attorney | Executive Council | — | — |
| 1953 | R. H. Lockhart | Crown Attorney-Magistrate (Registrar, Provost-Marshal) | Civil Establishment | — | — |
| 1954 | R. H. Lockhart | Crown Attorney-Magistrate (Registrar, Provost-Marshal) | Civil Establishment | — | — |
| 1955 | R. H. Lockhart | Crown Attorney | Civil Establishment | — | — |
| 1955 | R. H. Lockhart | Crown Attorney | Legislative Council | — | — |
| 1956 | R. H. Lockhart | Crown Attorney | Civil Establishment | — | — |
| 1957 | R. H. Lockhart | Crown Attorney | Civil Establishment | — | — |
| 1957 | R. H. Lockhart | Crown Attorney | Executive Council | — | — |

### Deterministic checks: `lockhart_r-h_b1900` vs `Lockhart, R. H___Leeward Islands___1950`

- [PASS] surname_gate: bio 'LOCKHART' vs stint 'Lockhart, R. H' (exact)
- [PASS] initials: bio ['R', 'H'] ~ stint ['R', 'H']
- [PASS] age_gate: stint starts 1950, birth 1900 (age 50)
- [FAIL] colony: no placed event resolves to 'Leeward Islands'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1950-1957
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

