"""Connection + tunables for col_matching.

Mirrors col_pipeline's credential resolution so there is a single source of
credentials: env vars first, then this repo's .env, then the production sibling
repo's .env. Read-only by intent — there is no write path here.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

try:
    from dotenv import load_dotenv as _load_dotenv
except ImportError:  # python-dotenv optional
    _load_dotenv = None

REPO_ROOT = Path(__file__).parent.parent
DEFAULT_PROD_URI = "bolt://206.12.90.118:7687"


def _ensure_dotenv_loaded() -> None:
    """Load .env idempotently; first value found wins (no override)."""
    if _load_dotenv is None:
        return
    for candidate in (
        Path.cwd() / ".env",
        REPO_ROOT / ".env",
        Path.home() / "textasdatacolonialofficelist" / ".env",
    ):
        if candidate.exists():
            _load_dotenv(candidate, override=False)


@dataclass(frozen=True)
class Config:
    neo4j_uri: str
    neo4j_user: str
    neo4j_password: str
    neo4j_database: str | None = None

    # Default cluster gate: same threshold col_pipeline uses to seed persons.
    max_uncertainty: float = 0.50

    @classmethod
    def from_env(cls, **overrides) -> "Config":
        _ensure_dotenv_loaded()
        uri = (
            os.environ.get("NEO4J_PROD_URI")
            or os.environ.get("NEO4J_URI")
            or DEFAULT_PROD_URI
        )
        user = os.environ.get("NEO4J_PROD_USER") or os.environ.get("NEO4J_USER") or "neo4j"
        pw = os.environ.get("NEO4J_PROD_PASSWORD") or os.environ.get("NEO4J_PASSWORD") or ""
        db = os.environ.get("NEO4J_DATABASE") or None
        kwargs = dict(neo4j_uri=uri, neo4j_user=user, neo4j_password=pw, neo4j_database=db)
        kwargs.update(overrides)
        return cls(**kwargs)
