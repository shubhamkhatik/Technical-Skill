# AGENTS.md — Technical Skill Learning Ingestion & Table System

> **Notice to AI Coding Agents:**  
> This file defines the repository architecture, file schemas, and execution workflows for **Technical-Skill**. Follow these instructions whenever the user provides a topic, raw notes, or asks to document a technical concept.

---

## 1. Core Workflow: Learning-to-Table Ingestion

Whenever the user inputs a **topic name** (e.g., `communication pattern in frontend`, `websocket`, `seo`), a **topic + raw learning notes**, or asks to **"process inbox"** (reading from `inbox.md`):

### Step 1: Domain & Target File Resolution
Automatically detect the appropriate file and section based on topic keywords (even if domain is not explicitly mentioned):

| Domain / Topics | Target File | Established Table Schema |
| :--- | :--- | :--- |
| **Frontend System Design** (Communication patterns, rendering, performance, security, caching, microfrontends) | `Frontend System Design/Frontend System Design.md` | `\| Topic \| Core Concepts & Mental Model \| Tools & Libraries \| Key Techniques \| Tradeoffs & Failure Modes \| Resources \|` |
| **Backend Engineering** (Node/Express, Fastify, APIs, SQL, NoSQL, Redis, Queues, Auth) | `Backend/Backend.md` | `\| Skill \| Core Concepts & Mental Model \| Tools & Libraries \| Key Techniques \| Tradeoffs & Failure Modes \| Resources \|` |
| **DevOps & Cloud** (Linux, Git, Docker, Kubernetes, CI/CD, Nginx, Terraform, SRE) | `DevOps for Developers/DevOps for Developer.md` | `\| Skill \| Core Concepts & Mental Model \| Key Commands & Techniques \| Tradeoffs & Failure Modes \| Resources \|` |
| **Frontend Core** (HTML, CSS, JS, TS, React, Next.js, Redux, Zustand) | `Frontend/Frontend.md`, `Frontend/React JS.md`, or `Frontend/Next JS.md` | `\| Skill \| Core Concepts \| Tools & Libraries \| Key Techniques \| Resources \|` |
| **Backend System Design** (HLD, sharding, distributed systems, consensus) | `Backend System Design/` | Match existing guide structure / tables |
| **AI Engineering — Core Foundations** (Embeddings, ANN, Attention, Compression) | `AI Engineering/Core AI/AI Engineering Concept.md` | `\| Topic / Skill \| Core Concepts & Mental Model \| Tools & Libraries \| Key Techniques \| Tradeoffs & Failure Modes \| Resources \|` |
| **AI Engineering — Backend & Runtime** (RAG, Vector DBs, Agents, MCP, Serving, Gateways) | `AI Engineering/AI Backend Engineering/` (`RAG & Vector Architecture.md`, `Agentic AI & Orchestration.md`, `LLM Serving & Gateways.md`) | `\| Topic / Skill \| Core Concepts & Mental Model \| Tools & Libraries \| Key Techniques \| Tradeoffs & Failure Modes \| Resources \|` |
| **AI Engineering — LLMOps & Quality** (Evals, Ragas, Tracing, Guardrails) | `AI Engineering/LLMsOps/` (`LLM Evals & Benchmarks.md`, `Observability & Guardrails.md`) | `\| Topic / Skill \| Core Concepts & Mental Model \| Tools & Libraries \| Key Techniques \| Tradeoffs & Failure Modes \| Resources \|` |
| **AI Engineering — Frontend & System Design** (Generative UI, Vercel AI SDK, GEO/AEO) | `AI Engineering/AI Frontend Engineering/` or `AI System Design/` | Match existing guide structure / tables |

---

## 2. Mandatory File Grounding & Deduplication (Read BEFORE Proposing)

> [!IMPORTANT]
> **Zero Guesswork / Never Generate from Memory:**  
> The agent MUST NOT generate table rows solely from general memory or `AGENTS.md`.  
> Before proposing any table row or diff, the agent **MUST read the target file's relevant section** using file inspection tools.

### Grounding Checklist for the Agent:
1. **Learn from Current Structure**: Open the target file and inspect:
   - What are the exact table headers in that specific section?
   - What is the tone, depth, and formatting style (e.g. bold titles, backtick usage, link formatting)?
   - How are existing rows formatted? (Use them as the direct few-shot template).
2. **Audit for Duplicates**:
   - Check if the topic or any sub-concept is already documented (e.g., `WebSockets` under `## Communication Patterns`).
   - If already present: **DO NOT** create a duplicate row. Propose an **enrichment diff** only if the user brings new tools, techniques, or tradeoffs.
3. **Section Placement**:
   - Confirm the exact heading and line position where the new row should be placed before proposing.

---

## 3. Raw Notes Cleanup & Gap Analysis
1. **Never add raw, unvetted text directly**: Strip conversational filler, timestamps, typos, and formatting noise. Extract clean, structured technical facts.
2. **If Raw Notes were provided**:
   - Compare what the user's notes cover vs. existing codebase coverage vs. industry best practices.
   - Present a clear comparison summary:
     - ✅ **Covered in User Notes**: Extracted key points.
     - 🔍 **Already in Codebase**: Existing context.
     - 💡 **Missing Gaps Found**: Key edge cases, failure modes, or RFC standards not in the user's notes.
   - **Ask permission** before adding the extra missing points into the final table.
3. **If only Topic Name was provided (No Raw Notes)**:
   - Automatically cover all standard, high-yield concepts under that pattern/topic.

---

## 4. Markdown Table Construction & Strict Rules

### Fundamental Rule: Tables Only, Zero Prose Clutter
- **DO NOT** add prose paragraphs, essays, study notes, or answer explanations above or below the tables.
- The files are strictly curated **reference tables**. Every piece of learning must be condensed into the appropriate table row.

### Context-Adaptive Table Schemas:
Tables adapt dynamically based on the nature of the topic:

#### 1. Rule of Existing Context:
- If appending to an existing table in any file, **ALWAYS match that table's exact column headers**.

#### 2. Architecture, System Design & Protocol Comparisons (e.g., API Design, Caching, DBs, Auth, Comm Patterns):
Requires the **6-column Tradeoffs schema** because system design is fundamentally about evaluating tradeoffs:
`| Topic / Skill | Core Concepts & Mental Model | Tools & Libraries | Key Techniques | Tradeoffs & Failure Modes | Resources |`
- `Tradeoffs & Failure Modes`: Highlight `✅` pros and `❌` failure modes/cons/limitations (e.g., in REST API design: over/under-fetching, N+1, breaking changes).

#### 3. Core Tech, Syntax & Language/Framework APIs (e.g., React Hooks, CSS Grid, HTML, TS Syntax):
Uses the **5-column Focused schema** without unnecessary tradeoffs clutter:
`| Skill | Core Concepts | Tools & Libraries | Key Techniques | Resources |`
- Concentrates on what it is, primary use cases, and how/where to implement it.

#### 4. DevOps & Cloud Infrastructure:
Uses the **5-column Command-Oriented schema**:
`| Skill | Core Concepts & Mental Model | Key Commands & Techniques | Tradeoffs & Failure Modes | Resources |`
- Replaces general libraries with practical terminal commands and execution techniques.

### Resource Linking Priority:
- **Priority 1**: Official documentation first (MDN, React, Next.js, Node, Socket.io, Stripe, RFCs).
- **Priority 2**: Authoritative tutorials (OWASP, web.dev, DigitalOcean, Cloudflare) only if official docs lack guides.

---

## 5. User Confirmation & Safe Append
- Show the table preview to the user matching the exact target schema.
- Upon approval, append cleanly to the exact table in the target markdown file without corrupting markdown table syntax or surrounding headings.
- If input was read from `inbox.md`, reset `inbox.md` to its original clean template.
