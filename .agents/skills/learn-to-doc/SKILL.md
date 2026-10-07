---
name: learn-to-doc
description: Ingests technical topics or raw learning notes, resolves target domain files, detects duplicates, performs gap analysis, asks permission for missing concepts, and formats clean markdown tables for Technical Skill documentation.
---

# Learn-to-Doc Skill

This skill guides the AI agent to turn raw technical notes or topic keywords into structured, schema-compliant documentation tables inside `Technical Skill`.

## Invocation Triggers
Trigger this skill whenever the user says:
- "Process inbox" (when content contains technical concepts or architecture notes)
- "Process inbox technical"
- "I learned X..."
- "Add topic X to my notes..."
- "Process this raw learning on X..."
- "Document X in table format..."

## Execution Steps

### 1. Identify Domain & Target File
- Analyze the topic keywords.
- Locate the target file inside the `Technical Skill/` directory:
  - `Technical Skill/Frontend System Design/Frontend System Design.md`
  - `Technical Skill/Backend/Backend.md`
  - `Technical Skill/DevOps for Developers/DevOps for Developer.md`
  - `Technical Skill/Frontend/` (`Frontend.md`, `React JS.md`, `Next JS.md`)
  - `Technical Skill/AI Engineering/`
  - `Technical Skill/Backend System Design/`
  - `Technical Skill/DSA/DSA.md`

### 2. Mandatory Grounding & Deduplication (Read First)
- **Inspect Target File**: Open and read the target section using `view_file`.
- **Learn from Existing Rows**: Check the exact column headers, formatting conventions, depth, and tone. Use existing rows as the direct few-shot template.
- **Audit & Enrichment Diff Mode**:
  - Check if the concept or synonyms already exist.
  - If already present, **do not duplicate**. Compare current content vs new learning.
  - If new tools, techniques, or failure modes are found, present an **Enrichment Diff** (`+ Added`) and merged row preview.
  - Update the existing row **in-place** upon user approval.

### 3. Clean & Analyze Notes
- Strip colloquial speech, timestamps, filler, and unverified data.
- If raw notes were provided:
  - Summarize what the user provided.
  - Check for critical missing industry concepts (e.g., reconnection backoff, heartbeat/ping-pong, fallback strategies).
  - Explicitly ask the user: *"Your notes cover A and B. Would you like me to include C and D as well?"*
- If no raw notes were provided:
  - Fill all standard canonical patterns under the topic.

### 4. Render Table Preview
- **Strict Rule: Tables Only, Zero Prose Clutter**: Everything goes strictly into the table row. Zero prose paragraphs outside tables.
- **Summarized Learning Reference (Not a Detailed Textbook)**: Keep cells crisp, punchy, and readable at a glance (1–2 sentences for mental models, canonical tools only, core practical techniques, 1–2 key tradeoffs `✅`/`❌`). Never output bloated textbook explanations.
- **💡 Plain-Language Intuition & Simple Use Cases**: Always use simple, intuitive words to explain concepts. The table exists to answer: (1) **WHAT** it is, (2) **WHY** we use it (real-world problem solved), and (3) **WHEN** to use it (relatable, concrete production use cases). Avoid academic jargon or convoluted phrasing.

- **Context-Adaptive Schemas**:
  - **Rule of Existing Context**: If target section already has a table, always match its exact columns.
  - **System Design & Architectural Topics** (API design, protocols, caching, databases, sharding, auth): 6 columns including `Tradeoffs & Failure Modes` (`✅` pros, `❌` pitfalls).
  - **Core Tech & Syntax Basics** (React hooks, CSS, HTML, TS syntax): 5-column focused schema (`Skill | Core Concepts | Tools & Libraries | Key Techniques | Resources`).
  - **DevOps & Cloud**: 5 columns with `Key Commands & Techniques` and `Tradeoffs & Failure Modes`.
- **Resource Priority**: MDN/official docs first; authoritative guides second.


### 5. Append & Reset Dropzone
- Upon user confirmation, append rows into the target table before section breaks (`---` or next `##`).
- If the content was processed from `inbox.md`, clear the processed technical notes from `inbox.md`.

### 6. Format & Coverage Sync
- Run `python scripts/prettify_tables.py <target_file>` to ensure vertical column pipe alignment.
- Run `python scripts/sync_coverage.py` to refresh [`INTERVIEW_COVERAGE.md`](../../../INTERVIEW_COVERAGE.md).

### 7. 🔄 2-Way Cross-Linking Bridge (Interview Inspire)
- For every documented or enriched concept (e.g. *WebSockets*, *Redis*, *RAG*):
  - Check whether relevant interview questions exist in the corresponding file in `Interview Inspire/`.
  - Proactively suggest a ready-to-copy snippet of **5 high-yield interview questions** formatted for `Interview Inspire/` covering:
    1. 🧠 **Core Concept**: Mental model & fundamental mechanics.
    2. ⚙️ **Implementation**: Low-level protocol, handshake, or internals.
    3. ⚖️ **Tradeoffs & Failure Modes**: Bottlenecks, edge cases, failure states.
    4. 📊 **Observability**: Latency, metrics, logs, tracing.
    5. 🚨 **Production Debugging**: Incident scenarios, memory/socket leaks.

