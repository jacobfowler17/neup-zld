#!/bin/bash

set -euo pipefail

# Resolve the project root from this script's location, so it works from any cwd
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# Run from the project root and make `src` importable
cd "$PROJECT_ROOT"
export PYTHONPATH="$PROJECT_ROOT${PYTHONPATH:+:$PYTHONPATH}"

# Use the venv's interpreter directly (no need to "activate")
PYTHON="$PROJECT_ROOT/.venv/bin/python"   # Windows Git Bash: .venv/Scripts/python.exe

# Run as a module so imports like `from src.core import ...` work
"$PYTHON" -u -m src.core.zld_sweep_1param "$@"

