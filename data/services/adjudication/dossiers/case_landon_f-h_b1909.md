<!-- {"case_id": "case_landon_f-h_b1909", "bio_ids": ["landon_f-h_b1909"], "stint_ids": ["Lanzon, F___Malta___1925"]} -->
# Dossier case_landon_f-h_b1909

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `landon_f-h_b1909`

- Printed name: **LANDON, F. H**
- Birth year: 1909 (attested in editions [1956])
- Appears in editions: [1956]

### Verbatim printed entry text (OCR)

**Version `col1956-L22401.v` — printed in editions [1956]:**

> LANDON, F. H.—b. 1909 ; ed. Winchester Coll. and Oxford Univ.; mil. serv., 1944-45; asst. consvr., forests, F.M.S., 1932; instr., forest sch., 1938; senr. asst. consvr., 1942; sec. G.C., 1943-44; silviculturist, 1945; consvr., ch. research offr., 1954; del. to 4th world forestry cong., Dehra Dun, 1954.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1932 | asst. consvr., forests | Federated Malay States | [1956] |
| 1 | 1938 | instr., forest sch | Federated Malay States *(inherited from previous clause)* | [1956] |
| 2 | 1942 | senr. asst. consvr | Federated Malay States *(inherited from previous clause)* | [1956] |
| 3 | 1943–1944 | sec. G.C | Federated Malay States *(inherited from previous clause)* | [1956] |
| 4 | 1945 | silviculturist | Federated Malay States *(inherited from previous clause)* | [1956] |
| 5 | 1954 | consvr., ch. research offr | Federated Malay States *(inherited from previous clause)* | [1956] |

## Candidate stint `Lanzon, F___Malta___1925`

- Staff-list name: **Lanzon, F** | colony: **Malta** | listed 1925–1937 | editions [1925, 1929, 1930, 1931, 1933, 1934, 1936, 1937]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1925 | F. Lanzon | Clerks, 1st Class | Treasury | — | — |
| 1929 | F. Lanzon | Clerks, 1st Class | Treasury | — | — |
| 1930 | F. Lanzon | Clerks, 1st Class | Treasury | — | — |
| 1931 | F. Lanzon | Examining Officer (Clerk, 1st Class) | Emigration Department | — | — |
| 1933 | F. Lanzon | Examining Officer (Clerk, 1st Class) | Emigration Department | — | — |
| 1934 | F. Lanzon | Examining Officer (Clerk, 1st Class) | Emigration Department | — | — |
| 1936 | F. Lanzon | Chief Clerk and Examining Officer | Emigration Department | — | — |
| 1937 | F. Lanzon | Chief Clerk and Examining Officer | Emigration Department | — | — |

### Deterministic checks: `landon_f-h_b1909` vs `Lanzon, F___Malta___1925`

- [PASS] surname_gate: bio 'LANDON' vs stint 'Lanzon, F' (fuzzy:1)
- [PASS] initials: bio ['F', 'H'] ~ stint ['F']
- [PASS] age_gate: stint starts 1925, birth 1909 (age 16)
- [FAIL] colony: no placed event resolves to 'Malta'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1925-1937
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

