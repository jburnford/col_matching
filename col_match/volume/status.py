"""Per-bio career-status classifier for the within-volume pilot.

A services-section biography is cumulative: it lists a person's whole career to
date, so in any single edition many people are NOT currently holding a colonial
post and therefore SHOULD NOT have a roster record in that volume. Treating
those as "missed links" is wrong — they are correct non-links. This module
labels each bio with its status as of the edition year so the link denominator
can exclude them:

  active         — last dated posting is in a Colonial-Office colony, no
                   terminal marker → a current roster record is expected.
  retired        — retired / pensioned / "placed on retired list".
  died           — died / deceased.
  resigned       — resigned.
  transferred_out— last posting is in an administration NOT covered by the
                   Colonial Office List (India [India Office], Egypt / Sudan
                   [Foreign Office], the UK home civil service, Ireland) — the
                   "moved on to India" case. No COL roster record expected.

Works on raw entry text even when the rules parser failed (unparsed bios), so
it is independent of parse success. Deterministic, no LLM.
"""

from __future__ import annotations

import re

from ..services import gazetteer

# Terminal markers, scanned near the END of the entry (last ~40% of clauses).
_DIED = re.compile(r"\b(died|deceased|d\.\s*1[89]\d\d)\b", re.I)
# "retired" is printed many ways: retired / retd. / ret. / ret'd / pensioned /
# "placed on the retired list" / superannuated / invalided. The bare "ret."
# abbreviation is the common one and must be matched (with its dot, to avoid
# "return"/"retained").
_RETIRED = re.compile(
    r"\b(retired|ret'?d\.?|ret\.|on pension|pensioned|placed on (the )?retired list"
    r"|superannuated|invalided)", re.I)
_RESIGNED = re.compile(r"\b(resigned|resig(?:ned)?\.)", re.I)

# Administrations / locations NOT in the Colonial Office List rosters. A bio
# whose CURRENT (last) posting is here has correctly no COL record. Normalized
# (lowercase, alpha-only) to match gazetteer.norm output.
_NON_COL_PLACES = {
    "india", "britishindia", "bengal", "bombay", "madras", "punjab",
    "burma", "burmah",                       # India Office
    "egypt", "sudan", "angloegyptiansudan",  # Foreign Office / condominium
    "england", "scotland", "ireland", "wales", "london",
    "unitedkingdom", "greatbritain", "home",  # UK home service
}
# Words that, as a place, mean the UK home establishment rather than a colony.
_HOME_HINT = re.compile(r"\b(home civil|home serv|war office|foreign office"
                        r"|board of trade|treasury, london|india office)\b", re.I)


def _last_placed_event(events: list[dict]) -> dict | None:
    placed = [e for e in events if e.get("place") and e.get("year_start")]
    if not placed:
        return None
    return max(placed, key=lambda e: e["year_start"])


def _tail(text: str) -> str:
    """The last portion of the entry, where terminal markers live (avoids a
    mid-career 'resigned from the army' false positive)."""
    parts = re.split(r"\s*;\s*", text)
    return "; ".join(parts[-max(2, len(parts) // 3):])


def classify_status(raw_text: str, events: list[dict], edition_year: int) -> dict:
    """Return {status, expect_record, reason, last_year, last_place}."""
    tail = _tail(raw_text)
    last = _last_placed_event(events)
    last_year = last["year_start"] if last else None
    last_place = last.get("place") if last else None

    # terminal markers (search the tail so mid-career mentions don't trip)
    if _DIED.search(tail):
        return _r("died", False, "death marker", last_year, last_place)
    if _RETIRED.search(tail):
        return _r("retired", False, "retired/pensioned marker", last_year, last_place)
    if _RESIGNED.search(tail):
        return _r("resigned", False, "resigned marker", last_year, last_place)

    # current posting outside the COL universe ("moved on to India")
    if last_place:
        n = gazetteer.norm(gazetteer.lookup(last_place, _data_dir()) or last_place)
        if n in _NON_COL_PLACES:
            return _r(f"transferred_out:{last_place}", False,
                      "current posting outside Colonial Office List", last_year, last_place)
    if _HOME_HINT.search(tail):
        return _r("transferred_out:home", False,
                  "home/other-office posting", last_year, last_place)

    return _r("active", True, "current colonial posting", last_year, last_place)


# data_dir is only needed for gazetteer.lookup of the last place; resolve lazily
# from config so callers need not thread it through.
_DATA_DIR: str | None = None


def _data_dir() -> str:
    global _DATA_DIR
    if _DATA_DIR is None:
        from ..config import Config
        _DATA_DIR = Config.from_env().data_dir
    return _DATA_DIR


def _r(status, expect, reason, last_year, last_place) -> dict:
    return {"status": status, "expect_record": expect, "reason": reason,
            "last_year": last_year, "last_place": last_place}
