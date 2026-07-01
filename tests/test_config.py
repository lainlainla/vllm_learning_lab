from __future__ import annotations

import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))

from vllm_lab.config import load_yaml, require_keys  # noqa: E402


def test_load_baseline_experiment_config() -> None:
    config = load_yaml(REPO_ROOT / "configs/experiments/exp_001_baseline.yaml")

    assert config["experiment_name"] == "exp_001_baseline"
    assert config["model_name"] == "Qwen/Qwen3-0.6B"
    assert len(config["prompts"]) == 2


def test_require_keys_reports_missing_key() -> None:
    with pytest.raises(KeyError, match="model_name"):
        require_keys({}, ["model_name"])

