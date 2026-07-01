.PHONY: setup check offline serve chat test lint

setup:
	uv venv --python 3.12 --seed
	uv pip install -e ".[dev,train]"

check:
	python scripts/check_env.py

offline:
	python scripts/run_offline.py --config configs/experiments/exp_001_baseline.yaml

serve:
	python scripts/serve_openai.py --config configs/serving/local_server.yaml

chat:
	python scripts/client_chat.py

test:
	pytest -q

lint:
	ruff check .
