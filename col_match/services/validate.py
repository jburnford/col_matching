"""Validation gates applied identically to BOTH parser tiers.

A ParsedEntry that fails any fatal gate is not accepted: rules-tier failures
route to the LLM tier; LLM-tier failures retry/escalate and finally land in
failures/*.jsonl for hand review. Warnings travel on ParsedEntry.flags.
"""

from __future__ import annotations

from rapidfuzz import fuzz

from .schema import EntryVersion, ParsedEntry

BIRTH_MIN = 1770
EVENT_MIN = 1800
SPAN_SIM = 92.0          # event text_span must align to the canonical text
MAX_INVERSIONS = 2       # entries occasionally group clauses by topic


def validate_parsed(parsed: ParsedEntry, version: EntryVersion) -> list[str]:
    """Return fatal errors (empty list = accepted). Mutates parsed.flags
    with non-fatal warnings."""
    fatal: list[str] = []
    edition = version.edition_year

    if not parsed.surname or not parsed.surname.strip():
        fatal.append("no_surname")
    if not parsed.events:
        fatal.append("no_events")

    if parsed.birth_year is not None and not (BIRTH_MIN <= parsed.birth_year <= edition):
        fatal.append(f"birth_year_out_of_range:{parsed.birth_year}")

    years: list[int] = []
    for i, ev in enumerate(parsed.events):
        for y in (ev.year_start, ev.year_end):
            if y is None:
                continue
            if not (EVENT_MIN <= y <= edition + 1):
                fatal.append(f"event_year_out_of_range:{i}:{y}")
        if ev.year_start is not None:
            years.append(ev.year_start)
        # hallucination gate (trivially true for rules parses)
        if fuzz.partial_ratio(ev.text_span, version.canonical_text) < SPAN_SIM:
            fatal.append(f"span_not_in_text:{i}")

    inversions = sum(1 for a, b in zip(years, years[1:]) if b < a - 1)
    if inversions > MAX_INVERSIONS:
        fatal.append(f"chronology_inversions:{inversions}")

    if parsed.birth_year is not None and years and min(years) < parsed.birth_year + 13:
        fatal.append("event_before_age_13")

    if parsed.terminal is not None and parsed.terminal.year is not None:
        if not (EVENT_MIN <= parsed.terminal.year <= edition + 1):
            fatal.append(f"terminal_year_out_of_range:{parsed.terminal.year}")

    if not fatal and inversions:
        parsed.flags.append(f"chronology_inversions:{inversions}")
    return fatal
