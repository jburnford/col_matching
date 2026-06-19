<!-- {"case_id": "case_tullock_h_b1914", "bio_ids": ["tullock_h_b1914"], "stint_ids": ["Tulloch, G. H___Kenya___1931"]} -->
# Dossier case_tullock_h_b1914

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 6 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['tullock_h_b1914'] carry a single initial only — the namesake trap applies.

## Biography `tullock_h_b1914`

- Printed name: **TULLOCK, H**
- Birth year: 1914 (attested in editions [1961, 1962])
- Appears in editions: [1961, 1962]

### Verbatim printed entry text (OCR)

**Version `col1961-L28205.v` — printed in editions [1961, 1962]:**

> TULLOCK, H.—b. 1914; ed. Firth Public (Secondary) Sch.; mil. serv., 1933-39; prisons and police serv., Shanghai, 1939-43; p.o.w. 1943-45; consulate-gen., Shanghai, 1945-46; asst. supt., prisons, Nig., 1947; supt., 1952; senr. supt., S. Leone, 1956; dep. dir., prisons, 1956-61.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1939–1943 | prisons and police serv., Shanghai | — | [1961, 1962] |
| 1 | 1943–1945 | p.o.w | — | [1961, 1962] |
| 2 | 1945–1946 | consulate-gen., Shanghai | — | [1961, 1962] |
| 3 | 1947 | asst. supt., prisons | Nigeria | [1961, 1962] |
| 4 | 1952 | supt | Nigeria *(inherited from previous clause)* | [1961, 1962] |
| 5 | 1956 | senr. supt., S. Leone | Nigeria *(inherited from previous clause)* | [1961, 1962] |

## Candidate stint `Tulloch, G. H___Kenya___1931`

- Staff-list name: **Tulloch, G. H** | colony: **Kenya** | listed 1931–1934 | editions [1931, 1932, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | G. H. Tulloch | Technical Instructors | Prisons Department | — | — |
| 1932 | G. H. Tulloch | Technical Instructors | Prisons Department | — | — |
| 1934 | G. H. Tulloch | Technical Instructor | Prisons Department | — | — |

### Deterministic checks: `tullock_h_b1914` vs `Tulloch, G. H___Kenya___1931`

- [PASS] surname_gate: bio 'TULLOCK' vs stint 'Tulloch, G. H' (fuzzy:1)
- [PASS] initials: bio ['H'] ~ stint ['G', 'H']
- [PASS] age_gate: stint starts 1931, birth 1914 (age 17)
- [FAIL] colony: no placed event resolves to 'Kenya'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1931-1934
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

