# AI Engineering Knowledge Base

> **Mental Model:** AI Engineering bridges raw foundation models and robust, scalable production systems. It spans mathematical foundations, user-facing client state, backend RAG & agent plumbing, continuous evaluation & observability, and enterprise-scale architecture.

---

## 🗺️ Complete AI Engineering Directory & Navigation

### 1. 🧠 [Core AI & Mathematical Foundations](./Core%20AI/AI%20Engineering%20Concept.md)
* Vector Embeddings & continuous semantic space
* Distance Metrics (Cosine similarity, $L_2$ Euclidean, Dot product)
* Vector Search execution pipelines & indexing (IVF, HNSW, Curse of Dimensionality)
* Vector Quantization (Product Quantization `PQ`, Scalar Quantization `SQ`)
* Hallucination mitigation, KV Caching, PagedAttention, FlashAttention, and Speculative Decoding

---

### 2. ⚙️ [AI Backend Engineering](./AI%20Backend%20Engineering/AI%20Backend%20Engineering.md)
* 🔍 **[RAG & Vector Architecture](./AI%20Backend%20Engineering/RAG%20&%20Vector%20Architecture.md)**: Chunking strategies (fixed, semantic, parent-child), Vector DBs (`pgvector`, `Qdrant`, `Pinecone`), Hybrid Search (Dense + BM25/SPLADE), Cross-Encoder Reranking, and Advanced RAG (HyDE, Multi-Query).
* 🤖 **[Agentic AI & Orchestration](./AI%20Backend%20Engineering/Agentic%20AI%20&%20Orchestration.md)**: Function Calling & Tool use, Model Context Protocol (MCP), ReAct loops, LangGraph state machines, state checkpointing/persistence, and Human-in-the-Loop approvals.
* ⚡ **[LLM Serving & Gateways](./AI%20Backend%20Engineering/LLM%20Serving%20&%20Gateways.md)**: High-throughput serving (`vLLM`, continuous batching, `Ollama`), Unified API Gateways (`LiteLLM`), Semantic Prompt Caching (`GPTCache`, Redis), Model Routing Cascades, and Token-bucket rate limiting.

---

### 3. 🛠️ [LLMsOps (Operations, Evals & Guardrails)](./LLMsOps/LLMsOps.md)
* 📊 **[LLM Evals & Benchmarks](./LLMsOps/LLM%20Evals%20&%20Benchmarks.md)**: The RAG Triad (Context Relevance, Groundedness/Faithfulness, Answer Relevance), Context Precision & Recall, LLM-as-a-Judge architectures, synthetic dataset generation, and CI/CD regression gates.
* 🛡️ **[Observability & Guardrails](./LLMsOps/Observability%20&%20Guardrails.md)**: Distributed OpenTelemetry tracing (`Langfuse`, `Arize Phoenix`), Token cost attribution, prompt injection & jailbreak defenses (`Llama Guard`, `NeMo Guardrails`), PII redaction (`Presidio`), and production feedback loops.

---

### 4. 🎨 [AI Frontend Engineering](./AI%20Frontend%20Engineering/AI%20Frontend%20Engineering.md)
* 💻 **[AI in Frontend Landscape](./AI%20Frontend%20Engineering/AI%20in%20Frontend%20Landscape.md)**: Vercel AI SDK integration layer, AI-specific prebuilt UI components, partial JSON streaming, client-side tool rendering (Generative UI), and client caching strategies.

---

### 5. 🏗️ [AI System Design](./AI%20System%20Design/AI%20System%20Design.md)
* AI/LLM Discoverability & Crawlers (GEO / AEO)
* The `llms.txt` standard & Content Negotiation
* Semantic scaffolding & bot interception via Edge middleware
* Citation & attribution tracking
