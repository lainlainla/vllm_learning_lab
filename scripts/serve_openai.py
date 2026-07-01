from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))

from vllm_lab.config import load_yaml, require_keys  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Start the vLLM OpenAI-compatible server.")
    parser.add_argument(
        "--config",
        default="configs/serving/local_server.yaml",
        help="Path to a serving YAML config.",
    )
    return parser.parse_args()


def build_command(config: dict[str, object]) -> list[str]:
    require_keys(config, ["model_name", "host", "port", "api_key"])
    command = [
        "vllm",
        "serve",
        str(config["model_name"]),
        "--host",
        str(config["host"]),
        "--port",
        str(config["port"]),
        "--api-key",
        str(config["api_key"]),
    ]

    optional_flags = {
        "dtype": "--dtype",
        "max_model_len": "--max-model-len",
        "gpu_memory_utilization": "--gpu-memory-utilization",
    }
    for key, flag in optional_flags.items():
        if key in config:
            command.extend([flag, str(config[key])])

    return command


def main() -> int:
    args = parse_args()
    config = load_yaml(args.config)
    command = build_command(config)

    print("Starting vLLM server:")
    print(" ".join(command))

    try:
        subprocess.run(command, check=True)
    except FileNotFoundError:
        print(
            "ERROR: 'vllm' command not found. Install project dependencies first.",
            file=sys.stderr,
        )
        return 1
    except subprocess.CalledProcessError as exc:
        return exc.returncode

    return 0


if __name__ == "__main__":
    raise SystemExit(main())


