from __future__ import annotations

import importlib.util
import platform
import sys


def print_python() -> None:
    print(f"Python: {sys.version.split()[0]}")
    print(f"Platform: {platform.platform()}")


def print_torch() -> None:
    if importlib.util.find_spec("torch") is None:
        print("WARNING: torch is not installed.")
        return

    import torch

    print(f"Torch: {torch.__version__}")
    cuda_available = torch.cuda.is_available()
    print(f"CUDA available: {cuda_available}")
    if cuda_available:
        print(f"CUDA device count: {torch.cuda.device_count()}")
        print(f"GPU: {torch.cuda.get_device_name(0)}")
    else:
        print("WARNING: CUDA is not available to PyTorch.")


def print_vllm() -> None:
    if importlib.util.find_spec("vllm") is None:
        print("WARNING: vLLM is not installed or not visible in this environment.")
        return

    try:
        import vllm
    except Exception as exc:  # pragma: no cover - diagnostic script
        print(f"WARNING: vLLM import failed: {exc}")
        return

    version = getattr(vllm, "__version__", "unknown")
    print(f"vLLM: import ok, version {version}")


def main() -> int:
    print_python()
    print_torch()
    print_vllm()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
