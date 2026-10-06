---
name: curate-questions
description: Ingests raw interview questions or problem dumps, maps them to the appropriate domain checklist in Interview Inspire, deduplicates, formats as numbered items, and cross-links with Technical Skill concepts.
---

# Curate-Questions Skill

This skill guides the AI agent to turn raw interview questions, interview experiences, or problem dumps into clean, high-yield question checklists inside `Interview Inspire/`.

## Invocation Triggers
Trigger this skill whenever the user says:
- "Process inbox" (when content contains interview questions)
- "Process inbox interview"
- "Add interview questions for X..."
- "Sort interview questions"
- "Curate these questions..."

## Execution Steps

### 1. Identify Domain & Target File
- Analyze the question topics and map to the corresponding target file inside `Interview Inspire/`:
  - `Interview Inspire/software-engineering/frontend/frontend.md`
  - `Interview Inspire/software-engineering/backend/backend.md`
  - `Interview Inspire/software-engineering/devops/devops.md`
  - `Interview Inspire/software-engineering/system-design/system-design.md`
  - `Interview Inspire/ai-engineering/foundations/foundations.md`
  - `Interview Inspire/ai-engineering/llm-and-rag/llm-and-rag.md`
  - `Interview Inspire/ai-engineering/agentic-ai/agentic-ai.md`
  - `Interview Inspire/ai-engineering/mlops-llmops/mlops-llmops.md`
  - `Interview Inspire/ai-engineering/ai-system-design/ai-system-design.md`
  - `Interview Inspire/dsa-problem-solving/dsa.md`
  - `Interview Inspire/interview-experiences/`

### 2. Mandatory Grounding & Deduplication (Read First)
- **Inspect Target File**: Open and read the relevant section in the target file using `view_file`.
- **Deduplicate**: Check existing numbered questions under the matching `## Heading`. Skip any question that is already present.
- **Section Selection**:
  - Identify the appropriate existing `## Heading` or `### Sub-heading`.
  - If no matching heading exists, propose a clean, canonical heading.

### 3. Format as Strict Question Checklists
- **Strict Rule: Questions Only**:
  - **Zero Answers**: No solutions, essays, explanations, or code blocks in question checklists.
  - **Keyword Formatting**: Wrap code keywords, APIs, and types in backticks (e.g., `useMemo`, `Promise.all()`, `pgvector`, `cgroups`).
  - **Sequential Numbering**: Continue the numbered list sequentially (`1. `, `2. `, etc.).

### 4. Append & Reset Dropzone
- Append the curated questions under the target section in the file.
- If processed from `inbox.md`, clear the processed questions from `inbox.md`.

### 5. Coverage Refresh
- Run `python scripts/sync_coverage.py` to refresh [`INTERVIEW_COVERAGE.md`](../../../INTERVIEW_COVERAGE.md).


### 6. 🔄 2-Way Cross-Linking Bridge (Technical Skill)
- Check whether the core concept underlying the new questions exists in `Technical Skill/`.
- If the concept is missing from `Technical Skill/`:
  - Alert the user: *"Concept X is not yet documented in Technical Skill/."*
  - Proactively offer a standardized reference table row drafted for the appropriate file in `Technical Skill/`.
