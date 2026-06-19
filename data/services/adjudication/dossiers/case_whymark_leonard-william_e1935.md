<!-- {"case_id": "case_whymark_leonard-william_e1935", "bio_ids": ["whymark_leonard-william_e1935"], "stint_ids": ["Whymark, L. W___Cyprus___1949"]} -->
# Dossier case_whymark_leonard-william_e1935

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Whymark, L. W___Cyprus___1949` is also gate-compatible with biography(ies) outside this case: ['whymack_leonard-william_e1935'] (already linked elsewhere or filtered).

## Biography `whymark_leonard-william_e1935`

- Printed name: **WHYMARK, Leonard William**
- Birth year: not printed
- Appears in editions: [1950]

### Verbatim printed entry text (OCR)

**Version `col1950-L40709.v` — printed in editions [1950]:**

> WHYMARK, Leonard William.—ed. Gram. Sch., Hampton-on-Thames; on mil. serv., 1939-45, lieut.; apptd. police, Pal., 1935; asst. supt., 1945; Cyp., 1945.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1935 | apptd. police | Palestine | [1950] |
| 1 | 1945 | asst. supt | Cyprus | [1950] |

## Candidate stint `Whymark, L. W___Cyprus___1949`

- Staff-list name: **Whymark, L. W** | colony: **Cyprus** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | L. W. Whymark | Superintendents and Assistant Superintendents of Police | POLICE | — | — |
| 1951 | L. W. Whymark | Superintendent/Assistant Superintendent of Police | Police | — | — |

### Deterministic checks: `whymark_leonard-william_e1935` vs `Whymark, L. W___Cyprus___1949`

- [PASS] surname_gate: bio 'WHYMARK' vs stint 'Whymark, L. W' (exact)
- [PASS] initials: bio ['L', 'W'] ~ stint ['L', 'W']
- [PASS] age_gate: stint starts 1949; no printed birth year — UNCHECKED
- [PASS] colony: 1 placed event(s) resolve to 'Cyprus'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 38 vs bar 60: 'asst. supt' ~ 'Superintendents and Assistant Superintendents of Police'
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

