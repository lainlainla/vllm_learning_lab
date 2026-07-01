from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))

from vllm_lab.training.sft_lora import summarize_training_config  # noqa: E402


def test_training_config_summary() -> None:
    summary = summarize_training_config(
        {
            "model_name": "Qwen/Qwen3-0.6B",
            "dataset_path": "data/processed/sample_sft.jsonl",
            "output_dir": "outputs/sft_lora_qwen",
            "lora": {"r": 16, "alpha": 32, "dropout": 0.05},
            "training": {"num_train_epochs": 1},
        }
    )

    assert "Model: Qwen/Qwen3-0.6B" in summary
    assert "  r: 16" in summary
    assert "  num_train_epochs: 1" in summary


def test_check_env_script_does_not_crash() -> None:
    result = subprocess.run(
        [sys.executable, "scripts/check_env.py"],
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 0
    assert "Python:" in result.stdout

