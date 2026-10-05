#!/usr/bin/env python3
"""
Backward-compatibility wrapper for scripts/sync_coverage.py.
Directly invokes the unified bidirectional coverage synchronization engine.
"""

from sync_coverage import main

if __name__ == "__main__":
    main()
