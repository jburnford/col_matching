<!-- {"case_id": "case_koram_e-m_b1914", "bio_ids": ["koram_e-m_b1914"], "stint_ids": ["Koram, E. M___Gold Coast___1949"]} -->
# Dossier case_koram_e-m_b1914

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `koram_e-m_b1914`

- Printed name: **KORAM, E. M**
- Birth year: 1914 (attested in editions [1956])
- Appears in editions: [1956]

### Verbatim printed entry text (OCR)

**Version `col1956-L22368.v` — printed in editions [1956]:**

> KORAM, E. M.—b. 1914; ed. Msant-sipim Sch., Achimota Coll. and Queen Mary Coll.; prob. asst. engnr., G.C., 1941; engnr., 1944; regl. engnr., 1952; dep. dir. and engnr.-in-chief, G.C. local serv., 1955.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1941 | prob. asst. engnr. | Gold Coast | [1956] |
| 1 | 1944 | engnr | Gold Coast *(inherited from previous clause)* | [1956] |
| 2 | 1952 | regl. engnr | Gold Coast *(inherited from previous clause)* | [1956] |
| 3 | 1955 | dep. dir. and engnr.-in-chief, G.C. local serv | Gold Coast | [1956] |

## Candidate stint `Koram, E. M___Gold Coast___1949`

- Staff-list name: **Koram, E. M** | colony: **Gold Coast** | listed 1949–1951 | editions [1949, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | E. M. Koram | Engineers | Posts and Telegraphs | — | — |
| 1951 | E. M. Koram | Engineers | Engineering Branch | — | — |

### Deterministic checks: `koram_e-m_b1914` vs `Koram, E. M___Gold Coast___1949`

- [PASS] surname_gate: bio 'KORAM' vs stint 'Koram, E. M' (exact)
- [PASS] initials: bio ['E', 'M'] ~ stint ['E', 'M']
- [PASS] age_gate: stint starts 1949, birth 1914 (age 35)
- [PASS] colony: 4 placed event(s) resolve to 'Gold Coast'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1949-1951
- [PASS] position_sim: best 71 vs bar 60: 'engnr' ~ 'Engineers'
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

