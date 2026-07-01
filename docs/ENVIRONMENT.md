# Environment

This project is Linux-first. Native Windows execution is not supported.

## Ubuntu Linux

1. Install NVIDIA drivers and confirm the GPU is visible:

   ```bash
   nvidia-smi
   ```

2. Install `uv`:

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. Create the environment from the repository root:

   ```bash
   uv venv --python 3.12 --seed
   source .venv/bin/activate
   uv pip install -e ".[dev,train]"
   python scripts/check_env.py
   ```

## Windows 11 + WSL2 Ubuntu

Use Ubuntu inside WSL2 with NVIDIA GPU passthrough. Do not run the project from
PowerShell or native Windows Python.

Recommended layout:

```bash
mkdir -p ~/code
cd ~/code
git clone https://github.com/lainlainla/vllm_learning_lab.git
cd vllm_learning_lab
```

Avoid cloning under `/mnt/c/...`; file I/O is slower and Python environments are
more fragile there.

Check the GPU from WSL2:

```bash
nvidia-smi
```

Then use the same `uv` setup as native Linux.

## What Not To Commit

Do not commit:

- `.env`
- `.venv/`
- model weights
- checkpoints
- local datasets
- API keys
- Hugging Face tokens
- local machine paths

Keep placeholder `.gitkeep` files in `data/raw/` and `data/processed/`.
