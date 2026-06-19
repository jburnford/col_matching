<!-- {"case_id": "case_kirkcaldy-willis_w-h_b1914", "bio_ids": ["kirkcaldy-willis_w-h_b1914"], "stint_ids": ["Kirkaldy-Willis, W. H___Kenya___1949"]} -->
# Dossier case_kirkcaldy-willis_w-h_b1914

## Case context

- 1 biography(ies) and 1 candidate stint(s) are entangled in this case.
- Corpus context: 1 official(s) with this surname in the graph's staff lists; 1 biography(ies) with this surname in the printed biographical sections. The commoner the surname, the weaker any name-based inference.

## Biography `kirkcaldy-willis_w-h_b1914`

- Printed name: **KIRKCALDY-WILLIS, W. H.**
- Birth year: 1914 (attested in editions [1963, 1964])
- Appears in editions: [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964]

### Verbatim printed entry text (OCR)

**Version `col1963-L21656.v` — printed in editions [1963, 1964]:**

> KIRKCALDY-WILLIS, W. H.—b. 1914; ed. Marlborough Coll., The London Hosp., Royal Coll. of Surgeons; M.O., Ken., 1944; specialist, orthopaedic, 1953; senr. speclst., min. health and soc. affrs., 1962–63. (Ken. Govt. service.)

**Version `col1957-L24740.v` — printed in editions [1957, 1958, 1959, 1960]:**

> KIRKCALDY-WILLIS, W. H.—b. 1914; ed. Marlborough Coll., The London Hosp., Royal Coll. of Surgeons; M.O., Ken., 1944, specialist, orthopaedic, 1953; pubns. Cystoscopy in Bilharziasis (B.I.S.); Excision of Elbow (Lancet); Volvulus of Small Intestine (B.M.J.); Ischiofemoral Arthrodesis of Hip (J.B.J.S.).

**Version `col1962-L23158.v` — printed in editions [1962]:**

> KIRKCALDY-WILLIS, W. H.—b. 1914; ed. Marlborough Coll., The London Hosp.; Royal Coll. of Surgeons; M.O., Ken., 1944; specialist, orthopaedic, 1953.

**Version `col1961-L24127.v` — printed in editions [1961]:**

> KIRCALDY-WILLIS, W. H.—b. 1914; ed. Marlborough Coll., The London Hosp., Royal Coll. of Surgeons; M.O., Ken., 1944; specialist, orthopaedic, 1953; pubns. Cystoscopy in Bilharziasis (B.J.S.); Excision of Elbow (Lancet); Volvulus of Small Intestine (B.M.J.); Ischiofemoral Arthrodesis of Hip (J.B.J.S.).

### Compiled career timeline

| # | years | position | place | editions |
|---|-------|----------|-------|----------|
| 0 | 1944 | M.O. | Kenya | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 1 | 1953 | specialist, orthopaedic | Kenya *(inherited from previous clause)* | [1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964] |
| 2 | 1962–1963 | senr. speclst., min. health and soc. affrs | Kenya *(inherited from previous clause)* | [1963, 1964] |

## Candidate stint `Kirkaldy-Willis, W. H___Kenya___1949`

- Staff-list name: **Kirkaldy-Willis, W. H** | colony: **Kenya** | listed 1949–1951 | editions [1949, 1950, 1951]

### Year-by-year staff-list records

| year | name as printed | position | department | honours | rank |
|------|-----------------|----------|------------|---------|------|
| 1949 | W. H. Kirkaldy-Willis | Medical Officer | Medical | — | — |
| 1950 | W. H. Kirkaldy-Willis | Medical Officer | Medical | — | — |
| 1951 | W. H. Kirkaldy-Willis | Medical Officer | Medical | — | — |

### Deterministic checks: `kirkcaldy-willis_w-h_b1914` vs `Kirkaldy-Willis, W. H___Kenya___1949`

- [PASS] surname_gate: bio 'KIRKCALDY-WILLIS' vs stint 'Kirkaldy-Willis, W. H' (fuzzy:1)
- [PASS] initials: bio ['W', 'H'] ~ stint ['W', 'H']
- [PASS] age_gate: stint starts 1949, birth 1914 (age 35)
- [PASS] colony: 3 placed event(s) resolve to 'Kenya'
- [PASS] tenure_overlap: 1 event tenure(s) overlap stint years 1949-1951
- [FAIL] position_sim: best 24 vs bar 60: 'M.O.' ~ 'Medical Officer'
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

