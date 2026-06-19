<!-- {"case_id": "case_hodgson_peter-charles_b1910", "bio_ids": ["hodgson_peter-charles_b1910"], "stint_ids": ["Hodgson, P. C___Gambia___1949"]} -->
# Dossier case_hodgson_peter-charles_b1910

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 37 official(s) with this surname in the graph's staff lists; 21 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `hodgson_peter-charles_b1910`

- Printed name: **HODGSON, Peter Charles**
- Birth year: 1910 (attested in editions [1948, 1949, 1950, 1951])
- Appears in editions: [1948, 1949, 1950, 1951]

### Verbatim printed entry text (OCR)

**Version `col1948-L33382.v` — printed in editions [1948, 1949, 1950, 1951]:**

> HODGSON, Peter Charles.—b. 1910; ed. Wellington Coll. (exhibir.) and Corpus Christi Coll., Camb. (schol. and prize-man), M.A. (Cantab.); barrister-at-law, Middle Temple; cadet, Nig., 1934; asst. dist. offr., 1937; dist. offr., 1944; comsnr., Gam., 1944.

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1934 | cadet | Nigeria | [1948, 1949, 1950, 1951] |
| 1 | 1937 | asst. dist. offr | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |
| 2 | 1944 | dist. offr | Nigeria *(inherited from previous clause)* | [1948, 1949, 1950, 1951] |

## Candidate stint `Hodgson, P. C___Gambia___1949`

- Staff-list name: **Hodgson, P. C** | colony: **Gambia** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | P. C. Hodgson | Commissioner | ADMINISTRATIVE SERVICE (including Secretariat) | — | — |
| 1950 | P. C. Hodgson | Assistant Commissioner | Administrative Service | — | — |
| 1951 | P. C. Hodgson | Commissioners, Senior Assistant Secretary, Assistant Commissioners, Assistant Secretaries | Administrative Service | — | — |

### Deterministic checks: `hodgson_peter-charles_b1910` vs `Hodgson, P. C___Gambia___1949`

- [PASS] surname_gate: bio 'HODGSON' vs stint 'Hodgson, P. C' (exact)
- [PASS] initials: bio ['P', 'C'] ~ stint ['P', 'C']
- [PASS] age_gate: stint starts 1949, birth 1910 (age 39)
- [FAIL] colony: no placed event resolves to 'Gambia'
- [FAIL] tenure_overlap: no colony-agreeing tenure overlaps stint years 1949-1951
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

