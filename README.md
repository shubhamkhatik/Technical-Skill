# 🚀 Technical Skill — Engineering Knowledge Base & Automated Ingestion System

> **A curated, production-grade engineering reference library and automated learning-to-table system.**  
> Built for zero prose clutter, strict markdown table schemas, evergreen concept enrichment, and seamless interview readiness tracking with [`shubhamkhatik/Interview-Inspire`](https://github.com/shubhamkhatik/Interview-Inspire).

---

## ⚡ Quick Navigation

| Track                        | Primary Guides                                                                                                                                                                                                                                                                              | Description                                                   | Interview Practice Bank                                                                                                                  |
| :--------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------- |
| **Frontend Engineering**     | [`Frontend.md`](./Frontend/Frontend.md) · [`React JS.md`](./Frontend/React%20JS.md) · [`Next JS.md`](./Frontend/Next%20JS.md)                                                                                                                                                               | Web APIs, React 18+ hooks, App Router, SSR/SSG/ISR            | [Frontend Questions ↗](https://github.com/shubhamkhatik/Interview-Inspire/blob/main/software-engineering/frontend/frontend.md)           |
| **Frontend System Design**   | [`Frontend System Design.md`](./Frontend%20System%20Design/Frontend%20System%20Design.md)                                                                                                                                                                                                   | Protocols (SSE/WS/Webhooks), Security (XSS/CSRF/CSP), Caching | [Frontend Design Questions ↗](https://github.com/shubhamkhatik/Interview-Inspire/blob/main/software-engineering/frontend/frontend.md)    |
| **Backend Engineering**      | [`Backend.md`](./Backend/Backend.md) · [`Nodejs+Express.md`](./Backend/Nodejs+Express.md)                                                                                                                                                                                                   | Node Event Loop, APIs, PostgreSQL, Redis, Queues, Auth        | [Backend Questions ↗](https://github.com/shubhamkhatik/Interview-Inspire/blob/main/software-engineering/backend/backend.md)              |
| **Backend System Design**    | [`Backend System Design.md`](./Backend%20System%20Design/Backend%20System%20Design.md) · [`roadmap.sh`](./Backend%20System%20Design/roadmap.sh%20system-design.md)                                                                                                                          | Scalability, Sharding, Caching, CAP, Consensus, HLD           | [System Design Bank ↗](https://github.com/shubhamkhatik/Interview-Inspire/blob/main/software-engineering/system-design/system-design.md) |
| **Production System Design** | [`Production System Design.md`](./Production%20System%20Design/Production%20System%20Design.md)                                                                                                                                                                                             | High Availability, Fault Tolerance, SLOs/SLIs, Zero Downtime  | [Production Design ↗](https://github.com/shubhamkhatik/Interview-Inspire/blob/main/software-engineering/system-design/system-design.md)  |
| **DevOps & Cloud**           | [`DevOps for Developer.md`](./DevOps%20for%20Developers/DevOps%20for%20Developer.md)                                                                                                                                                                                                        | Linux, Git, Docker, Kubernetes, CI/CD, Nginx, Terraform       | [DevOps Questions ↗](https://github.com/shubhamkhatik/Interview-Inspire/blob/main/software-engineering/devops/devops.md)                 |
| **AI Engineering**           | [`AI Engineering Hub`](./AI%20Engineering/AI%20Engineering.md) · [`Core AI`](./AI%20Engineering/Core%20AI/AI%20Engineering%20Concept.md) · [`AI Backend`](./AI%20Engineering/AI%20Backend%20Engineering/AI%20Backend%20Engineering.md) · [`LLMsOps`](./AI%20Engineering/LLMsOps/LLMsOps.md) | Vector Search, RAG, Agentic AI, MCP, vLLM, Evals              | [AI Engineering Banks ↗](https://github.com/shubhamkhatik/Interview-Inspire/tree/main/ai-engineering)                                    |
| **DSA & Algorithms**         | [`DSA.md`](./DSA/DSA.md)                                                                                                                                                                                                                                                                    | Sliding Window, Two Pointers, Trees, Graphs, DP               | [DSA Problem Bank ↗](https://github.com/shubhamkhatik/Interview-Inspire/blob/main/dsa-problem-solving/dsa.md)                            |

---

## 🌟 Key Features & Workflow

### 1. 📥 Learning Dropzone (`inbox.md`)
Never worry about manually finding the right file or formatting markdown tables while watching a course or video:
1. Paste raw, messy notes or bullet points directly into [`inbox.md`](./inbox.md).
2. Type in AI chat: **`"Process inbox"`**.
3. The AI agent cleans up the notes, auto-detects the domain, matches the target schema, updates the table, and resets `inbox.md` to a clean template.

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

### 3. 🎯 Live Interview Sync (`INTERVIEW_COVERAGE.md`)
Cross-references notes in real time against [`shubhamkhatik/Interview-Inspire`](https://github.com/shubhamkhatik/Interview-Inspire) (390+ curated interview questions):
- Tracks your **Overall Preparation Score** (e.g. `25.6%` of questions covered).
- Generates a visual domain-by-domain progress bar.
- Outputs an actionable **High-Yield Checklist** showing interview questions that don't yet have concept notes in this repo.
- Refresh anytime with:
  ```bash
  python scripts/sync_interview_coverage.py
  ```

### 4. 📐 Zero-Dependency Table Prettifier (`scripts/prettify_tables.py`)
No matter how messy table pipes get during editing, running the prettifier vertically aligns all table columns across every file:
```bash
python scripts/prettify_tables.py --all
```

### 5. 🤖 Automated AI Pair-Programming (`AGENTS.md`)
All repository rules, schema formats, deduplication logic, and automation protocols are codified in [`AGENTS.md`](./AGENTS.md) and `.agents/skills/learn-to-doc/`. Every AI agent automatically adheres to these rules—you don't have to remember manual commands.

---

## 📖 How to Use This Repo

### Scenario A: You Just Finished a Video / Course
1. Open [`inbox.md`](./inbox.md) and paste your notes.
2. In chat, say: **`"Process inbox"`**.
3. Review the preview and say **`"Approve"`**.

### Scenario B: You Want to Research / Document a Specific Concept
1. In chat, say: **`"Document Server-Sent Events"`** or **`"Add notes on Redis caching patterns"`**.
2. The AI inspects the target file first, audits for duplicates, suggests key failure modes, and renders a clean preview.

### Scenario C: You Want to Prepare for Interviews
1. Open [`INTERVIEW_COVERAGE.md`](./INTERVIEW_COVERAGE.md) to inspect your readiness %.
2. Copy any gap question from the checklist into [`inbox.md`](./inbox.md).
3. Say in chat: **`"Process inbox"`** to turn that question into a permanent reference table entry!

---

## 🛠️ Repository Scripts

| Script               | Purpose                                                    | Command                                     |
| :------------------- | :--------------------------------------------------------- | :------------------------------------------ |
| **Table Prettifier** | Aligns all vertical `\|` pipes across markdown tables      | `python scripts/prettify_tables.py --all`   |
| **Interview Sync**   | Fetches latest questions from remote repo & updates matrix | `python scripts/sync_interview_coverage.py` |

---

## 🏛️ Schema Guidelines

All documentation files follow strict reference table formats with **zero prose clutter**:

- **System Design & Protocols** (6 columns): `| Topic / Skill | Core Concepts & Mental Model | Tools & Libraries | Key Techniques | Tradeoffs & Failure Modes | Resources |`
- **Core Syntax & Language APIs** (5 columns): `| Skill | Core Concepts | Tools & Libraries | Key Techniques | Resources |`
- **DevOps & Infrastructure** (5 columns): `| Skill | Core Concepts & Mental Model | Key Commands & Techniques | Tradeoffs & Failure Modes | Resources |`
