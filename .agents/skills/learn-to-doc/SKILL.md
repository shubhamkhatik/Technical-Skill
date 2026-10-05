---
name: learn-to-doc
description: Ingests technical topics or raw learning notes, resolves target domain files, detects duplicates, performs gap analysis, asks permission for missing concepts, and formats clean markdown tables for Technical Skill documentation.
---

# Learn-to-Doc Skill

This skill guides the AI agent to turn raw technical notes or topic keywords into structured, schema-compliant documentation tables inside `Technical Skill`.

## Invocation Triggers
Trigger this skill whenever the user says:
- "Process inbox"
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
- **Strict Rule**: Zero prose notes or answer dumps outside tables. Everything goes into the table row.
- **Context-Adaptive Schemas**:
  - **Rule of Existing Context**: If target section already has a table, always match its exact columns.
  - **System Design & Architectural Topics** (API design, protocols, caching, databases, sharding, auth): 6 columns including `Tradeoffs & Failure Modes` (`✅` pros, `❌` pitfalls).
  - **Core Tech & Syntax Basics** (React hooks, CSS, HTML, TS syntax): 5-column focused schema (`Skill | Core Concepts | Tools & Libraries | Key Techniques | Resources`).
  - **DevOps & Cloud**: 5 columns with `Key Commands & Techniques` and `Tradeoffs & Failure Modes`.
- **Resource Priority**: MDN/official docs first; authoritative guides second.

### 5. Append
- Upon user confirmation, append rows into the target table before section breaks (`---` or next `##`).
- If the content was processed from `inbox.md`, reset `inbox.md` to its original empty dropzone template.

### 6. Format & Coverage Sync
- Run `python scripts/prettify_tables.py <target_file>` to ensure vertical column pipe alignment.
- Run `python scripts/sync_interview_coverage.py` to refresh [INTERVIEW_COVERAGE.md](file:///g:/study/Doc-Update/Technical%20Skill/INTERVIEW_COVERAGE.md) and update readiness against [`Interview-Inspire`](https://github.com/shubhamkhatik/Interview-Inspire).

