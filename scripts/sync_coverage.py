#!/usr/bin/env python3
"""
Dual-Track Engineering Coverage & Bidirectional Sync Script
Zero external dependencies (Python 3 standard library).

Features:
- Bidirectional synchronization between Technical Skill and Interview Inspire.
- Track A -> Track B: Identifies Orphan Concepts in Technical Skill (concepts with 0 interview questions).
- Track B -> Track A: Identifies Uncovered Questions in Interview Inspire (questions with 0 concept rows).
- Calculates domain-by-domain readiness scores and question coverage percentages.
- Generates the unified INTERVIEW_COVERAGE.md dual-track dashboard.
"""

import os
import sys
import re
import urllib.request
import urllib.error

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

TRACK_MAPPING = {
    "Frontend Engineering": {
        "remote_file": "software-engineering/frontend/frontend.md",
        "local_files": [
            "Frontend/Frontend.md",
            "Frontend/React JS.md",
            "Frontend/Next JS.md",
            "Frontend System Design/Frontend System Design.md",
        ],
    },
    "Backend Engineering": {
        "remote_file": "software-engineering/backend/backend.md",
        "local_files": [
            "Backend/Backend.md",
            "Backend/Nodejs+Express.md",
        ],
    },
    "DevOps & Cloud": {
        "remote_file": "software-engineering/devops/devops.md",
        "local_files": [
            "DevOps for Developers/DevOps for Developer.md",
        ],
    },
    "System Design": {
        "remote_file": "software-engineering/system-design/system-design.md",
        "local_files": [
            "Backend System Design/Backend System Design.md",
            "Production System Design/Production System Design.md",
            "Backend System Design/roadmap.sh system-design.md",
        ],
    },
    "AI Foundations & Core": {
        "remote_file": "ai-engineering/foundations/foundations.md",
        "local_files": [
            "AI Engineering/Core AI/AI Engineering Concept.md",
        ],
    },
    "AI - LLM & RAG": {
        "remote_file": "ai-engineering/llm-and-rag/llm-and-rag.md",
        "local_files": [
            "AI Engineering/AI Backend Engineering/RAG & Vector Architecture.md",
        ],
    },
    "AI - Agentic AI": {
        "remote_file": "ai-engineering/agentic-ai/agentic-ai.md",
        "local_files": [
            "AI Engineering/AI Backend Engineering/Agentic AI & Orchestration.md",
        ],
    },
    "AI - MLOps & LLMOps": {
        "remote_file": "ai-engineering/mlops-llmops/mlops-llmops.md",
        "local_files": [
            "AI Engineering/AI Backend Engineering/LLM Serving & Gateways.md",
            "AI Engineering/LLMsOps/LLM Evals & Benchmarks.md",
            "AI Engineering/LLMsOps/Observability & Guardrails.md",
        ],
    },
    "AI - System Design": {
        "remote_file": "ai-engineering/ai-system-design/ai-system-design.md",
        "local_files": [
            "AI Engineering/AI System Design/AI System Design.md",
        ],
    },
    "DSA": {
        "remote_file": "dsa-problem-solving/dsa.md",
        "local_files": [
            "DSA/DSA.md",
        ],
    },
}

GITHUB_RAW_BASE = "https://raw.githubusercontent.com/shubhamkhatik/Interview-Inspire/main"
GITHUB_REPO_BASE = "https://github.com/shubhamkhatik/Interview-Inspire/blob/main"

def resolve_tech_skill_path(repo_root: str, rel_path: str) -> str:
    """Resolves path whether inside Technical Skill/ subfolder or at root."""
    p1 = os.path.join(repo_root, "Technical Skill", rel_path)
    if os.path.exists(p1):
        return p1
    p2 = os.path.join(repo_root, rel_path)
    if os.path.exists(p2):
        return p2
    return p1

def fetch_question_file(repo_root: str, rel_path: str) -> str:
    """Fetches interview questions from local Interview Inspire directory or fallback remote URL."""
    local_path = os.path.join(repo_root, "Interview Inspire", rel_path)
    if os.path.exists(local_path):
        try:
            with open(local_path, "r", encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            print(f"Warning: Could not read local {local_path}: {e}", file=sys.stderr)

    url = f"{GITHUB_RAW_BASE}/{rel_path}"
    req = urllib.request.Request(url, headers={"User-Agent": "TechnicalSkillSync/2.0"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except Exception as e:
        print(f"Warning: Could not fetch {url}: {e}", file=sys.stderr)
        return ""

def parse_interview_questions(markdown_content: str) -> list[dict]:
    """Extracts numbered questions from a markdown file with headings."""
    questions = []
    current_heading = "General"

    for line in markdown_content.splitlines():
        stripped = line.strip()
        if stripped.startswith("## "):
            current_heading = stripped[3:].strip()
            continue

        q_match = re.match(r"^\d+\.\s+(.*)", stripped)
        if q_match:
            q_text = q_match.group(1).strip()
            questions.append({
                "heading": current_heading,
                "question": q_text
            })

    return questions

def extract_structured_concepts(repo_root: str, local_files: list[str]) -> list[dict]:
    """
    Extracts individual concept entities from markdown tables.
    Returns a list of dicts:
    {
        'display_name': 'WebSockets',
        'search_terms': ['websockets', 'websocket'],
        'source_file': 'Backend/Backend.md',
    }
    """
    concepts = []
    seen_display_names = set()

    for rel_path in local_files:
        full_path = resolve_tech_skill_path(repo_root, rel_path)
        if not os.path.exists(full_path):
            continue

        try:
            with open(full_path, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception:
            continue

        in_code_block = False

        for line in content.splitlines():
            stripped = line.strip()
            if stripped.startswith("```"):
                in_code_block = not in_code_block
                continue
            if in_code_block:
                continue

            if stripped.startswith("|") and stripped.endswith("|") and stripped.count("|") >= 2:
                cells = [c.strip() for c in stripped[1:-1].split("|")]
                if not cells or not cells[0]:
                    continue
                if re.match(r"^:?-+:?$", cells[0]):
                    continue

                first_cell = cells[0].replace("**", "").replace("*", "").replace("`", "").strip()
                cell_lower = first_cell.lower()

                if any(h in cell_lower for h in ["topic", "skill", "method / domain", "layer", "concept"]) and len(cell_lower.split()) <= 4:
                    continue

                if len(first_cell) >= 2 and first_cell not in seen_display_names:
                    seen_display_names.add(first_cell)
                    search_terms = {cell_lower}

                    # Add aliases from parentheses e.g. "Product Quantization (PQ)"
                    m = re.findall(r"\((.*?)\)", first_cell)
                    for alias in m:
                        for sub_alias in re.split(r"[/,]| vs ", alias):
                            sub = sub_alias.strip().lower()
                            if len(sub) >= 2 and sub not in ("legacy", "modern", "new", "pattern", "system design"):
                                search_terms.add(sub)

                    base_topic = re.sub(r"\(.*?\)", "", cell_lower).strip()
                    if len(base_topic) >= 3:
                        search_terms.add(base_topic)

                    concepts.append({
                        "display_name": first_cell,
                        "search_terms": search_terms,
                        "source_file": rel_path,
                    })

            # DSA pattern lines
            pat_match = re.match(r"^([A-Za-z0-9\s\-]+)\s*\[(Pattern|Algorithm|Data Structure|Core Concept)\]", stripped)
            if pat_match:
                pat_name = pat_match.group(1).strip()
                if len(pat_name) >= 3 and pat_name not in seen_display_names:
                    seen_display_names.add(pat_name)
                    concepts.append({
                        "display_name": pat_name,
                        "search_terms": {pat_name.lower()},
                        "source_file": rel_path,
                    })

    return concepts

def normalize_text(text: str) -> set[str]:
    """Tokenizes and cleans text for matching."""
    cleaned = re.sub(r"[^\w\s-]", " ", text.lower())
    tokens = set(cleaned.split())
    stop_words = {"what", "is", "the", "difference", "between", "how", "do", "you", "and", "or", "in", "to", "for", "a", "an", "of", "with", "does", "explain", "use", "when", "would", "which", "are"}
    return tokens - stop_words

def match_question_against_concept(question: str, concept: dict) -> bool:
    """Checks if a question matches any search term of a specific concept."""
    q_lower = question.lower()
    q_tokens = normalize_text(question)

    for term in sorted(concept["search_terms"], key=lambda t: len(t), reverse=True):
        if term in ("rest",):
            if not (re.search(r"\brest\s+(api|apis|endpoint|service|ful)\b", q_lower) or "restful" in q_lower):
                continue
        if term in ("can use", "state", "props", "use"):
            continue

        # Regex whole word boundary
        pattern = r"\b" + re.escape(term) + r"\b"
        if re.search(pattern, q_lower):
            return True

        # Multi-word token overlap
        term_tokens = normalize_text(term)
        if len(term_tokens) >= 2 and term_tokens.issubset(q_tokens):
            return True

    return False

def generate_bidirectional_report(repo_root: str) -> str:
    """Builds the comprehensive bidirectional INTERVIEW_COVERAGE.md content."""
    domain_stats = []
    orphan_concepts_checklist = []
    uncovered_questions_checklist = []
    covered_samples = []

    total_questions_all = 0
    total_questions_covered = 0
    total_concepts_all = 0
    total_concepts_with_q = 0

    print("Executing Bidirectional Synchronization across Technical Skill & Interview Inspire...")

    for domain, config in TRACK_MAPPING.items():
        remote_rel = config["remote_file"]
        local_files = config["local_files"]

        print(f"  -> Scanning {domain}...")
        remote_content = fetch_question_file(repo_root, remote_rel)
        questions = parse_interview_questions(remote_content)
        concepts = extract_structured_concepts(repo_root, local_files)

        # Track concept -> matched questions
        concept_matches = {c["display_name"]: [] for c in concepts}
        question_matched = [False] * len(questions)

        for i, q in enumerate(questions):
            q_text = q["question"]
            for c in concepts:
                if match_question_against_concept(q_text, c):
                    question_matched[i] = True
                    concept_matches[c["display_name"]].append(q_text)
                    if len(covered_samples) < 15:
                        if os.path.exists(os.path.join(repo_root, "Interview Inspire", remote_rel)):
                            sample_link = f"./Interview%20Inspire/{remote_rel}"
                        else:
                            sample_link = f"{GITHUB_REPO_BASE}/{remote_rel}"
                        covered_samples.append({
                            "domain": domain,
                            "question": q_text,
                            "topic": c["display_name"],
                            "remote_link": sample_link,
                        })
                    break

        domain_questions_total = len(questions)
        domain_questions_covered = sum(1 for m in question_matched if m)
        q_pct = (domain_questions_covered / domain_questions_total * 100) if domain_questions_total > 0 else 0

        domain_concepts_total = len(concepts)
        domain_concepts_with_q = sum(1 for c in concepts if len(concept_matches[c["display_name"]]) > 0)
        c_pct = (domain_concepts_with_q / domain_concepts_total * 100) if domain_concepts_total > 0 else 0

        total_questions_all += domain_questions_total
        total_questions_covered += domain_questions_covered
        total_concepts_all += domain_concepts_total
        total_concepts_with_q += domain_concepts_with_q

        domain_stats.append({
            "domain": domain,
            "q_total": domain_questions_total,
            "q_covered": domain_questions_covered,
            "q_pct": q_pct,
            "c_total": domain_concepts_total,
            "c_covered": domain_concepts_with_q,
            "c_pct": c_pct,
            "remote_rel": remote_rel,
            "primary_local": local_files[0],
        })

        # Track A Gaps: Orphan Concepts (Concepts in Technical Skill with 0 questions)
        orphans = [c for c in concepts if len(concept_matches[c["display_name"]]) == 0]
        if orphans:
            orphan_concepts_checklist.append({
                "domain": domain,
                "remote_rel": remote_rel,
                "primary_local": local_files[0],
                "orphans": orphans[:6], # Top 6
                "total_orphans": len(orphans),
            })

        # Track B Gaps: Uncovered Questions (Questions in Interview Inspire with no concept row)
        uncovered_q = [q for i, q in enumerate(questions) if not question_matched[i]]
        if uncovered_q:
            uncovered_questions_checklist.append({
                "domain": domain,
                "remote_rel": remote_rel,
                "primary_local": local_files[0],
                "gaps": uncovered_q[:5],
                "total_gaps": len(uncovered_q),
            })

    overall_q_pct = (total_questions_covered / total_questions_all * 100) if total_questions_all > 0 else 0
    overall_c_pct = (total_concepts_with_q / total_concepts_all * 100) if total_concepts_all > 0 else 0

    lines = [
        "# 🎯 Dual-Track Engineering Coverage & Readiness Dashboard",
        "",
        "> **Unified Live Synchronization between [`Technical Skill/`](./Technical%20Skill/TECHNICAL%20SKILL.md) and [`Interview Inspire/`](./Interview%20Inspire/README.md)**  ",
        f"> - 🎯 **Question Preparation Readiness:** `{overall_q_pct:.1f}%` of tracked interview questions ({total_questions_covered}/{total_questions_all}) have corresponding technical concept notes.",
        f"> - 🧠 **Concept Question Coverage:** `{overall_c_pct:.1f}%` of documented technical concepts ({total_concepts_with_q}/{total_concepts_all}) have active interview questions in the bank.",
        "",
        "---",
        "",
        "## 📊 Domain-by-Domain Scorecard",
        "",
        "| Track / Domain | Questions Total | Questions Covered | Q Score | Concepts Total | Concepts with Qs | Concept Score | Primary Notes | Question Bank Link |",
        "| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :--- |",
    ]

    for s in domain_stats:
        bar_len = int(s["q_pct"] / 10)
        progress = "🟩" * bar_len + "⬜" * (10 - bar_len)
        primary_rel = s["primary_local"]
        primary_target = f"./Technical%20Skill/{primary_rel}" if os.path.exists(os.path.join(repo_root, "Technical Skill", primary_rel)) else f"./{primary_rel}"
        bank_target = f"./Interview%20Inspire/{s['remote_rel']}" if os.path.exists(os.path.join(repo_root, "Interview Inspire", s["remote_rel"])) else f"{GITHUB_REPO_BASE}/{s['remote_rel']}"

        lines.append(
            f"| **{s['domain']}** | {s['q_total']} | {s['q_covered']} | {progress} `{s['q_pct']:.1f}%` | {s['c_total']} | {s['c_covered']} | `{s['c_pct']:.1f}%` | [`{os.path.basename(primary_rel)}`]({primary_target}) | [Practice Bank ↗]({bank_target}) |"
        )

    lines.extend([
        "",
        "---",
        "",
        "## 🚨 Track A Gaps: High-Yield Orphan Concepts (Need Interview Questions)",
        "",
        "> **Actionable Opportunity**: These concepts are documented in your `Technical Skill/` reference tables, but currently have **0 interview questions** in `Interview Inspire/`.",
        "> 👉 *When reviewing these, use the AI agent's **Top 5 Question Generator** archetype to populate questions for them!*",
        "",
    ])

    for item in orphan_concepts_checklist:
        lines.append(f"### {item['domain']} ({item['total_orphans']} Concepts without Questions)")
        lines.append(f"> Documented in: [`{os.path.basename(item['primary_local'])}`](./Technical%20Skill/{item['primary_local']}) ──► Target Question Checklist: [`{os.path.basename(item['remote_rel'])}`](./Interview%20Inspire/{item['remote_rel']})")
        lines.append("")
        for o in item["orphans"]:
            lines.append(f"- [ ] **`{o['display_name']}`**: Add interview questions (Mental model, Internals, Tradeoffs, Observability, Debugging)")
        if item["total_orphans"] > 6:
            lines.append(f"- *...and {item['total_orphans'] - 6} more concepts documented in `{item['primary_local']}`.*")
        lines.append("")

    lines.extend([
        "---",
        "",
        "## 🔍 Track B Gaps: Uncovered Interview Questions (Need Reference Tables)",
        "",
        "> **Actionable Opportunity**: These interview questions exist in `Interview Inspire/`, but do not yet have dedicated reference table entries in `Technical Skill/`.",
        "> 👉 *Copy any question below into [`inbox.md`](./inbox.md) and ask the AI agent to draft reference table rows!*",
        "",
    ])

    for gap in uncovered_questions_checklist:
        lines.append(f"### {gap['domain']} ({gap['total_gaps']} Questions without Notes)")
        lines.append(f"> Question source: [`{os.path.basename(gap['remote_rel'])}`](./Interview%20Inspire/{gap['remote_rel']}) ──► Destination Note: [`{os.path.basename(gap['primary_local'])}`](./Technical%20Skill/{gap['primary_local']})")
        lines.append("")
        for g in gap["gaps"]:
            lines.append(f"- [ ] **{g['heading']}**: {g['question']}")
        if gap['total_gaps'] > 5:
            lines.append(f"- *...and {gap['total_gaps'] - 5} more questions in `{gap['remote_rel']}`.*")
        lines.append("")

    lines.extend([
        "---",
        "",
        "## 💡 Sample Verified 2-Way Cross-Links",
        "",
        "| Domain | Question from Interview Inspire | Matched Concept in Technical Skill | Practice Link |",
        "| :--- | :--- | :--- | :--- |",
    ])

    for sample in covered_samples:
        clean_q = sample["question"][:75] + ("..." if len(sample["question"]) > 75 else "")
        lines.append(
            f"| **{sample['domain']}** | {clean_q} | `{sample['topic']}` | [View in Bank ↗]({sample['remote_link']}) |"
        )

    lines.extend([
        "",
        "---",
        "",
        "## 🔄 Automation & How to Refresh",
        "",
        "Run this script anytime you add new notes or questions to refresh the bidirectional matrix:",
        "```bash",
        "# Run bidirectional coverage sync",
        "python scripts/sync_coverage.py",
        "",
        "# Or use the legacy alias",
        "python scripts/sync_interview_coverage.py",
        "```",
    ])

    return "\n".join(lines) + "\n"

def main():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    report = generate_bidirectional_report(repo_root)

    output_path = os.path.join(repo_root, "INTERVIEW_COVERAGE.md")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"\n[OK] Generated bidirectional dashboard {output_path} successfully!")

    try:
        from prettify_tables import process_file
        process_file(output_path, check_only=False)
    except Exception:
        pass

if __name__ == "__main__":
    main()
