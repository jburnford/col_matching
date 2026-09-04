# Applied class-C links (career -> bio person)

- 'same' verdicts scored: 13,727
- applied: 10,009 pairs / 10,009 careers (tier1 7,003, tier2 2,879, tier3 skeptic/hard 99, hand 28); corroboration {'llm_only': 2887, 'hard': 1022, 'place': 6026, 'possim': 74}
- hand-ledger suppressions (silver-refuted links): 3
- not linked (FINAL under this policy — no review required): 3,718 (ambiguous careers: 143)

## Verification basis

34 pairs read closely across strata + 10/10 skeptic-tier promotions
verified (July 2026); 200-item silver standard 2026-07-12 (NOBIO_SILVER.md):
t1 28/28, t2 7/7, t3 11/14 -> t3 gated to det=hard 2026-09-04, the
three refuted t3 links suppressed via the hand ledger.
Every earlier false positive failed the exact-initials
test; every policy-passing pair was correct (0 observed FPs in the
applied strata). LLM confidence is uniform (90-95) and was NOT used;
corroboration is recomputed deterministically; tier3 additionally
requires the skeptic's quoted appointment to ground in the person's
events.

## Link-rate lift (roster careers with a bio identity)

- before: 20,516 / 179,033 careers (11.5%)
- after:  30,525 / 179,033 (17.0%)

Links are an OVERLAY (career_person_links.jsonl) joining careers.jsonl
on career_id; careers.jsonl itself is untouched (it stays the product
of the within-volume linker).
