# ⚡ Tech Skills & Interview Guide — Dual-Track Engineering Ecosystem

> **A curated, production-grade engineering reference library and automated question ingestion system.**  
> Built for zero prose clutter, strict markdown table schemas, evergreen concept enrichment, and high-yield interview preparation across Software Engineering, AI Engineering, and DSA.

---

## ⚡ Quick Navigation

| Track                        | Primary Guides                                                                                                                                                                                                                                                                                                                                                      | Description                                                        | Interview Practice Bank                                                                           |
| :--------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :----------------------------------------------------------------- | :------------------------------------------------------------------------------------------------ |
| **Frontend Engineering**     | [`Frontend.md`](./Technical%20Skill/Frontend/Frontend.md) · [`React JS.md`](./Technical%20Skill/Frontend/React%20JS.md) · [`Next JS.md`](./Technical%20Skill/Frontend/Next%20JS.md)                                                                                                                                                                                 | Web APIs, React 18+ hooks, App Router, SSR/SSG/ISR                 | [Frontend Questions ↗](./Interview%20Inspire/software-engineering/frontend/frontend.md)           |
| **Frontend System Design**   | [`Frontend System Design.md`](./Technical%20Skill/Frontend%20System%20Design/Frontend%20System%20Design.md)                                                                                                                                                                                                                                                         | Protocols (SSE/WS/Webhooks), Security (XSS/CSRF/CSP), Caching      | [Frontend Design Questions ↗](./Interview%20Inspire/software-engineering/frontend/frontend.md)    |
| **Backend Engineering**      | [`Backend.md`](./Technical%20Skill/Backend/Backend.md) · [`Nodejs+Express.md`](./Technical%20Skill/Backend/Nodejs+Express.md)                                                                                                                                                                                                                                       | Node Event Loop, APIs, PostgreSQL, Redis, Queues, Auth             | [Backend Questions ↗](./Interview%20Inspire/software-engineering/backend/backend.md)              |
| **Backend System Design**    | [`Backend System Design.md`](./Technical%20Skill/Backend%20System%20Design/Backend%20System%20Design.md) · [`roadmap.sh`](./Technical%20Skill/Backend%20System%20Design/roadmap.sh%20system-design.md)                                                                                                                                                              | Scalability, Sharding, Caching, CAP, Consensus, HLD                | [System Design Bank ↗](./Interview%20Inspire/software-engineering/system-design/system-design.md) |
| **Production System Design** | [`Production System Design.md`](./Technical%20Skill/Production%20System%20Design/Production%20System%20Design.md)                                                                                                                                                                                                                                                   | High Availability, Fault Tolerance, SLOs/SLIs, Zero Downtime       | [Production Design ↗](./Interview%20Inspire/software-engineering/system-design/system-design.md)  |
| **DevOps & Cloud**           | [`DevOps for Developer.md`](./Technical%20Skill/DevOps%20for%20Developers/DevOps%20for%20Developer.md)                                                                                                                                                                                                                                                              | Linux, Git, Docker, Kubernetes, CI/CD, Nginx, Terraform            | [DevOps Questions ↗](./Interview%20Inspire/software-engineering/devops/devops.md)                 |
| **AI Engineering**           | [`AI Engineering Hub`](./Technical%20Skill/AI%20Engineering/AI%20Engineering.md) · [`Core AI`](./Technical%20Skill/AI%20Engineering/Core%20AI/AI%20Engineering%20Concept.md) · [`AI Backend`](./Technical%20Skill/AI%20Engineering/AI%20Backend%20Engineering/AI%20Backend%20Engineering.md) · [`LLMsOps`](./Technical%20Skill/AI%20Engineering/LLMsOps/LLMsOps.md) | Vector Search, RAG, Agentic AI, MCP, vLLM, Evals                   | [AI Question Banks ↗](./Interview%20Inspire/ai-engineering/)                                      |
| **DSA & Algorithms**         | [`DSA.md`](./Technical%20Skill/DSA/DSA.md)                                                                                                                                                                                                                                                                                                                          | Sliding Window, Two Pointers, Trees, Graphs, DP                    | [DSA Problem Bank ↗](./Interview%20Inspire/dsa-problem-solving/dsa.md)                            |
| **Behavioral & Leadership**  | [`behavioral.md`](./Interview%20Inspire/software-engineering/behavioral/behavioral.md)                                                                                                                                                                                                                                                                              | Ownership, Deadlines, Production Incidents, Mentorship & Standards | [Behavioral Questions ↗](./Interview%20Inspire/software-engineering/behavioral/behavioral.md)     |

---

## 🌟 Key Features & Workflow

### 1. 📥 Learning & Question Dropzone (`inbox.md`)
Never worry about manually finding the right file or formatting tables while studying or reading interview experiences:
1. Paste raw, messy notes or interview questions directly into [`inbox.md`](./inbox.md).
2. Type in AI chat: **`"Process inbox"`**.
3. The AI agent automatically:
   - Detects whether it contains **technical learning notes** or **interview questions**.
   - Appends learning notes as clean reference rows in `Technical Skill/` (or updates existing rows via Enrichment Diff).
   - Appends interview questions as clean numbered checklists in `Interview Inspire/`.
   - Resets `inbox.md` to a clean template.

### 2. 🔄 Enrichment Diff Mode (Evergreen Notes)
Instead of rejecting topics with *"already exists"*, the system treats your documentation as living, evergreen knowledge:
- If you document a concept that already exists (e.g. `WebSockets`), the agent compares what is currently recorded against your new input.
- Shows a clean visual diff:
  ```diff
    Topic: WebSockets
      Tools: Socket.io, native WebSocket API
  +   Added Tools: PartyKit, Cloudflare Durable Objects
      Key Techniques: Event-based messaging, heartbeat/ping-pong
  +   Added Techniques: Exponential backoff with jitter
  ```
- Merges new tools, techniques, and failure modes **in-place** without creating duplicate rows.

### 3. 📐 Zero-Dependency Table Prettifier (`scripts/prettify_tables.py`)
No matter how messy table pipes get during editing, running the prettifier vertically aligns all table columns across every file:
```bash
python scripts/prettify_tables.py --all
```

### 4. 🤖 Automated AI Pair-Programming (`AGENTS.md`)
All repository rules, schema formats, deduplication logic, and automation protocols are codified in [`AGENTS.md`](./AGENTS.md) and `.agents/skills/`. Every AI agent automatically adheres to these rules—you don't have to remember manual commands.

---

## 📖 How to Use This Repo

### Scenario A: You Just Finished a Video / Course
1. Open [`inbox.md`](./inbox.md) and paste your notes.
2. In chat, say: **`"Process inbox"`**.
3. Review the preview and say **`"Approve"`**.

### Scenario B: You Encountered New Interview Questions
1. Open [`inbox.md`](./inbox.md) and paste the questions (or open a GitHub Issue on mobile).
2. The system auto-sorts, deduplicates, and places them in the right domain checklist in `Interview Inspire/`.

### Scenario C: You Want to Prepare Before an Interview
1. Open the domain checklist (e.g. [`frontend.md`](./Interview%20Inspire/software-engineering/frontend/frontend.md) or [`backend.md`](./Interview%20Inspire/software-engineering/backend/backend.md)) to rapidly test your recall against high-yield questions and output snippets.

---

## 🛠️ Repository Scripts

| Script               | Purpose                                               | Command                                   |
| :------------------- | :---------------------------------------------------- | :---------------------------------------- |
| **Table Prettifier** | Aligns all vertical `\|` pipes across markdown tables | `python scripts/prettify_tables.py --all` |
| **Interview Sorter** | Classifies, deduplicates & formats raw question dumps | `python scripts/process_questions.py`     |

---

## 🏛️ Schema Guidelines

All documentation files follow strict reference table formats with **zero prose clutter**:

- **System Design & Protocols** (6 columns): `| Topic / Skill | Core Concepts & Mental Model | Tools & Libraries | Key Techniques | Tradeoffs & Failure Modes | Resources |`
- **Core Syntax & Language APIs** (5 columns): `| Skill | Core Concepts | Tools & Libraries | Key Techniques | Resources |`
- **DevOps & Infrastructure** (5 columns): `| Skill | Core Concepts & Mental Model | Key Commands & Techniques | Tradeoffs & Failure Modes | Resources |`
