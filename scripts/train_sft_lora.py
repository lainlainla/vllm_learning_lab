from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))

from vllm_lab.config import load_yaml, require_keys  # noqa: E402
from vllm_lab.training.sft_lora import summarize_training_config  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Print the SFT/LoRA training scaffold config.")
    parser.add_argument(
        "--config",
        default="configs/training/sft_lora_qwen.yaml",
        help="Path to a training YAML config.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    config = load_yaml(args.config)
    require_keys(config, ["model_name", "dataset_path", "output_dir"])

    print("SFT/LoRA scaffold")
    print("=================")
    for line in summarize_training_config(config):
        print(line)

    print()
    print("This is a scaffold for a later TRL + PEFT implementation.")
    print("It does not launch training yet.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


