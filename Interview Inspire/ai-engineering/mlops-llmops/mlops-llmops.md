# MLOps & LLMOps Interview Questions

---

## Model Serving & High-Throughput Inference
1. What are the key metrics for LLM inference performance: TTFT (Time to First Token), TPOT (Time Per Output Token), and Tokens Per Second (TPS)?
2. What is PagedAttention, and how does vLLM eliminate memory fragmentation in the KV Cache?
3. What is Continuous Batching (Dynamic Batching) in model serving engines (vLLM, TGI, Triton), and how does it outperform static batching?
4. What is Speculative Decoding, and how does using a draft model speed up generation without changing the output distribution?
5. How do you deploy and scale self-hosted open-source models (Llama 3, Mistral) on Kubernetes using vLLM or Ollama?

---

## Model Optimization & Quantization
1. What is Post-Training Quantization (PTQ) vs Quantization-Aware Training (QAT)?
2. What are the differences between weight-only quantization (AWQ, GPTQ) and full weight+activation quantization (SmoothQuant, FP8, INT4)?
3. What is the GGUF file format (llama.cpp), and how does it enable efficient CPU/GPU offloading on local hardware?
4. What is Model Pruning (Structured vs Unstructured) and Knowledge Distillation? When are they practical for LLMs?

---

## Fine-Tuning & Alignment (PEFT, LoRA, RLHF)
1. What is Parameter-Efficient Fine-Tuning (PEFT)? Why is full fine-tuning rarely performed on large frontier models?
2. How does LoRA (Low-Rank Adaptation) work mathematically? What are rank ($r$) and alpha ($\alpha$) hyperparameters?
3. What is QLoRA (Quantized LoRA), and how does 4-bit NormalFloat (NF4) enable fine-tuning large models on a single consumer GPU?
4. What is the difference between Supervised Fine-Tuning (SFT), Reinforcement Learning from Human Feedback (RLHF with PPO), and Direct Preference Optimization (DPO)?
5. When should you choose Fine-Tuning vs RAG (Retrieval-Augmented Generation)?

---

## Evaluation (LLM Evals) & Benchmarking
1. What is the RAG Triad in evaluation: Context Relevance, Groundedness (Faithfulness), and Answer Relevance?
2. How do modern evaluation frameworks (Ragas, TruLens, DeepEval) compute automated metrics using "LLM-as-a-Judge"?
3. What are the known biases of LLM-as-a-Judge (Position bias, Verbosity bias, Self-enhancement bias), and how do you mitigate them?
4. How do you create and maintain a regression test dataset for production LLM prompts?

---

## Guardrails, Security & Observability
1. How do you implement input and output guardrails (NeMo Guardrails, Llama Guard, Guardrails AI) for PII redaction and toxicity filtering?
2. How do you detect and defend against Indirect Prompt Injection in retrieved web data or documents?
3. What tracing tools are used for LLM observability (LangSmith, Phoenix/Arize, OpenInference, Helicone)?
4. How do you monitor and optimize token consumption, API costs, and latency drift across multi-tenant LLM applications?
