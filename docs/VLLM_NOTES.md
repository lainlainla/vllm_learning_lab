# vLLM Notes

Use this file for short learning notes and links.

## PagedAttention

Write down how vLLM manages attention memory with page-like blocks.

## KV Cache

Track notes on cache size, reuse, and memory pressure.

## Continuous Batching

Record how vLLM schedules requests together while requests arrive over time.

## Tensor Parallelism

Document when multi-GPU tensor parallelism is needed and how to configure it.

## OpenAI-Compatible Serving

Keep notes on request format, model names, API keys, and client compatibility.

## LoRA Serving

Track how adapters are loaded and how model routing should work.

## Benchmarking

Record the metrics that matter for each experiment: latency, throughput, GPU
memory, prompt length, output length, and concurrency.
