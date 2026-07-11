# Applied class-C links (career -> bio person)

- 'same' verdicts scored: 13,737
- applied: 10,555 pairs / 10,555 careers (tier1 6,711, tier2 3,104, tier3 skeptic 740); corroboration {'hard': 979, 'llm_only': 3104, 'place': 6367, 'possim': 105}
- not linked (FINAL under this policy — no review required): 3,182 (ambiguous careers: 175)

## Verification basis

34 pairs read closely across strata + 10/10 skeptic-tier promotions
verified (July 2026). Every false positive failed the exact-initials
test; every policy-passing pair was correct (0 observed FPs in the
applied strata). LLM confidence is uniform (90-95) and was NOT used;
corroboration is recomputed deterministically; tier3 additionally
requires the skeptic's quoted appointment to ground in the person's
events.

## Link-rate lift (roster careers with a bio identity)

- before: 23,152 / 179,148 careers (12.9%)
- after:  33,707 / 179,148 (18.8%)

Links are an OVERLAY (career_person_links.jsonl) joining careers.jsonl
on career_id; careers.jsonl itself is untouched (it stays the product
of the within-volume linker).
