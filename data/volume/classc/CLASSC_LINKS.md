# Applied class-C links (career -> bio person)

- 'same' verdicts scored: 13,688
- applied: 10,559 pairs / 10,559 careers (tier1 6,801, tier2 3,006, tier3 skeptic 752); corroboration {'llm_only': 3006, 'hard': 989, 'place': 6468, 'possim': 96}
- not linked (FINAL under this policy — no review required): 3,129 (ambiguous careers: 178)

## Verification basis

34 pairs read closely across strata + 10/10 skeptic-tier promotions
verified (July 2026). Every false positive failed the exact-initials
test; every policy-passing pair was correct (0 observed FPs in the
applied strata). LLM confidence is uniform (90-95) and was NOT used;
corroboration is recomputed deterministically; tier3 additionally
requires the skeptic's quoted appointment to ground in the person's
events.

## Link-rate lift (roster careers with a bio identity)

- before: 23,226 / 179,147 careers (13.0%)
- after:  33,785 / 179,147 (18.9%)

Links are an OVERLAY (career_person_links.jsonl) joining careers.jsonl
on career_id; careers.jsonl itself is untouched (it stays the product
of the within-volume linker).
