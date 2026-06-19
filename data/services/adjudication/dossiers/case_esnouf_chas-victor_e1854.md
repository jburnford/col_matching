<!-- {"case_id": "case_esnouf_chas-victor_e1854", "bio_ids": ["esnouf_chas-victor_e1854"], "stint_ids": ["Esnouf, V___Mauritius___1877"]} -->
# Dossier case_esnouf_chas-victor_e1854

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 7 official(s) with this surname in the graph's staff lists; 3 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `esnouf_chas-victor_e1854`

- Printed name: **ESNOUF, CHAS. VICTOR**
- Birth year: not printed
- Appears in editions: [1883]

### Verbatim printed entry text (OCR)

**Version `col1883-L27365.v` — printed in editions [1883]:**

> ESNOUF, CHAS. VICTOR.—District and stipendiary magistrate at Black River, Mauritius, August, 1854; junior district magistrate, at Port Louis, Aug., 1857; master of supreme court, July, 1866.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1854 | District and stipendiary magistrate at Black River | Mauritius | [1883] |
| 1 | 1857 | junior district magistrate, at Port Louis | Mauritius *(inherited from previous clause)* | [1883] |
| 2 | 1866 | master of supreme court | Mauritius *(inherited from previous clause)* | [1883] |

## Candidate stint `Esnouf, V___Mauritius___1877`

- Staff-list name: **Esnouf, V** | colony: **Mauritius** | listed 1877–1883 | editions [1877, 1878, 1879, 1880, 1883]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1877 | V. Esnouf | Master | Supreme Court | — | — |
| 1878 | V. Esnouf | Master | Supreme Court | — | — |
| 1879 | V. Esnouf | Master | Supreme Court | — | — |
| 1880 | V. Esnouf | Master | Supreme Court | — | — |
| 1883 | V. Esnouf | Master | Supreme Court | — | — |

### Deterministic checks: `esnouf_chas-victor_e1854` vs `Esnouf, V___Mauritius___1877`

- [PASS] surname_gate: bio 'ESNOUF' vs stint 'Esnouf, V' (exact)
- [PASS] initials: bio ['C', 'V'] ~ stint ['V']
- [PASS] age_gate: stint starts 1877; no printed birth year — UNCHECKED
- [PASS] colony: 3 placed event(s) resolve to 'Mauritius'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1877-1883
- [PASS] position_sim: best 100 vs bar 60: 'master of supreme court' ~ 'Master'
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

