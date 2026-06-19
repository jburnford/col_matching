<!-- {"case_id": "case_hodge_henry-parnell_b1887", "bio_ids": ["hodge_henry-parnell_b1887"], "stint_ids": ["Hodge, H. P___Straits Settlements___1931"]} -->
# Dossier case_hodge_henry-parnell_b1887

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 14 official(s) with this surname in the graph's staff lists; 8 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hodge_henry-parnell_b1887`

- Printed name: **HODGE, HENRY PARNELL**
- Birth year: 1887 (attested in editions [1935, 1936, 1937, 1940])
- Honours: L.S.T.M, R.A.M.C
- Appears in editions: [1935, 1936, 1937, 1940]

### Verbatim printed entry text (OCR)

**Version `dol1935-L59455.v` — printed in editions [1935, 1936, 1937, 1940]:**

> HODGE, HENRY PARNELL, CAPT., R.A.M.C., B.A. (Oxon.), L.M.S.S.A. (Loud.), Grad., L.S.T.M.—B. 1887; med. offr., S.S., May, 1923; med. offr., S'pore, June, 1923; do., K. Lumpur, July, 1923; do., Coast, Selangor, Aug., 1923; do., Pahang, May, 1925; do., gen. hosp., K. Lumpur, Aug., 1928; med. offr., Coast, Selangor, Aug., 1933; superscale offr., grade B, May, 1935.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1923 | med. offr. | Straits Settlements | [1935, 1936, 1937, 1940] |
| 1 | 1925 | do., Pahang | Straits Settlements *(inherited from previous clause)* | [1935, 1936, 1937, 1940] |
| 2 | 1928 | do., gen. hosp., K. Lumpur | Straits Settlements *(inherited from previous clause)* | [1935, 1936, 1937, 1940] |
| 3 | 1933 | med. offr., Coast, Selangor | Straits Settlements *(inherited from previous clause)* | [1935, 1936, 1937, 1940] |
| 4 | 1935 | superscale offr., grade B | Straits Settlements *(inherited from previous clause)* | [1935, 1936, 1937, 1940] |

## Candidate stint `Hodge, H. P___Straits Settlements___1931`

- Staff-list name: **Hodge, H. P** | colony: **Straits Settlements** | listed 1931–1933 | editions [1931, 1932, 1933]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1931 | H. P. Hodge | Medical Officer | Medical | — | — |
| 1932 | H. P. Hodge | Medical Officer | Medical | — | — |
| 1933 | H. P. Hodge | Medical Officer | Medical | — | — |

### Deterministic checks: `hodge_henry-parnell_b1887` vs `Hodge, H. P___Straits Settlements___1931`

- [PASS] surname_gate: bio 'HODGE' vs stint 'Hodge, H. P' (exact)
- [PASS] initials: bio ['H', 'P'] ~ stint ['H', 'P']
- [PASS] age_gate: stint starts 1931, birth 1887 (age 44)
- [PASS] colony: 5 placed event(s) resolve to 'Straits Settlements'
- [PASS] tenure_overlap: 2 event tenure(s) overlap stint years 1931-1933
- [FAIL] position_sim: best 47 vs bar 60: 'med. offr., Coast, Selangor' ~ 'Medical Officer'
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

