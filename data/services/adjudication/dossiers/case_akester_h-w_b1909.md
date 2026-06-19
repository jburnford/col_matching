<!-- {"case_id": "case_akester_h-w_b1909", "bio_ids": ["akester_h-w_b1909"], "stint_ids": ["Akester, H. W___Gold Coast___1950"]} -->
# Dossier case_akester_h-w_b1909

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `akester_h-w_b1909`

- Printed name: **AKESTER, H. W**
- Birth year: 1909 (attested in editions [1956])
- Appears in editions: [1956]

### Verbatim printed entry text (OCR)

**Version `col1956-L19361.v` — printed in editions [1956]:**

> AKESTER, H. W.—b. 1909; b'cast offr., G.C., 1945; tech. supt., 1953; chief tech. supt., b'casting, G.C. local serv., 1955.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1945 | b'cast offr. | Gold Coast | [1956] |
| 1 | 1953 | tech. supt | Gold Coast *(inherited from previous clause)* | [1956] |
| 2 | 1955 | chief tech. supt., b'casting, G.C. local serv | Gold Coast | [1956] |

## Candidate stint `Akester, H. W___Gold Coast___1950`

- Staff-list name: **Akester, H. W** | colony: **Gold Coast** | listed 1950–1951 | editions [1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1950 | H. W. Akester | Senior Broadcast Officers | Broadcasting | — | — |
| 1951 | H. W. Akester | Senior Broadcast Engineers and Broadcast Engineers | Broadcasting | — | — |

### Deterministic checks: `akester_h-w_b1909` vs `Akester, H. W___Gold Coast___1950`

- [PASS] surname_gate: bio 'AKESTER' vs stint 'Akester, H. W' (exact)
- [PASS] initials: bio ['H', 'W'] ~ stint ['H', 'W']
- [PASS] age_gate: stint starts 1950, birth 1909 (age 41)
- [PASS] colony: 3 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1950-1951
- [FAIL] position_sim: best 57 vs bar 60: 'b'cast offr.' ~ 'Senior Broadcast Officers'
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

