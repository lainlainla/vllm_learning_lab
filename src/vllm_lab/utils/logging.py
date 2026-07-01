"""Logging setup used by scripts."""

from __future__ import annotations

import logging


def configure_logging(level: int = logging.INFO) -> None:
    """Configure a simple console logger."""
    logging.basicConfig(
        level=level,
        format="%(levelname)s: %(message)s",
    )
