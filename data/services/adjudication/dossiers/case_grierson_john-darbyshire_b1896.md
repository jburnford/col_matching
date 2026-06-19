<!-- {"case_id": "case_grierson_john-darbyshire_b1896", "bio_ids": ["grierson_john-darbyshire_b1896"], "stint_ids": ["Grierson, J. D___British Guiana___1929"]} -->
# Dossier case_grierson_john-darbyshire_b1896

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 4 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `grierson_john-darbyshire_b1896`

- Printed name: **GRIERSON, JOHN DARBYSHIRE**
- Birth year: 1896 (attested in editions [1939])
- Appears in editions: [1939]

### Verbatim printed entry text (OCR)

**Version `col1939-L67244.v` — printed in editions [1939]:**

> GRIERSON, JOHN DARBYSHIRE, M.B., Ch.B., U. Edin., F.R.C.S., Edin., F.R.C.S., Eng.—B. 1896; med. ser., B. Guiana, 1927; res. surg. and surg. spec., pub. hosp., 1931. ag. aast. dist. offr., K. Selangor, Apr., 1916; passed cadets' law exam., Dec., 1917; Malay. offr., grade II, Jan., 1918; ditto, grade I, Jan., 1919; ditto, spl. cls., Jan., 1920; offr., cls. V, Oct., 1921; asst. offr. assignee, Perak, Jan., 1923; offr. cls. IV, dist. offr., Temerloh, Oct., 1925; 2nd mag., K. Lumpur, June, 1929; dist. offr., K. Langat, Feb., 1930; offr. cls. III, mag., Seremban, Oct., 1930; dist. offr., U. Selangor, May, 1934; offr. cls. II., Oct., 1935.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1916 | ag. aast. dist. offr. | Kuala Selangor | [1939] |
| 1 | 1917 | — | — | [1939] |
| 2 | 1918 | Malay. offr., grade II | — | [1939] |
| 3 | 1919 | ditto, grade I | — | [1939] |
| 4 | 1920 | ditto, spl. cls. | — | [1939] |
| 5 | 1921 | offr., cls. V | — | [1939] |
| 6 | 1923 | asst. offr. assignee | Perak | [1939] |
| 7 | 1925 | offr. cls. IV, dist. offr. | Temerloh | [1939] |
| 8 | 1927 | med. ser. | British Guiana | [1939] |
| 9 | 1929 | 2nd mag. | Kuala Lumpur | [1939] |
| 10 | 1930 | dist. offr. | Kuala Langat | [1939] |
| 11 | 1930 | offr. cls. III, mag. | Seremban | [1939] |
| 12 | 1931 | res. surg. and surg. spec., pub. hosp. | — | [1939] |
| 13 | 1934 | dist. offr. | Ulu Selangor | [1939] |
| 14 | 1935 | offr. cls. II. | — | [1939] |

## Candidate stint `Grierson, J. D___British Guiana___1929`

- Staff-list name: **Grierson, J. D** | colony: **British Guiana** | listed 1929–1930 | editions [1929, 1930]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1929 | J. D. Grierson | Surgeon Specialist, Public Hospital, Georgetown | Medical Department | — | — |
| 1930 | J. D. Grierson | Surgeon Specialist, Public Hospital, Georgetown | Medical Department | — | — |

### Deterministic checks: `grierson_john-darbyshire_b1896` vs `Grierson, J. D___British Guiana___1929`

- [PASS] surname_gate: bio 'GRIERSON' vs stint 'Grierson, J. D' (exact)
- [PASS] initials: bio ['J', 'D'] ~ stint ['J', 'D']
- [PASS] age_gate: stint starts 1929, birth 1896 (age 33)
- [PASS] colony: 1 placed event(s) resolve to 'British Guiana'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1929-1930
- [FAIL] position_sim: best 19 vs bar 60: 'med. ser.' ~ 'Surgeon Specialist, Public Hospital, Georgetown'
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

