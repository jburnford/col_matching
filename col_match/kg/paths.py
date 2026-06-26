"""Corpus-relocatable output root for the KG pipeline.

The pipeline was built for the Colonial Office List and hard-coded ``data/kg``
everywhere. To run a second corpus (the India Office List) without clobbering
the CO List artifacts, every driver roots its outputs at ``KG_OUT`` instead of a
literal ``data/kg``. Point a run at a parallel tree with the ``COL_KG_OUT`` env
var, e.g.::

    COL_KG_OUT=data/iol python3 kg_build.py persons --corpus iol

Default stays ``data/kg`` so existing CO List commands are unchanged.
"""

from __future__ import annotations

import os
from pathlib import Path

KG_OUT = Path(os.environ.get("COL_KG_OUT", "data/kg"))


def kg_out() -> Path:
    """Resolve the root fresh from the environment (test-friendly)."""
    return Path(os.environ.get("COL_KG_OUT", "data/kg"))
