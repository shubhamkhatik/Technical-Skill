# Observability & Guardrails

> **Mental Model:** Deploying an LLM application to production without observability is flying blind. LLMs are black boxes that incur variable costs, non-deterministic latency, and security risks. Production LLMOps requires: (1) **Distributed Tracing** (tracking every prompt, tool call, and token), (2) **Safety Guardrails** (intercepting attacks before/after generation), and (3) **Cost & Drift Governance**.

---

## Distributed Tracing & Telemetry

| Topic / Skill | Core Concepts & Mental Model | Tools & Libraries | Key Techniques | Tradeoffs & Failure Modes | Resources |
| --- | --- | --- | --- | --- | --- |
| **LLM Tracing & Span Trees** | Visualizing multi-step agent and RAG workflows as hierarchical trace trees, capturing the exact inputs, outputs, latency, and tokens of every sub-step | `Langfuse` *(Open-source)*, `Arize Phoenix`, `LangSmith` | OpenTelemetry standard instrumentation, nesting tool spans under agent run spans, capturing metadata (user ID, session ID, model name) | ✅ Debug complex agent chains in seconds; replay failed user sessions; pinpoint slow tool calls ❌ Storing full prompt/completion payloads increases database storage; requires PII redaction before logging | [Langfuse Documentation](https://langfuse.com/docs), [Arize Phoenix](https://phoenix.arize.com/) |
| **Token Cost & Latency Attribution** | Tracking token consumption (input vs output tokens) and wall-clock latency per user, endpoint, feature, or tenant in real time | `Langfuse`, `Portkey`, `OpenLLMetry` | Compute cost from provider pricing tables dynamically, alert on P95/P99 latency spikes, set hard monthly dollar caps per team | ✅ Prevents unexpected thousand-dollar cloud bills; identifies runaway token leaks early ❌ Pricing tables change frequently across providers; token count discrepancies between tokenizers (e.g. tiktoken vs Llama) | [OpenLLMetry GitHub](https://github.com/traceloop/openllmetry) |

---

## Safety & Security Guardrails

| Topic / Skill | Core Concepts & Mental Model | Tools & Libraries | Key Techniques | Tradeoffs & Failure Modes | Resources |
| --- | --- | --- | --- | --- | --- |
| **Input Guardrails & Prompt Injection Defense** | Inspecting incoming user prompts before they reach the main LLM to detect prompt injections, jailbreaks ("DAN" prompts), and malicious payloads | `Llama Guard 3`, `NeMo Guardrails`, `Prompt Injection Classifier` | Fast classifier model screening input, semantic pattern matching, separating system instructions from untrusted user text using XML tags | ✅ Blocks malicious prompt override attempts before expensive LLM processing ❌ Adds 50–100ms latency to every request; false positives can block legitimate user queries containing sensitive words | [Meta Llama Guard Docs](https://www.llama.com/docs/model-cards-and-prompt-formats/llama-guard-3/), [NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) |
| **PII Detection & Redaction** | Automatically detecting and masking Personally Identifiable Information (emails, SSNs, credit cards, phone numbers, API keys) from prompts before sending to cloud providers | `Microsoft Presidio`, `Private AI` | NER (Named Entity Recognition) + Regex pattern matching, replace entities with placeholders (`<EMAIL_1>`), reverse mapping for output display | ✅ Meets GDPR, HIPAA, and SOC2 compliance; prevents sensitive customer data from being logged or trained on ❌ Masking can degrade the LLM's contextual understanding if entities are over-redacted | [Microsoft Presidio Docs](https://microsoft.github.io/presidio/) |
| **Output Hallucination & Factuality Guardrails** | Validating the model's generated output against deterministic business logic, policies, or facts before streaming to the client | `Guardrails AI`, `Pydantic`, Custom validators | Regex assertion validators, checking numeric ranges ("discount cannot exceed 20%"), re-prompting on validation failure | ✅ 100% deterministic safety net against catastrophic model hallucinations ❌ Re-prompting on failed validation doubles latency and token consumption | [Guardrails AI Documentation](https://www.guardrailsai.com/docs) |

---

## Production Monitoring, Drift & Feedback Loops

| Topic / Skill | Core Concepts & Mental Model | Tools & Libraries | Key Techniques | Tradeoffs & Failure Modes | Resources |
| --- | --- | --- | --- | --- | --- |
| **User Feedback Loops (RLHF/DPO Data)** | Capturing explicit user ratings (👍 / 👎, copy-to-clipboard, retry clicks) and correlating them directly with the corresponding trace ID | `Langfuse Feedback API`, `Arize Phoenix` | Pass `trace_id` to client, log feedback events (`score: 1.0` or `0.0`), filter traces by low ratings for engineering inspection | ✅ Direct signal on real-world application quality; builds curated datasets for future fine-tuning or few-shot prompts ❌ Passive feedback is noisy (users only click thumbs-down when frustrated); low overall feedback engagement | [Langfuse User Feedback](https://langfuse.com/docs/scores/user-feedback) |
| **Semantic Drift & Distribution Shift** | Monitoring whether production user queries are drifting away from the original training or benchmark distribution over time | `Arize AI`, `Evidently AI` | Track embedding drift across rolling 7-day windows using Wasserstein distance or Maximum Mean Discrepancy (MMD) | ✅ Detects emerging user topics, broken integrations, or new attack vectors before users complain ❌ High compute overhead to continuously calculate drift metrics over high-dimensional vector spaces | [Evidently AI Docs](https://docs.evidentlyai.com/) |
