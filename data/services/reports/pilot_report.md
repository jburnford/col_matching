# Services-section pipeline — pilot report (2026-06-11)

Review gate before the full LLM batch and downstream phases (compile → match
→ coverage). Everything below ran locally; total LLM spend so far: **< $0.10**
(one 60-entry pilot batch + 3 escalations).

## Corpus and segmentation (free, done)

- **62 services-bearing volumes** found (COL 1883–1966 except 1946 + 1952,
  plus Dominions Office List 1935). 1952's absence is confirmed by its own
  preface (paper shortage); the density-based section detector correctly
  returned "no section" for it.
- **199,099 raw entries** segmented. Section bounds match known header
  locations in every checked volume. Multi-line entries join correctly
  (verified on known page-wrapped cases).
- Same-volume double prints detected and collapsed: 1,369 twin pairs
  (1939: 567, 1909: 499, 1928: 175, others small).

## Cross-edition dedup (free, done)

- 199,099 instances → **42,231 distinct entry-versions** (4.7×), 4.5s runtime.
- Sanity: Guggisberg's 9 appearances (1920–1930) → exactly 1 chain, longest
  text canonical. 5,608 versions attested in 10+ editions.

## Tiered parsing

- **Rules tier: 77.0%** (32,522/42,231) parsed and validated deterministically.
- **9,709 entries → LLM tier** (narrative careers, leading-year formats,
  multi-date clauses, OCR-damaged dashes).
- Tier routing is strict: any clause containing a year that doesn't parse
  cleanly fails the whole entry to the LLM; position strings never contain
  embedded years; both tiers pass identical validation gates.

## Accuracy evidence

**Gold set** (28 blind-annotated entries across 7 eras; 20 rules-tier
evaluated now, 8 are LLM-tier and measured after the main batch):

| metric | result | target |
|---|---|---|
| surname | 20/20 | ≥97% |
| given names | 20/20 | — |
| birth year | 19/20 (miss = genuine "L. 1865" OCR) | ≥97% |
| event recall | 73/73 (100%) | ≥90% |
| event precision | 77/78 (99%) | ≥90% |
| place accuracy (matched, gold-placed) | 25/27 | — |
| position accuracy (matched) | 72/73 | — |

**Twin check** (1,172 double-printed pairs = two independent OCR readings of
the same plate, both rules-parsed and compared): surname agreement 99.3%,
birth year 93.0%, full event-year sequence 77.4%, event count 95.2%.
→ Single-reading OCR flips a year digit ~1.7% of the time per year. This is
an OCR (not parser) error bound, and it motivates compile-stage year voting
across attesting editions (planned, cheap: regex year-tokens per attestation,
flag minority readings).

**LLM tier pilot** (60-entry batch on gemini-flash-lite-latest): 57/60
accepted first pass; validation gates caught 1 span hallucination and
1 chronology violation (both recovered on escalation to flash-latest);
1 hard failure is a genuine career-less stub entry (honour-holder, no
postings) — correctly rejected.

## Cost to finish parsing

- Full LLM batch: 9,709 entries ≈ 5.8M input + 3.4M output tokens
  → **~$1 on flash-lite batch** (worst case ~$5 if everything escalated to
  flash). Turnaround ≤24h, usually much faster.

## Known limitations (current state)

- Inherited places (place persists across clauses until restated) are
  flagged `place_inherited` — matching will treat them as weaker evidence.
- DRAYSON-style OCR'd birth markers ("L. 1865") are lost to rules; recoverable
  only if we later vote across attestations or let the LLM see those.
- 2 of 28 gold entries have place subtleties still imperfect (office vs
  posting during secondment).

## Next (pending approval)

1. Submit full LLM batch (~$1), harvest + escalate failures, re-run gold eval
   on the 8 LLM-tier entries.
2. Compile per-person biographies (cross-version merge, year voting,
   per-fact edition provenance).
3. Bulk-fetch graph stints (read-only), match biographies → stints
   (≥2 independent agreements), produce the coverage report.
