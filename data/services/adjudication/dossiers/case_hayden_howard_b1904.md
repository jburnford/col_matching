<!-- {"case_id": "case_hayden_howard_b1904", "bio_ids": ["hayden_howard_b1904"], "stint_ids": ["Hayden, H___Fiji___1950", "Hayden, H___Western Pacific___1951"]} -->
# Dossier case_hayden_howard_b1904

## Case context

- 1 biography(ies) and 2 candidate stint(s) are entangled in this case.
- Corpus context: 10 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['hayden_howard_b1904'] carry a single initial only — the namesake trap applies.

## Biography `hayden_howard_b1904`

- Printed name: **HAYDEN, Howard**
- Birth year: 1904 (attested in editions [1953, 1954])
- Appears in editions: [1948, 1950, 1951, 1953, 1954]

### Verbatim printed entry text (OCR)

**Version `col1953-L17647.v` — printed in editions [1953, 1954]:**

> HAYDEN, H.—b. 1904; ed. Owens Sch. and Pembroke Coll., Camb.; dir. educ., Barb., 1943; Fiji, 1946; Trin., 1953; off. del. tr. Barb., W.I. cont., 1946 (chmn. drafting comttee.); Idr., Fiji del. to 7th Pac. science congress, N.Z., 1949; jt. author of Britain's Railways, 1938; School Drama, 1937; The Evaluation of Education in Barbados—a First Experiment, 1946, etc.

**Version `col1948-L33242.v` — printed in editions [1948]:**

> HAYDEN, Howard, M.A. (Cantab.).—b. 1904; ed. Owens Sch., Pembroke Coll., Cambridge, dip. in geog.; dir. of educ., Barb., 1943; dir. of educ., Fiji, 1946; Barb. del. and chmn., drafting comttee, W.I. Confce., 1946; jt. author of Britains Railways, 1938, School Drama, 1937, The Evaluation of Education in Barbados, 1946, etc.

**Version `col1950-L36235.v` — printed in editions [1950, 1951]:**

> HAYDEN, Howard, M.A. (Cantab.).—b. 1904; ed. Owens Sch. and Pembroke Coll., Camb., dip. geog.; dir., educ., Barb., 1943; Fiji, 1946; off. dist. fr. Barb. W.I. conf., 1946 (chmn., drafting comteee.); jt. auth. of Britain's Railways, 1938; School Drama, 1937; The Evaluation of Education in Barbados—a First Experiment, 1946, etc.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1943 | dir. educ. | Barbados | [1948, 1950, 1951, 1953, 1954] |
| 1 | 1946 | dir. educ. | Fiji | [1948, 1950, 1951, 1953, 1954] |
| 2 | 1946 | off. del. tr. Barb., W.I. cont. (chmn. drafting comttee.) | Barbados | [1948, 1950, 1951, 1953, 1954] |
| 3 | 1949 | Idr., Fiji del. to 7th Pac. science congress | New Zealand | [1953, 1954] |
| 4 | 1953 | dir. educ. | Trinidad | [1953, 1954] |

## Candidate stint `Hayden, H___Fiji___1950`

- Staff-list name: **Hayden, H** | colony: **Fiji** | listed 1950–1953 | editions [1950, 1951, 1952, 1953]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | H. Hayden | Director of Education | Education | — | — |
| 1951 | H. Hayden | Director of Education | Education | — | — |
| 1952 | H. Hayden | Director of Education | Civil Establishment | — | — |
| 1953 | H. Hayden | Director of Education | Civil Establishment | — | — |

### Deterministic checks: `hayden_howard_b1904` vs `Hayden, H___Fiji___1950`

- [PASS] surname_gate: bio 'HAYDEN' vs stint 'Hayden, H' (exact)
- [PASS] initials: bio ['H'] ~ stint ['H']
- [PASS] age_gate: stint starts 1950, birth 1904 (age 46)
- [PASS] colony: 1 placed event(s) resolve to 'Fiji'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1950-1953
- [FAIL] position_sim: best 55 vs bar 60: 'dir. educ.' ~ 'Director of Education'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [PASS] place_inherited: at least one supporting event names its place in print

## Candidate stint `Hayden, H___Western Pacific___1951`

- Staff-list name: **Hayden, H** | colony: **Western Pacific** | listed 1951–1953 | editions [1951, 1953]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1951 | H. Hayden | Adviser on Education | Civil Establishment | — | — |
| 1953 | H. Hayden | Adviser on Education | Civil Establishment | — | — |

### Deterministic checks: `hayden_howard_b1904` vs `Hayden, H___Western Pacific___1951`

- [PASS] surname_gate: bio 'HAYDEN' vs stint 'Hayden, H' (exact)
- [PASS] initials: bio ['H'] ~ stint ['H']
- [PASS] age_gate: stint starts 1951, birth 1904 (age 47)
- [FAIL] colony: no placed event resolves to 'Western Pacific'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1951-1953
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

