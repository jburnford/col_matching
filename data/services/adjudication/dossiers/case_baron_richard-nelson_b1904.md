<!-- {"case_id": "case_baron_richard-nelson_b1904", "bio_ids": ["baron_richard-nelson_b1904"], "stint_ids": ["Baron, R. N___Sarawak___1940"]} -->
# Dossier case_baron_richard-nelson_b1904

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 3 official(s) with this surname in the graph's staff lists; 4 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `baron_richard-nelson_b1904`

- Printed name: **BARON, Richard Nelson**
- Birth year: 1904 (attested in editions [1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951, 1954]

### Verbatim printed entry text (OCR)

**Version `col1949-L30264.v` — printed in editions [1949, 1950, 1951]:**

> BARON, Richard Nelson.—b. 1904; ed. Framlingham Coll. and Selwyn Coll., Camb., B.A. (hons.) (Cantab.); survr., Sarawak, 1928; asst. supt., 1933; supt., land and surveys dept., 1941; civ. intern., 1941-46; comsnr. for natl. regist., 1949.

**Version `col1954-L19461.v` — printed in editions [1954]:**

> BARON, R. N.—b. 1904; ed. Framlingham Coll. and Selwyn Coll., Camb.; survr., Sarawak, 1928; asst. supt., land and surv. dept., 1933; supt., 1941; state survr., Brunei, 1953; comsnr., nat. regn., 1949.

**Version `col1948-L30992.v` — printed in editions [1948]:**

> BARON, Richard Nelson.—b. 1904; ed. Cambridge Univ., B.A. (hons.) (Cantab.); asst. survr., Sarawak, 1928; supt., land and surveys dept.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1928 | survr. | Sarawak | [1948, 1949, 1950, 1951, 1954] |
| 1 | 1933 | asst. supt | Sarawak *(inherited from previous clause)* | [1949, 1950, 1951, 1954] |
| 2 | 1941 | supt., land and surveys dept | Sarawak *(inherited from previous clause)* | [1949, 1950, 1951, 1954] |
| 3 | 1949 | comsnr. for natl. regist | Sarawak *(inherited from previous clause)* | [1949, 1950, 1951, 1954] |
| 4 | 1953 | state survr. | Brunei | [1954] |

## Candidate stint `Baron, R. N___Sarawak___1940`

- Staff-list name: **Baron, R. N** | colony: **Sarawak** | listed 1940–1951 | editions [1940, 1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1940 | R. N. Baron | Assistants, Lands and Surveys Dept. | Civil Establishment | — | — |
| 1949 | R. N. Baron | Superintendent of Lands and Surveys | Lands and Surveys | — | — |
| 1950 | R. N. Baron | Superintendent of Lands and Surveys | LANDS AND SURVEYS | — | — |
| 1951 | R. N. Baron | Superintendent of Lands and Surveys | Lands and Surveys | — | — |

### Deterministic checks: `baron_richard-nelson_b1904` vs `Baron, R. N___Sarawak___1940`

- [PASS] surname_gate: bio 'BARON' vs stint 'Baron, R. N' (exact)
- [PASS] initials: bio ['R', 'N'] ~ stint ['R', 'N']
- [PASS] age_gate: stint starts 1940, birth 1904 (age 36)
- [PASS] colony: 4 placed event(s) resolve to 'Sarawak'
- [PASS] tenure_overlap: 3 event tenure(s) overlap stint years 1940-1951
- [PASS] position_sim: best 76 vs bar 60: 'supt., land and surveys dept' ~ 'Assistants, Lands and Surveys Dept.'
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

