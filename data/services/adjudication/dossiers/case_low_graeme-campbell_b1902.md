<!-- {"case_id": "case_low_graeme-campbell_b1902", "bio_ids": ["low_graeme-campbell_b1902"], "stint_ids": ["Low, G. C___Uganda___1936"]} -->
# Dossier case_low_graeme-campbell_b1902

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 30 official(s) with this surname in the graph's staff lists; 13 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `low_graeme-campbell_b1902`

- Printed name: **LOW, Graeme Campbell**
- Birth year: 1902 (attested in editions [1948, 1949, 1950, 1951, 1953, 1954, 1955])
- Appears in editions: [1948, 1949, 1950, 1951, 1953, 1954, 1955]

### Verbatim printed entry text (OCR)

**Version `col1948-L34151.v` — printed in editions [1948, 1949, 1950, 1951, 1953, 1954, 1955]:**

> LOW, Graeme Campbell.—b. 1902; ed. Charterhouse and Magdalen Coll., Oxford; B.A.; barrister-at-law; on mil. serv., 1940-41 and naval serv., 1942-46, sub-lieut.; appt. judicial dept., Uga., 1935; res. mag.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1935 | appt. judicial dept. | Uganda | [1948, 1949, 1950, 1951, 1953, 1954, 1955] |

## Candidate stint `Low, G. C___Uganda___1936`

- Staff-list name: **Low, G. C** | colony: **Uganda** | listed 1936–1955 | editions [1936, 1937, 1939, 1940, 1949, 1951, 1953, 1954, 1955]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | G. C. Low | Senior Magistrates and Magistrates (for the township of Entebbe, Kampala, Jinja and Mabale) | Legal Department | — | — |
| 1937 | G. C. Low | Magistrate | Judicial | — | — |
| 1939 | G. C. Low | Senior Magistrate | Judicial | — | — |
| 1940 | G. C. Low | Resident Magistrate | Judicial | — | — |
| 1949 | G. C. Low | Resident Magistrates | JUDICIAL | — | — |
| 1951 | G. C. Low | Puisne Judges | Judicial | — | — |
| 1953 | G. C. Low | Puise Judges | Civil Establishment | — | — |
| 1954 | G. C. Low | Puisne Judges | Civil Establishment | — | — |
| 1955 | G. C. Low | Puisne Judge | Civil Establishment | — | — |

### Deterministic checks: `low_graeme-campbell_b1902` vs `Low, G. C___Uganda___1936`

- [PASS] surname_gate: bio 'LOW' vs stint 'Low, G. C' (exact)
- [PASS] initials: bio ['G', 'C'] ~ stint ['G', 'C']
- [PASS] age_gate: stint starts 1936, birth 1902 (age 34)
- [PASS] colony: 1 placed event(s) resolve to 'Uganda'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1936-1955
- [FAIL] position_sim: best 33 vs bar 60: 'appt. judicial dept.' ~ 'Puise Judges'
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

