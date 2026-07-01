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

The default config uses `Qwen/Qwen3-0.6B`. Each successful run writes isolated local artifacts to:

```text
outputs/runs/<experiment_name>/<run_id>/
```

`outputs/` is ignored by git. Copy only summaries into the matching `experiments/<experiment_name>/results.md` file.

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

## Multiple Experiments

The framework is meant to extend across different experiment angles: offline inference, serving latency, batching, quantization, SFT/LoRA, eval, and adapter serving.

Create a new isolated experiment scaffold:

```bash
python scripts/new_experiment.py --name exp_002_batching --angle offline
```

Each experiment should have:

- A config under `configs/experiments/<experiment_name>.yaml`.
- A folder under `experiments/<experiment_name>/`.
- A unique `output_dir`, normally `outputs/runs/<experiment_name>`.
- The exact command used.
- Results and notes.

Do not reuse one experiment folder for a different question. Use a new experiment name when the model, dataset, serving mode, or measurement goal changes.

## Training Scaffold

The first SFT/LoRA entrypoint is intentionally a scaffold:

```bash
python scripts/train_sft_lora.py --config configs/training/sft_lora_qwen.yaml
```

It prints the selected model, dataset path, output directory, and LoRA settings. The full TRL + PEFT implementation can be added after the serving and experiment workflow is stable.