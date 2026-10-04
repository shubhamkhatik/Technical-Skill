# AI Backend Engineering

> **Mental Model:** AI Backend Engineering is the runtime systems layer connecting foundation models, data stores, external APIs, and client applications. It is structured into three dedicated core pillars:

---

## 🗺️ Architectural Pillars & Quick Links

### 1. 🔍 [RAG & Vector Architecture](./RAG%20&%20Vector%20Architecture.md)
* **What it covers:** Chunking strategies (fixed, semantic, parent-child), Vector Databases (`pgvector`, `Qdrant`, `Pinecone`), Hybrid Search (Dense + BM25/SPLADE), Cross-Encoder Reranking, and Advanced RAG patterns (HyDE, Multi-Query, Contextual Compression).
* **When to reach for it:** When building grounded retrieval pipelines over private documents, search systems, or enterprise knowledge bases.

---

### 2. 🤖 [Agentic AI & Orchestration](./Agentic%20AI%20&%20Orchestration.md)
* **What it covers:** Function & Tool Calling, Model Context Protocol (MCP) servers/transports, Agent loops (ReAct), LangGraph state machine graphs, checkpointing/time-travel, and Human-in-the-Loop approval gates.
* **When to reach for it:** When building autonomous agents, multi-agent teams, workflow automations, or systems that need to execute code and database operations safely.

---

### 3. ⚡ [LLM Serving & Gateways](./LLM%20Serving%20&%20Gateways.md)
* **What it covers:** High-throughput open model serving engines (`vLLM`, continuous batching, `Ollama`), unified LLM gateways (`LiteLLM`), semantic prompt caching (`GPTCache`, Redis), model routing cascades, and rate limiting.
* **When to reach for it:** When running self-hosted models, standardizing 10+ provider APIs into a single endpoint, reducing token costs, or ensuring 99.99% high availability.

---

## Pillar Comparison Matrix

| Layer | Primary Focus | Core Tools & Frameworks | Primary Metrics |
| :--- | :--- | :--- | :--- |
| **RAG & Search** | Data grounding & context assembly | `pgvector`, `Qdrant`, `Cohere Rerank`, `LlamaIndex` | Recall@K, Precision@K, Context Relevance |
| **Agentic Loops** | Multi-step reasoning & tool execution | `LangGraph`, `MCP SDK`, `Pydantic`, `CrewAI` | Task Completion Rate, Step Count, Error Recovery |
| **Serving & Gateway** | Infrastructure, routing & latency | `vLLM`, `LiteLLM`, `Redis`, `Portkey` | Tokens/sec, TTFT (Time to First Token), Cost ($/req) |
