<!-- {"case_id": "case_james_a-w-d_b1916", "bio_ids": ["james_a-w-d_b1916"], "stint_ids": ["James, A. W___Fiji___1939"]} -->
# Dossier case_james_a-w-d_b1916

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 79 official(s) with this surname in the graph's staff lists; 42 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `james_a-w-d_b1916`

- Printed name: **JAMES, A. W. D**
- Birth year: 1916 (attested in editions [1953, 1954, 1955, 1956, 1957])
- Honours: D.F.C (1945)
- Appears in editions: [1953, 1954, 1955, 1956, 1957]

### Verbatim printed entry text (OCR)

**Version `col1953-L17928.v` — printed in editions [1953, 1954, 1955, 1956, 1957]:**

> JAMES, A. W. D., D.F.C. (1945).—b. 1916; ed. The Edin. Acad. and Magdalen Coll., Oxford; mil. serv., 1939-46; cadet, M.C.S., 1939; S.O., cl. I, Chinese affrs., B.M.A. (M.), 1945; cl. IV, D.O., Christmas Is., 1946; asst. comsnr., labour (Chinese), Perak, 1949; dep. comsnr., N. Sembilan, 1949; cl. III, 1950; head, emergency inf. serv., 1951; cl. IC, dep. Mal. estab. offr., 1952; ag. dep. sec., Chinese affrs., 1955.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1939 | cadet, M.C.S | — | [1953, 1954, 1955, 1956, 1957] |
| 1 | 1945 | S.O., cl. I, Chinese affrs., B.M.A. (M.) | — | [1953, 1954, 1955, 1956, 1957] |
| 2 | 1946 | cl. IV, D.O., Christmas Is | Dominions Office | [1953, 1954, 1955, 1956, 1957] |
| 3 | 1949 | asst. comsnr., labour (Chinese), Perak | Dominions Office *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957] |
| 4 | 1950 | cl. III | Dominions Office *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957] |
| 5 | 1951 | head, emergency inf. serv | Dominions Office *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957] |
| 6 | 1952 | cl. IC, dep. Mal. estab. offr | Dominions Office *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957] |
| 7 | 1955 | ag. dep. sec., Chinese affrs | Dominions Office *(inherited from previous clause)* | [1953, 1954, 1955, 1956, 1957] |

## Candidate stint `James, A. W___Fiji___1939`

- Staff-list name: **James, A. W** | colony: **Fiji** | listed 1939–1940 | editions [1939, 1940]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1939 | A. W. James | Senior Customs Officer, Grade II | Customs Department | — | — |
| 1940 | A. W. James | Senior Customs Officer, Grade II | Customs Department | — | — |

### Deterministic checks: `james_a-w-d_b1916` vs `James, A. W___Fiji___1939`

- [PASS] surname_gate: bio 'JAMES' vs stint 'James, A. W' (exact)
- [PASS] initials: bio ['A', 'W', 'D'] ~ stint ['A', 'W']
- [PASS] age_gate: stint starts 1939, birth 1916 (age 23)
- [FAIL] colony: no placed event resolves to 'Fiji'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1939-1940
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

