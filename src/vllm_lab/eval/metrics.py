"""Small metrics used in simple learning experiments."""

from __future__ import annotations


def exact_match(prediction: str, reference: str) -> bool:
    """Return true when normalized strings match exactly."""
    return prediction.strip() == reference.strip()


def average_length(texts: list[str]) -> float:
    """Return the average character length for generated texts."""
    if not texts:
        return 0.0
    return sum(len(text) for text in texts) / len(texts)
