<!-- {"case_id": "case_field_henry-trevor-cromwell_b1891", "bio_ids": ["field_henry-trevor-cromwell_b1891"], "stint_ids": ["Field, H. T. C___Nigeria___1929"]} -->
# Dossier case_field_henry-trevor-cromwell_b1891

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 38 official(s) with this surname in the graph's staff lists; 18 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `field_henry-trevor-cromwell_b1891`

- Printed name: **FIELD, HENRY TREVOR CROMWELL**
- Birth year: 1891 (attested in editions [1933, 1934, 1935, 1936])
- Appears in editions: [1933, 1934, 1935, 1936, 1940]

### Verbatim printed entry text (OCR)

**Version `col1933-L59730.v` — printed in editions [1933, 1934, 1935, 1936]:**

> FIELD, HENRY TREVOR CROMWELL.—B. 1891; ed. St. John's Schl., Leatherhead and Queen's Coll., Cambridge (B.A.); on war serv., 1914-18; demob. (capt.) 1919; inspr. and schoolmast., S.P., Nigeria, 1922; supt., educn., 1926; prin., govt. coll., Ibadan, 1932.

**Version `col1940-L64227.v` — printed in editions [1940]:**

> FIELD, HENRY TREVOR CROMWELL.—B. 1891; ED. ST. JOHN'S SCHL., LEATHERHEAD AND QUEEN'S COLL., CAMBRIDGE (B.A.); ON WAR SERV., 1914-18; DEMOB. (CAPT.) 1919; INSPR. AND SCHOOLMASTER, S.P., NIGERIA, 1922; SUPT., EDUC., 1926; PRIN., GOVT. COLL., IBADAN, 1932.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1919 | demob. (capt.) | — | [1933, 1934, 1935, 1936, 1940] |
| 1 | 1922 | inspr. and schoolmast., S.P. | Nigeria | [1933, 1934, 1935, 1936, 1940] |
| 2 | 1926 | supt., educn | Nigeria *(inherited from previous clause)* | [1933, 1934, 1935, 1936, 1940] |
| 3 | 1932 | prin., govt. coll., Ibadan | Nigeria *(inherited from previous clause)* | [1933, 1934, 1935, 1936, 1940] |

## Candidate stint `Field, H. T. C___Nigeria___1929`

- Staff-list name: **Field, H. T. C** | colony: **Nigeria** | listed 1929–1930 | editions [1929, 1930]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | H. Field | Superintendent (Bandmaster) | Marine | — | — |
| 1930 | Capt. H. T. C. Field | Superintendent of Education | Education | — | Captain |
| 1930 | H. Field | Superintendent (Bandmaster) | Police | — | — |

### Deterministic checks: `field_henry-trevor-cromwell_b1891` vs `Field, H. T. C___Nigeria___1929`

- [PASS] surname_gate: bio 'FIELD' vs stint 'Field, H. T. C' (exact)
- [PASS] initials: bio ['H', 'T', 'C'] ~ stint ['H', 'T', 'C']
- [PASS] age_gate: stint starts 1929, birth 1891 (age 38)
- [PASS] colony: 3 placed event(s) resolve to 'Nigeria'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1929-1930
- [FAIL] position_sim: best 54 vs bar 60: 'supt., educn' ~ 'Superintendent of Education'
- [FAIL] honour: no shared honour
- [not met] edition_cooccurrence (strict corroboration bonus — same edition-year with colony-agreeing position match; absence is normal even for true matches and is NOT evidence against): no agreeing edition-years
- [FAIL] place_inherited: ALL supporting events inherit their place from an earlier clause — weak evidence

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

