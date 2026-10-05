#!/usr/bin/env python3
"""
Root alias wrapper for Interview Inspire question processor.
Invokes Interview Inspire/scripts/curate_questions.py with all CLI arguments and environment variables.
"""

import os
import sys
import subprocess

if __name__ == "__main__":
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    target_script = os.path.join(repo_root, "Interview Inspire", "scripts", "curate_questions.py")
    
    cmd = [sys.executable, target_script] + sys.argv[1:]
    sys.exit(subprocess.call(cmd))
