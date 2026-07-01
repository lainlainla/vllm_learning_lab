# vLLM Learning Lab

A small two-person learning lab for understanding and practicing vLLM. The project focuses on local experiments instead of production infrastructure:

- Run vLLM offline inference.
- Serve a local model with the vLLM OpenAI-compatible API server.
- Call that server with the OpenAI Python client.
- Prepare a basic SFT/LoRA training scaffold.
- Record experiments in a reproducible way.

Co-founders: lainlainla and zzq.

## Who This Is For

This repository is for developers learning how to use vLLM on a Linux GPU machine or on Windows 11 through WSL2 Ubuntu. It is intentionally simple: readable scripts, YAML configs, and experiment notes.

## Supported Environments

- Ubuntu Linux with NVIDIA drivers and CUDA-capable GPU.
- Windows 11 + WSL2 Ubuntu with NVIDIA GPU support.

Native Windows execution is not supported. Put the repo inside the Linux file system when using WSL2, for example `~/code/vllm_learning_lab`, not under `/mnt/c/...`.

## Quickstart

```bash
git clone https://github.com/lainlainla/vllm_learning_lab.git
cd vllm_learning_lab
uv venv --python 3.12 --seed
source .venv/bin/activate
uv pip install -e ".[dev,train]"
python scripts/check_env.py
```

## Offline Inference

Run the baseline experiment config:

```bash
python scripts/run_offline.py --config configs/experiments/exp_001_baseline.yaml
```

The default config uses `Qwen/Qwen3-0.6B`.

## OpenAI-Compatible Server

Start the local vLLM server:

```bash
python scripts/serve_openai.py --config configs/serving/local_server.yaml
```

In another terminal, call the server:

```bash
python scripts/client_chat.py
```

The default local API values are:

- `VLLM_BASE_URL=http://localhost:8000/v1`
- `VLLM_API_KEY=token-abc123`
- `DEFAULT_MODEL=Qwen/Qwen3-0.6B`

## Environment Check

Use the check script any time the environment changes:

```bash
python scripts/check_env.py
```

It reports Python, PyTorch, CUDA/GPU visibility, and whether vLLM imports.

## Experiments

Each experiment should have:

- A config under `configs/experiments/`.
- A folder under `experiments/`.
- The exact command used.
- Results and notes.

Start from:

```bash
cp -r experiments/template experiments/exp_002_my_test
```

Then update `config.yaml`, `command.sh`, and `results.md`.

## Training Scaffold

The first SFT/LoRA entrypoint is intentionally a scaffold:

```bash
python scripts/train_sft_lora.py --config configs/training/sft_lora_qwen.yaml
```

It prints the selected model, dataset path, output directory, and LoRA settings. The full TRL + PEFT implementation can be added after the serving and experiment workflow is stable.
