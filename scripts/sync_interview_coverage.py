#!/usr/bin/env python3
"""
Interview-Inspire Cross-Linking & Coverage Sync Script
Zero external dependencies (Python 3 standard library).

Features:
- Fetches all interview questions from shubhamkhatik/Interview-Inspire.
- Extracts all documented topics and skills from Technical-Skill tables.
- Calculates domain-by-domain coverage statistics and readiness percentages.
- Identifies knowledge gaps (interview questions without concept notes).
- Generates a clean, beautifully formatted INTERVIEW_COVERAGE.md dashboard.
"""

import os
import sys
import re
import json
import urllib.request
import urllib.error

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# Track files mapping between Interview-Inspire and Technical-Skill
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

def fetch_remote_file(rel_path: str) -> str:
    """Fetches a markdown file from the GitHub repository."""
    url = f"{GITHUB_RAW_BASE}/{rel_path}"
    req = urllib.request.Request(url, headers={"User-Agent": "TechnicalSkillSync/1.0"})
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
            
        # Match numbered questions: '1. What is...' or '12. Explain...'
        q_match = re.match(r"^\d+\.\s+(.*)", stripped)
        if q_match:
            q_text = q_match.group(1).strip()
            questions.append({
                "heading": current_heading,
                "question": q_text
            })
            
    return questions

def extract_local_topics(repo_root: str, local_files: list[str]) -> set[str]:
    """Extracts topic/skill names from markdown tables and pattern lists in given files."""
    topics = set()
    
    for rel_path in local_files:
        full_path = os.path.join(repo_root, rel_path)
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
                
            # 1. Table rows
            if stripped.startswith("|") and stripped.endswith("|") and stripped.count("|") >= 2:
                cells = [c.strip() for c in stripped[1:-1].split("|")]
                if not cells or not cells[0]:
                    continue
                # Skip divider rows (e.g. | --- |)
                if re.match(r"^:?-+:?$", cells[0]):
                    continue
                # Skip header row (Skill, Topic, Topic / Skill, etc.)
                first_cell = cells[0].replace("**", "").replace("*", "").replace("`", "").strip()
                cell_lower = first_cell.lower()
                if any(h in cell_lower for h in ["topic", "skill", "method / domain", "layer", "concept"]) and len(cell_lower.split()) <= 4:
                    continue
                    
                if first_cell and len(cell_lower) >= 2:
                    topics.add(cell_lower)
                    
                    # Extract parenthesized acronyms/aliases e.g. "Product Quantization (PQ)" -> "pq"
                    m = re.findall(r"\((.*?)\)", first_cell)
                    for alias in m:
                        for sub_alias in re.split(r"[/,]| vs ", alias):
                            sub = sub_alias.strip().lower()
                            if len(sub) >= 2 and sub not in ("legacy", "modern", "new", "pattern", "system design"):
                                topics.add(sub)
                                
                    # Base topic without parentheses
                    base_topic = re.sub(r"\(.*?\)", "", cell_lower).strip()
                    if len(base_topic) >= 3:
                        topics.add(base_topic)
                        
            # 2. DSA / Non-table pattern lines like "Two Pointers [Pattern]"
            pat_match = re.match(r"^([A-Za-z0-9\s\-]+)\s*\[(Pattern|Algorithm|Data Structure|Core Concept)\]", stripped)
            if pat_match:
                pat_name = pat_match.group(1).strip().lower()
                if len(pat_name) >= 3:
                    topics.add(pat_name)
                    
    return topics

def normalize_text(text: str) -> set[str]:
    """Tokenizes and cleans text for matching."""
    cleaned = re.sub(r"[^\w\s-]", " ", text.lower())
    tokens = set(cleaned.split())
    # Filter common stop words
    stop_words = {"what", "is", "the", "difference", "between", "how", "do", "you", "and", "or", "in", "to", "for", "a", "an", "of", "with", "does", "explain", "use", "when", "would", "which", "are"}
    return tokens - stop_words

def is_question_covered(question: str, local_topics: set[str]) -> tuple[bool, str]:
    """Checks if a question matches any documented topic in the local notes with high precision."""
    q_lower = question.lower()
    q_tokens = normalize_text(question)
    
    # Sort topics by length descending so longer/more specific phrases match first
    sorted_topics = sorted(local_topics, key=lambda t: len(t), reverse=True)
    
    for topic in sorted_topics:
        # Avoid generic false positive triggers
        if topic in ("rest",):
            if not (re.search(r"\brest\s+(api|apis|endpoint|service|ful)\b", q_lower) or "restful" in q_lower):
                continue
        if topic in ("can use", "state", "props", "use"):
            continue
            
        # 1. Whole-word regex boundary match
        pattern = r"\b" + re.escape(topic) + r"\b"
        if re.search(pattern, q_lower):
            return True, topic
            
        # 2. Multi-word token overlap
        topic_tokens = normalize_text(topic)
        if len(topic_tokens) >= 2 and topic_tokens.issubset(q_tokens):
            return True, topic
            
    return False, ""

def generate_coverage_report(repo_root: str) -> str:
    """Builds the full INTERVIEW_COVERAGE.md content."""
    domain_stats = []
    gap_checklist = []
    covered_samples = []
    
    total_questions_all = 0
    total_covered_all = 0
    
    print("Fetching interview questions from Interview-Inspire and analyzing coverage...")
    
    for domain, config in TRACK_MAPPING.items():
        remote_rel = config["remote_file"]
        local_files = config["local_files"]
        
        print(f"  -> Scanning {domain}...")
        remote_content = fetch_remote_file(remote_rel)
        questions = parse_interview_questions(remote_content)
        local_topics = extract_local_topics(repo_root, local_files)
        
        domain_total = len(questions)
        domain_covered = 0
        domain_gaps = []
        
        for item in questions:
            q_text = item["question"]
            covered, matched_topic = is_question_covered(q_text, local_topics)
            if covered:
                domain_covered += 1
                if len(covered_samples) < 15:
                    covered_samples.append({
                        "domain": domain,
                        "question": q_text,
                        "topic": matched_topic,
                        "remote_link": f"{GITHUB_REPO_BASE}/{remote_rel}",
                    })
            else:
                domain_gaps.append(item)
                
        pct = (domain_covered / domain_total * 100) if domain_total > 0 else 0
        total_questions_all += domain_total
        total_covered_all += domain_covered
        
        domain_stats.append({
            "domain": domain,
            "total": domain_total,
            "covered": domain_covered,
            "pct": pct,
            "remote_rel": remote_rel,
            "primary_local": local_files[0],
        })
        
        if domain_gaps:
            gap_checklist.append({
                "domain": domain,
                "remote_rel": remote_rel,
                "gaps": domain_gaps[:5], # Show top 5 gaps per domain
                "total_gaps": len(domain_gaps),
            })
            
    overall_pct = (total_covered_all / total_questions_all * 100) if total_questions_all > 0 else 0
    
    # Build Markdown document
    lines = [
        "# 🎯 Interview Readiness & Question Coverage Matrix",
        "",
        "> **Live Synchronization with [`shubhamkhatik/Interview-Inspire`](https://github.com/shubhamkhatik/Interview-Inspire)**  ",
        f"> **Overall Preparation Score:** `{overall_pct:.1f}%` of tracked interview questions ({total_covered_all}/{total_questions_all}) have corresponding concept notes in `Technical-Skill`.",
        "",
        "---",
        "",
        "## 📊 Domain Coverage Breakdown",
        "",
        "| Track / Domain | Questions in Bank | Concepts Documented | Coverage % | Primary Notes | Question Bank Link |",
        "| :--- | :---: | :---: | :---: | :--- | :--- |",
    ]
    
    for s in domain_stats:
        bar_len = int(s["pct"] / 10)
        progress = "🟩" * bar_len + "⬜" * (10 - bar_len)
        lines.append(
            f"| **{s['domain']}** | {s['total']} | {s['covered']} | {progress} `{s['pct']:.1f}%` | [`{os.path.basename(s['primary_local'])}`](./{s['primary_local']}) | [Practice Questions ↗]({GITHUB_REPO_BASE}/{s['remote_rel']}) |"
        )
        
    lines.extend([
        "",
        "---",
        "",
        "## 🔍 Sample Verified Concept Matches",
        "",
        "| Domain | Question from Interview-Inspire | Matched Skill / Note | Practice Link |",
        "| :--- | :--- | :--- | :--- |",
    ])
    
    for sample in covered_samples:
        clean_q = sample["question"][:75] + ("..." if len(sample["question"]) > 75 else "")
        lines.append(
            f"| **{sample['domain']}** | {clean_q} | `{sample['topic'].title()}` | [View in Bank ↗]({sample['remote_link']}) |"
        )
        
    lines.extend([
        "",
        "---",
        "",
        "## 💡 Identified Knowledge Gaps (High-Yield Checklist)",
        "",
        "> These are questions currently tracked in `Interview-Inspire` that do not have dedicated table entries in `Technical-Skill`. You can paste any of these into `inbox.md` to draft notes for them!",
        "",
    ])
    
    for gap in gap_checklist:
        lines.append(f"### {gap['domain']} ({gap['total_gaps']} Gaps)")
        lines.append(f"> Question source: [`{gap['remote_rel']}`]({GITHUB_REPO_BASE}/{gap['remote_rel']})")
        lines.append("")
        for g in gap["gaps"]:
            lines.append(f"- [ ] **{g['heading']}**: {g['question']}")
        if gap['total_gaps'] > 5:
            lines.append(f"- *...and {gap['total_gaps'] - 5} more questions in `{gap['remote_rel']}`.*")
        lines.append("")
        
    lines.extend([
        "---",
        "",
        "## 🔄 How to Refresh This Report",
        "",
        "Run this script anytime you add new notes or questions:",
        "```bash",
        "python scripts/sync_interview_coverage.py",
        "```",
    ])
    
    return "\n".join(lines) + "\n"

def main():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    report = generate_coverage_report(repo_root)
    
    output_path = os.path.join(repo_root, "INTERVIEW_COVERAGE.md")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(report)
        
    print(f"\n[OK] Generated {output_path} successfully!")
    
    # Prettify the generated file
    try:
        from prettify_tables import process_file
        process_file(output_path, check_only=False)
    except Exception:
        pass

if __name__ == "__main__":
    main()
