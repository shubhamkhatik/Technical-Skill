# LLMsOps (LLM Operations & Lifecycle)

> **Mental Model:** LLMsOps (or LLMOps) covers the operational practices, tooling, and lifecycle management for production AI applications. It ensures applications are: (1) **Reliable & Grounded** (rigorous evaluations), (2) **Observable & Auditable** (end-to-end tracing), and (3) **Safe & Cost-Effective** (guardrails and quota governance).

---

## 🗺️ Operational Pillars & Quick Links

### 1. 📊 [LLM Evals & Benchmarks](./LLM%20Evals%20&%20Benchmarks.md)
* **What it covers:** The RAG Triad (Context Relevance, Groundedness/Faithfulness, Answer Relevance), Context Precision & Recall, LLM-as-a-Judge architectures (single-answer grading, pairwise A/B comparison), synthetic dataset generation, and CI/CD regression gates.
* **When to reach for it:** When evaluating retrieval accuracy, measuring hallucination rates, comparing model performance, or preventing prompt regressions in GitHub Actions.

---

### 2. 🛡️ [Observability & Guardrails](./Observability%20&%20Guardrails.md)
* **What it covers:** OpenTelemetry-based distributed tracing (`Langfuse`, `Arize Phoenix`), token cost attribution, prompt injection & jailbreak defenses (`Llama Guard`, `NeMo Guardrails`), PII redaction (`Microsoft Presidio`), output assertion validators, and production user feedback loops.
* **When to reach for it:** When debugging production agent loops, monitoring live latency/costs, protecting against adversarial inputs, or capturing data for model fine-tuning.

---

## Operations Comparison Matrix

| Pillar | Primary Purpose | Core Tools & Frameworks | Key Metrics |
| :--- | :--- | :--- | :--- |
| **Evaluations** | Measure quality & prevent regressions | `Ragas`, `DeepEval`, `Promptfoo`, `TruLens` | Faithfulness, Answer Relevance, Context Recall |
| **Observability** | Live telemetry, debugging & cost tracking | `Langfuse`, `Arize Phoenix`, `OpenLLMetry` | Latency (P95/P99), Total Cost ($), Error Rate |
| **Guardrails** | Security, compliance & safety enforcement | `NeMo Guardrails`, `Llama Guard`, `Presidio` | Attack Block Rate, PII Leaks, False Positive Rate |
