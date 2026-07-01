"""Dataset helpers for future SFT work."""

from __future__ import annotations

from pathlib import Path


def resolve_dataset_path(path: str) -> Path:
    """Return a normalized dataset path without requiring that it exists yet."""
    return Path(path).expanduser()
