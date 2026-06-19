<!-- {"case_id": "case_grunberg_s_b1910", "bio_ids": ["grunberg_s_b1910"], "stint_ids": ["Grunberg, S___Gold Coast___1949"]} -->
# Dossier case_grunberg_s_b1910

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- WARNING: biography(ies) ['grunberg_s_b1910'] carry a single initial only — the namesake trap applies.

## Biography `grunberg_s_b1910`

- Printed name: **GRUNBERG, S**
- Birth year: 1910 (attested in editions [1956])
- Appears in editions: [1956]

### Verbatim printed entry text (OCR)

**Version `col1956-L21586.v` — printed in editions [1956]:**

> GRUNBERG, S.—b. 1910; ed. Brighton Coll. and City and Guilds Coll.; asst. engrnr., G.C. rly., 1939; senr. engrnr., 1946; dep. chief engrnr., 1950 (G.C. local serv.).

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1939 | asst. engrnr., G.C. rly | Gold Coast | [1956] |
| 1 | 1946 | senr. engrnr | Gold Coast *(inherited from previous clause)* | [1956] |
| 2 | 1950 | dep. chief engrnr | Gold Coast *(inherited from previous clause)* | [1956] |

## Candidate stint `Grunberg, S___Gold Coast___1949`

- Staff-list name: **Grunberg, S** | colony: **Gold Coast** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | S. Grunberg | Senior Engineers | Railway and Takoradi Harbour | — | — |
| 1951 | S. Grunberg | Senior Engineers | Engineering Branch | — | — |

### Deterministic checks: `grunberg_s_b1910` vs `Grunberg, S___Gold Coast___1949`

- [PASS] surname_gate: bio 'GRUNBERG' vs stint 'Grunberg, S' (exact)
- [PASS] initials: bio ['S'] ~ stint ['S']
- [PASS] age_gate: stint starts 1949, birth 1910 (age 39)
- [PASS] colony: 3 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [PASS] position_sim: best 74 vs bar 60: 'senr. engrnr' ~ 'Senior Engineers'
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

