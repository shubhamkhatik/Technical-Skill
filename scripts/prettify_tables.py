#!/usr/bin/env python3
"""
Markdown Table Prettifier & Auto-Aligner
Zero external dependencies (Python 3 standard library).

Features:
- Aligns all vertical pipes (|) in markdown tables for perfect raw-text readability.
- Respects and preserves divider alignments (:---, :---:, ---:).
- Safely handles escaped pipes (\\|) inside cell contents and links.
- Ignores code blocks (```) and prose outside tables.
- Supports single file, multiple files, or entire repository (--all).
"""

import sys
import os
import re

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

ESCAPED_PIPE_PLACEHOLDER = "@@ESCAPED_PIPE@@"

def is_divider_cell(cell: str) -> bool:
    """Checks if a cell is a markdown table divider (e.g. ---, :---, :---:, ---:)."""
    stripped = cell.strip()
    return bool(re.match(r"^:?-+:?$", stripped))

def is_table_row(line: str) -> bool:
    """Checks if a line looks like a markdown table row."""
    stripped = line.strip()
    return stripped.startswith("|") and stripped.endswith("|") and stripped.count("|") >= 2

def split_table_row(line: str) -> list[str]:
    """Splits a markdown table row into cells, respecting escaped pipes."""
    # Temporarily mask escaped pipes
    masked = line.replace(r"\|", ESCAPED_PIPE_PLACEHOLDER)
    stripped = masked.strip()
    
    # Remove leading and trailing pipe
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|"):
        stripped = stripped[:-1]
        
    raw_cells = stripped.split("|")
    # Restore escaped pipes and strip whitespace
    cells = [c.replace(ESCAPED_PIPE_PLACEHOLDER, r"\|").strip() for c in raw_cells]
    return cells

def format_divider_cell(cell: str, width: int) -> str:
    """Formats a divider cell preserving its alignment while matching column width."""
    stripped = cell.strip()
    has_left = stripped.startswith(":")
    has_right = stripped.endswith(":")
    
    dash_count = max(3, width)
    if has_left and has_right:
        return ":" + "-" * (dash_count - 2) + ":"
    elif has_left:
        return ":" + "-" * (dash_count - 1)
    elif has_right:
        return "-" * (dash_count - 1) + ":"
    else:
        return "-" * dash_count

def prettify_table(table_lines: list[str]) -> list[str]:
    """Formats a list of table lines so all columns align neatly."""
    if len(table_lines) < 2:
        return table_lines
        
    parsed_rows = [split_table_row(line) for line in table_lines]
    
    # Determine the maximum number of columns across all rows
    num_cols = max(len(row) for row in parsed_rows)
    if num_cols == 0:
        return table_lines
        
    # Pad rows that have fewer columns
    for row in parsed_rows:
        while len(row) < num_cols:
            row.append("")
            
    # Check if the second row is indeed a divider row
    is_valid_divider = all(is_divider_cell(cell) for cell in parsed_rows[1])
    if not is_valid_divider:
        # Not a standard markdown table, return unmodified
        return table_lines

    # Calculate max width for each column (minimum 3 chars)
    col_widths = [3] * num_cols
    for row_idx, row in enumerate(parsed_rows):
        for col_idx, cell in enumerate(row):
            if row_idx == 1 and is_divider_cell(cell):
                continue
            col_widths[col_idx] = max(col_widths[col_idx], len(cell))
            
    # Format each row
    formatted_lines = []
    for row_idx, row in enumerate(parsed_rows):
        formatted_cells = []
        is_divider = (row_idx == 1)
        
        for col_idx, cell in enumerate(row):
            width = col_widths[col_idx]
            if is_divider:
                formatted_cells.append(format_divider_cell(cell, width))
            else:
                # Left-align cell content padded with spaces
                formatted_cells.append(cell.ljust(width))
                
        line = "| " + " | ".join(formatted_cells) + " |"
        formatted_lines.append(line)
        
    return formatted_lines

def prettify_markdown_content(content: str) -> tuple[str, int]:
    """Prettifies all markdown tables in content. Returns (new_content, tables_formatted)."""
    lines = content.splitlines()
    output_lines = []
    current_table = []
    in_code_block = False
    table_count = 0
    
    for line in lines:
        stripped = line.strip()
        
        # Toggle code block state
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            if current_table:
                output_lines.extend(prettify_table(current_table))
                current_table = []
                table_count += 1
            output_lines.append(line)
            continue
            
        if in_code_block:
            output_lines.append(line)
            continue
            
        # Check if line belongs to a table
        if is_table_row(line):
            current_table.append(line)
        else:
            if current_table:
                output_lines.extend(prettify_table(current_table))
                current_table = []
                table_count += 1
            output_lines.append(line)
            
    # If file ends with a table
    if current_table:
        output_lines.extend(prettify_table(current_table))
        table_count += 1
        
    # Preserve trailing newline if present in original
    result = "\n".join(output_lines)
    if content.endswith("\n"):
        result += "\n"
        
    return result, table_count

def process_file(file_path: str, check_only: bool = False) -> bool:
    """Prettifies a single markdown file. Returns True if file was modified/needed formatting."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            original = f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}", file=sys.stderr)
        return False
        
    prettified, count = prettify_markdown_content(original)
    if count == 0:
        return False
        
    if original != prettified:
        if check_only:
            print(f"[NEEDS FORMATTING] {file_path} ({count} tables)")
            return True
        else:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(prettified)
            print(f"[FORMATTED] {file_path} ({count} tables aligned)")
            return True
    else:
        if not check_only:
            print(f"[OK - ALIGNED] {file_path} ({count} tables)")
        return False

def find_markdown_files(root_dir: str) -> list[str]:
    """Finds all .md files in the directory tree, skipping ignored directories."""
    ignored_dirs = {".git", "node_modules", ".agents", ".gemini", "scratch"}
    md_files = []
    
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in ignored_dirs]
        for f in sorted(files):
            if f.endswith(".md"):
                md_files.append(os.path.join(root, f))
                
    return md_files

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python scripts/prettify_tables.py <file.md>         # Format single file")
        print("  python scripts/prettify_tables.py --all             # Format all .md files in repo")
        print("  python scripts/prettify_tables.py --check           # Check without modifying")
        sys.exit(1)
        
    arg = sys.argv[1]
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    
    if arg in ("--all", "-a"):
        files = find_markdown_files(repo_root)
        print(f"Scanning {len(files)} markdown files across repository...")
        formatted_count = 0
        for f in files:
            if process_file(f, check_only=False):
                formatted_count += 1
        print(f"\nDone! Aligned tables across {formatted_count} files.")
        
    elif arg in ("--check", "-c"):
        files = find_markdown_files(repo_root)
        unformatted = 0
        for f in files:
            if process_file(f, check_only=True):
                unformatted += 1
        if unformatted > 0:
            print(f"\n{unformatted} files need table formatting. Run with --all to align them.")
            sys.exit(1)
        else:
            print("\nAll markdown tables are cleanly aligned!")
            sys.exit(0)
            
    else:
        # Single file
        target_path = os.path.abspath(arg)
        if not os.path.exists(target_path):
            print(f"File not found: {target_path}", file=sys.stderr)
            sys.exit(1)
        process_file(target_path, check_only=False)

if __name__ == "__main__":
    main()
