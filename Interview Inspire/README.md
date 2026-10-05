# Interview Inspire

A curated, production-grade repository of interview questions across **Software Engineering**, **AI Engineering**, and **Data Structures & Algorithms**.

---

## 🗺️ Repository Structure & Quick Links

### 💻 [Software Engineering](software-engineering/)
- 🎨 **[Frontend Engineering](software-engineering/frontend/frontend.md)** — HTML5, CSS/Layouts, Core JS, TypeScript, React & Next.js, Web Performance, Browser Internals, Machine Coding.
- ⚙️ **[Backend Engineering](software-engineering/backend/backend.md)** — API Design (REST/GraphQL/gRPC), Relational DBs (PostgreSQL/MySQL), NoSQL, Caching & Redis, Kafka/RabbitMQ, Auth & Security, Concurrency.
- 🚀 **[DevOps & Cloud Engineering](software-engineering/devops/devops.md)** — Linux & Shell, Networking & Nginx, Docker Containers, Kubernetes (K8s), CI/CD & GitOps, Terraform (IaC), Observability & SRE.
- 📐 **[System Design (HLD & LLD)](software-engineering/system-design/system-design.md)** — Scalability principles, Sharding, Consistent Hashing, CDNs, Classic HLD Problems (TinyURL, Rate Limiter, Newsfeed, Chat, Video Streaming), LLD Design Patterns & Class Modeling.

---

### 🤖 [AI Engineering](ai-engineering/)
- 🧠 **[AI Foundations](ai-engineering/foundations/foundations.md)** — Python for AI/Data Science, Math for ML (Linear Algebra, Calculus, Stats), Core ML, Deep Learning, Transformer Attention & NLP.
- 🔍 **[LLM & RAG](ai-engineering/llm-and-rag/llm-and-rag.md)** — LLM Fundamentals, Prompt Engineering, Dense vs Sparse Embeddings, Vector DBs (HNSW/IVF-PQ), Advanced RAG (Hybrid Search, Reranking, HyDE).
- 🛠️ **[Agentic AI](ai-engineering/agentic-ai/agentic-ai.md)** — Autonomous Agents, ReAct Pattern, Function Calling, Model Context Protocol (MCP), LangGraph, CrewAI/AutoGen, Multi-Agent Orchestration.
- ⚡ **[MLOps & LLMOps](ai-engineering/mlops-llmops/mlops-llmops.md)** — Model Serving (vLLM/Triton), PagedAttention & Continuous Batching, Quantization (AWQ/GPTQ/GGUF), PEFT/LoRA/DPO, LLM Evals (Ragas/TruLens), Guardrails.
- 🏛️ **[AI System Design](ai-engineering/ai-system-design/ai-system-design.md)** — Token Economics, Semantic Caching (GPTCache), LLM Routing & Cascading, Enterprise RAG at Scale, Customer Support Agents, Multimodal Extraction.

---

### 🧩 [Data Structures & Algorithms (DSA)](dsa-problem-solving/dsa.md)
- **[DSA Questions by Pattern](dsa-problem-solving/dsa.md)** — Strings, Arrays, Two Pointers & Sliding Window, Linked Lists, Stacks & Queues, Trees & BSTs, Graphs, Dynamic Programming (DP).

---

### 📝 [Interview Experiences](interview-experiences/)
- **[Real-World Interview Experiences](interview-experiences/)** — Actual interview rounds, technical quizzes, and machine coding problems.

---

## 📥 How to Add Questions Automatically

1. **On Laptop / IDE**: Paste raw questions into [inbox.md](inbox.md) and ask the IDE to *"Process inbox"*, or run:
   ```bash
   python scripts/process_questions.py
   ```
2. **On Mobile**: Open GitHub in your mobile browser or app, create a **New Issue**, and paste the questions. The GitHub Actions bot will sort and commit them to the repository automatically.
