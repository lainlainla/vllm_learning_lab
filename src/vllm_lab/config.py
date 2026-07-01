"""Config loading helpers for small YAML-driven experiments."""

from __future__ import annotations

from pathlib import Path
from typing import Any


def load_yaml(path: str | Path) -> dict[str, Any]:
    """Load a YAML file and return an empty dict for empty files."""
    try:
        import yaml
    except ImportError as exc:  # pragma: no cover - depends on local environment
        raise RuntimeError("PyYAML is required. Install with: uv pip install -e '.[dev]'") from exc

    config_path = Path(path)
    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with config_path.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file) or {}

    if not isinstance(data, dict):
        raise ValueError(f"Expected YAML mapping in {config_path}")

    return data


def require_keys(config: dict[str, Any], keys: list[str]) -> None:
    """Raise a readable error when required keys are missing."""
    missing = [key for key in keys if key not in config]
    if missing:
        raise KeyError(f"Missing required config keys: {', '.join(missing)}")
