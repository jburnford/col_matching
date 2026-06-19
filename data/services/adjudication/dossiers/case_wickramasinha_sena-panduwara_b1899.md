<!-- {"case_id": "case_wickramasinha_sena-panduwara_b1899", "bio_ids": ["wickramasinha_sena-panduwara_b1899"], "stint_ids": ["Wickramasinha, S. P___Ceylon___1936"]} -->
# Dossier case_wickramasinha_sena-panduwara_b1899

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 2 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.
- NOTE: stint `Wickramasinha, S. P___Ceylon___1936` is also gate-compatible with biography(ies) outside this case: ['wickramasinha_sena-pandukabhaya_b1899'] (already linked elsewhere or filtered).

## Biography `wickramasinha_sena-panduwara_b1899`

- Printed name: **WICKRAMASINHA, SENA PANDUWARA**
- Birth year: 1899 (attested in editions [1925])
- Honours: B.A
- Appears in editions: [1925]

### Verbatim printed entry text (OCR)

**Version `col1925-L60347.v` — printed in editions [1925]:**

> WICKRAMASINHA, SENA PANDUWARA, B.A., LL.B. (Cantab.)—B. 1899; cadet, Ceylon civ. serv., Nov., 1922; att'd. to Matara in Dec., 1922; ditto, Batticaloa kach., Apr., 1923.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1922 | cadet, Ceylon civ. serv | Ceylon | [1925] |
| 1 | 1923 | ditto, Batticaloa kach | Ceylon *(inherited from previous clause)* | [1925] |

## Candidate stint `Wickramasinha, S. P___Ceylon___1936`

- Staff-list name: **Wickramasinha, S. P** | colony: **Ceylon** | listed 1936–1937 | editions [1936, 1937]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1936 | S. P. Wickramasinha | Assistant Settlement Officer | Land Settlement Department | — | — |
| 1937 | S. P. Wickramasinha | Deputy Rubber Controller | Rubber Controller | — | — |

### Deterministic checks: `wickramasinha_sena-panduwara_b1899` vs `Wickramasinha, S. P___Ceylon___1936`

- [PASS] surname_gate: bio 'WICKRAMASINHA' vs stint 'Wickramasinha, S. P' (exact)
- [PASS] initials: bio ['S', 'P'] ~ stint ['S', 'P']
- [PASS] age_gate: stint starts 1936, birth 1899 (age 37)
- [PASS] colony: 2 placed event(s) resolve to 'Ceylon'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1936-1937
- [FAIL] position_sim: best 33 vs bar 60: 'ditto, Batticaloa kach' ~ 'Assistant Settlement Officer'
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

