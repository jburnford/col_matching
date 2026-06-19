<!-- {"case_id": "case_oleibo_abdul-razzak-ali_b1887", "bio_ids": ["oleibo_abdul-razzak-ali_b1887"], "stint_ids": ["Kleibo, Abdel Razak___Palestine___1924"]} -->
# Dossier case_oleibo_abdul-razzak-ali_b1887

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `oleibo_abdul-razzak-ali_b1887`

- Printed name: **OLEIBO, Abdul Razzak Ali**
- Birth year: 1887 (attested in editions [1948])
- Honours: O.B.E
- Appears in editions: [1948, 1949]

### Verbatim printed entry text (OCR)

**Version `col1948-L35375.v` — printed in editions [1948]:**

> OLEIBO, Abdul Razzak Ali, O.B.E.—b. 1887; ed. Rashidiya Sch., Jerusalem and Dar Ash-Shafaqa Coll., Constantinople; Turkish C.S., 1905–17; O.E.T.A., 1917; dist. admin., Pal., 1920; asst. dist. comsnr., 1946.

**Version `col1949-L35082.v` — printed in editions [1949]:**

> QLEIBO, Abdul Razzak Ali, O.B.E.—b. 1887; ed. Rashidiya Sch., Jerus. and Dar Ash-Shafaqa Coll., Constan.; Turkish C.S., 1905–17; O.E.T.A., 1917; dist. admin., Pal., 1920; asst. dist. comsnr., 1946.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1905–1917 | Turkish C.S | — | [1948, 1949] |
| 1 | 1917 | O.E.T.A | — | [1948, 1949] |
| 2 | 1920 | dist. admin. | Palestine | [1948, 1949] |
| 3 | 1946 | asst. dist. comsnr | Palestine *(inherited from previous clause)* | [1948, 1949] |

## Candidate stint `Kleibo, Abdel Razak___Palestine___1924`

- Staff-list name: **Kleibo, Abdel Razak** | colony: **Palestine** | listed 1924–1932 | editions [1924, 1925, 1927, 1928, 1929, 1931, 1932]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1924 | Abdel Razak Kleibo | Assistant District Officer | Administrative Staff | — | — |
| 1925 | Abdel Razak Kleibo | Assistant District Officer | District Staff | — | — |
| 1927 | Abdel Razak Kleibo | Assistant District Officers | District Staff | — | — |
| 1928 | Abdel Razak Kleibo | Assistant District Officer | District Staff | — | — |
| 1929 | Abdel Razak Kleibo | Assistant District Officer | Civil Establishment | — | — |
| 1931 | Abdel Razak Kleibo | Assistant District Officer | District Staff | — | — |
| 1932 | Abdel Razak Kleibo | Assistant District Officer | District Staff | — | — |

### Deterministic checks: `oleibo_abdul-razzak-ali_b1887` vs `Kleibo, Abdel Razak___Palestine___1924`

- [PASS] surname_gate: bio 'OLEIBO' vs stint 'Kleibo, Abdel Razak' (fuzzy:1)
- [PASS] initials: bio ['A', 'R', 'A'] ~ stint ['A', 'R']
- [PASS] age_gate: stint starts 1924, birth 1887 (age 37)
- [PASS] colony: 2 placed event(s) resolve to 'Palestine'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1924-1932
- [FAIL] position_sim: best 44 vs bar 60: 'dist. admin.' ~ 'Assistant District Officer'
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

