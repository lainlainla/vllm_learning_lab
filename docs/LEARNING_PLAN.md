# Learning Plan

## Stage 1: Environment Setup

- Install Ubuntu or WSL2 Ubuntu.
- Confirm `nvidia-smi` works.
- Create the Python 3.12 environment with `uv`.
- Run `python scripts/check_env.py`.

## Stage 2: Offline Inference

- Run `scripts/run_offline.py`.
- Change prompts and sampling settings in YAML.
- Record outputs in `experiments/`.

## Stage 3: OpenAI-Compatible Serving

- Start `scripts/serve_openai.py`.
- Call the server with `scripts/client_chat.py`.
- Test base URL, API key, and model naming.

## Stage 4: Benchmarking

- Record latency, throughput, and GPU memory.
- Compare prompt counts and max token settings.
- Add benchmark scripts only after the manual workflow is clear.

## Stage 5: SFT/LoRA Scaffold

- Prepare a small JSONL dataset.
- Inspect `configs/training/sft_lora_qwen.yaml`.
- Extend `scripts/train_sft_lora.py` with TRL + PEFT when ready.

## Stage 6: Serving Trained Adapters Or Merged Models

- Decide whether to serve adapters directly or merge them.
- Record serving config changes.
- Compare base model and adapted model outputs.
