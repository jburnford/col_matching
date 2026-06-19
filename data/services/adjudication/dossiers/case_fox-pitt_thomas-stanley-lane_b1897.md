<!-- {"case_id": "case_fox-pitt_thomas-stanley-lane_b1897", "bio_ids": ["fox-pitt_thomas-stanley-lane_b1897"], "stint_ids": ["Fox-Pitt, T. S. L___Northern Rhodesia___1936"]} -->
# Dossier case_fox-pitt_thomas-stanley-lane_b1897

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `fox-pitt_thomas-stanley-lane_b1897`

- Printed name: **FOX-PITT, Thomas Stanley Lane**
- Birth year: 1897 (attested in editions [1948, 1949, 1950])
- Honours: O.B.E. (mil.)
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L32675.v` — printed in editions [1948, 1949, 1950]:**

> FOX-PITT, Thomas Stanley Lane, O.B.E. (mil.).—b. 1897; ed. St. David's, Reigate, R.N. Coll., Osborne and Dartmouth; on naval serv. 1914–18, lieut.; 1939–45, comdr.; cadet, R.N., 1910; cadet, N. Rhod. 1927; dist. offr., 1929; prov. comsnr., 1949.

**Version `col1951-L38174.v` — printed in editions [1951]:**

> FOX-PITT, Comdr. Thomas Stanley Lane, O.B.E. (mil.)—b. 1897; ed. St. David’s, Reigate and R.N.C., Osborne and Dartmouth; on naval serv., 1914-19 and 1939-46, comdr., R.N.; apptd. N. Rhod., 1927; prov. comsnr., 1949; naval mem., cont. comsn., Indo-China, 1945.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1910–1910 | cadet | — | [1948, 1949, 1950] |
| 1 | 1914–1918 | lieut. | — | [1948, 1949, 1950] |
| 2 | 1914–1946 | comdr., R.N. | — | [1951] |
| 3 | 1927–1927 | cadet | Northern Rhodesia | [1948, 1949, 1950, 1951] |
| 4 | 1929–1929 | dist. offr. | — | [1948, 1949, 1950] |
| 5 | 1939–1945 | comdr. | — | [1948, 1949, 1950] |
| 6 | 1945–1945 | naval mem., cont. comsn. | Indo-China | [1951] |
| 7 | 1949–1949 | prov. comsnr. | — | [1948, 1949, 1950, 1951] |

## Candidate stint `Fox-Pitt, T. S. L___Northern Rhodesia___1936`

- Staff-list name: **Fox-Pitt, T. S. L** | colony: **Northern Rhodesia** | listed 1936–1940 | editions [1936, 1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | T. S. L. Fox-Pitt | District Officers | District Administration | — | — |
| 1939 | T. S. L. Fox-Pitt | District Officer | District Administration | — | — |
| 1940 | T. S. L. Fox-Pitt | District Officer | District Administration | — | — |

### Deterministic checks: `fox-pitt_thomas-stanley-lane_b1897` vs `Fox-Pitt, T. S. L___Northern Rhodesia___1936`

- [PASS] surname_gate: bio 'FOX-PITT' vs stint 'Fox-Pitt, T. S. L' (exact)
- [PASS] initials: bio ['T', 'S', 'L'] ~ stint ['T', 'S', 'L']
- [PASS] age_gate: stint starts 1936, birth 1897 (age 39)
- [PASS] colony: 1 placed event(s) resolve to 'Northern Rhodesia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1936-1940
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

