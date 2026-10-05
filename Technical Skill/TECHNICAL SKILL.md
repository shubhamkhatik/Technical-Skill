# 🧭 Technical Skill Master Dashboard

> **Curated Knowledge Base & Engineering Reference**  
> A structured, high-yield reference library covering Frontend, Backend, System Design, DevOps, AI Engineering, and Data Structures & Algorithms. All entries are condensed into clean, production-grade reference tables with zero prose clutter.

---

## ⚡ Quick Navigation

| Domain                       | Primary Files                                                                                                                                                                                                    | Key Focus Areas                                                        | Interview Practice Bank (Interview-Inspire)                                                                                                  |
| :--------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------- |
| **Frontend Development**     | [`Frontend.md`](./Frontend/Frontend.md) · [`React JS.md`](./Frontend/React%20JS.md) · [`Next JS.md`](./Frontend/Next%20JS.md)                                                                                    | Core JS/TS, React 18+ hooks, Next.js App Router, State Management, PWA | [Frontend Practice Bank ↗](https://github.com/shubhamkhatik/Interview-Inspire/blob/main/software-engineering/frontend/frontend.md)           |
| **Frontend System Design**   | [`Frontend System Design.md`](./Frontend%20System%20Design/Frontend%20System%20Design.md)                                                                                                                        | API Paradigms, Comm Patterns, Security (CSP/XSS), Storage, Web Perf    | [Frontend System Design ↗](https://github.com/shubhamkhatik/Interview-Inspire/blob/main/software-engineering/frontend/frontend.md)           |
| **Backend Engineering**      | [`Backend.md`](./Backend/Backend.md) · [`Nodejs+Express.md`](./Backend/Nodejs+Express.md)                                                                                                                        | Node/Express, Fastify, SQL/Postgres, NoSQL/Mongo, Redis, Queues, Auth  | [Backend Practice Bank ↗](https://github.com/shubhamkhatik/Interview-Inspire/blob/main/software-engineering/backend/backend.md)              |
| **Backend System Design**    | [`Backend System Design.md`](./Backend%20System%20Design/Backend%20System%20Design.md) · [`roadmap.sh`](./Backend%20System%20Design/roadmap.sh%20system-design.md)                                               | Scalability, Sharding, Caching, Consensus, HLD Architectures           | [System Design Bank ↗](https://github.com/shubhamkhatik/Interview-Inspire/blob/main/software-engineering/system-design/system-design.md)     |
| **Production System Design** | [`Production System Design.md`](./Production%20System%20Design/Production%20System%20Design.md)                                                                                                                  | High Availability, Fault Tolerance, Disaster Recovery, SLOs/SLAs       | [Production Design Bank ↗](https://github.com/shubhamkhatik/Interview-Inspire/blob/main/software-engineering/system-design/system-design.md) |
| **DevOps & Cloud**           | [`DevOps for Developer.md`](./DevOps%20for%20Developers/DevOps%20for%20Developer.md)                                                                                                                             | Linux, Git, Docker, Kubernetes, CI/CD, Nginx, Terraform, SRE           | [DevOps Practice Bank ↗](https://github.com/shubhamkhatik/Interview-Inspire/blob/main/software-engineering/devops/devops.md)                 |
| **AI Engineering**           | [`AI Engineering.md`](./AI%20Engineering/AI%20Engineering.md) · [`AI Backend`](./AI%20Engineering/AI%20Backend%20Engineering/AI%20Backend%20Engineering.md) · [`LLMsOps`](./AI%20Engineering/LLMsOps/LLMsOps.md) | Embeddings, RAG, Vector DBs, Agents, MCP, Serving (vLLM), Evals        | [AI Question Bank ↗](https://github.com/shubhamkhatik/Interview-Inspire/tree/main/ai-engineering)                                            |
| **Data Structures & Algo**   | [`DSA.md`](./DSA/DSA.md)                                                                                                                                                                                         | Two Pointers, Sliding Window, Trees, Graphs, Dynamic Programming       | [DSA Problem Bank ↗](https://github.com/shubhamkhatik/Interview-Inspire/blob/main/dsa-problem-solving/dsa.md)                                |

---

## 📚 Complete Domain Breakdown

### 1. 🎨 Frontend Engineering
> 🎯 **Interview Practice:** [Frontend Question Bank ↗](https://github.com/shubhamkhatik/Interview-Inspire/blob/main/software-engineering/frontend/frontend.md)
* 📄 **[Frontend Overview](./Frontend/Frontend.md)** — Core Web Tech (HTML5, CSS3, JS ES6+, TS), Auth & Security, Payment Gateways (Stripe/Razorpay), Real-time Comm, State Management (Redux/Zustand), Mobile & PWA.
* ⚛️ **[React.js Deep Dive](./Frontend/React%20JS.md)** — Functional Components, React 18 Hooks (`useTransition`, `useDeferredValue`), React Router v6, React Hook Form + Zod, Error Boundaries, Suspense.
* 🔺 **[Next.js Architecture](./Frontend/Next%20JS.md)** — App Router vs Pages Router, Server vs Client Components, Route Handlers, Server Actions, Dynamic Metadata / SEO, Middleware, Image/Font Optimization.
* 📐 **[UI System Design in Next.js](./Frontend/UI%20System%20Design%20in%20Next%20JS.md)** — Design Tokens, Component Composition, Micro-interactions, Accessibility (ARIA), Dark Mode.

---

### 2. 🌐 Frontend System Design
> 🎯 **Interview Practice:** [Frontend System Design Questions ↗](https://github.com/shubhamkhatik/Interview-Inspire/blob/main/software-engineering/frontend/frontend.md)
* 📄 **[Frontend System Design](./Frontend%20System%20Design/Frontend%20System%20Design.md)**:
  * **Networking & API Paradigms**: REST, GraphQL, gRPC-Web, tRPC.
  * **Communication Patterns**: Short Polling, Long Polling, Server-Sent Events (SSE), WebSockets, Webhooks.
  * **Frontend Security**: XSS (DOM/Stored/Reflected), CSRF, CORS, CSP Headers, Clickjacking, SRI, Storage Security.
  * **Browser Storage & Caching**: `localStorage`, `sessionStorage`, IndexedDB, Cache API, Service Workers.
  * **Rendering & Performance**: Critical Rendering Path, Code Splitting, Resource Hints (Preload/Prefetch), Core Web Vitals.

---

### 3. ⚙️ Backend Engineering
> 🎯 **Interview Practice:** [Backend Question Bank ↗](https://github.com/shubhamkhatik/Interview-Inspire/blob/main/software-engineering/backend/backend.md)
* 📄 **[Backend Engineering Guide](./Backend/Backend.md)**:
  * **Runtimes & Frameworks**: Node.js Event Loop, Express.js, Fastify, NestJS, FastAPI, Django.
  * **API Design & Protocols**: REST Best Practices, GraphQL Schemas, gRPC Protobuf, tRPC RPC, Versioning.
  * **Database Systems**: PostgreSQL, Prisma vs Drizzle ORM, MongoDB, Redis Caching, Vector Databases, BullMQ/Kafka Queues.
  * **Authentication & Authorization**: Session-based, JWT Rotation, OAuth 2.0 & OIDC (PKCE).
* 🟢 **[Node.js + Express.js Deep Dive](./Backend/Nodejs+Express.md)** — Asynchronous I/O, Streams & Buffers, Child Processes, Cluster Module, Custom Middleware, Centralized Error Handling.

---

### 4. 🏗️ System Design (HLD & Production)
> 🎯 **Interview Practice:** [System Design Question Bank ↗](https://github.com/shubhamkhatik/Interview-Inspire/blob/main/software-engineering/system-design/system-design.md)
* 🏛️ **[Backend System Design Guide](./Backend%20System%20Design/Backend%20System%20Design.md)** — Scalability, Horizontal vs Vertical Scaling, Load Balancers, CAP Theorem, Database Sharding & Partitioning.
* 🗺️ **[roadmap.sh System Design](./Backend%20System%20Design/roadmap.sh%20system-design.md)** — Comprehensive reference based on industry system design roadmaps.
* 🔰 **[System Design for Beginners](./Backend%20System%20Design/system-design-for-beginners.md)** — Foundational concepts for cracking mid-to-senior design rounds.
* 🛡️ **[Production System Design](./Production%20System%20Design/Production%20System%20Design.md)** — High Availability, Fault Tolerance, Circuit Breakers, Disaster Recovery, SLOs/SLIs, Zero-Downtime Deployments.

---

### 5. 🐧 DevOps & Cloud Infrastructure
> 🎯 **Interview Practice:** [DevOps Question Bank ↗](https://github.com/shubhamkhatik/Interview-Inspire/blob/main/software-engineering/devops/devops.md)
* 📄 **[DevOps for Developers](./DevOps%20for%20Developers/DevOps%20for%20Developer.md)**:
  * **01. Linux & Terminal**: File permissions (chmod/chown), Process management (PID, SIGTERM/SIGKILL), Text streams (grep/awk/sed/jq), SSH key management.
  * **02. Git & Version Control**: Git internals (blobs/trees/commits), Branching strategies, Interactive rebase, Safe undoing (reflog/revert), Conventional Commits.
  * **03. CI/CD Pipelines**: Automated test/build workflows, Environment secrets, Matrix builds, Deployment triggers.
  * **04. Containers & Docker**: Multi-stage builds, Layer caching, `.dockerignore`, Rootless containers.
  * **05. Kubernetes (K8s)**: Pods, Deployments, Services (ClusterIP/NodePort/LoadBalancer), Ingress, ConfigMaps, Secrets.
  * **06. Web Servers & Nginx**: Reverse proxying, SSL termination, Load balancing algorithms, Rate limiting.
  * **07. Infrastructure as Code (Terraform)**: State management, HCL providers, Modules, Drift detection.
  * **08. Observability & SRE**: Metrics (Prometheus), Dashboards (Grafana), Log aggregation, P99 latency alerts.

---

### 6. 🧠 AI Engineering
> 🎯 **Interview Practice:** [AI Engineering Question Banks ↗](https://github.com/shubhamkhatik/Interview-Inspire/tree/main/ai-engineering) ([Foundations](https://github.com/shubhamkhatik/Interview-Inspire/blob/main/ai-engineering/foundations/foundations.md) · [LLM & RAG](https://github.com/shubhamkhatik/Interview-Inspire/blob/main/ai-engineering/llm-and-rag/llm-and-rag.md) · [Agentic AI](https://github.com/shubhamkhatik/Interview-Inspire/blob/main/ai-engineering/agentic-ai/agentic-ai.md) · [MLOps & LLMOps](https://github.com/shubhamkhatik/Interview-Inspire/blob/main/ai-engineering/mlops-llmops/mlops-llmops.md) · [AI System Design](https://github.com/shubhamkhatik/Interview-Inspire/blob/main/ai-engineering/ai-system-design/ai-system-design.md))
* 📄 **[AI Engineering Hub](./AI%20Engineering/AI%20Engineering.md)** — Central architecture map for the AI stack.
* 🧬 **[Core AI & Foundations](./AI%20Engineering/Core%20AI/AI%20Engineering%20Concept.md)** — Vector Embeddings, Distance Metrics (Cosine/L2), Vector Search Pipelines, ANN Indexing (IVF/HNSW), Quantization (PQ/SQ), Attention (FlashAttention, PagedAttention), Speculative Decoding.
* ⚙️ **[AI Backend Engineering](./AI%20Engineering/AI%20Backend%20Engineering/AI%20Backend%20Engineering.md)**:
  * 🔍 **[RAG & Vector Architecture](./AI%20Engineering/AI%20Backend%20Engineering/RAG%20&%20Vector%20Architecture.md)** — Chunking strategies, `pgvector`/Qdrant/Pinecone, Dense + Sparse Hybrid Search, Cross-Encoder Reranking, Advanced RAG (HyDE).
  * 🤖 **[Agentic AI & Orchestration](./AI%20Engineering/AI%20Backend%20Engineering/Agentic%20AI%20&%20Orchestration.md)** — Function Calling, Model Context Protocol (MCP), ReAct loops, LangGraph state machines, Human-in-the-Loop.
  * ⚡ **[LLM Serving & Gateways](./AI%20Engineering/AI%20Backend%20Engineering/LLM%20Serving%20&%20Gateways.md)** — `vLLM` high-throughput serving, Continuous batching, `LiteLLM` Unified Gateway, Semantic prompt caching.
* 🛠️ **[LLMsOps (Operations, Evals & Quality)](./AI%20Engineering/LLMsOps/LLMsOps.md)**:
  * 📊 **[LLM Evals & Benchmarks](./AI%20Engineering/LLMsOps/LLM%20Evals%20&%20Benchmarks.md)** — The RAG Triad (Ragas), Context Precision & Recall, LLM-as-a-Judge, Synthetic test datasets, CI/CD regression gates.
  * 🛡️ **[Observability & Guardrails](./AI%20Engineering/LLMsOps/Observability%20&%20Guardrails.md)** — Distributed tracing (`Langfuse`, `Arize Phoenix`), Token cost attribution, Prompt injection defense, PII masking.
* 🎨 **[AI Frontend Engineering](./AI%20Engineering/AI%20Frontend%20Engineering/AI%20Frontend%20Engineering.md)** — [AI in Frontend Landscape](./AI%20Engineering/AI%20Frontend%20Engineering/AI%20in%20Frontend%20Landscape.md) (Vercel AI SDK, Generative UI, Partial JSON Streaming).
* 🏗️ **[AI System Design](./AI%20Engineering/AI%20System%20Design/AI%20System%20Design.md)** — GEO / AEO, `llms.txt`, Bot Interception, Citation Tracking.

---

### 7. 💻 Data Structures & Algorithms (DSA)
> 🎯 **Interview Practice:** [DSA Problem Bank ↗](https://github.com/shubhamkhatik/Interview-Inspire/blob/main/dsa-problem-solving/dsa.md)
* 📄 **[DSA Core Patterns](./DSA/DSA.md)** — Arrays, Strings, Two Pointers, Sliding Window, Fast & Slow Pointers, Linked Lists, Binary Trees & BSTs, Graph Traversals (BFS/DFS), Dynamic Programming.

---

## 🛠️ Repository Automation & Dropzone

* 📥 **[Learning Dropzone (inbox.md)](./inbox.md)** — Paste raw notes, bullet points, or topic keywords from any course or video. Say *"Process inbox"* in chat to automatically categorize, ground, format, and append to the tables.
* 📐 **[Table Prettifier Script](./scripts/prettify_tables.py)** — Automatically aligns all vertical pipes across all markdown tables:
  ```bash
  python scripts/prettify_tables.py --all
  ```
* 🎯 **[Live Dual-Track Coverage Matrix (INTERVIEW_COVERAGE.md)](./INTERVIEW_COVERAGE.md)** — Synchronizes in real time with [`Interview-Inspire`](./Interview%20Inspire/README.md) to track concept coverage % and uncover missing question gaps:
  ```bash
  python scripts/sync_coverage.py
  ```
* 🤖 **[Agent Instructions (AGENTS.md)](./AGENTS.md)** — Mandatory AI coding agent guidelines for grounding, deduplication, enrichment diffs, and adaptive schemas.