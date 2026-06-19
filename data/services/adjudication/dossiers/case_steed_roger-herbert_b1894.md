<!-- {"case_id": "case_steed_roger-herbert_b1894", "bio_ids": ["steed_roger-herbert_b1894"], "stint_ids": ["Steed, R. H___Straits Settlements___1933"]} -->
# Dossier case_steed_roger-herbert_b1894

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 2 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `steed_roger-herbert_b1894`

- Printed name: **STEED, ROGER HERBERT**
- Birth year: 1894 (attested in editions [1939, 1940])
- Honours: M.I.C.E
- Appears in editions: [1939, 1940]

### Verbatim printed entry text (OCR)

**Version `col1939-L70869.v` — printed in editions [1939, 1940]:**

> STEED, ROGER HERBERT, M.I.C.E., Chtd.civ. engrn.—B. 1894; ed Dulwich Coll.; war serv., 1915-19; asst. engtn., P.W.D., Malaya, Feb., 1924; supt., stores & furniture, S'pore, Oct., 1926; ag. ex. engrn., S'pore, Nov., 1929; ex., engrn., S'pore, Feb., 1933; ag. senr. ex. engrn., hdgtrs., Jan., 1933.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1924 | asst. engtn., P.W.D. | Malaya | [1939, 1940] |
| 1 | 1926 | supt., stores & furniture, S'pore | Malaya *(inherited from previous clause)* | [1939, 1940] |
| 2 | 1929 | ag. ex. engrn., S'pore | Malaya *(inherited from previous clause)* | [1939, 1940] |
| 3 | 1933 | ex., engrn., S'pore | Malaya *(inherited from previous clause)* | [1939, 1940] |

## Candidate stint `Steed, R. H___Straits Settlements___1933`

- Staff-list name: **Steed, R. H** | colony: **Straits Settlements** | listed 1933–1934 | editions [1933, 1934]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1933 | R. H. Steed | Assistant Engineers | Public Works | — | — |
| 1934 | R. H. Steed | Executive Engineer | Public Works | — | — |

### Deterministic checks: `steed_roger-herbert_b1894` vs `Steed, R. H___Straits Settlements___1933`

- [PASS] surname_gate: bio 'STEED' vs stint 'Steed, R. H' (exact)
- [PASS] initials: bio ['R', 'H'] ~ stint ['R', 'H']
- [PASS] age_gate: stint starts 1933, birth 1894 (age 39)
- [FAIL] colony: no placed event resolves to 'Straits Settlements'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1933-1934
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

