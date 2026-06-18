"""Deterministic segmentation: locate the services section in a volume's
olmOCR markdown and split it into RawEntry records.

Detection is by entry *shape*, never by section headers (headers vary by era
and are absent in some volumes). All eras print the surname in CAPS followed
by a comma; the name block is separated from the career text by an em-dash.
The services section is found as the densest contiguous run of such lines.
"""

from __future__ import annotations

import re
from collections import defaultdict

from rapidfuzz import fuzz

from .corpus import Volume
from .schema import RawEntry

# Entry start: CAPS surname (allowing Mc/Mac/O'/De internal lowercase), comma.
_START = re.compile(r"^([A-Z][A-Za-z'’’\-]{1,}(?: [A-Z][A-Za-z'’’\-]+)*),\s+\S")
# Em-dash (or OCR'd en-dash) separating name block from career text.
_DASH = re.compile(r"[—–]")
# Page furniture / markdown artifacts to skip inside the section.
_FURNITURE = (
    re.compile(r"^\s*$"),
    re.compile(r"^[\divxlc .,—–-]{1,12}$", re.I),      # page numbers
    re.compile(r"^#{1,6}\s"),                                     # md headers
    re.compile(r"^[|!]"),                                         # tables, images
    re.compile(r"^[A-Z][A-Z &'’.,—–-]{2,70}$"),         # running heads (caps, no entry comma shape)
)

_WINDOW = 150          # lines per density window
_MIN_DENSITY = 8       # candidate starts per window to count as "inside"
_MIN_SECTION_STARTS = 300   # smallest plausible services section (entries)
_TWIN_SIM = 85.0       # same-volume duplicate threshold (1939 double print)


def _caps_fraction(surname: str) -> float:
    letters = [c for c in surname if c.isalpha()]
    if not letters:
        return 0.0
    return sum(1 for c in letters if c.isupper()) / len(letters)


def _is_start(line: str) -> bool:
    m = _START.match(line)
    if not m:
        return False
    # surname must be predominantly CAPS ("ABBOTT", "MACDONALD", "O'BRIEN",
    # "McCALLUM") — rejects index/title-case lines.
    return _caps_fraction(m.group(1)) >= 0.7


def _is_furniture(line: str) -> bool:
    if _is_start(line):
        return False
    return any(rx.match(line) for rx in _FURNITURE)


def _find_section(starts: list[int], n_lines: int) -> tuple[int, int] | None:
    """Densest contiguous region of entry-start lines -> (first, last) line idx."""
    if not starts:
        return None
    inside = [False] * (n_lines // _WINDOW + 2)
    counts = defaultdict(int)
    for ln in starts:
        counts[ln // _WINDOW] += 1
    for w, c in counts.items():
        if c >= _MIN_DENSITY:
            inside[w] = True
    # contiguous runs of dense windows (allow 1-window gaps: page furniture)
    runs: list[tuple[int, int, int]] = []  # (start_w, end_w, n_starts)
    w = 0
    while w < len(inside):
        if not inside[w]:
            w += 1
            continue
        end = w
        gap = 0
        for v in range(w + 1, len(inside)):
            if inside[v]:
                end, gap = v, 0
            else:
                gap += 1
                if gap > 1:
                    break
        n = sum(counts[x] for x in range(w, end + 1))
        runs.append((w, end, n))
        w = end + gap + 1
    runs = [r for r in runs if r[2] >= _MIN_SECTION_STARTS]
    if not runs:
        return None
    best = max(runs, key=lambda r: r[2])
    lo, hi = best[0] * _WINDOW, (best[1] + 1) * _WINDOW
    in_region = [ln for ln in starts if lo <= ln < hi]
    return in_region[0], in_region[-1]


def _join(cur: list[str]) -> str:
    """Join entry lines, de-hyphenating line-break hyphens."""
    out = ""
    for piece in cur:
        piece = piece.strip()
        if out.endswith("-") and piece and piece[0].islower():
            out = out[:-1] + piece
        else:
            out = (out + " " + piece).strip()
    return re.sub(r"\s+", " ", out)


def segment_volume(vol: Volume) -> tuple[list[RawEntry], dict]:
    """Segment one volume. Returns (entries, stats)."""
    lines = vol.path.read_text(encoding="utf-8").splitlines()
    start_idx = [i for i, ln in enumerate(lines) if _is_start(ln)]
    bounds = _find_section(start_idx, len(lines))
    stats: dict = {"volume": vol.name, "year": vol.year, "era": vol.era}
    if bounds is None:
        stats.update(section=None, entries=0)
        return [], stats
    lo, hi = bounds
    stats["section"] = [lo + 1, hi + 1]  # 1-based for humans

    entries: list[RawEntry] = []
    cur: list[str] = []
    cur_start = 0
    dropped_short = orphans = 0

    def close(end_idx: int) -> None:
        nonlocal dropped_short
        if not cur:
            return
        text = _join(cur)
        if len(text) < 25 and not _DASH.search(text):
            dropped_short += 1
        else:
            entries.append(
                RawEntry(
                    entry_id=f"{vol.slug}-L{cur_start + 1}",
                    volume=vol.name,
                    edition_year=vol.year,
                    era=vol.era,
                    line_start=cur_start + 1,
                    line_end=end_idx + 1,
                    raw_text=text,
                )
            )
        cur.clear()

    i = lo
    while i <= min(hi + 30, len(lines) - 1):  # +30: tail continuation lines
        ln = lines[i].strip()
        if _is_start(ln):
            if i > hi:
                break
            close(i - 1)
            cur_start = i
            cur.append(ln)
        elif not ln:
            # blank usually ends an entry; rescue page-break splits below
            if cur:
                # peek: if next content line is a continuation (non-start,
                # non-furniture) and current text looks unterminated, keep going
                j = i + 1
                while j < len(lines) and (not lines[j].strip() or _is_furniture(lines[j].strip())):
                    j += 1
                nxt = lines[j].strip() if j < len(lines) else ""
                unterminated = cur and not _join(cur).rstrip().endswith((".", ".)"))
                if nxt and not _is_start(nxt) and unterminated and j <= hi + 30:
                    i = j - 1  # skip the gap, continue accumulating
                else:
                    close(i - 1)
        elif _is_furniture(ln):
            pass
        elif cur:
            cur.append(ln)
        else:
            orphans += 1
        i += 1
    close(min(hi + 30, len(lines) - 1))

    entries, twins = _dedup_twins(entries)
    stats.update(
        entries=len(entries),
        twins=twins,
        dropped_short=dropped_short,
        orphan_lines=orphans,
        no_dash=sum(1 for e in entries if not _DASH.search(e.raw_text)),
    )
    return entries, stats


def _surname_key(text: str) -> str:
    head = text.split(",", 1)[0]
    return re.sub(r"[^A-Z]", "", head.upper())


def _dedup_twins(entries: list[RawEntry]) -> tuple[list[RawEntry], int]:
    """Collapse same-volume double prints (1939): near-identical entries with
    the same surname key. Keeper retains the twin's id/text for the
    consistency check. Distinct same-surname people survive (low similarity)."""
    by_key: dict[str, list[int]] = defaultdict(list)
    for idx, e in enumerate(entries):
        by_key[_surname_key(e.raw_text)].append(idx)
    drop: set[int] = set()
    twins = 0
    for idxs in by_key.values():
        for a_pos, a in enumerate(idxs):
            if a in drop:
                continue
            for b in idxs[a_pos + 1:]:
                if b in drop:
                    continue
                if fuzz.ratio(entries[a].raw_text, entries[b].raw_text) >= _TWIN_SIM:
                    keeper, dup = entries[a], entries[b]
                    keeper.twin_entry_id = dup.entry_id
                    keeper.twin_text = dup.raw_text
                    drop.add(b)
                    twins += 1
    return [e for i, e in enumerate(entries) if i not in drop], twins
